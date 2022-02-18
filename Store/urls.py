from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('detail/<str:pk>/', views.Details, name='detail'),
    path('cart/<str:pk>/', views.Cart, name='cart'),
]