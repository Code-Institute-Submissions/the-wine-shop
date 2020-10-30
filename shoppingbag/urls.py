from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_bag, name='view_bag'),
    path('add/<item_id>/', views.add_to_shoppingbag, name='add_to_shoppingbag'),
    path('amend/<item_id>/', views.amend_shoppingbag, name='amend_shoppingbag'),
    path('remove/<item_id>/', views.remove_from_shoppingbag, name='remove_from_shoppingbag'),
]
