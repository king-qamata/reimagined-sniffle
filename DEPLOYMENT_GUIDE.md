# Deployment & Installation Guide

Complete guide to deploy the improved Altaviz Backend with all new features.

## 📋 Pre-Deployment Checklist

- [ ] Python 3.10+ installed locally
- [ ] Docker & Docker Compose installed (if using containers)
- [ ] PostgreSQL 13+ (if not using Docker)
- [ ] Git access to repository
- [ ] .env file configured
- [ ] All tests passing locally

---

## 🚀 Quick Deployment (5 minutes)

### Option A: Docker (Recommended)

```bash
# 1. Navigate to project
cd altavizbackend

# 2. Copy environment
cp .env.example .env

# 3. Edit configuration
nano .env

# 4. Build and run
docker compose up --build

# 5. In another terminal, create admin user
docker compose exec app python manage.py createsuperuser

# 6. Verify
curl http://localhost:8000/health/
```

### Option B: Local Python

```bash
# 1. Create virtual environment
python3 -m venv venv
source venv/bin/activate

# 2. Install dependencies
pip install -r requirements-pinned.txt

# 3. Configure environment
cp .env.example .env
nano .env

# 4. Setup database
cd app
python manage.py migrate
python manage.py createsuperuser

# 5. Run server
python manage.py runserver

# 6. Verify
curl http://localhost:8000/health/
```

---

## 🔧 Configuration

### Environment Variables (.env file)

```env
# Core Django
DJANGO_SECRET_KEY=<generate-random-key>
DEBUG=False
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1,yourdomain.com

# Database
DATABASE_URL=postgresql://user:password@db-host:5432/altaviz_db

# Email
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=mail.yourdomain.com
EMAIL_PORT=465
EMAIL_HOST_USER=alerts@yourdomain.com
EMAIL_HOST_PASSWORD=your-email-password
EMAIL_USE_TLS=False
EMAIL_USE_SSL=True

# CORS
CORS_ALLOWED_ORIGINS=https://yourdomain.com,https://www.yourdomain.com

# Admin
ADMIN_EMAIL=admin@yourdomain.com

# Logging
LOG_LEVEL=INFO
```

### Generate Secure Secret Key

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

---

## 🐳 Docker Deployment

### Building

```bash
# Build image
docker compose build

# Push to registry (optional)
docker tag altaviz-app registry.example.com/altaviz:latest
docker push registry.example.com/altaviz:latest
```

### Running

```bash
# Start services
docker compose up -d

# View logs
docker compose logs -f app

# Stop services
docker compose down

# Stop and remove volumes (WARNING: deletes data!)
docker compose down -v
```

### Scaling

```bash
# Run multiple app instances
docker compose up -d --scale app=3

# Behind a load balancer like nginx
# Configure nginx to round-robin to port 8000, 8001, 8002
```

---

## 📊 Post-Deployment Verification

### 1. Health Check

```bash
curl http://localhost:8000/health/

# Expected response:
# {"status": "healthy", "message": "Application is running normally"}
```

### 2. Admin Panel

```bash
open http://localhost:8000/admin
# Login with superuser credentials
```

### 3. API Documentation

```bash
# Swagger UI
open http://localhost:8000/api/v1/schema/swagger/

# ReDoc
open http://localhost:8000/api/v1/schema/redoc/

# Note: May need to add ?format=json for schema
open http://localhost:8000/api/v1/schema/?format=json
```

### 4. Run Tests

```bash
# Run full test suite
pytest -v

# Expected: All tests pass
# Coverage: 70%+
```

### 5. Create Backup

```bash
# Test backup functionality
python manage.py backup_database --compress

# Verify backup file created
ls -lh app/backups/
```

---

## 🔒 Security Configuration

### Before Going to Production

1. **Generate New Secret Key**
   ```bash
   export DJANGO_SECRET_KEY=$(python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())")
   ```

2. **Set DEBUG=False**
   ```env
   DEBUG=False
   ```

3. **Configure CORS Properly**
   ```env
   CORS_ALLOWED_ORIGINS=https://yourdomain.com
   ```

4. **Enable HTTPS**
   ```python
   # In settings.py
   SECURE_SSL_REDIRECT = True
   SESSION_COOKIE_SECURE = True
   CSRF_COOKIE_SECURE = True
   ```

5. **Setup Email Properly**
   - Use proper SMTP server
   - Use strong authentication credentials
   - Enable TLS/SSL

6. **Database Security**
   ```bash
   # Use strong password
   # Enable SSL for remote connections
   # Restrict firewall access
   ```

