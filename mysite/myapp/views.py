from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib import messages
from . import models
from . import forms

# Landing Page
def index(request):
    context = {
       "title":"Welcome to WhiteBoard",
    }
    return render(request,"myapp/index.html", context = context)

    # Server side validation of the user
    if request.user.is_authenticated:
        return redirect("/dashboard/")
    # User is not validated on srver side - redirect to login
    else:
        return render(request,"myapp/index.html", context = context)

# Register view
def register(request):
    #profile_instance = models.Profile.objects.all()
    if request.method == "POST":
        RF_instance = forms.RegistrationForm(request.POST)
        if RF_instance.is_valid():
            #profile_instance = models.Profile(first_name=RF_instance.cleaned_data["first_name"],
            #last_name=RF_instance.cleaned_data["last_name"],
            #username=RF_instance.cleaned_data["username"],
            #email=RF_instance.cleaned_data["email"])
            RF_instance.save()
            #first_name = RF_instance.cleaned_data.get('first_name')
            #messages.success(request, 'Your account has been created!')
            #profile_instance.save()
            return redirect("/login/")
    else:
        RF_instance = forms.RegistrationForm()
    context = {
        "registration_form":RF_instance,
        #"profile":profile_instance,
    }
    return render(request,"registration/register.html", context = context)


@csrf_exempt
@login_required(login_url='/login/')
def dashboard(request):
    #WF_instance = forms.WhiteboardForm()
    whiteboards = models.WhiteBoard.objects.all()
    context = {
        #"form": WF_instance,
        "whiteboards": whiteboards,
    }
    return render(request,"whiteboard/dashboard.html", context=context)


def submit(request):
    WF_instance = forms.WhiteboardForm(request.POST)
    if WF_instance.is_valid():
        #print("Valid")
        whiteboard = models.WhiteBoard(subject=WF_instance.cleaned_data["subject"],
        whiteboard_key=WF_instance.cleaned_data["whiteboard_key"])
        #whiteboard.user = request.user
        whiteboard.save()
        #WF_instance = forms.WhiteboardForm()
    return redirect('dashboard/')


# New Whiteboard View
def create_whiteboard(request):
    form_instance = forms.WhiteboardForm()
    #whiteboards = models.WhiteBoard.objects.all()
    context = {
        "form": form_instance,
    }
    return render(request,"whiteboard/whiteboardform.html", context=context)


# Whiteboard
@csrf_exempt
@login_required(login_url='/login/')
def whiteboard(request):
    # Server side validation of the user
    if request.user.is_authenticated:
        context = {
            "title":"Whiteboard", 
        }
        return render(request,"whiteboard/whiteboard.html", context = context)
    # User is not validated on srver side - redirect to login
    else:
        return redirect("/login/")


# Logout View
def logout_view(request):
    #logout(request)
#    context = {
#        "title":"Logout"
#    }
    return redirect("/")
    #return render(request,"registration/logout.html",context = context)

# Live Chat View - Django Channels


# Profile View
@csrf_exempt
@login_required(login_url='/login/')
def profile(request):
    if request.user.is_authenticated:
        context = {
        }
        return render(request, "profile.html", context = context)
    # User is not validated on srver side - redirect to login
    else:
        return redirect("/login/")

 
