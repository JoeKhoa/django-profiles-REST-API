#   All source code
# https://www.tma.vn/Hoi-dap/Cam-nang-nghe-nghiep/Con-duong-tro-thanh-cao-thu-Web-developer-ban-chon-huong-di-nao/6636
# https://github.com/LondonAppDev/profiles-rest-api


from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets

from profiles_api import serializers
from rest_framework import status



class HelloApiView(APIView):
    """""""""Test APIView"""""""""
    serializer_class = serializers.HelloSerializer

    def get(self,request,format=None):
        """""""""Return a list of APIView features"""""""""

        an_apiview = [
            'Uses http methods as function (get, post, patch, put, delete)',
            'Is similar to traditional django View',
            'Gives you most control over your application logic',
            'Is mapped manually to URLs',
        ]
        return Response({
            'message':'Hello',
            'ap_apiview':an_apiview
        })

    def post(self,request):
        """"""""" Create a hello message with our name """""""""
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
        """""""""Handling updating an object"""""""""
        return Response({'method':'PUT'})

    def patch(self,request,pk=None):
        """""""""Handling PARTIAL update of an Object"""""""""
        return Response({'method':'Patch'})

    def delete(self,request,pk=None):
        """""""""delete an object in database"""""""""
        return Response({'method':'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    serializer_class = serializers.HelloSerializer

    """""""""Test API ViewSet"""""""""
    def list(self,request):
        """list ALL object in DB"""
        a_viewset = [
            'Uses action {list, create, retrieve, update, partial_update}',
            'Automatically maps URL using Routers',
            'Provide more functionality with less code',
        ]
        return Response({
                        'message':'Hello',
                        'a_viewset':a_viewset
        })

    def create(self,request):
        """"""""" Create an object """""""""
        data_ = request.data
        print(data_)
        serializer = self.serializer_class(data=data_)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self,request,pk=None):
        """get object by pk=id"""
        return Response({ 'http_method':'GET'})

    def update(self,request,pk=None):
        """modify object by id like PUT"""
        return Response({'http_method':'PUT'})

    def partial_update(self,request,pk=None):
        """modify part of an object by its id"""
        return Response({'http_method':'PATCH'})

    def destroy(self,request,pk=None):
        """delete an object"""
        return Response({"http_method":'DELETE'})
