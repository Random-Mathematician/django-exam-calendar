from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("new/", views.newExam, name="new exam"),
    path("create-sd/", views.newSD, name="new SD"),
    path("<int:month>/", views.altmonth, name="altmonth"),
    path("submit", views.submit, name="submit"),
]
