# Development Best Practices Guide

This guide outlines best practices for developing and maintaining the Altaviz Backend.

## Environment Configuration

### Local Development Setup

1. **Create a Python virtual environment:**
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Copy and configure environment file:**
```bash
cp .env.example .env
# Edit .env with your local settings
```

4. **Run migrations:**
```bash
cd app
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

### Using Docker

```bash
# Build and run
docker compose up --build

# View logs
docker compose logs -f app

# Access container shell
docker compose exec app python manage.py shell

# Run management commands
docker compose exec app python manage.py migrate
```

## Code Style & Quality

### Python Code Style

Follow PEP 8 guidelines:
- 4 spaces for indentation (not tabs)
- Max line length: 100 characters
- Use meaningful variable names
- Add docstrings to functions and classes

### Django-Specific Guidelines

1. **View Classes:**
```python
class MyAPIView(generics.RetrieveUpdateAPIView):
    """Clear docstring explaining the view's purpose"""
    serializer_class = MySerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]
    
    def get_queryset(self):
        """Override to filter data based on user"""
        return MyModel.objects.filter(user=self.request.user)
```

2. **Models:**
```python
class MyModel(models.Model):
    """Model docstring"""
    name = models.CharField(max_length=255, help_text="User's full name")
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = "My Models"
    
    def __str__(self):
        return self.name
```

3. **Serializers:**
```python
class MySerializer(serializers.ModelSerializer):
    """Serializer docstring"""
    class Meta:
        model = MyModel
        fields = ['id', 'name', 'created_at']
        read_only_fields = ['id', 'created_at']
```

### Code Linting

```bash
# Check code style
flake8 app/

# Fix common style issues
black app/  # requires: pip install black

# Type checking
mypy app/  # requires: pip install mypy
```

## API Design Standards

### RESTful Endpoints

Follow REST conventions:
- `GET /api/v1/resource/` - List all resources (paginated)
- `POST /api/v1/resource/` - Create new resource
- `GET /api/v1/resource/{id}/` - Retrieve specific resource
- `PATCH /api/v1/resource/{id}/` - Update resource (partial)
- `PUT /api/v1/resource/{id}/` - Replace resource (full)
- `DELETE /api/v1/resource/{id}/` - Delete resource

### Response Format

**Success Response:**
```json
{
    "id": 1,
    "name": "Example",
    "created_at": "2024-04-24T10:00:00Z"
}
```

**Error Response:**
```json
{
    "error": {
        "detail": "Not found.",
        "code": "not_found"
    },
    "status_code": 404
}
```

### Pagination

All list endpoints return paginated results:
```json
{
    "count": 100,
    "next": "http://api.example.com/resource/?page=2",
    "previous": null,
    "results": [...]
}
```

## Security Best Practices

### Authentication & Permissions

1. **Always use authentication:**
```python
permission_classes = [permissions.IsAuthenticated]
authentication_classes = [authentication.TokenAuthentication]
```

2. **Only allow public endpoints when necessary:**
```python
permission_classes = [permissions.AllowAny]  # Document why!
```

3. **Protect user data:**
```python
def get_queryset(self):
    """Only return user's own data"""
    return self.request.user.resources.all()
```

### Secrets Management

**NEVER commit secrets!** Always use environment variables:

```python
# ✅ GOOD
SECRET = os.getenv('MY_SECRET')

# ❌ BAD
SECRET = "hardcoded-value"
```

### Input Validation

Always validate user input:
```python
from rest_framework import serializers

class MySerializer(serializers.Serializer):
    email = serializers.EmailField()  # Automatic validation
    age = serializers.IntegerField(min_value=0, max_value=120)
    
    def validate_email(self, value):
        """Custom field validation"""
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already exists")
        return value
```

## Testing

### Writing Tests

```bash
# Run all tests
python manage.py test

# Run specific test file
python manage.py test app.tests.test_views

# Run with verbose output
python manage.py test -v 2

# Run with coverage
coverage run --source='.' manage.py test
coverage report
```

### Test Example

```python
from django.test import TestCase
from rest_framework.test import APIClient
from core.models import User

class UserAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            email='test@example.com',
            password='testpass123'
        )
    
    def test_get_user_list(self):
        response = self.client.get('/api/v1/users/')
        self.assertEqual(response.status_code, 200)
    
    def test_create_user(self):
        data = {
            'email': 'new@example.com',
            'password': 'newpass123'
        }
        response = self.client.post('/api/v1/users/', data)
        self.assertEqual(response.status_code, 201)
```

## Logging & Debugging

### Using Django's Logging

```python
import logging

logger = logging.getLogger(__name__)

# Log at different levels
logger.debug("Debug message")
logger.info("Info message")
logger.warning("Warning message")
logger.error("Error message")

# With extra context
logger.error(
    "User action failed",
    extra={'user_id': user.id, 'action': 'delete'}
)
```

### Debug Mode

```bash
# Check logs
docker compose logs app

# Follow logs in real-time
docker compose logs -f app

# Shell into container
docker compose exec app bash
```

## Database Migrations

### Creating Migrations

```bash
# Create new migration
python manage.py makemigrations app_name

# Review migration before applying
cat app/app_name/migrations/0001_*.py

# Apply migrations
python manage.py migrate
```

### Best Practices

1. Always review migrations before deploying
2. Test migrations on a copy of production data
3. Keep migrations small and focused
4. Write data migrations for complex changes
5. Never delete migration files (squash if needed)

## Deployment

### Pre-deployment Checklist

- [ ] All tests pass
- [ ] No uncommitted changes in git
- [ ] Environment variables configured
- [ ] Database backups created
- [ ] Static files collected
- [ ] Migrations reviewed and tested

### Deploying to Production

```bash
# Set environment variables
export DJANGO_SECRET_KEY="your-secret-key"
export DEBUG=False
export DATABASE_URL="postgres://user:pass@host:5432/db"

# Run migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput

# Start server
gunicorn app.wsgi:application --bind 0.0.0.0:8000
```

## Git Workflow

### Branch Naming

```
feature/add-user-api
bugfix/fix-login-issue
hotfix/security-patch
```

### Commit Messages

```
# Good commit message
Implement user profile endpoint

- Add UserProfile model
- Create ProfileSerializer
- Add GET/PATCH endpoints
- Add tests for new endpoints

# Bad commit messages
❌ fixed stuff
❌ wip
❌ stuff
```

### Pull Request Process

1. Create feature branch from `develop`
2. Make changes with meaningful commits
3. Write tests for new functionality
4. Update documentation
5. Create PR with clear description
6. Get code review approval
7. Merge to develop
8. Deploy to staging for testing
9. After verification, merge to main

## Common Tasks

### Creating a New App

```bash
python manage.py startapp myapp
```

### Creating a Management Command

```bash
# File: app/myapp/management/commands/mycommand.py
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Does something'
    
    def handle(self, *args, **options):
        # Your code here
        self.stdout.write(self.style.SUCCESS('Success!'))
```

Run with: `python manage.py mycommand`

### Checking for Security Issues

```bash
# Check for known vulnerabilities
pip install safety
safety check

# Django-specific security check
python manage.py check --deploy
```

## Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [PEP 8 Style Guide](https://www.python.org/dev/peps/pep-0008/)
- [Django Deployment Guide](https://docs.djangoproject.com/en/stable/howto/deployment/)

## Questions & Support

For questions or issues, refer to:
- Project README.md
- IMPROVEMENTS.md (recent changes)
- Django documentation
- Team wiki/documentation
