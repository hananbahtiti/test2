from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import RegisterSerializer
from .services.user_service import UserService
from django.views import View
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import  RefreshToken
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.exceptions import ValidationError




# Create your views here.

class RegisterHTMLView(View):
    def get(self, request):
        return render(request, 'register.html')

class RegisterAPIView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data) 

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            user = UserService.create_user(
                name=serializer.validated_data['name'],
                email=serializer.validated_data['email'],
                password=serializer.validated_data['password']
            )
            return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
        except ValidationError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)



class LoginHTMLView(View):
    def get(self, request):
        return render(request, 'login.html')


class LoginAPIView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({"error": "Email not found"}, status=status.HTTP_401_UNAUTHORIZED)
        
        user = authenticate(username=user.username, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            refresh.set_exp(lifetime=3600)

            return Response(
                {"message": "Login successful",
                 "token":access_token},
                 status=status.HTTP_200_OK
            )
        else:
            return Response({"error": "Invalid password"}, status=status.HTTP_401_UNAUTHORIZED)