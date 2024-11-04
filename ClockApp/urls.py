from django.urls import path
from . import views

urlpatterns = [
    path("", views.digital_clock, name="digit_clock"),

]
