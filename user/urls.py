from django.contrib import admin
from django.urls import path

from user.controllers.controllers import \
    GetUserController, \
    CreateUserController, \
    UpdateUserController, \
    DeleteUserController, \
    TopPerformerUserController, \
    LoginUserController

urlpatterns = [
    path('getusers/', GetUserController.as_view()),
    path('createusers/', CreateUserController.as_view()),
    path('updateusers/', UpdateUserController.as_view()),
    path('deleteusers/', DeleteUserController.as_view()),
    path('top-performers/', TopPerformerUserController.as_view()),
    path('login/', LoginUserController.as_view())
]