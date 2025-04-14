from django.urls import path
from .views import registerapi

urlpatterns = [
    path("register/", registerapi.as_view(), name="register")
]