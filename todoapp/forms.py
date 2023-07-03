from .models import User
#from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']