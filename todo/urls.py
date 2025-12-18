from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_list, name='todo_list'),
    path('add/', views.todo_create, name='todo_create'),
    path('view/<int:id>/', views.todo_view, name='todo_view'),
    path('edit/<int:id>/', views.todo_edit, name='todo_edit'),
    path('delete/<int:id>/', views.todo_delete, name='todo_delete'),
]
