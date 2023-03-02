from django.urls import path
from . import views

from rest_framework.authtoken.views import obtain_auth_token

### from rest_framework import routers

urlpatterns = [
    path('register/',views.RegisterAPIView.as_view()),
    path('login/',obtain_auth_token),
    path('users/',views.UsersAPIView.as_view()),
    path('notes/create/',views.CreateNotesAPIView.as_view()),
    path('notes/get/',views.GetNotesAPIView.as_view()),
    path('notes/detail/<int:pk>', views.GetNotesDetailAPIView.as_view()),
    path('notes/update/<int:pk>',views.UpdateNotesAPIView.as_view()),
]