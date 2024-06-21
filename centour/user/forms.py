from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CentourUser

class CentourUserCreationForm(UserCreationForm):
    class Meta:
        model = CentourUser
        fields = ('email', 'username')