from django.conf.urls import url 
from leave import views

urlpatterns = [
	url(r'^$', views.HomePageView.as_view()),
	url(r'^create$', views.CreateLeaveView.as_view()),
	url(r'^leave$', views.LeavePageView.as_view()),
]