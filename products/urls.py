from django.urls import path
from . import views


app_name = 'products'

urlpatterns = [
    path('product-create/', views.create_product, name='create'),
    path('detail/<int:product_id>/', views.product_detail, name='detail'),
    path('category/', views.product_by_category, name='by_category')
]