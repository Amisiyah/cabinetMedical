from __future__ import unicode_literals
from django.db import models
from django.utils.text import slugify
from django.db.models.signals import post_save, pre_save
from django.urls import reverse
from django.core.exceptions import ValidationError


AGE_GROUP = (
	(0, " < 14 "),
	(1, " 14-18 "),
	(2, " > 18 ")
)


class Event(models.Model):
	day = models.DateField(u'Day of the event', help_text=u'Day of the event')
	start_time = models.TimeField(u'Starting time', help_text=u'Starting time')
	end_time = models.TimeField(u'Final time', help_text=u'Final time')
	notes = models.TextField(u'Textual Notes', help_text=u'Textual Notes', blank=True, null=True)

	class Meta:
		verbose_name = u'Scheduling'
		verbose_name_plural = u'Scheduling'

	def check_overlap(self, fixed_start, fixed_end, new_start, new_end):
		overlap = False
		if new_start == fixed_end or new_end == fixed_start:    # edge case
			overlap = False
		elif (new_start >= fixed_start and new_start <= fixed_end) or (new_end >= fixed_start and new_end <= fixed_end): # innner limits
			overlap = True
		elif new_start <= fixed_start and new_end >= fixed_end: # outter limits
			overlap = True

		return overlap

	def get_absolute_url(self):
		url = reverse('admin:%s_%s_change' % (self._meta.app_label, self._meta.model_name), args=[self.id])
		return u'<a href="%s">%s</a>' % (url, str(self.start_time))

	def clean(self):
		if self.end_time <= self.start_time:
			raise ValidationError('Ending hour must be after the starting hour')

		events = Event.objects.filter(day=self.day)
		if events.exists():
			for event in events:
				if self.check_overlap(event.start_time, event.end_time, self.start_time, self.end_time):
					raise ValidationError(
						'There is an overlap with another event: ' + str(event.day) + ', ' + str(event.start_time) + '-' + str(event.end_time))

	def __str__(self):
		return "%s, [%s, %s]" % (self.day, self.start_time, self.end_time)


class Patient(models.Model):
	first_name = models.CharField(max_length=50)
	middle_name = models.CharField(max_length=50, blank=True, null=True)
	last_name = models.CharField(max_length=50)
	address = models.CharField(max_length=50, blank=True, null=True)
	city = models.CharField(max_length=50, blank=True, null=True)
	country = models.CharField(max_length=50, blank=True, null=True)
	pin = models.CharField(max_length=13)  # Personal Identification Number
	age = models.IntegerField(choices=AGE_GROUP, default=2)  # >19
	email = models.EmailField()

	def __str__(self):
		return "%s, %s" % (self.last_name, self.first_name)

	def get_absolute_url(self):
		return reverse("patients:patientdetail", kwargs={'pk': self.pk})

	def get_patient_list_url(self):
		return reverse("patients:patientlist")


class Doctor(models.Model):
	first_name = models.CharField(max_length=50)
	middle_name = models.CharField(max_length=50, blank=True, null=True)
	last_name = models.CharField(max_length=50)
	tag = models.CharField(max_length=50)
	address = models.CharField(max_length=50, blank=True, null=True)
	city = models.CharField(max_length=50, blank=True, null=True)
	country = models.CharField(max_length=50, blank=True, null=True)

	def __str__(self):
		return "%s [%s, %s]" % (self.tag, self.last_name, self.first_name)

	@property
	def admin_name(self):
		return "%s (%s)" % (self.tag, self.last_name)


class MedicalFile(models.Model):
	title = models.CharField(max_length=100)
	slug = models.SlugField(unique=True, blank=True)
	calendar = models.ManyToManyField(Event)
	patients = models.ForeignKey(Patient, related_name="medicalFile", on_delete=models.CASCADE)
	doctors = models.ManyToManyField(Doctor)
	comments = models.TextField()
	prescription = models.TextField()
	price_for_consultation = models.DecimalField(decimal_places=2, max_digits=5, default=0)
	consultation_date = models.DateField(null=True, blank=True)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True, verbose_name="Created on")
	updated = models.DateTimeField("Last updated", auto_now=True, auto_now_add=False)

	def __str__(self):
		return self.title
