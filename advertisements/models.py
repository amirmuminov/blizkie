from django.db import models
from myauth.models import CustomUser
from patient.models import Patient
from sitter.models import Sitter


# Create your models here.
class Advertisement(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    sex = models.CharField(max_length=50)
    age = models.IntegerField()
    weight = models.IntegerField(null=True, blank=True)
    decease = models.CharField(max_length=200)
    contact_name = models.CharField(max_length=100)
    contact_mail = models.EmailField(max_length=100)
    street = models.CharField(max_length=100)
    comments = models.CharField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    requests = models.ManyToManyField(Sitter)

    def __str__(self):
        return "%s (%s)" % (
            self.pk,
            ", ".join(sitter.user.username for sitter in self.requests.all()),
        )
