from django.urls import path
from . import views

app_name = 'website'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('products/rice/', views.rice, name='rice'),
    path('products/spices/', views.spices, name='spices'),
    path('products/wood/', views.wood, name='wood'),
    path('products/agro/', views.agro, name='agro'),
    path('products/', views.all_products, name='all_products'),
]

