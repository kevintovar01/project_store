from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import SignupForm



# Create your views here.


def login_view(request):
    """Login view."""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home:home')
        else:
            return render(request, 'login/login.html', {'error': 'Invalid username and password'})

    return render(request, 'login/login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('/customer/login/')


def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/customer/login/')
    else:
        form = SignupForm
    return render(request, 'login/signup.html', {'form':form})