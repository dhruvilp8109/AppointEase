from django.urls import path

from .views import test

urlpatterns = [

    path("registration/", test.as_view()),


]
