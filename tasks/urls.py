from django.urls import path
from tasks.views import index, visitor_login


urlpatterns = [
    path("", index, name="tasks-page"),
    path("login/", visitor_login, name="login-page"),
]
