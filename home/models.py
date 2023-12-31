from django.db import models


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    desc = models.TextField()

    def __str__(self):
        return self.name + " " + self.email
