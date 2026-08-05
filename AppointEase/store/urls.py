from django.urls import path

from .views import Login, Registration, test

urlpatterns = [

    path("registration/", Registration.as_view()),
    path("login/", Login.as_view()),

]