7. **Run Security Check**
   ```bash
   python manage.py check --deploy
   ```

---

## 📈 Performance Tuning

### Database Optimization

```python
# In settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'CONN_MAX_AGE': 600,  # Connection pooling
        'OPTIONS': {
            'connect_timeout': 10,
        }
    }
}
```

### Caching

```python
# Add Redis caching
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',
    }
}
```

### Static Files

```python
# Whitenoise for serving static files
# Already configured in settings.py
# Make sure to collect static files:
python manage.py collectstatic --noinput
```

### Rate Limiting Tuning

```python
# In settings.py, adjust as needed
'DEFAULT_THROTTLE_RATES': {
    'anon': '100/hour',     # Increase if needed
    'user': '1000/hour',    # Increase if needed
}
```

---

## 🔄 Maintenance Tasks

### Daily

```bash
# Check application health
curl https://yourdomain.com/health/

# Review error logs
docker compose logs app | grep ERROR
```

### Weekly

```bash
# Create backup
python manage.py backup_database --compress

# Verify backup integrity
python manage.py restore_database backups/last_backup.sql.gz --test

# Run database maintenance
python manage.py dbshell < maintenance.sql
```

### Monthly

```bash
# Review old backups, delete if needed
ls -lh app/backups/

# Update dependencies
pip list --outdated
pip install -r requirements-pinned.txt --upgrade

# Run full test suite
pytest --cov=app

# Review API usage metrics
# Check rate limiting stats
```

### Quarterly

```bash
# Full security audit
python manage.py check --deploy

# Dependency security check
safety check

# Database optimization
VACUUM ANALYZE;
```

---

## 🚨 Troubleshooting

### Application Won't Start

```bash
# Check logs
docker compose logs app

# Common issues:
# 1. Environment variables not set
# 2. Database connection failed
# 3. Invalid SECRET_KEY

# Fix:
# 1. Verify .env file
# 2. Check database connection
# 3. Generate new SECRET_KEY
```

### Database Connection Failed

```bash
# Check database service
docker compose ps db

# Restart database
docker compose restart db

# Check database logs
docker compose logs db

# Verify connection string
echo $DATABASE_URL
```

### Rate Limiting Not Working

```bash
# Check cache configuration
python manage.py shell

>>> from django.core.cache import cache
>>> cache.set('test', 'value')
>>> cache.get('test')

# If returns None, cache is not working
# Configure cache in settings.py
```

### Tests Failing

```bash
# Run with verbose output
pytest -vv

# Check for missing dependencies
pip install -r requirements-pinned.txt

# Check database
python manage.py migrate

# Re-run tests
pytest
```

---

## 📞 Support Commands

```bash
# Django checks
python manage.py check
python manage.py check --deploy

# Database info
python manage.py shell
>>> from django.db import connection
>>> print(connection.connection.server_version)

# List installed apps
python manage.py shell
>>> from django.conf import settings
>>> print(settings.INSTALLED_APPS)

# Clear cache
python manage.py shell
>>> from django.core.cache import cache
>>> cache.clear()

# Generate API schema
python manage.py spectacular --file openapi.json
```

---

## 📚 Additional Resources

- [Django Deployment Checklist](https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/)
- [Docker Best Practices](https://docs.docker.com/develop/dev-best-practices/)
- [PostgreSQL Administration](https://www.postgresql.org/docs/current/admin.html)
- [Django Security](https://docs.djangoproject.com/en/5.0/topics/security/)

---

## ✅ Deployment Verification Checklist

After deployment, verify:

- [ ] Health endpoint returns 200
- [ ] Admin panel accessible
- [ ] API documentation accessible
- [ ] Rate limiting working (test with multiple requests)
- [ ] Database backups working
- [ ] All tests passing
- [ ] Error logging functional
- [ ] CORS configured correctly
- [ ] HTTPS working (if applicable)
- [ ] Email notifications working
- [ ] Static files serving correctly
- [ ] Media files accessible
- [ ] Rate limit headers present in responses

---

## 🎯 Next Steps

1. **Day 1**: Deploy to staging, run full test suite
2. **Day 2-5**: Load test, performance tuning, security audit
3. **Day 6-7**: Deploy to production with monitoring
4. **Ongoing**: Monitor performance, collect metrics, optimize

---

**Deployment Guide Complete**

For issues or questions, refer to:
- `QUICKSTART.md` - Getting started
- `DEVELOPMENT.md` - Development guidelines
- `DJANGO5_UPGRADE.md` - Framework details
- `COMPLETE_IMPLEMENTATION_SUMMARY.md` - All improvements
