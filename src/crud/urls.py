from django.urls import path
from .views import index


app_name = 'crud'
urlpatterns = [
    path('', index),
]
