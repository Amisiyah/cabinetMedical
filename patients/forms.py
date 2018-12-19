from django import forms
from .models import Patient


class PatientForm(forms.ModelForm):
	class Meta:
		fields = ['first_name', 'middle_name', 'last_name', 'email', 'pin', 'address', 'city', 'country']
		model = Patient
