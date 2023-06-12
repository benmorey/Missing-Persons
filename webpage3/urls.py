from django.urls import path
from .views import webPage3View

urlpatterns = [
    path('', webPage3View)
]