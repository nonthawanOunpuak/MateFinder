from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
    username = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    year = models.IntegerField()

    def __str__(self):
        return f"{self.id}, {self.username}, {self.name},{self.password}, {self.email}, {self.phone}, {self.year}"


class RequestInformation(models.Model):
    username = models.CharField(max_length=255)
    name_req = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.id}, {self.username}, {self.name_req}"


class SentRequestInformation(models.Model):
    username = models.CharField(max_length=255)
    name_sent = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.id}, {self.username}, {self.name_sent}"


class DormInformation(models.Model):

    # username = models.ForeignKey(
    #     Student, on_delete=models.CASCADE, related_name="ustudent")
    username = models.CharField(max_length=255)
    name_dorm = models.CharField(max_length=255)
    details_dorm = models.CharField(max_length=255)
    type_dorm = models.CharField(max_length=255)
    price = models.IntegerField()
    light = models.BooleanField()
    timetosleep = models.CharField(max_length=255)
    pet = models.BooleanField()

    def __str__(self):
        return f"{self.id}, {self.username}, {self.name_dorm}, {self.details_dorm}, {self.type_dorm}, {self.price},{self.light}, {self.timetosleep},{self.pet}"
