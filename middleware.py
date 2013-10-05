from django.http import HttpResponse
from django.conf import settings

allow_headers = getattr(settings, 'CORS_ALLOW_HEADERS', 'Content-Type, Authorization')
origin_allow_all = getattr(settings, 'CORS_ORIGIN_ALLOW_ALL', False)


class CorsMiddleware(object):
    def process_request(self, request):
        if request.method == 'OPTIONS':
            return HttpResponse()

    def process_response(self, request, response):
        origin = request.META.get('HTTP_ORIGIN')
        if origin:
            response['Access-Control-Allow-Origin'] = "*" if origin_allow_all else origin
            response['Access-Control-Allow-Methods'] = 'POST, GET, OPTIONS, DELETE, PUT, PATCH'
            response['Access-Control-Allow-Headers'] = allow_headers
        return response
