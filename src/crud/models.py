from django.db import models


# Create your models here.


class Employee(models.Model):
    first_name = models.CharField(max_length=30, verbose_name="Firstname")
    last_name = models.CharField(max_length=30, verbose_name="Lastname")
    email = models.EmailField(verbose_name="Email")
    phone = models.CharField(max_length=13, verbose_name="Phone number")
    location = models.CharField(max_length=50, verbose_name="Location")
    university = models.CharField(max_length=50, verbose_name="University")

    def __str__(self):
        return f"{self.first_name} {self.last_name} | {self.phone}"
