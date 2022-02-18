from django.shortcuts import render, redirect
from . forms import RegisterForm
from django.contrib import messages
# Create your views here.

def Register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created successfully!')
            return redirect('login')
    else:
        form = RegisterForm()    
    return render(request, 'Account/register.html', {'form': form})

def Login(request):
    return render(request, 'Account/login.html')