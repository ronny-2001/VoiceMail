from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import *
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

# def home(request):
    # return HttpResponse('<h1>Home</h1>')

# def register(request):
#     if request.method == "POST":
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             messages.success(request,f'Hi {username} your account is created successfully')
#             return redirect('home')
#     else:
#         form=UserCreationForm()

def home(request):
    return render(request,'users/home.html')

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hi {username} ,your account is created successfully')
            return redirect('home')
    else:
        form = UserRegisterForm()

    return render(request,'users/register.html',{'form':form})

@login_required()
def profile(request):
    return render(request, 'users/profile.html')