from django.urls import path
from .views import webPage1View

urlpatterns = [
    path('', webPage1View)
]
