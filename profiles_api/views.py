#   All source code
# https://www.tma.vn/Hoi-dap/Cam-nang-nghe-nghiep/Con-duong-tro-thanh-cao-thu-Web-developer-ban-chon-huong-di-nao/6636
# https://github.com/LondonAppDev/profiles-rest-api


from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from profiles_api import serializers
from rest_framework import status



class HelloApiView(APIView):
    """Test APIView"""
    serializer_class = serializers.HelloSerializer

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

    def post(self,request):
        """ Create a hello message with our name """
        serializer = self.serializer_class(data=request.data)
        # Like handle of modelForm
        if serializer.is_valid():
            name = serializer.validated_data.get('name')    #   validated_data == cleaned_data()???
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self,request,pk=None):
        """Handling updating an object"""
        return Response({'method':'PUT'})

    def patch(self,request,pk=None):
        """Handling PARTIAL update of an Object"""
        return Response({'method':'Patch'})

    def delete(self,request,pk=None):
        """delete an object in database"""
        return Response({'method':'DELETE'})
