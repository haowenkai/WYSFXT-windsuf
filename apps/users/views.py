from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, UpdateView
from django.shortcuts import redirect, render
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User

class LoginView(APIView):
    permission_classes = [permissions.AllowAny]
    
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = User.objects.filter(username=username).first()
        
        if user and user.check_password(password):
            login(request, user)
            return Response({'message': '登录成功'})
        return Response({'message': '用户名或密码错误'}, status=400)

class LogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response({'message': '退出成功'})

class ProfileView(LoginRequiredMixin, UpdateView):
    model = User
    fields = ['username', 'email', 'phone', 'address']
    template_name = 'users/profile.html'
    
    def get_object(self):
        return self.request.user

class RegisterView(APIView):
    permission_classes = [permissions.AllowAny]
    
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')
        
        if User.objects.filter(username=username).exists():
            return Response({'message': '用户名已存在'}, status=400)
            
        user = User.objects.create_user(
            username=username,
            password=password,
            email=email
        )
        login(request, user)
        return Response({'message': '注册成功'})

class ChangePasswordView(LoginRequiredMixin, View):
    def post(self, request):
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')
        
        if not request.user.check_password(old_password):
            return Response({'message': '原密码错误'}, status=400)
            
        request.user.set_password(new_password)
        request.user.save()
        return Response({'message': '密码修改成功'})
