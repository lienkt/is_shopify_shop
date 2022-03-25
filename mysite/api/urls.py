from django.urls import path
from . import views

urlpatterns = [
    path('is_shopify_shop/', views.is_shopify_shop, name='is_shopify_shop'),
    path('first_missing_positive/', views.first_missing_positive, name='first_missing_positive'),
]