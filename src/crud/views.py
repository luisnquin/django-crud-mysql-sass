from django.shortcuts import render

from .models import Employee
# Create your views here.


def index(request):
    alldata = Employee.objects.all()
    return render(request, "index.html", {"alldata": alldata})
