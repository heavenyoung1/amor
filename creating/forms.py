from django import forms
from creating.models import User

class UserInput(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__" #добавить поля формы явно

    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) < $
