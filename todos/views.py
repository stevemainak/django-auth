from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions, filters
from todos.models import Todo
from todos.serializers import TodoSerializer
from django_filters.rest_framework import DjangoFilterBackend

class TodosAPIView(ListCreateAPIView):
    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends=[DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    filterset_fields=['id','title', 'description','is_completed']
    search_fields=['id','title', 'description','is_completed']
    ordering_fields=['id','title', 'description','is_completed']


    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    queryset = Todo.objects.all()

    def get_queryset(self):
        return Todo.objects.filter(owner=self.request.user)

class TodoDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = "id"

    def get_queryset(self):
        return Todo.objects.filter(owner=self.request.user)

# class CreateTodoAPIView(CreateAPIView):
#     serializer_class = TodoSerializer
#     permission_classes = (IsAuthenticated,)

#     def perform_create(self, serializer):
#         return serializer.save(owner=self.request.user)

# class TodolistAPIView(ListAPIView):
#     serializer_class = TodoSerializer
#     permission_classes = (IsAuthenticated,)

#     queryset = Todo.objects.all()

#     def get_queryset(self):
#         return Todo.objects.filter(owner=self.request.user)
    