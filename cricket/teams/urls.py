from django.urls import path

from . import views

urlpatterns = [
    path("home/", views.teams_data, name="teams_data"),
]