from django import forms
from django.core.validators import validate_slug
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.contrib.auth.forms import AuthenticationForm

from .models import WhiteBoard

# User Registration Form
class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "First Name"}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Last Name"}))
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"placeholder": "Username"}))
    email = forms.EmailField(label = "Email", widget=forms.TextInput(attrs={"placeholder": "Email"}), required=True)
    password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={"placeholder": "Password"}))
    password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={"placeholder": "Password Confirmation"}))

    class Meta:
        model = User
        fields = ["first_name","last_name","username","email","password1","password2"]

    #def save(self,commit=True):
    #   user = super(RegistrationForm,self).save(commit=False)
    #    user.email = self.cleaned_data["email"]
    #    user.first_name = self.cleaned_data["first_name"]
    #    user.last_name = self.cleaned_data["last_name"]
    #   if commit:
    #        user.save()
    #    return user


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Username"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Password"}))

# Create Whiteboard Form
class WhiteboardForm(forms.Form):
    subject = forms.CharField(label='Subject', max_length=30)
    # If checked, the whiteboard is open to the public
    #public = forms.BooleanField()
    #if public == True:
    whiteboard_key = forms.IntegerField(label='Whiteboard Password')
    class Meta:
        model = WhiteBoard
        fields = ['subject','whiteboard_key']


