from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path(
        "<int:patient_id>/exams",
        views.exams_by_patient_view,
        name="exams_by_patient_view",
    ),
]
