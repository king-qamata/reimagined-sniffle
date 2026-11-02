"""
Django management command for restoring a database backup

Usage:
    python manage.py restore_database /path/to/backup.sql
    python manage.py restore_database /path/to/backup.sql.gz
"""
import os
import subprocess
import gzip
from django.core.management.base import BaseCommand
from django.conf import settings


class Command(BaseCommand):
    help = 'Restore a PostgreSQL database from a backup'

    def add_arguments(self, parser):
        parser.add_argument(
            'backup_file',
            type=str,
            help='Path to the backup file',
        )
        parser.add_argument(
            '--confirm',
            action='store_true',
            help='Skip confirmation prompt',
        )

    def handle(self, *args, **options):
        """Execute the restore"""
        backup_file = options['backup_file']

        if not os.path.exists(backup_file):
            self.stdout.write(
                self.style.ERROR(f'Backup file not found: {backup_file}')
            )
            return

        # Get database configuration
        db_config = settings.DATABASES['default']
        
        if db_config['ENGINE'] != 'django.db.backends.postgresql':
            self.stdout.write(
                self.style.ERROR('This command only supports PostgreSQL databases')
            )
            return

        db_name = db_config['NAME']

        # Confirmation
        if not options['confirm']:
            self.stdout.write(
                self.style.WARNING(f'WARNING: This will overwrite the database "{db_name}"')
            )
            response = input('Are you sure? Type "yes" to continue: ')
            if response.lower() != 'yes':
                self.stdout.write(self.style.ERROR('Restore cancelled'))
                return

        # Prepare psql command
        env = os.environ.copy()
        if db_config['PASSWORD']:
            env['PGPASSWORD'] = db_config['PASSWORD']

        psql_cmd = [
            'psql',
            '-h', db_config.get('HOST', 'localhost'),
            '-p', str(db_config.get('PORT', 5432)),
            '-U', db_config.get('USER', 'postgres'),
            '-d', db_name,
        ]

        try:
            self.stdout.write(
                self.style.SUCCESS(f'Starting database restore from {backup_file}...')
            )

            # Read backup file
            if backup_file.endswith('.gz'):
                with gzip.open(backup_file, 'rb') as gz_file:
                    backup_data = gz_file.read()
            else:
                with open(backup_file, 'rb') as f:
                    backup_data = f.read()

            # Restore database
            with subprocess.Popen(
                psql_cmd,
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                env=env
            ) as process:
                _, stderr = process.communicate(input=backup_data)
                
                if process.returncode != 0:
                    raise Exception(f'psql error: {stderr.decode()}')

            self.stdout.write(
                self.style.SUCCESS(f'✓ Database restored from {backup_file}')
            )

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'✗ Restore failed: {str(e)}'))
            raise
