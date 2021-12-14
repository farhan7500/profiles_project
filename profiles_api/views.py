from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters

from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions

class HelloAPIView(APIView):
    serializers_class = serializers.HelloSerializer

    def get(self, request, format=None):
        an_apiview = [
            'User HTTP methods as functions',
            'Is similar to a traditional django view',
            'Gives you the most control over uour application logic',
            'Is mapped manually to URLs'
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})

    def post(self, request):
        serializer = self.serializers_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        return Response({'method': 'DELETE'})

class HelloViewSet(viewsets.ViewSet):
    serializers_class = serializers.HelloSerializer

    def list(self, request):
        a_viewset = [
            'User HTTP methods as functions',
            'Is similar to a traditional django view',
            'Gives you the most control over uour application logic',
            'Is mapped manually to URLs. DROGBA',
        ]
        return Response({'message': 'Hello', 'a_viewset': a_viewset})

    def create(self, request):
        serializer = self.serializers_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        return Response({'method': 'GET'})

    def update(self, request, pk=None):
        return Response({'method': 'PUT'})

    def partial_update(self, request, pk=None):
        return Response({'method': 'PATCH'})

    def destroy(self, request, pk=None):
        return Response({'method': 'DELETE'})

class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()

    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email')
