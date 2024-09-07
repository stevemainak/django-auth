# from django.shortcuts import render
# from rest_framework.generics import GenericAPIView
# from authentication.serializers import LoginSerializer, RegisterSerializer
# from rest_framework import response, status
# from django.contrib.auth import authenticate
# from rest_framework.permissions import AllowAny
# from django.contrib import auth

# class RegisterAPIVIew(GenericAPIView):
#     serializer_class = RegisterSerializer

#     def post(self, request):
#         serializer = self.serializer_class(data=request.data)
#         print(f'response is {request.data}')

#         if serializer.is_valid():
#             serializer.save()
#             return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        
#         return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class LoginAPIVIew(GenericAPIView):
#     permission_classes = [AllowAny,]
#     serializer_class = LoginSerializer

#     def post(self, request):
#         email = request.data.get('email', None)
#         password = request.data.get('password', None)
#         print(email)
#         print(password)

#         user = auth.authenticate(email=email, password=password)
#         print(user)

#         if user:
#             serializer = self.serializer_class(user)
#             return response.Response(serializer.data, status=status.HTTP_200_OK)
        
#         return response.Response({'message': "Invalid credentials, try again"}, status=status.HTTP_401_UNAUTHORIZED)


from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from authentication import serializers
from authentication.serializers import LoginSerializer, RegisterSerializer
from rest_framework import response, status, permissions
from rest_framework.permissions import AllowAny
from django.contrib import auth


class AuthUserAPIVIew (GenericAPIView):

    permission_classes = (permissions.IsAuthenticated,)
    
    
    def get(self,request):
        user=request.user
        serializer = RegisterSerializer(user)
        return response.Response({'user':serializer.data})


class RegisterAPIVIew(GenericAPIView):
    authentication_classes = []
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        print(f'response is {request.data}')

        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginAPIVIew(GenericAPIView):
    authentication_classes = []
    permission_classes = [AllowAny,]
    serializer_class = LoginSerializer

    def post(self, request):
        email = request.data.get('email', None)
        password = request.data.get('password', None)
        print(email)
        print(password)

        # Use the User model's custom manager to authenticate
        user = auth.authenticate(request, username=email, password=password)
        print(user)

        if user:
            serializer = self.serializer_class(user)
            return response.Response(serializer.data, status=status.HTTP_200_OK)
        
        return response.Response({'message': "Invalid credentials, try again"}, status=status.HTTP_401_UNAUTHORIZED)
