from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()


class Measurement(models.Model):
    temperature = models.FloatField(max_length=100.00, null=False)
    data_create = models.DateTimeField(auto_now_add=True)
    data_update = models.DateTimeField(auto_now=True)
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
