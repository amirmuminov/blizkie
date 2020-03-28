from django.db import models
from myauth.models import CustomUser


# Create your models here.

class Meal(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Toilet(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Mobility(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class MentalState(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class LevelSelfServ(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Place(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Patient(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True, related_name='child_patient')
    lss = models.ForeignKey(LevelSelfServ, on_delete=models.CASCADE)
    ms = models.ForeignKey(MentalState, on_delete=models.CASCADE)
    mobility = models.ForeignKey(Mobility, on_delete=models.CASCADE)
    toilet = models.ForeignKey(Toilet, on_delete=models.CASCADE)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
