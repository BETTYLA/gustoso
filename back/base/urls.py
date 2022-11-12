from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.index),
    path('products', views.products),
    path('products/<id>', views.products),

  # signin
    path('login', views.MyTokenObtainPairView.as_view()),
    # signup
    path('register', views.register),

    # test login...
    path('test', views.test_members),
    # path('buy_product', views.buy_product),
    # path('getAllProducts', views.getAllProducts),
    # path('getMyCart', views.getMyCart),
   

]

