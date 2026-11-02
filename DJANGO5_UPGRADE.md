# Django 5.x Upgrade Guide & New Features

This guide documents the upgrade from Django 3.0.4 to Django 5.x and the new features added to the Altaviz Backend.

## 🚀 Upgrade Summary

### What Changed

- **Django Version:** 3.0.4 → 5.0.6
- **Python Version:** 3.8 → 3.11+ (required)
- **Bootstrap Version:** 4 → 5
- **API Documentation:** django-rest-swagger → drf-spectacular
- **Rate Limiting:** Added (100/hour for anonymous, 1000/hour for authenticated)
- **Testing:** Added pytest framework with comprehensive tests

---

## 📋 Breaking Changes & Migration Notes

### 1. **Python Version**

**Before:** Python 3.5+
**After:** Python 3.10+ (3.11 recommended)

```bash
# Check your Python version
python --version

# If using Docker, verify Dockerfile is using python:3.11-alpine
cat Dockerfile
```

### 2. **Middleware Changes**

**Before:**
```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # ...
]
```

**After:** Django 5.x is compatible, but added:
```python
MIDDLEWARE = [
    'app.exceptions.RequestLoggingMiddleware',  # Custom logging
    # ...
]
```

### 3. **Database Configuration**

**No changes needed** - existing configuration works with Django 5.x

### 4. **Removed Features**

- `django-rest-swagger` (use `drf-spectacular` instead)
- `bootstrap4` CSS framework (use `bootstrap5` instead)
- Python < 3.10 compatibility

### 5. **Template Tags**

If you use custom template tags, verify they work with Django 5.x:

```bash
# Run Django checks
python manage.py check
```

---

## 🔒 Rate Limiting

### Overview

API endpoints are now rate-limited to protect against abuse:

- **Anonymous Users:** 100 requests/hour
- **Authenticated Users:** 1000 requests/hour

### Configuration

Edit `app/settings.py`:

```python
REST_FRAMEWORK = {
    'DEFAULT_THROTTLE_RATES': {
        'anon': '100/hour',      # Requests per hour for anonymous users
        'user': '1000/hour',     # Requests per hour for authenticated users
    }
}
```

### How It Works

When a rate limit is exceeded, the API returns:

```json
{
  "detail": "Request was throttled. Expected available in 3600 seconds."
}
```

HTTP Status: `429 Too Many Requests`

### Custom Rate Limits

Create a custom throttle class for specific endpoints:

```python
from rest_framework.throttling import UserRateThrottle

class CustomThrottle(UserRateThrottle):
    scope = 'custom'  # Must match scope in settings

# In settings.py
'DEFAULT_THROTTLE_RATES': {
    'custom': '10/hour',
}

# In views.py
class MyAPIView(APIView):
    throttle_classes = [CustomThrottle]
```

---

## 📚 API Documentation

### Overview

API documentation is now available via **drf-spectacular** in multiple formats:

1. **Swagger UI** - Interactive API browser
2. **ReDoc** - Beautiful API documentation
3. **OpenAPI Schema** - Machine-readable API spec

### Accessing Documentation

#### Swagger UI
```
http://localhost:8000/api/v1/schema/swagger/
```

#### ReDoc
```
http://localhost:8000/api/v1/schema/redoc/
```

#### OpenAPI Schema (JSON)
```
http://localhost:8000/api/v1/schema/
```

### Authentication for Documentation

Documentation endpoints require authentication. Add your API token:

```bash
# Get your token
curl -X POST http://localhost:8000/api/v1/get-token/ \
  -H "Content-Type: application/json" \
  -d '{"email":"your@email.com","password":"yourpassword"}'

# Use token in requests
curl -H "Authorization: Token YOUR_TOKEN" \
  http://localhost:8000/api/v1/schema/swagger/
```

### Documenting Your Endpoints

Add docstrings to your views:

```python
from drf_spectacular.utils import extend_schema

class UserListView(APIView):
    @extend_schema(
        description="List all users",
        responses={200: UserSerializer(many=True)},
    )
    def get(self, request):
        """Get list of users"""
        users = User.objects.all()
        return Response(UserSerializer(users, many=True).data)
    
    @extend_schema(
        description="Create a new user",
        request=UserCreateSerializer,
        responses={201: UserSerializer},
    )
    def post(self, request):
        """Create new user"""
        # ...implementation...
```

### OpenAPI Schema Download

For integration with API gateways:

```bash
# Download OpenAPI schema as JSON
curl -H "Authorization: Token YOUR_TOKEN" \
  http://localhost:8000/api/v1/schema/ > openapi.json

# Download as YAML
curl -H "Authorization: Token YOUR_TOKEN" \
  http://localhost:8000/api/v1/schema/?format=yaml > openapi.yaml
```

---

## 💾 Database Backups

### Quick Backup

```bash
# Create a backup
python manage.py backup_database

# Backup is saved to: app/backups/db_YYYYMMDD_HHMMSS.sql
```

### Backup with Compression

```bash
# Create compressed backup
python manage.py backup_database --compress

# Compressed backup: app/backups/db_YYYYMMDD_HHMMSS.sql.gz
```

### Custom Output Path

```bash
python manage.py backup_database --output /path/to/my_backup.sql
```

### Backup Media Files

```bash
# Backup both database and media files
python manage.py backup_database --compress --include-media

# Creates:
# - app/backups/db_YYYYMMDD_HHMMSS.sql.gz
# - app/backups/media_YYYYMMDD_HHMMSS.tar.gz
```

### Restore from Backup

```bash
# Restore from backup (will ask for confirmation)
python manage.py restore_database app/backups/db_YYYYMMDD_HHMMSS.sql

# Restore with confirmation flag (no prompt)
python manage.py restore_database app/backups/db_YYYYMMDD_HHMMSS.sql --confirm
```

