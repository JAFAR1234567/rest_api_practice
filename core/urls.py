from django.urls import path

from .import views

urlpatterns = [
    path('course/', views.course, name='course'),
    path('course/<int:pk>/', views.course, name='course'),
    # path('create_course', views.create_course, name='course'),
]
