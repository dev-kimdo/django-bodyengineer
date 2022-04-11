from multiprocessing import context
import re
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from platformdirs import user_runtime_path

# Create your views here.

def sign_up(request):
    context = {}

    if request.method == 'POST':
        if (request.POST.get('username') and 
            request.POST.get('password') and 
            request.POST.get('password') == request.POST.get('password_check') 
            # request.POST.get('chk1') == 1 and
            # request.POST.get('chk2') == 2 and
            # request.POST.get('chk3') == 3 
        ):
            
            new_user = User.objects.create_user(
                username = request.POST.get('username'),
                password = request.POST.get('password'),
                email = request.POST.get('email'),
            )

            auth.login(request, new_user)
            return redirect('sites:main')

        else:
            context['error'] = '아이디와 비밀번호 또는 동의하기를 다시 확인해주세요'

    return render(request, 'accounts/sign_up.html', context)

def login(request):
    context ={}

    if request.method == 'POST':
        if request.POST.get('username') and request.POST.get('password'):

            user = auth.authenticate(
                request,
                username = request.POST.get('username'),
                password = request.POST.get('password'),
            )

            if user is not None:
                auth.login(request, user)
                return redirect('sites:main')
            
            else:
                context['error']='아이디와 비밀번호를 다시 확인하세요.'
        else:
            context['error']='아이디와 비밀번호를 다시 확인하세요.'
    return render(request, 'accounts/login.html', context)

def logout(request):
    if request.method == 'POST':
        auth.logout(request)

        return redirect('sites:main')
