"""
Django management command for backing up the database

Usage:
    python manage.py backup_database
    python manage.py backup_database --output /path/to/backup.sql
    python manage.py backup_database --compress
"""
import os
import subprocess
import gzip
from datetime import datetime
from django.core.management.base import BaseCommand
from django.conf import settings
from django.db import connection


class Command(BaseCommand):
    help = 'Backup the PostgreSQL database'

    def add_arguments(self, parser):
        parser.add_argument(
            '--output',
            type=str,
            help='Output file path',
            default=None,
        )
        parser.add_argument(
            '--compress',
            action='store_true',
            help='Compress the backup file',
        )
        parser.add_argument(
            '--include-media',
            action='store_true',
            help='Also backup media files',
        )

    def handle(self, *args, **options):
        """Execute the backup"""
        # Get database configuration
        db_config = settings.DATABASES['default']
        
        if db_config['ENGINE'] != 'django.db.backends.postgresql':
            self.stdout.write(
                self.style.ERROR('This command only supports PostgreSQL databases')
            )
            return

        # Generate backup filename
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        db_name = db_config['NAME']
        
        if options['output']:
            backup_file = options['output']
        else:
            backup_dir = os.path.join(settings.BASE_DIR, 'backups')
            os.makedirs(backup_dir, exist_ok=True)
            backup_file = os.path.join(backup_dir, f'{db_name}_{timestamp}.sql')

        # Prepare pg_dump command
        env = os.environ.copy()
        if db_config['PASSWORD']:
            env['PGPASSWORD'] = db_config['PASSWORD']

        pg_dump_cmd = [
            'pg_dump',
            '-h', db_config.get('HOST', 'localhost'),
            '-p', str(db_config.get('PORT', 5432)),
            '-U', db_config.get('USER', 'postgres'),
            '-d', db_name,
            '--verbose'
        ]

        try:
            self.stdout.write(
                self.style.SUCCESS(f'Starting database backup to {backup_file}...')
            )

            if options['compress']:
                # Backup with compression
                with gzip.open(f'{backup_file}.gz', 'wb') as gz_file:
                    with subprocess.Popen(
                        pg_dump_cmd,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        env=env
                    ) as process:
                        gz_file.write(process.stdout.read())
                        _, stderr = process.communicate()
                        
                        if process.returncode != 0:
                            raise Exception(f'pg_dump error: {stderr.decode()}')
                
                self.stdout.write(
                    self.style.SUCCESS(f'✓ Database backed up and compressed to {backup_file}.gz')
                )
            else:
                # Backup without compression
                with open(backup_file, 'w') as f:
                    with subprocess.Popen(
                        pg_dump_cmd,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        env=env
                    ) as process:
                        f.write(process.stdout.read().decode())
                        _, stderr = process.communicate()
                        
                        if process.returncode != 0:
                            raise Exception(f'pg_dump error: {stderr.decode()}')
                
                self.stdout.write(
                    self.style.SUCCESS(f'✓ Database backed up to {backup_file}')
                )

            # Get file size
            if options['compress']:
                file_size = os.path.getsize(f'{backup_file}.gz')
                self.stdout.write(f'Backup size: {file_size / 1024 / 1024:.2f} MB (compressed)')
            else:
                file_size = os.path.getsize(backup_file)
                self.stdout.write(f'Backup size: {file_size / 1024 / 1024:.2f} MB')

            # Backup media files if requested
            if options['include_media']:
                self._backup_media(timestamp)

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'✗ Backup failed: {str(e)}'))
            raise

    def _backup_media(self, timestamp):
        """Backup media files"""
        media_root = settings.MEDIA_ROOT
        
        if not os.path.exists(media_root):
            self.stdout.write(self.style.WARNING('Media directory not found, skipping media backup'))
            return

        backup_dir = os.path.join(settings.BASE_DIR, 'backups')
        media_backup = os.path.join(backup_dir, f'media_{timestamp}.tar.gz')

        try:
            subprocess.run(
                ['tar', '-czf', media_backup, '-C', media_root, '.'],
                check=True,
                capture_output=True
            )
            
            file_size = os.path.getsize(media_backup)
            self.stdout.write(
                self.style.SUCCESS(f'✓ Media files backed up to {media_backup}')
            )
            self.stdout.write(f'Media backup size: {file_size / 1024 / 1024:.2f} MB')
            
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'✗ Media backup failed: {str(e)}'))
