from django.urls import path
from . import views

urlpatterns = [
    path('check/<int:pk>',views.Todolist.as_view()),
    path('create/',views.Detailtodo.as_view()),
    
]