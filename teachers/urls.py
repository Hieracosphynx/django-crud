from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name = 'index-teachers'),
    path('create/', views.create, name = 'create-teachers')
]