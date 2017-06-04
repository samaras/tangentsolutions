from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def create_employee(sender, created, instance, **kwargs):
	if created:
		employee = Employee(user=instance)
		employee.save()