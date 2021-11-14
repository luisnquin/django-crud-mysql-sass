from django.shortcuts import render
from django.http import HttpResponse

from .models import Employee
# Create your views here.


def index(request):
    alldata = Employee.objects.all()
    return render(request, "index.html", {"alldata": alldata})


def addEmployee(request):
    return HttpResponse("Estás tratando de añadir un empleado, huh")


def updateEmployee(request, id):
    return HttpResponse(f"Update, your ID is {id}")


def deleteEmployee(request, id):
    return HttpResponse(f"Delete, your ID is {id}")


def downloadCSVFile(request):
    return HttpResponse("Descargar el CSV eh, excel? Puag")
