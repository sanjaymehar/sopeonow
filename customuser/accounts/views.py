from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib import messages


def login(request):

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)


        if user is not None :
            login_dict = {'id': user.id, 'email': user.email,"username":user.username}
            request.session['login_data'] = login_dict
            return redirect('dashboard')

        else:
            messages.error(request, 'Invalid login credentials')
    return render(request, 'login.html')


def dashboard(request):
    return render(request, 'dashboard.html')


def logout(request):
    del request.session['login_data']
    return redirect('login')