from django.shortcuts import render
from .serializers import TodoSerializers
from .models import Todo
from rest_framework.generics import RetrieveUpdateDestroyAPIView , ListCreateAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly

class Todolist(RetrieveUpdateDestroyAPIView):
    queryset=Todo.objects.all()
    serializer_class=TodoSerializers
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticatedOrReadOnly]

class Detailtodo(ListCreateAPIView):
    queryset=Todo.objects.all()
    serializer_class=TodoSerializers
    authentication_CLASSES=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
