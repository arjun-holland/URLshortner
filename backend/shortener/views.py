from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .utils import create_short_url, get_long_url, urls_collection
import re

def is_valid_url(url):
    regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return re.match(regex, url) is not None

class ShortenURLView(APIView):
    def post(self, request):
        long_url = request.data.get('long_url')
        
        if not long_url:
            return Response({"error": "long_url is required"}, status=status.HTTP_400_BAD_REQUEST)
            
        if not is_valid_url(long_url):
            return Response({"error": "Invalid URL format"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            short_code = create_short_url(long_url)
            # In production, we'd use the actual domain. 
            # We'll return just the code and let frontend construct the full URL or we can return a relative path.
            short_url = f"/{short_code}" 
            return Response({"short_url": short_url, "short_code": short_code}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class RedirectURLView(APIView):
    def get(self, request, short_code):
        long_url = get_long_url(short_code)
        
        if long_url:
            # Use 302 Found for temporary redirect
            # Or 301 Moved Permanently if caching heavily
            response = Response(status=status.HTTP_302_FOUND)
            response['Location'] = long_url
            return response
            
        return Response({"error": "URL not found"}, status=status.HTTP_404_NOT_FOUND)


