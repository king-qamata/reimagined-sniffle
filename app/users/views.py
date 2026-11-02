from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate

from rest_framework import generics, authentication, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.settings import api_settings

from core import models
from core.models import User, Profile
from . import serializers
from .serializers import (
    UserSerializer,
    AuthTokenSerializer,
    UserSignupSerializer,
    UserSerializerLogin,
    UserSerializerCreate,
    ProfileSerializer,
    ProfileSerializerUpdate
)

class HomePageView(TemplateView):
    """Home page view"""
    template_name = 'home.html'


class ProfileView(APIView):
    """List all user profiles - Read-only public endpoint"""
    authentication_classes = []
    permission_classes = [permissions.AllowAny]
    queryset = models.Profile.objects.all()
    serializer_class = serializers.ProfileSerializer

    def get(self, request):
        """List profiles"""
        profiles = Profile.objects.all()
        return Response(ProfileSerializer(profiles, many=True).data)


class ProfileDetail(APIView):
    """Update user's own profile"""
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def patch(self, request, profile_id):
        """Update profile of authenticated user"""
        profile = get_object_or_404(Profile, pk=profile_id)
        if profile.user != request.user:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        serializer = ProfileSerializerUpdate(
            profile,
            data=request.data,
            context={'request': request},
            partial=True
        )
        if serializer.is_valid():
            profile = serializer.save()
            return Response(UserSerializerLogin(profile.user).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class UserListView(APIView):
    """List users and create new users"""
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer

    def get(self, request):
        """
        List all users - public endpoint
        Note: Consider restricting this to authenticated users only in production
        """
        users = User.objects.all()
        return Response(UserSerializer(users, many=True).data)

    def post(self, request):
        """Create a new user - public endpoint for registration"""
        serializer = UserSerializerCreate(data=request.data, context={'request': request})
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(serializer.validated_data['password'])
            user.save()
            Profile(user=user).save()
            return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system"""
    serializer_class = UserSerializer


class CreateTokenView(ObtainAuthToken):
    """Create a new auth token for user"""
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user"""
    serializer_class = UserSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        """Retrieve and return authentication user"""
        return self.request.user
