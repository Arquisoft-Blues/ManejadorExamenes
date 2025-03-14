from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.exams_view, name="exams_view"),
    path("<int:pk>/", views.exam_view, name="exam_view"),
]