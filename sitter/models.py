from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.utils import timezone

from myauth.models import CustomUser


# Create your models here.

class Day(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Sitter(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True, related_name='child_sitter')
    date_of_birth = models.DateField(null=True, blank=True)
    payment = models.FloatField(null=True, blank=True)
    experience = models.IntegerField(null=True, blank=True)
    working_days = models.ManyToManyField(Day)

    def __str__(self):
        return "%s (%s)" % (
            self.user.username,
            ", ".join(day.name for day in self.working_days.all()),
        )



