from django.urls import path

from . import views


urlpatterns = [
    path('add/<int:product_id>/', views.add_product, name='add'),
    path('delete/<int:product_id>/', views.delete_product, name='delete'),
    path('subtract/<int:product_id>/', views.subtract_product, name='subtract'),
    path('clear/<int:product_id>/', views.clear_product, name='clear'),

]


