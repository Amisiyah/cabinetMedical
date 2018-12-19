from django.conf.urls import url
from .views import PatientDetail, PatientList


urlpatterns = [
	url(r'^$', PatientList.as_view(), name="patientlist"),
	url(r'^(?P<pk>\d+)/$', PatientDetail.as_view(), name="patientdetail"),
]