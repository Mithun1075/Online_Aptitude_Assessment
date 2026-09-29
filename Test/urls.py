from django.urls import path
from . import views

urlpatterns = [

    path("", views.register, name="register"),
    path("register-success/", views.register_success, name="register_success"),
    path("assessment/", views.assessment, name="assessment"),
    path("submit/", views.submit_test, name="submit"),
    path("result/", views.result, name="result"),
    path("finish/", views.finish, name="finish"),

]