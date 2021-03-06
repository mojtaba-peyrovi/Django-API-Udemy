from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken

from . import serializers
from . import models
from . import permissions
# Create your views here.
class HelloApiView(APIView):
    """ test API view"""
    serializer_class = serializers.HelloSerializer
    def get(self, request, format=None):
        """ returns a list of APIView features """
        an_apiview = [
            'Users HTTP methods as function(get,post,put,patch,delete)',
            'It is similar to a traditional django view',
            'gives you the most control over your logic',
            'is mapped manually to URLs'
        ]
        return Response({'an_apiview': an_apiview, 'message':'hello', })

    def post(self, request):
        """create a hello message with our name"""
        serializer = serializers.HelloSerializer(data=request.data)

        # data validation
        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message':message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def put(self, request, pk=None):
        """Handles Updating an Object"""
        return Response({'method': 'put'})

    def patch(self, request, pk=None):
        """Patch request only updates fields provided in the request"""
        return Response({'method': 'patch'})

    def delete(self, request, pk=None):
        """deletes an object"""
        return Response({'method': 'delete'})
class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""
    serializer_class = serializers.HelloSerializer
    def list(self, request):
        """Rerturns a hello message"""
        a_viewset = [
            'Uses actions(list, create, retrieve, update, partial_update)',
            'automatically maps to URLs using routers',
            'provides more functionality with less code'
        ]
        return Response({'message':'Hello!', 'a_viewset':a_viewset})
    def create(self, request):
        """create a new hello message"""

        serializer = serializers.HelloSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message':message})
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def retrieve(self, request, pk=None):
        """handles getting an object by its id"""
        return Response({'http_method':'GET'})
    def update(self, request, pk=None):
        """hendles updating an object"""
        return Response({'http_method':'PUT'})
    def partial_update(self, request, pk=None):
        """ handles updating part of an object"""
        return Response({'http_method':'PATCH'})
    def destroy(self, request, pk=None):
        """ handles deleting an object"""
        return Response({'http_method':'DELETE'})

class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles creating, reading, updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.object.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','email',)
class LoginViewSet(viewsets.ViewSet):
    """Checks email and password and returns an auth token"""
    serializer_class = AuthTokenSerializer

    def create(self, request):
        """Use the ObtainAuthToken APIView to validate and create a token"""
        return ObtainAuthToken().post(request)
