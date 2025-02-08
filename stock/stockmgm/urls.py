from django.urls import path
from stockmgm import views

urlpatterns = [
    path('',views.home,name="home"),
    path('list/', views.list_item, name='list'), 
    path('add/', views.add_item, name='add_item'),
    path('update/<str:pk>/', views.update_items, name="update_items"),
    path('delete/<str:pk>/', views.delete_items, name="delete_items"),
]