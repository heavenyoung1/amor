from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .forms import UserInput

def signupuser(request):
    '''Регистрация пользователя'''
    return render(request, 'creating/signupuser.html', {'form':UserCreationForm()})

def desc_form(request):
    '''Страница с формой'''
    return render(request, 'creating/desc_form.html', {'form':UserInput()})