### Automated Backups (Docker Compose)

Add to `docker-compose.yml`:

```yaml
services:
  backup:
    image: postgres:13-alpine
    volumes:
      - ./backups:/backups
    environment:
      - PGPASSWORD=your_db_password
    command: >
      sh -c "while true; do
        pg_dump -h db -U postgres altaviz_db > /backups/db_$(date +%Y%m%d_%H%M%S).sql;
        sleep 86400;
      done"
    depends_on:
      - db
```

### Backup Strategy

**Recommended backup schedule:**

1. **Daily automated backups** to local storage
2. **Weekly backups** to cloud storage (S3, Azure Blob)
3. **Monthly** long-term archive
4. **Monthly restore tests** to verify backups work

### Recovery Procedures

**Steps to recover:**

1. Identify the backup needed
2. Restore to a test database first
3. Verify data integrity
4. If OK, restore to production
5. Test application functionality
6. Monitor for issues

---

## 🧪 Unit Testing

### Setup

pytest is configured with Django integration. Configuration is in `pytest.ini`.

### Running Tests

```bash
# Run all tests
pytest

# Run specific test file
pytest app/users/tests/test_api.py

# Run specific test class
pytest app/users/tests/test_api.py::TestUserAPI

# Run specific test
pytest app/users/tests/test_api.py::TestUserAPI::test_create_user

# Run with verbose output
pytest -v

# Run with coverage report
pytest --cov=app --cov-report=html

# Run specific tests by marker
pytest -m django_db  # Only database tests
pytest -m "not slow"  # Skip slow tests
```

### Test Coverage

Generate coverage reports:

```bash
# Terminal report
pytest --cov=app --cov-report=term-missing

# HTML report
pytest --cov=app --cov-report=html
open htmlcov/index.html

# Coverage threshold (fail if below 70%)
# Configured in pytest.ini
```

### Writing Tests

Example test structure:

```python
import pytest
from rest_framework import status
from core.models import User

@pytest.mark.django_db
class TestUserAPI:
    """Test suite for User API endpoints"""
    
    def test_create_user(self):
        """Test creating a new user"""
        data = {
            'email': 'test@example.com',
            'password': 'testpass123'
        }
        response = self.client.post('/api/v1/users/', data)
        assert response.status_code == status.HTTP_201_CREATED
        assert User.objects.filter(email=data['email']).exists()
```

### Available Fixtures

Fixtures defined in `conftest.py`:

```python
# Unauthenticated API client
@pytest.fixture
def api_client():
    ...

# Authenticated API client with user
@pytest.fixture
def authenticated_api_client(db):
    ...

# Test user
@pytest.fixture
def test_user(db):
    ...

# Test superuser
@pytest.fixture
def test_superuser(db):
    ...
```

### Best Practices

1. **Use fixtures** instead of creating data in each test
2. **Mark database tests** with `@pytest.mark.django_db`
3. **Test one thing per test** function
4. **Use descriptive names:** `test_create_user_with_valid_email`
5. **Test both success and failure** cases

Example:

```python
@pytest.mark.django_db
class TestUserAPI:
    
    def test_create_user_success(self):
        """Test successful user creation"""
        # Should pass
        ...
    
    def test_create_user_duplicate_email(self):
        """Test user creation fails with duplicate email"""
        # Should fail with 400
        ...
    
    def test_create_user_missing_password(self):
        """Test user creation fails without password"""
        # Should fail with 400
        ...
```

---

## 🔄 Deployment Checklist

Before deploying Django 5.x to production:

- [ ] Update Python to 3.10+
- [ ] Update all dependencies with `pip install -r requirements-pinned.txt`
- [ ] Run migrations: `python manage.py migrate`
- [ ] Run Django checks: `python manage.py check --deploy`
- [ ] Run full test suite: `pytest --cov=app`
- [ ] Test API documentation endpoints
- [ ] Verify rate limiting works
- [ ] Create backup before upgrading: `python manage.py backup_database --compress`
- [ ] Test backup restoration
- [ ] Monitor error logs for 24 hours after deployment

---

## 🆘 Troubleshooting

### ModuleNotFoundError for drf_spectacular

```bash
# Install missing packages
pip install -r requirements-pinned.txt
```

### Rate limiting not working

Check if cache is configured:

```python
# Add to settings.py if missing
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake',
    }
}
```

### API documentation returns 401

Add authentication header:

```bash
curl -H "Authorization: Token YOUR_TOKEN" \
  http://localhost:8000/api/v1/schema/
```

### Backup command not found

Create management command directories:

```bash
mkdir -p app/core/management/commands
touch app/core/management/__init__.py
touch app/core/management/commands/__init__.py
```

---

## 📚 Additional Resources

- [Django 5.0 Release Notes](https://docs.djangoproject.com/en/5.0/releases/5.0/)
- [drf-spectacular Documentation](https://drf-spectacular.readthedocs.io/)
- [Django REST Framework Rate Limiting](https://www.django-rest-framework.org/api-guide/throttling/)
- [pytest-django Documentation](https://pytest-django.readthedocs.io/)

---

## ✅ Verification Commands

```bash
# Verify Django version
python -c "import django; print(django.VERSION)"

# Verify Python version
python --version

# Run all checks
python manage.py check --deploy

# Test database connection
python manage.py dbshell

# Run tests
pytest -v

# Check API documentation
curl http://localhost:8000/api/v1/schema/

# Test rate limiting
for i in {1..10}; do curl http://localhost:8000/health/; done
```

---

**Status:** ✅ Django 5.x Ready

**Date:** April 24, 2026

**Next Steps:**
1. Review and test all changes locally
2. Update deployment scripts if needed
3. Plan and schedule production upgrade
4. Monitor closely after deployment
