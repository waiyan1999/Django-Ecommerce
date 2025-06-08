from django.urls import path
from myapp.views import *

urlpatterns = [
    path('',indexView, name = 'index'),
    path('base/',baseView, name = 'base'),
    path('cart/<int:id>', cartView , name = 'cart'),
    path('productlist/', productListView , name = 'productlist'),
    path('cart/', cartView , name = 'cart' ,),
    path('checkout/', checkOutView , name = 'checkout'),
    path('addtocart/', addToCart , name = 'addtocart'),
    path('productdetail/<int:id>/', productDetailView , name = 'productdetail'),
    path('deletecartproduct/<int:id>/', deleteCartProduct , name = 'deletecartproduct'),
    path('login', loginView , name = 'login')
]