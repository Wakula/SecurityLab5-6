from django.contrib.auth import authenticate, login as auth_login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from storage.models import SecureUser
from storage.forms import SecureRegistrationForm, LoginForm, UserDataForm


def registration(request):
    if request.method == 'POST':
        form = SecureRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/storage/login/')
        return render(request, 'storage/registration.html', {'form': form})
    return render(request, 'storage/registration.html', {'form': SecureRegistrationForm()})


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user:
                auth_login(request, user)
                return redirect('/storage/users/')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'storage/login.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        form = UserDataForm(data=request.POST, instance=request.user)
        if form.is_valid():
            form.save()
        return render(request, 'storage/profile.html', {'form': form})
    username = request.user.username
    address = request.user.address
    return render(
        request,
        'storage/profile.html',
        {
            'form': UserDataForm(initial={
                'username': username,
                'address': address
            })
        })


@login_required
def users(request):
    if request.method == 'GET':
        return render(request, 'storage/users.html', {'users': SecureUser.objects.all()})
