from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .forms import UserInput
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate


def home(request):
    return render(request, 'creating/home.html')

def loginuser(request):
    if request.method == 'GET':
        return render(request, 'creating/loginuser.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'creating/loginuser.html', {'form': AuthenticationForm(), 'error': 'Такого пользователя нет'})
        else:
            login(request, user)
            return redirect('desc_form')
def signupuser(request):
    '''Регистрация пользователя'''
    if request.method == 'GET':
        return render(request, 'creating/signupuser.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('desc_form')
            except IntegrityError:
                return render(request, 'creating/signupuser.html',{'form': UserCreationForm(), 'error': 'Такое имя уже существует'})

        else:
            return render(request, 'creating/signupuser.html', {'form': UserCreationForm(), 'error': 'Пароли не совпадают'})

def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')

def desc_form(request):
    '''Страница с формой'''
    return render(request, 'creating/desc_form.html', {'form':UserInput()})

