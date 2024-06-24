from django.urls import path
from . import views

app_name= 'shop'

urlpatterns = [
     path('', views.index, name='index'),
     path('index.html', views.index),
     path('contact.html', views.contact, name='contact'),
     path('account.html', views.account, name='account'),
     path('account', views.account),
     path('contact', views.contact),
     path('logout', views.logout_view, name='logout'),
     path('men.html', views.men, name ='men'),
     path('men', views.men),
     path('stripee.html', views.stripee, name='stripee'),
     path('products.html', views.products, name='products'),
     path('products', views.products),
     path('register.html', views.register, name='register'),
     path('register', views.register),
     path('update_item/', views.updateItem, name="update_item"),
     path('women.html', views.women, name='women'),
     path('women', views.women),
     path('checkout.html', views.checkout, name='checkout'),
     path('checkout', views.checkout),
     path('cart_ad.html', views.cart_ad, name='cart_ad'),
     path('cart_ad', views.cart_ad),
     path('product/<int:product_id>/', views.single, name='single'),
]