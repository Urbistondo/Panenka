from django.shortcuts import render
from django.contrib.auth import authenticate, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages

from .models import User
# from .forms import UserForm


def users_signup(request):
    if request.method == 'GET':
        return render(request, 'users/signup.html')
    elif request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.create_user(email=email, password=password)
        if user is not None:
            authenticate(username=email, password=password)
            return render(request, 'users/dashboard.html')
        else:
            return render(request, 'panenka/404.html')


def users_signin(request):
    if request.method == 'GET':
        return render(request, 'users/signin.html')
    elif request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                return HttpResponseRedirect('/contests/list')
            return render(request, 'panenka/404.html')
        else:
            return render(request, 'panenka/404.html')


def users_logout(request):
    logout(request)
    return render(request, 'panenka/index.html')


def users_account(request):
    current_user = request.user
    return render(request, 'users/account.html', {'user': current_user})
