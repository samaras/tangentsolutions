from django.conf.urls import url 
from leave import views

urlpatterns = [
	url(r'^$', views.HomePageView.as_view()),
]