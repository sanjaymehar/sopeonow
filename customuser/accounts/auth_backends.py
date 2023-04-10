from django.contrib.auth.backends import BaseBackend
from .models import Seller, Customer, Admin, Delivery


class MultiUserModelBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        user = None

        if email is not None:
            try:
                user = Seller.objects.get(email=email)
            except Seller.DoesNotExist:
                try:
                    user = Customer.objects.get(email=email)
                except Customer.DoesNotExist:
                    try:
                        user = Admin.objects.get(email=email)
                    except Admin.DoesNotExist:
                        try:
                            user = Delivery.objects.get(email=email)
                        except Delivery.DoesNotExist:
                            pass
        if user is not None and user.password ==password:
            return user

    def get_user(user_id):
        try:
            return Seller.objects.get(pk=user_id)
        except Seller.DoesNotExist:
            try:
                return Customer.objects.get(pk=user_id)
            except Customer.DoesNotExist:
                try:
                    return Admin.objects.get(pk=user_id)
                except Admin.DoesNotExist:
                    try:
                        return Delivery.objects.get(pk=user_id)
                    except Delivery.DoesNotExist:
                        pass
