from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import *

class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']

class ProjectsForm(forms.ModelForm):
	class Meta:
		model=Projects
		fields='__all__'
class ProjectBugForm(forms.ModelForm):
	class Meta:
		model=ProjectBug
		fields=['name','bug_description']


