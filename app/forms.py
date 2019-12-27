from django import forms
from .models import Users



class UsersForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['name','username', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }