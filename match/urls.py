from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.student_list, name='student_list'),
	url(r'^apply/$', views.apply, name='apply'),
]