from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render
from .models import NewEmployee
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required

def dashboard(request):
    # Here you can get any data you want to display on the dashboard
    # For now, we'll just pass the user object to the template
    return render(request, 'efl_passchange-page.html', {'user': request.user})

def home(request):
    return render(request, 'efl_home-page.html')

def about(request):
    return render(request, 'efl_about.html')

def contact(request):
    return render(request, 'efl_contact.html')

def data(request):
    return render(request, 'efl_data.html')

def forgotpassword(request):
    return render(request, 'efl_forgot-password.html')

def passchangepage(request):
    return render(request, 'efl_passchange-page.html')

def verifypage(request):
    return render(request, 'efl_verify-page.html')

def profilepage(request):
    return render(request, 'efl_profile-page.html')

def signuppage(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            employee = form.cleaned_data.get('employee')
            messages.success(request, f'Account created for {employee}!')
            return redirect('loginpage')
    else:
        form = UserRegisterForm()
    return render(request, 'efl_signup-page.html', {'form': form})

from .forms import LoginForm

from .forms import LoginForm

def loginpage(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            employee = form.cleaned_data.get('employee')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=employee, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'You are now logged in')
                if user.role == 'MNG':
                    return redirect('manager_dashboard')  # replace with the name of the view for the manager dashboard
                elif user.role == 'CEO':
                    return redirect('ceo_dashboard')  # replace with the name of the view for the CEO dashboard
                else:
                    return redirect('home')  # replace 'home' with the name of the view you want to redirect to after login for regular employees
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = LoginForm()
    return render(request, 'efl_login-page.html', {'form': form})

def is_admin(user):
    return user.is_superuser