from django.urls import path
from . import views
from .views import update_new, del_new, detail_new, add_new

urlpatterns = [
    path('', views.home, name='home'),

    path('add_category/', views.add_category, name='add_category'),
    path('category/<int:pk>/', views.detail_category, name='detail_category'),
    path('category/update/<int:pk>/', views.update_category, name='update_category'),
    path('category/delete/<int:pk>/', views.del_category, name='del_category'),

    path('add_news/', add_new, name='add_news'),
    path('del_new/<int:pk>/', del_new, name='del_news'),
    path('detail_new/<int:pk>/', detail_new, name='detail_new'),
    path('update_new/<int:pk>/', update_new, name='update_new'),
]
