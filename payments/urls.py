from django.urls import path
from .views import *
app_name="payments"


urlpatterns = [
	path('make_payment', initiate_payment, name='initiate_payment'),
    #path('payment', payment, name='payment'),
	#path('verify-payment/<str:ref>', verify_payment, name='verify_payment'),
]