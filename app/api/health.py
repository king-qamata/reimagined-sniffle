"""
Health check endpoint for monitoring application status
"""
from django.http import JsonResponse
from django.views import View
from django.db import connection


class HealthCheckView(View):
    """
    Health check endpoint for application monitoring
    Returns 200 if app is healthy, 503 if database is unavailable
    """

    def get(self, request):
        """Check application health"""
        try:
            # Try to access the database
            with connection.cursor() as cursor:
                cursor.execute("SELECT 1")
            return JsonResponse({
                'status': 'healthy',
                'message': 'Application is running normally'
            }, status=200)
        except Exception as e:
            return JsonResponse({
                'status': 'unhealthy',
                'message': f'Database error: {str(e)}'
            }, status=503)
