from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name = 'index-teachers'),
    path('create/', views.create, name = 'create-teachers'),
    path('list/', views.listStudents, name = 'list-teachers'),
    path('update/<id>', views.update, name = 'update-teachers'),
    path('delete/<id>', views.delete, name = 'delete-teachers')
]