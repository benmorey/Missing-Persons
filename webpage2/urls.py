from django.urls import path
from .views import webPage2View

urlpatterns = [
    path('', webPage2View)
]