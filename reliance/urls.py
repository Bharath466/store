from django.urls import path
from . import views

urlpatterns=[path('home/',views.home,name='home'),
             path('customer/',views.customer,name='customer'),
             path('products/',views.products,name='products'),
             ]