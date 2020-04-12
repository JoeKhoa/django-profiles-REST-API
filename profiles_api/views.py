#   All source code

# https://github.com/LondonAppDev/profiles-rest-api


from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class HelloApiView(APIView):
    """Test APIView"""

    def get(self,request,format=None):
        """Return a list of APIView features"""

        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to traditional django View',
            'Gives you most control over your application logic',
            'Is mapped manually to URLs',
        ]
        return Response({
            'message':'Hello',
            'ap_apiview':an_apiview
        })
