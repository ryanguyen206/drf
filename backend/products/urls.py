from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductListCreateAPIView.as_view()),  # Use CreateAPIView for creating a product
    path('<int:pk>/', views.ProductDetailAPIView.as_view()), 
    path('<int:pk>/update/', views.ProductUpdateAPIView.as_view()),  # Use RetrieveAPIView for product details
    path('<int:pk>/delete/', views.ProductDeleteAPIView.as_view()),  # Use RetrieveAPIView for product details
]
