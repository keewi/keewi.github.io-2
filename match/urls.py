from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.main_home, name='main_home'),
	url(r'^student_list$', views.student_list, name='student_list'),
	url(r'^apply/$', views.apply, name='apply'),
]