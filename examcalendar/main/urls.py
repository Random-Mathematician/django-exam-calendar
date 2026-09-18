from django.urls import path
from django.contrib.auth import views as auth_view
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("new/", views.newExam, name="new_exam"),
    path("create-sd/", views.newSD, name="new_SD"),
    path("<int:month>/", views.altmonth, name="altmonth"),
    path("exam/<int:examid>", views.examdesc, name="exam_description"),
    path("submit/", views.submit, name="submit"),
    path("delete/", views.delete, name="delete"),
    path("login/", views.loginpage, name="login_page"),
    path("logging-in/", views.performlogin, name="processlogin"),
    path("logging-out/", views.performlogout, name="processlogout")
]
