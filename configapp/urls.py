from django.urls import path
from . import views

urlpatterns = [
    path('', views.universities_list, name='universities_list'),
    path('groups/<int:university_id>/', views.groups_list, name='groups_list'),
    path('students/<int:group_id>/', views.students_list, name='students_list'),
    path('student/add/<int:group_id>/', views.add_student, name='add_student'),
    path('student/delete/<int:student_id>/', views.delete_student, name='delete_student'),
]


