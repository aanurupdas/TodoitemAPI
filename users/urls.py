from django.urls import path
from users.api.views import (
    RegisterView,
    LoginView,
    TodoCreate,
    TodoDelete,
    TodoRetrieve,
    TodoList,
    TodoUpdate,
)


urlpatterns = [
    path("register", RegisterView.as_view()),
    path("login", LoginView.as_view()),
    path("getall", TodoList.as_view()),
    path("create", TodoCreate.as_view()),
    path("get/<int:pk>", TodoRetrieve.as_view()),
    path("put/<int:pk>", TodoUpdate.as_view()),
    path("delete/<int:pk>", TodoDelete.as_view()),
]
