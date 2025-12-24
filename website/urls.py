from django.urls import path
from . import views

app_name = 'website'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('products/rice/', views.rice, name='rice'),
    path('products/spices/', views.spices, name='spices'),
    path('products/plywood/', views.plywood, name='plywood'),
    path('products/industrial/', views.industrial, name='industrial'),
    path('products/safety-shoes/', views.safety_shoes, name='safety_shoes'),
    path('products/', views.all_products, name='all_products'),
    path('thank-you/', views.thank_you, name='thank_you'),
]

