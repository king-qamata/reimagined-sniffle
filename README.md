# Altaviz Backend

Altaviz Backend is a Django support desk for logging incidents, managing fault lists, assigning work, and tracking ticket progress across teams.

## What Changed In This UI Update

- Added a shared responsive UI layer for mobile and desktop
- Improved the main dashboard header so action buttons wrap cleanly on small screens
- Fixed the task list page so the Add Task button script no longer errors on the `mine` view
- Wrapped task tables and attachment areas so they scroll safely on phones
- Reworked the task detail page into a two-column responsive layout
- Replaced placeholder navigation content with real support desk shortcuts
- Updated the login experience to match the new branded layout
- Cleaned up broken support and register links in the older auth templates
- Swapped duplicate dashboard chart canvas ids for unique ones

## Tech Stack

- Django
- Django REST Framework
- Bootstrap 4 / Argon Dashboard assets
- PostgreSQL or SQLite depending on environment

## Local Setup

1. Create and activate a Python virtual environment.
2. Install dependencies:

```bash
python3 -m pip install -r requirements.txt
```

3. Run migrations:

```bash
python3 app/manage.py migrate
```

4. Start the development server:

```bash
python3 app/manage.py runserver
```

## Docker

You can also run the app with Docker Compose:

```bash
docker compose up --build
```

## Key Pages

- `/incidents/` - dashboard
- `/incidents/lists` - fault lists
- `/incidents/mine/` - tasks assigned to the current user
- `/incidents/ticket/add/` - add a ticket
- `/incidents/import_csv/` - import ticket data
- `/incidents/login` - sign in

## UI Notes

- `app/static/assets/css/custom-ui.css` contains the shared responsive overrides
- `app/templates/base.html` and `app/templates/layouts/base-fullscreen.html` now load the branded shell styles
- `app/static/assets/js/argon.js` now initializes every dashboard bar chart canvas

## Development Notes

- The project keeps the legacy Argon template structure, so most UI improvements are shared through the base templates.
- If you add new dashboard pages, prefer using the same responsive utility classes introduced in `custom-ui.css`.
