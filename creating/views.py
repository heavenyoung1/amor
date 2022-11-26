from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def signupuser(request):
    '''Регистрация пользователя'''
    return render(request, 'creating/signupuser.html', {'form':UserCreationForm()})
