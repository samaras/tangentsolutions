import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

# Create your models here.

NEW = 0
APPROVED = 1
DECLINED = 2
STATUS_CHOICES = (
	(NEW, 'New'),
	(DECLINED, 'Declined'),
	(APPROVED, 'Approved'),
)

class TimeStamped(models.Model):
	created_on = models.DateTimeField("Created on", auto_now_add=True)
	updated_on = models.DateTimeField("Updated on", auto_now=True)

	class Meta:
		abstract = True

class Employee(models.Model):
	""" Employee """
	user = models.OneToOneField(User, related_name="employee", verbose_name=_("employee"), on_delete=models.CASCADE)
	start_date = models.DateField(blank=True)
	leave_remaining = models.IntegerField(default=0, blank=True)
	
	class Meta:
		verbose_name_plural = _("employees")

	def calculate_leave():
		""" Calculates the amount leave employee accrued per year """
		leave_per_month = 18 / 12
		current_month = timezone.now().month

		# Check if employee is on probation
		probation = current_month - datetime.timedelta(months=3)
		if self.start_date >= probation:
			return 0
		else:
			return 

	def __str__(self):
		return "%s %s" % (self.user.first_name, self.user.last_name)

class Leave(TimeStamped):
	""" Leave """
	start_date = models.DateField()
	end_date = models.DateField()
	days_of_leave = models.IntegerField()
	status = models.IntegerField(choices=STATUS_CHOICES)
	employee = models.ForeignKey(Employee, verbose_name=_("Employee"))

	class Meta:
		verbose_name_plural = _("leave")

	def __str__(self):
		return self.employee