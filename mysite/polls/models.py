from django.db import models

# Create your models here.


class Engineer(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    project = models.CharField(max_length=50)
    date_presence = models.DateTimeField('Date presence ')

    def __str__(self):
        return self.name

    def __str__(self):
        return self.surname
