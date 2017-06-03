import datetime
import dateutil.relativedelta

import math

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class TimeStamped(models.Model):
	created_on = models.DateTimeField("Created on", auto_now_add=True)
	updated_on = models.DateTimeField("Updated on", auto_now=True)

	class Meta:
		abstract = True

class Employee(models.Model):
	""" Employee """
	user = models.OneToOneField(User, related_name="employee", verbose_name=_("employee"), on_delete=models.CASCADE)
	start_date = models.DateTimeField(blank=True)
	leave_remaining = models.IntegerField(default=0, blank=True)
	
	class Meta:
		verbose_name_plural = _("employees")

	def calculate_leave():
		""" Calculates the amount leave employee accrued per year """
		leave_per_month = 18 / 12
		today = timezone.now().date()

		# Check if employee is on probation
		probation = today - datetime.relativedelta(months=3)
		if self.start_date >= probation:
			return 0
		else:
			# calculate leave this year
			r = relativedelta.relativedelta(today, self.start_date)
			leave = r.months * leave_per_month
			return math.floor(leave)

	def __str__(self):
		return "%s %s" % (self.user.first_name, self.user.last_name)

class Leave(TimeStamped):
	""" Leave """
	NEW = 1
	APPROVED = 2
	DECLINED = 3
	STATUS_CHOICES = (
		(NEW, 'New'),
		(DECLINED, 'Declined'),
		(APPROVED, 'Approved'),
	)

	start_date = models.DateField()
	end_date = models.DateField()
	leave_days = models.IntegerField()
	status = models.IntegerField(choices=STATUS_CHOICES, default=NEW)
	employee = models.ForeignKey(Employee, verbose_name=_("Employee"))

	class Meta:
		verbose_name_plural = _("leave")

	def __str__(self):
		return self.employee