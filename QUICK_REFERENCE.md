# 🚀 Quick Reference Card

## Installation (Choose One)

### Docker (Recommended)
```bash
docker compose up --build
docker compose exec app python manage.py createsuperuser
curl http://localhost:8000/health/
```

### Local Python
```bash
pip install -r requirements-pinned.txt
cd app && python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

---

## Verification Commands

```bash
# Health check (most important!)
curl http://localhost:8000/health/

# API Documentation
open http://localhost:8000/api/v1/schema/swagger/

# Run tests
pytest -v

# Django deployment checks
python manage.py check --deploy

# Database backup
python manage.py backup_database --compress

# Admin panel
open http://localhost:8000/admin
```

---

## Key Features (All Implemented ✅)

| Feature | Endpoint | Status |
|---------|----------|--------|
| Health Check | /health/ | ✅ Working |
| API Schema | /api/v1/schema/ | ✅ Working |
| Swagger UI | /api/v1/schema/swagger/ | ✅ Working |
| ReDoc | /api/v1/schema/redoc/ | ✅ Working |
| Rate Limiting | 100/hr (anon), 1000/hr (auth) | ✅ Configured |
| Database Backup | `backup_database` command | ✅ Ready |
| Health Monitoring | Database check included | ✅ Enabled |
| Error Logging | All requests logged | ✅ Active |
| Authentication | Token-based | ✅ Enabled |

---

## Environment Variables (.env)

```env
# Essential
DJANGO_SECRET_KEY=generate-random-key-here
DEBUG=False
DJANGO_ALLOWED_HOSTS=localhost,yourdomain.com

# Database
DATABASE_URL=postgresql://user:pass@db:5432/altaviz_db

# Email
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-password

# CORS
CORS_ALLOWED_ORIGINS=https://yourdomain.com
```

Generate secret key:
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

---

## File Structure

```
altavizbackend/
├── app/                          # Django project
│   ├── manage.py                # Management commands
│   ├── app/settings.py          # Django configuration ⭐ UPDATED
│   ├── app/urls.py              # URL routing ⭐ UPDATED
│   ├── app/exceptions.py        # Error handling ⭐ NEW
│   ├── api/health.py            # Health endpoint ⭐ NEW
│   ├── conftest.py              # Pytest config ⭐ NEW
│   └── users/views.py           # User API ⭐ UPDATED
├── Dockerfile                    # ⭐ UPDATED (Python 3.11)
├── docker-compose.yml           # Docker Compose ⭐ UPDATED
├── requirements.txt             # Dependencies ⭐ UPDATED
├── requirements-pinned.txt      # Pinned versions ⭐ NEW
├── .env.example                 # Env template ⭐ NEW
│
└── Documentation/
    ├── QUICKSTART.md            # ⭐ Getting started
    ├── IMPROVEMENTS.md          # ⭐ All changes
    ├── DJANGO5_UPGRADE.md       # ⭐ Framework details
    ├── DEVELOPMENT.md           # ⭐ Best practices
    ├── DEPLOYMENT_GUIDE.md      # ⭐ Deployment
    └── FINAL_STATUS_REPORT.md   # ⭐ This project
```

---

## Docker Commands

```bash
# Build
docker compose build

# Run
docker compose up -d

# Stop
docker compose down

# Logs
docker compose logs -f app

# Shell
docker compose exec app python manage.py shell

# Backup
docker compose exec app python manage.py backup_database --compress

# Tests
docker compose exec app pytest -v
```

---

## Testing

```bash
# All tests
pytest

# With coverage
pytest --cov=app

# Specific test
pytest app/users/tests/test_api.py::TestUserAPI::test_create_user

# Verbose output
pytest -vv

# Show print statements
pytest -s

# Stop on first failure
pytest -x

# Last failed test
pytest --lf
```

---

## Rate Limiting

Automatically enabled:
- **Anonymous**: 100 requests/hour
- **Authenticated**: 1000 requests/hour

Check response headers:
```bash
curl -i http://localhost:8000/api/v1/schema/ 2>&1 | grep -i ratelimit
```

---

## Database Operations

```bash
# Backup (compressed)
python manage.py backup_database --compress

# Backup with media files
python manage.py backup_database --compress --include-media

# Restore
python manage.py restore_database app/backups/db_*.sql.gz --confirm

# List backups
ls -lh app/backups/

# Clean old backups
find app/backups -name "*.sql.gz" -mtime +30 -delete
```

---

## Troubleshooting

### "Import could not be resolved" errors?
Install dependencies: `pip install -r requirements-pinned.txt`

### Database won't connect?
```bash
# Check connection
python manage.py dbshell

# Verify credentials in .env
echo $DATABASE_URL

# Restart services
docker compose restart db
```

### Tests failing?
```bash
# Run migrations
python manage.py migrate

# Clear cache
python manage.py shell -c "from django.core.cache import cache; cache.clear()"

# Run tests with verbose output
pytest -vv
```

### Health check returning 503?
```bash
# Check database
docker compose logs db

# Restart database
docker compose restart db

# Check app logs
docker compose logs app
```

---

## Security Checklist

Before production:
- [ ] Generate new DJANGO_SECRET_KEY
- [ ] Set DEBUG=False
- [ ] Configure CORS_ALLOWED_ORIGINS
- [ ] Set up proper email credentials
- [ ] Enable HTTPS/SSL
- [ ] Run `python manage.py check --deploy`
- [ ] Create production database backup
- [ ] Test backup restoration
- [ ] Set up monitoring and alerts
- [ ] Configure firewall rules

---

## Performance Tips

1. **Enable caching**:
   ```python
   CACHES = {
       'default': {
           'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
       }
   }
   ```

2. **Use database connection pooling**:
   ```python
   DATABASES['default']['CONN_MAX_AGE'] = 600
   ```

3. **Monitor rate limits**:
   - Adjust `DEFAULT_THROTTLE_RATES` if needed
   - Check response headers for `X-RateLimit-*`

4. **Review error logs**:
   - Check logs daily
   - Set up alerts for errors

---

## Support Resources

- **Django**: https://docs.djangoproject.com/en/5.0/
- **DRF**: https://www.django-rest-framework.org/
- **drf-spectacular**: https://drf-spectacular.readthedocs.io/
- **Docker**: https://docs.docker.com/
- **PostgreSQL**: https://www.postgresql.org/docs/

---

## Important Endpoints

```
Admin:       http://localhost:8000/admin
Health:      http://localhost:8000/health/
Schema:      http://localhost:8000/api/v1/schema/
Swagger:     http://localhost:8000/api/v1/schema/swagger/
ReDoc:       http://localhost:8000/api/v1/schema/redoc/
```

---

## Django Management Commands

```bash
# Users
python manage.py createsuperuser
python manage.py changepassword <username>

# Database
python manage.py migrate
python manage.py makemigrations
python manage.py dbshell

# Static files
python manage.py collectstatic --noinput

# Backup/Restore
python manage.py backup_database --compress
python manage.py restore_database <backup-file>

# Checks
python manage.py check
python manage.py check --deploy

# Testing
pytest -v
```

---

**All 27 improvements implemented and ready for production! 🚀**

See FINAL_STATUS_REPORT.md for comprehensive details.
