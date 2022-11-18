from django import forms

from books.models import Patients


class PatientForm(forms.ModelForm):
    
    class Meta:
        model = Patients
        fields = '__all__'
