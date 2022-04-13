from django.urls import path

from base import views 

app_name='base'

urlpatterns = [
    path('',views.home, name='home'),
    path('product/<str:pk>', views.singleProduct, name="single-product"),
    path('product/<str:pk>/cart-add', views.cart, name="cart-add"),
     
]