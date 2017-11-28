from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.main, name = 'main'),
	url(r'^search/$', views.search, name = 'search'),
	url(r'^add/$', views.add, name = 'add'),
	url(r'^add_job/$', views.add_job, name = 'add_job'),
	url(r'^add_post/$', views.add_post, name = 'add_post'),
	url(r'^add_city/$', views.add_city, name = 'add_city'),
	url(r'^add_street/$', views.add_street, name = 'add_street'),
	url(r'^add/add_new_contact/$', views.add_new, name = 'add_new'),
	url(r'^add_new_some/([a-z]+)/$', views.add_new_some, name = 'add_new_some'),
	url(r'^search/surname/$', views.search_surname, name = 'search_surname'),
	url(r'^search/job/$', views.search_job, name = 'search_job'),
	url(r'^search/telephone/$', views.search_telephone, name = 'search_telephone'),
	url(r'^search/surname/list/$', views.search_list_surname, name = 'search_list_surname'),
	url(r'^search/job/list/$', views.search_list_job, name = 'search_list_job'),
	url(r'^search/telephone/list/$', views.search_list_telephone, name = 'search_list_telephone'),
	url(r'^edit_id=([1-9]+)/$', views.edit, name = 'edit'),
	url(r'^edit_id=([1-9]+)/save/$', views.save_changes, name = 'save_changes'),
]