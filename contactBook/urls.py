from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.main, name = 'main'),
	url(r'^search/$', views.search, name = 'search'),
	url(r'^add/$', views.add, name = 'add'),
	url(r'^add/add_new_contact/$', views.add_new, name = 'add_new'),
	url(r'^search/surname/$', views.search_surname, name = 'search_surname'),
	url(r'^search/job/$', views.search_job, name = 'search_job'),
	url(r'^search/telephone/$', views.search_telephone, name = 'search_telephone'),
]