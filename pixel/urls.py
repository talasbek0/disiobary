from django.urls import path
from .views import CatProductsAPIView, ProductAPIView, OrderedAPIView

urlpatterns = [
    path('catProducts/', CatProductsAPIView.as_view(), name='Products'),
    path('product/', ProductAPIView.as_view(), name='product'),
    path('order/', OrderedAPIView.as_view(), name='order')
]