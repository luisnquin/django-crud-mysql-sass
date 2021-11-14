from django.shortcuts import render, redirect
from django.http import HttpResponse

import csv

from .models import Employee
# Create your views here.


def index(request):
    alldata = Employee.objects.all()
    return render(request, "index.html", {"alldata": alldata})


def formularyAddUpdate(request, method: str, id=""):
    if method == "update":
        target = Employee.objects.get(id=id)
        return render(request, "add-update-formulary.html", {"method": method, "id": id, "target": target})

    return render(request, "add-update-formulary.html", {"method": method, "id": id})


def addEmployee(request):
    new_data = [request.POST.get("firstname"),
                request.POST.get("lastname"),
                request.POST.get("email"),
                request.POST.get("phone"),
                request.POST.get("location"),
                request.POST.get("university")]

    if None in new_data:
        return HttpResponse("Data not inserted, there was a shortage.")

    Employee.objects.create(first_name=new_data[0],
                            last_name=new_data[1],
                            email=new_data[2],
                            phone=new_data[3],
                            location=new_data[4],
                            university=new_data[5])

    return redirect("/crud/")


def updateEmployee(request, id):
    target = Employee.objects.get(id=id)
    new_data = [request.POST.get("firstname"),
                request.POST.get("lastname"),
                request.POST.get("email"),
                request.POST.get("phone"),
                request.POST.get("location"),
                request.POST.get("university")]

    if None in new_data:
        return HttpResponse("New data not inserted, there was a shortage.")

    target.first_name = new_data[0]
    target.last_name = new_data[1]
    target.email = new_data[2]
    target.phone = new_data[3]
    target.location = new_data[4]
    target.university = new_data[5]

    target.save()

    return redirect("/crud/")


def deleteEmployee(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()

    return redirect("/crud/")


def downloadCSVFile(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="database-data.csv"'

    writer = csv.writer(response)
    writer.writerow(['Firstname', 'lastname', 'email',
                    'phone', 'location', 'university'])

    employees_data = Employee.objects.all()
    for employee in employees_data:
        writer.writerow([employee.first_name,
                         employee.last_name,
                         employee.email,
                         employee.phone,
                         employee.location,
                         employee.university])

    return response
