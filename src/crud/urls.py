from django.urls import path
from .views import formularyAddUpdate, index, formularyAddUpdate, addEmployee, updateEmployee, deleteEmployee, downloadCSVFile


app_name = 'crud'
urlpatterns = [
    path('', index),
    path('formulary/<str:method>/<int:id>/', formularyAddUpdate, name="formulary"),
    path('add/', addEmployee, name="add-e"),
    path('update/<int:id>/', updateEmployee, name="update-e"),
    path('delete/<int:id>/', deleteEmployee, name="delete-e"),
    path('download/csv/', downloadCSVFile, name="download-csv"),
]
