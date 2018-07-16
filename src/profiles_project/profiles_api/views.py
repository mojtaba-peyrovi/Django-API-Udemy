from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import serializers
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
