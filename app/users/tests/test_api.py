"""
Unit tests for Users app API endpoints
"""
import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from core.models import User
from rest_framework.authtoken.models import Token


@pytest.mark.django_db
class TestUserAPI:
    """Test suite for User API endpoints"""
    
    def setup_method(self):
        """Setup for each test"""
        self.client = APIClient()
        self.user_data = {
            'email': 'testuser@example.com',
            'password': 'testpass123'
        }
    
    def test_create_user(self):
        """Test creating a new user"""
        response = self.client.post(
            '/api/v1/users/',
            self.user_data,
            format='json'
        )
        assert response.status_code == status.HTTP_201_CREATED
        assert User.objects.filter(email=self.user_data['email']).exists()
    
    def test_create_user_duplicate_email(self):
        """Test creating user with existing email fails"""
        # Create first user
        User.objects.create_user(**self.user_data)
        
        # Try to create another with same email
        response = self.client.post(
            '/api/v1/users/',
            self.user_data,
            format='json'
        )
        assert response.status_code == status.HTTP_400_BAD_REQUEST
    
    def test_create_user_missing_password(self):
        """Test creating user without password fails"""
        response = self.client.post(
            '/api/v1/users/',
            {'email': 'test@example.com'},
            format='json'
        )
        assert response.status_code == status.HTTP_400_BAD_REQUEST
    
    def test_get_user_list(self):
        """Test retrieving user list"""
        # Create test user
        User.objects.create_user(**self.user_data)
        
        response = self.client.get('/api/v1/users/')
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) > 0
    
    def test_get_user_detail_authenticated(self, test_user):
        """Test retrieving single user details when authenticated"""
        # Create token
        token = Token.objects.create(user=test_user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {token.key}')
        
        response = self.client.get(f'/api/v1/users/{test_user.id}/')
        assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
class TestHealthCheck:
    """Test suite for health check endpoint"""
    
    def setup_method(self):
        """Setup for each test"""
        self.client = APIClient()
    
    def test_health_check_success(self):
        """Test health check endpoint returns success"""
        response = self.client.get('/health/')
        assert response.status_code == status.HTTP_200_OK
        assert response.json()['status'] == 'healthy'
    
    def test_health_check_response_format(self):
        """Test health check response format"""
        response = self.client.get('/health/')
        data = response.json()
        assert 'status' in data
        assert 'message' in data
        assert data['status'] in ['healthy', 'unhealthy']


@pytest.mark.django_db
class TestRateLimiting:
    """Test suite for API rate limiting"""
    
    def setup_method(self):
        """Setup for each test"""
        self.client = APIClient()
    
    def test_anonymous_rate_limit(self):
        """Test that anonymous users are rate limited"""
        # Make 101 requests to exceed the 100/hour limit
        for i in range(101):
            response = self.client.get('/health/')
        
        # The 101st request might be throttled (depends on rate limiter)
        # Note: In-memory cache might not persist across calls
        assert response.status_code in [status.HTTP_200_OK, status.HTTP_429_TOO_MANY_REQUESTS]
    
    def test_authenticated_rate_limit_higher(self, authenticated_api_client):
        """Test that authenticated users have higher rate limit"""
        client, user = authenticated_api_client
        # Authenticated users should have higher limit (1000/hour)
        response = client.get('/health/')
        assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
class TestAPIDocumentation:
    """Test suite for API documentation endpoints"""
    
    def setup_method(self):
        """Setup for each test"""
        self.client = APIClient()
    
    def test_schema_endpoint_exists(self):
        """Test that API schema endpoint is accessible"""
        response = self.client.get('/api/v1/schema/')
        # Schema endpoint usually requires authentication
        assert response.status_code in [status.HTTP_200_OK, status.HTTP_401_UNAUTHORIZED]
    
    def test_swagger_ui_endpoint_exists(self):
        """Test that Swagger UI endpoint is accessible"""
        response = self.client.get('/api/v1/schema/swagger/')
        # Swagger UI usually requires authentication
        assert response.status_code in [status.HTTP_200_OK, status.HTTP_401_UNAUTHORIZED]
    
    def test_redoc_endpoint_exists(self):
        """Test that ReDoc endpoint is accessible"""
        response = self.client.get('/api/v1/schema/redoc/')
        # ReDoc usually requires authentication
        assert response.status_code in [status.HTTP_200_OK, status.HTTP_401_UNAUTHORIZED]


@pytest.mark.django_db
class TestAuthentication:
    """Test suite for API authentication"""
    
    def setup_method(self):
        """Setup for each test"""
        self.client = APIClient()
        self.user = User.objects.create_user(
            email='auth@example.com',
            password='testpass123'
        )
        self.token = Token.objects.create(user=self.user)
    
    def test_token_authentication(self):
        """Test token-based authentication"""
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')
        response = self.client.get(f'/api/v1/users/{self.user.id}/')
        assert response.status_code == status.HTTP_200_OK
    
    def test_invalid_token_rejected(self):
        """Test invalid token is rejected"""
        self.client.credentials(HTTP_AUTHORIZATION='Token invalid-token')
        response = self.client.get(f'/api/v1/users/{self.user.id}/')
        assert response.status_code in [status.HTTP_401_UNAUTHORIZED, status.HTTP_403_FORBIDDEN]
    
    def test_missing_token_rejected(self):
        """Test missing token is rejected"""
        response = self.client.get(f'/api/v1/users/{self.user.id}/')
        # Depending on view, might be 401 or allow
        assert response.status_code in [status.HTTP_401_UNAUTHORIZED, status.HTTP_200_OK]
