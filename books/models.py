from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=40)
    
class Requests(models.Model):
    medicament = models.CharField(max_length=50)
    quant = models.IntegerField()
    type = models.CharField(max_length=40)
    status = models.IntegerField()
    patient =  models.ForeignKey(Patient, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)

class Offers(models.Model):
    medicament = models.CharField(max_length=50)
    quant = models.IntegerField()
    type = models.CharField(max_length=50)
    price = models.FloatField()
    status = models.IntegerField()
    requests = models.ForeignKey(Requests, on_delete=models.CASCADE)
    
    
