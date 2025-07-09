from django.db import models


class Doctor(models.Model):
    name = models.CharField(max_length=200)
    specialty = models.CharField(max_length=100)

    def __str__(self):
        return self.name

