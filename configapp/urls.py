from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_category/', views.add_category, name='add_category'),
    path('category/<int:pk>/', views.detail_category, name='detail_category'),
    path('category/update/<int:pk>/', views.update_category, name='update_category'),
    path('category/delete/<int:pk>/', views.del_category, name='del_category'),
]
