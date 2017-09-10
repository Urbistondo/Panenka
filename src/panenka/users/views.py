from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages

from .models import User
from .forms import UserForm


def users_signup(request):
    return render(request, 'users/signup.html')


def users_login(request):
    return render(request, 'users/login.html')


def users_create(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, 'Successfully created')
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        'form': form,
    }
    return render(request, 'users/signup.html', context)
