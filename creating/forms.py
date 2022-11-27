from django import forms
from creating.models import User
from django.core.exceptions import ValidationError

class UserInput(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__" #добавить поля формы явно
