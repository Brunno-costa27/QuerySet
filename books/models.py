from django.db import models


class Patients(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=40)
    
    def __str__(self):
        return self.name
    
class Request(models.Model):
    medicament = models.CharField(max_length=50)
    quant = models.IntegerField()
    type = models.CharField(max_length=40)
    status = models.IntegerField()
    patient =  models.ForeignKey(Patients, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    
    def __str__(self):
        return self.medicament

class Offer(models.Model):
    medicament = models.CharField(max_length=50)
    quant = models.IntegerField()
    type = models.CharField(max_length=50)
    price = models.FloatField()
    status = models.IntegerField()
    requests = models.ForeignKey(Request, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.medicament
