from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView, View
from .models import MedicalFile, Patient


def patient_list(request):
	template_name = "patients/patient_list.html"
	queryset = Patient.objects.all()
	context = {
		"object_list": queryset
	}
	return render(request, template_name, context)


class PatientList(ListView):

	queryset = Patient.objects.all()

	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(*args, **kwargs)
		return context


class PatientDetail(DetailView):
	model = Patient
