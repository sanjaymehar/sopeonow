from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import User, Seller, Customer, Admin, Delivery



def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        #user = authenticate(request, email=email, password=password)
        user = User.objects.get(email=email, password=password)
        if user is not None:
            try:
                user = Seller.objects.get(email=email)
                return render(request, 'seller_home.html')
            except Seller.DoesNotExist:
                try:
                    user = Customer.objects.get(email=email)
                    return render(request, 'customer_home.html')
                except Customer.DoesNotExist:
                    try:
                        user = Admin.objects.get(email=email)
                        return render(request, 'admin_home.html')
                    except Admin.DoesNotExist:
                        try:
                            user = Delivery.objects.get(email=email)
                            return render(request, 'delivery_home.html')
                        except Delivery.DoesNotExist:
                            pass
        else:
            messages.error(request, 'Invalid email or password')
            return redirect('login')
    else:
        return render(request, 'login.html')

