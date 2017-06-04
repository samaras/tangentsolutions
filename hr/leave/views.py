from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from leave.models import Leave, Employee

# Create your views here.

class HomePageView(LoginRequiredMixin, TemplateView):
	def get(self, request, **kwargs):
		return render(request, 'index.html', context=None)

class CreateLeaveView(LoginRequiredMixin, TemplateView):
	def get(self, request, **kwargs):
		return render(request, 'index.html', context=None)

class LeavePageView(LoginRequiredMixin, ListView):
	queryset = Leave.objects.order_by('-end_date')
	context_object_name = 'leave_taken'
	template_name = 'leave/list.html'