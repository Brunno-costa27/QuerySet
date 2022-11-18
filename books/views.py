from django.http import HttpResponse
from django.shortcuts import render

from books.forms import PatientForm
from books.models import Offer, Patients, Request


def userTableAll(request):
    
    patient = Patients.objects.all()
    requests = Request.objects.all()
    offers = Offer.objects.all()
    
    entidades = {
        "patient": patient,
        "offer": offers,
        "request": requests
    }
    
    return render(request, 'tabela.html', entidades)

def cadastroPatient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if  form.is_valid():
            form.save()
    else:
        form = PatientForm()
    
    return render(request, 'form.html', { 'form': form })
    