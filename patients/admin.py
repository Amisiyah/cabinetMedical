from __future__ import unicode_literals
from django.contrib import admin
from .models import Patient, MedicalFile, Doctor
from .forms import PatientForm

from .models import Event
import datetime
import calendar
from django.urls import reverse
from django.utils.safestring import mark_safe
from .utils import EventCalendar


class MedicalFileInline(admin.StackedInline):
	model = MedicalFile
	filter_horizontal = ['calendar', ]
	extra = 0


class PatientAdmin(admin.ModelAdmin):
	list_display = ['first_name', 'last_name', 'email']
	ordering = ['last_name', 'email']
	list_filter = ['last_name']
	form = PatientForm
	save_as = True
	radio_fields = {'age': admin.HORIZONTAL}
	inlines = [MedicalFileInline]


@admin.register(MedicalFile)
class MedicalFileAdmin(admin.ModelAdmin):
	list_display = ['title', 'consultation_date']
	search_fields = ['title', 'doctors__country', 'patients__last_name']
	date_hierarchy = 'consultation_date'
	filter_horizontal = ['doctors', 'calendar']
	prepopulated_fields = {'slug': ('title',)}

	fieldsets = (
		(None, {
			'fields': (
				('title', 'slug'),
				'patients',
			)
		}),
		('More details', {
			'classes': ('collapse',),
			'fields': (
				'calendar',
				'doctors',
				'comments',
				'prescription',
				'price_for_consultation',
				'consultation_date',
			)
		})
	)


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
	list_display = ['admin_name']


class EventAdmin(admin.ModelAdmin):
	list_display = ['day', 'start_time', 'end_time', 'notes']
	change_list_template = 'admin/patients/change_list.html'

	def changelist_view(self, request, extra_context=None):
		after_day = request.GET.get('day__gte', None)
		extra_context = extra_context or {}

		if not after_day:
			d = datetime.date.today()
		else:
			try:
				split_after_day = after_day.split('-')
				d = datetime.date(year=int(split_after_day[0]), month=int(split_after_day[1]), day=1)
			except:
				d = datetime.date.today()

		previous_month = datetime.date(year=d.year, month=d.month, day=1)
		previous_month = previous_month - datetime.timedelta(days=1)
		previous_month = datetime.date(year=previous_month.year, month=previous_month.month, day=1)

		last_day = calendar.monthrange(d.year, d.month)
		next_month = datetime.date(year=d.year, month=d.month, day=last_day[1])
		next_month = next_month + datetime.timedelta(days=1)
		next_month = datetime.date(year=next_month.year, month=next_month.month,
                                   day=1)

		extra_context['previous_month'] = reverse('admin:patients_event_changelist') + '?day__gte=' + str(previous_month)
		extra_context['next_month'] = reverse('admin:patients_event_changelist') + '?day__gte=' + str(next_month)

		cal = EventCalendar()
		html_calendar = cal.formatmonth(d.year, d.month, withyear=True)
		html_calendar = html_calendar.replace('<td ', '<td  width="150" height="150"')
		extra_context['calendar'] = mark_safe(html_calendar)

		return super(EventAdmin, self).changelist_view(request, extra_context)


admin.site.register(Event, EventAdmin)
admin.site.register(Patient, PatientAdmin)
