from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from .forms import RegistrationForm, loginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

# USER REGISTRATION VIEW 
def registrationView(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')
    if request.method == 'POST':
        fm = RegistrationForm(request.POST)
        if fm.is_valid():
            messages.success(request, "Account Created Successfully")
            fm.save()
            return HttpResponseRedirect('/')
    else:
        fm = RegistrationForm()
    return render(request, 'accounts/registration.html', {'form': fm})


# USER LOGIN VIEW
def loginView(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')
    if request.method == 'POST':
        fm = loginForm(request=request, data=request.POST)

        if fm.is_valid():
            user_name = fm.cleaned_data['username']
            password = fm.cleaned_data['password']

            # authenticate the user and get the user instance
            user = authenticate(username= user_name, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login Successful')
                return HttpResponseRedirect('/')
    else:
        fm = loginForm()
    return render(request, 'accounts/login.html', {'form': fm})


# LOGOUT VIEW
def logoutView(request):
    logout(request)
    messages.success(request, 'Logout Successful')
    return HttpResponseRedirect('/accounts/login')


