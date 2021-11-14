from django.urls import path
from .views import index, addEmployee, updateEmployee, deleteEmployee, downloadCSVFile


app_name = 'crud'
urlpatterns = [
    path('', index),
    path('add/', addEmployee, name="add-e"),
    path('update/<int:id>/', updateEmployee, name="update-e"),
    path('delete/<int:id>/', deleteEmployee, name="delete-e"),
    path('download/csv/', downloadCSVFile, name="download-csv"),
]
