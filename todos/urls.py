from django.urls import path
from todos.views import TodosAPIView,TodoDetailAPIView
from . import views

urlpatterns=[
    path("", views.TodosAPIView.as_view(), name="todos"),
    path('<int:id>', views.TodoDetailAPIView.as_view(), name="todo"),
    
]