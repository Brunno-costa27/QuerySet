from django.http import HttpResponse
from django.shortcuts import render

from books.models import Offers, Patient, Requests


def userTableAll(request):
    
    patient = Patient.objects.all()
    requests = Requests.objects.all()
    offers = Offers.objects.all()
    
    entidades = {
        "patient": patient,
        "offer": offers,
        "request": requests
    }
    
    return render(request, 'tabela.html', entidades)

