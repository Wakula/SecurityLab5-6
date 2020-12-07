from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.shortcuts import render


from storage.forms import SecureRegistrationForm, LoginForm


def registration(request):
    if request.method == 'POST':
        form = SecureRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'storage/registration.html', {'form': form})
    return render(request, 'storage/registration.html', {'form': SecureRegistrationForm()})


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user:
                return HttpResponse('Authenticated successfully')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'storage/login.html', {'form': form})
