"""
Pytest configuration and fixtures for Altaviz Backend tests
"""
import os
import django
from django.conf import settings
from pathlib import Path

# Add the app directory to the path
BASE_DIR = Path(__file__).resolve().parent.parent


def pytest_configure():
    """Configure pytest to use Django"""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
    
    if not settings.configured:
        django.setup()


# Shared fixtures for testing
import pytest
from django.test import Client
from rest_framework.test import APIClient
from core.models import User
from rest_framework.authtoken.models import Token


@pytest.fixture
def api_client():
    """Provide an API client for tests"""
    return APIClient()


@pytest.fixture
def authenticated_api_client(db):
    """Provide an authenticated API client"""
    client = APIClient()
    user = User.objects.create_user(
        email='test@example.com',
        password='testpass123'
    )
    token = Token.objects.create(user=user)
    client.credentials(HTTP_AUTHORIZATION=f'Token {token.key}')
    return client, user


@pytest.fixture
def test_user(db):
    """Create a test user"""
    return User.objects.create_user(
        email='test@example.com',
        password='testpass123'
    )


@pytest.fixture
def test_superuser(db):
    """Create a test superuser"""
    return User.objects.create_superuser(
        email='admin@example.com',
        password='adminpass123'
    )


@pytest.fixture
def django_client():
    """Provide a Django test client"""
    return Client()


@pytest.fixture
def authenticated_django_client(test_user):
    """Provide an authenticated Django test client"""
    client = Client()
    client.login(email='test@example.com', password='testpass123')
    return client
