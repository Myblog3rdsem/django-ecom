from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username is already taken')
                return redirect('userAuths:register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email is already taken')
                    return redirect('userAuths:register')
                else:
                    user = User.objects.create_user(
                        username=username, email=email, password=password)
                    user.save()
                    messages.success(request, 'Account created successfully')
                    auth.login(request, user)
                    return redirect('core:index')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('userAuths:register')
    context = {}
    return render(request, 'userAuths/register.html', context)

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = auth.authenticate(
            request,
            username=username,
            password=password
        )
        
        if user is not None:
            auth.login(request, user)
            return redirect('core:index')
        else:
            messages.error(request, 'Username or password is incorrect')
            return redirect('userAuths:login')
    context = {}
    return render(request, 'userAuths/login.html', context)

def logoutUser(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('core:index')
    return redirect('userAuths:login')


