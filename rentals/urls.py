from django.urls import path
from . import views

urlpatterns = [
    path('', views.catalog, name='catalog'),
    path('register/', views.register, name='register'), # Resolved NoReverseMatch
    path('my-dashboard/', views.user_dashboard, name='user_dashboard'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('product/<int:pk>/book/', views.book_product, name='book_product'),
]