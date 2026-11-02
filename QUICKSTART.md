# Quick Start Guide - Altaviz Backend

Get up and running with the improved Altaviz Backend in minutes.

## Prerequisites

- Docker & Docker Compose installed
- OR Python 3.8+ with pip
- Git

---

## 🚀 Quick Start with Docker (Recommended)

### Step 1: Clone and Setup
```bash
# Navigate to project directory
cd altavizbackend

# Copy environment template
cp .env.example .env

# Edit configuration (required!)
nano .env
```

### Step 2: Configure Environment

Edit `.env` with your values:
```env
# Django Settings
DJANGO_SECRET_KEY=your-secure-random-key-here
DEBUG=False
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1

# Database (local PostgreSQL)
DB_NAME=altaviz_db
DB_USER=postgres
DB_PASSWORD=your-db-password

# Email Configuration
EMAIL_HOST=your-mail-server.com
EMAIL_PORT=465
EMAIL_HOST_USER=your-email@example.com
EMAIL_HOST_PASSWORD=your-email-password
EMAIL_USE_TLS=False
EMAIL_USE_SSL=True

# Optional incident/task email notifications
TODO_MAIL_BACKENDS_ENABLED=True
TODO_MAIL_BACKEND_SLUGS=faultcalls
TODO_MAIL_BACKEND=smtp
TODO_MAIL_FROM_ADDRESS=alerts@yourdomain.com

# Optional incoming Gmail worker for creating/updating incident tasks by email
TODO_MAIL_TRACKERS_ENABLED=True
TODO_MAIL_TRACKER_NAMES=faultcalls
TODO_MAIL_TRACKER_FAULTCALLS_GROUP=Fault Calls
TODO_MAIL_TRACKER_FAULTCALLS_TASK_LIST_SLUG=faultcalls
TODO_MAIL_TRACKER_FAULTCALLS_INPUT_FOLDER=INBOX
GMAIL_CLIENT_SECRET_FILE=/path/to/credentials.json
GMAIL_CREDS_FILE=/path/to/gmail_token.json

# CORS
CORS_ALLOWED_ORIGINS=http://localhost:3000

# Admin Contact
ADMIN_EMAIL=admin@yourdomain.com
```

### Step 3: Start Services
```bash
# Build and start containers
docker compose up --build

# In another terminal, create superuser
docker compose exec app python manage.py createsuperuser
```

### Step 4: Verify Setup
```bash
# Check health
curl http://localhost:8000/health/

# Expected response:
# {"status": "healthy", "message": "Application is running normally"}

# Access application
open http://localhost:8000
```

### Step 5: Access Admin
```bash
# Navigate to admin panel
open http://localhost:8000/admin

# Login with superuser credentials
```

---

## 🐍 Local Python Setup (Development)

### Step 1: Create Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Setup Environment
```bash
# Copy template
cp .env.example .env

# Edit for local development
nano .env
```

### Step 4: Initialize Database
```bash
cd app
python manage.py migrate
python manage.py createsuperuser
```

### Step 5: Run Development Server
```bash
python manage.py runserver
```

### Step 6: Access Application
```bash
open http://localhost:8000
```

---

## 📋 Common Tasks

### View Logs
```bash
# Docker logs
docker compose logs -f app

# Database logs
docker compose logs -f db
```

### Run Management Commands
```bash
# Create migration
docker compose exec app python manage.py makemigrations

# Apply migrations
docker compose exec app python manage.py migrate

# Create superuser
docker compose exec app python manage.py createsuperuser

# Django shell
docker compose exec app python manage.py shell
```

### Access Database
```bash
# Connect to PostgreSQL
docker compose exec db psql -U postgres -d altaviz_db

# Or with local psql
psql -h localhost -U postgres -d altaviz_db
```

### Stop Services
```bash
# Stop and remove containers
docker compose down

# Stop and remove with volumes
docker compose down -v
```

---

## 🔍 Verify Everything Works

### Check Health Endpoint
```bash
curl http://localhost:8000/health/
```

Expected: `{"status": "healthy", ...}`

### Check Admin Interface
```bash
curl -u admin:password http://localhost:8000/admin/
```

Expected: 200 status

### Check API Authentication
```bash
# Get API token
curl -X POST http://localhost:8000/api-token-auth/ \
  -H "Content-Type: application/json" \
  -d '{"username":"admin","password":"password"}'
```

---

## 🐛 Troubleshooting

### Database Connection Failed
```bash
# Check if PostgreSQL is running
docker compose ps

# Restart services
docker compose restart db app

# Check logs
docker compose logs db
```

### Email Configuration Issues
```bash
# Test email settings with Django shell
docker compose exec app python manage.py shell

# In shell:
from django.core.mail import send_mail
send_mail(
    'Test Subject',
    'Test Body',
    'from@example.com',
    ['to@example.com'],
    fail_silently=False,
)
```

### Port Already in Use
```bash
# Change port in docker-compose.yml or use different port
docker compose up -d -p 8001:8000 app
```

### Permission Denied on .env
```bash
# Fix permissions
chmod 600 .env
```

---

## 📚 Documentation

- **Full Changes:** See [IMPROVEMENTS.md](IMPROVEMENTS.md)
- **Development Guide:** See [DEVELOPMENT.md](DEVELOPMENT.md)
- **Detailed Checklist:** See [IMPLEMENTATION_CHECKLIST.md](IMPLEMENTATION_CHECKLIST.md)
- **Original Docs:** See [README.md](README.md)

---

## 🚨 Security Checklist

Before deploying to production:

- [ ] Change DJANGO_SECRET_KEY
- [ ] Set DEBUG=False
- [ ] Configure DJANGO_ALLOWED_HOSTS
- [ ] Setup HTTPS/SSL
- [ ] Configure email credentials
- [ ] Set secure CORS origins
- [ ] Create database backups
- [ ] Run security checks: `python manage.py check --deploy`
- [ ] Update dependencies: `pip install -r requirements-pinned.txt`

---

## 📞 Support

### Common Issues

**Issue:** `psycopg2 connection refused`
```bash
# Ensure DB service is running
docker compose logs db
# May need to wait: docker compose up --wait
```

**Issue:** `Secret key not set`
```bash
# Ensure .env file exists and has DJANGO_SECRET_KEY
cat .env | grep DJANGO_SECRET_KEY
```

**Issue:** `Port 8000 already in use`
```bash
# Kill process on port 8000 or use different port
lsof -i :8000
kill -9 <PID>
```

---

## ✅ Next Steps

After successful setup:

1. **Review Documentation**
   - Read IMPROVEMENTS.md for security changes
   - Read DEVELOPMENT.md for coding standards

2. **Run Tests**
   ```bash
   docker compose exec app python manage.py test
   ```

3. **Start Development**
   - Create a feature branch
   - Follow guidelines in DEVELOPMENT.md

4. **Deploy**
   - Use docker-compose in production
   - Set environment variables appropriately
   - Monitor health endpoint

---

## 🎉 You're Ready!

Your Altaviz Backend is now:
- ✅ Secure (environment-based secrets)
- ✅ Observable (logging & health checks)
- ✅ Well-documented
- ✅ Production-ready
- ✅ Developer-friendly

Start building amazing features!

---

**Last Updated:** April 24, 2026
**Status:** ✅ Ready for Development & Production
