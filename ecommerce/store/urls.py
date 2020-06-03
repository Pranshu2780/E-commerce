from django.urls import path
from . import views

urlpatterns = [

    path('',views.store,name="store"),
    path('checkout/',views.checkout,name="checkout"),
    path('cart/',views.cart,name="views")
]