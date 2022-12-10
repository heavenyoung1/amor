from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .forms import UserInput
from django.db import IntegrityError
from django.contrib.auth import login

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

def desc_form(request):
    '''Страница с формой'''
    return render(request, 'creating/desc_form.html', {'form':UserInput()})

