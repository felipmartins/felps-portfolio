from django import forms
from tasks.models import User


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["name", "email"]
        labels = {
            "name": "Nome",
            "email": "E-mail",
        }
