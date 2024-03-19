from django.urls import path
from todo_app import views

urlpatterns = [
    path('add-todo/', views.add_todo, name='add_todo'),
    path('update-todo/<int:id>/', views.update_todo, name='update_todo'),
    path('delete-todo/<int:id>/', views.delete_todo, name='delete_todo'),
    path('', views.todo_list, name='todo_list'),
]