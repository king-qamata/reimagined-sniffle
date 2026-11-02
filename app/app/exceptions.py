"""
Custom exception handlers and middleware for better error handling and logging
"""
import logging
from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status

logger = logging.getLogger(__name__)


def custom_exception_handler(exc, context):
    """
    Custom exception handler for DRF that logs exceptions and returns formatted responses
    """
    # Get the standard exception response
    response = exception_handler(exc, context)

    # Log the exception
    logger.error(
        f"Exception occurred: {exc.__class__.__name__}",
        exc_info=True,
        extra={
            'view': context.get('view'),
            'request': context.get('request'),
        }
    )

    # Customize the response format
    if response is not None:
        # Add request ID or trace ID for debugging
        response.data = {
            'error': response.data if isinstance(response.data, dict) else {'detail': str(response.data)},
            'status_code': response.status_code,
        }
    else:
        # Handle exceptions not caught by DRF
        response = Response(
            {
                'error': 'An unexpected error occurred',
                'status_code': status.HTTP_500_INTERNAL_SERVER_ERROR,
            },
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

    return response


class RequestLoggingMiddleware:
    """
    Middleware to log all HTTP requests and responses
    """

    def __init__(self, get_response):
        self.get_response = get_response
        self.logger = logging.getLogger(__name__)

    def __call__(self, request):
        # Log incoming request
        self.logger.info(
            f"{request.method} {request.path}",
            extra={
                'method': request.method,
                'path': request.path,
                'user': str(request.user),
                'ip': self._get_client_ip(request),
            }
        )

        response = self.get_response(request)

        # Log outgoing response
        self.logger.info(
            f"Response: {response.status_code}",
            extra={
                'status_code': response.status_code,
                'method': request.method,
                'path': request.path,
            }
        )

        return response

    @staticmethod
    def _get_client_ip(request):
        """Get client IP address from request"""
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
