# cabinetMedical/views.py

from django.shortcuts import render


def all_links(request):
	return render(request, 'cabinetMedical/all_links.html')
