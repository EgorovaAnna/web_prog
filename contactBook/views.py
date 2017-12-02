# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.template.context_processors import csrf
from contactBook.forms import *
from contactBook.models import *
from django.db.models.query import EmptyQuerySet

def main(request):
	context = {}
	return render(request, 'main.html', context)

def search(request):
	context = {}
	return render(request, 'search_choice.html', context)

def add(request):
	context = {'form': ContactForm()}
	#context.update(csrf(request))
	#return render(request, 'add.html', context, RequestContext(request))
	return render(request, 'add.html', context)

def add_job(request):
	context = {'add_string': 'организации', 'some': 'job', 'form': AddJob()}
	return render(request, 'add_new_some.html', context)

def add_post(request):
	context = {'add_string': 'должности', 'some': 'post', 'form': AddPost()}
	return render(request, 'add_new_some.html', context)

def add_city(request):
	context = {'add_string': 'города', 'some': 'city', 'form': AddCity()}
	return render(request, 'add_new_some.html', context)

def add_street(request):
	context = {'add_string': 'улицы', 'some': 'street', 'form': AddStreet()}
	return render(request, 'add_new_some.html', context)

def add_new_some(request, some):
	if request.method == 'POST':
		if some == 'job':
			form = AddJob(request.POST)
			if form.is_valid():
				some = form.cleaned_data['add']
				new_job, created = Job.objects.get_or_create(job = some)
				if created:
					new_job.save()
		if some == 'post':
			form = AddPost(request.POST)
			if form.is_valid():
				some = form.cleaned_data['add']
				new_post, created = Post.objects.get_or_create(post = some)
				if created:
					new_post.save()
		if some == 'city':
			form = AddCity(request.POST)
			if form.is_valid():
				some = form.cleaned_data['add']
				new_city, created = City.objects.get_or_create(city = some)
				if created:
					new_city.save()
		if some == 'street':
			form = AddStreet(request.POST)
			if form.is_valid():
				some_c = form.cleaned_data['add_c']
				some_s = form.cleaned_data['add_s']
				new_city, created = City.objects.get_or_create(city = some_c)
				if created:
					new_city.save()
				new_street, created = Street.objects.get_or_create(city = new_city, street = some_s)
				if created:
					new_street.save()
	return HttpResponseRedirect('http://127.0.0.1:8000/contactBook/')


def add_new(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			contact = Contact()
			contact.surname = form.cleaned_data['surname']
			contact.name = form.cleaned_data['name']
			contact.patronymic = form.cleaned_data['patronymic']
			contact.gender = form.cleaned_data['gender']
			contact.birthday = form.cleaned_data['birthday']
			j = form.cleaned_data['job']
			if j == None:
				j = form.cleaned_data['job_new']
			new_job, created = Job.objects.get_or_create(job = j)
			if created:
				new_job.save()
			contact.job = new_job
			p = form.cleaned_data['post']
			if p == None:
				p = form.cleaned_data['post_new']
			new_post, created = Post.objects.get_or_create(post = p)
			if created:
				new_post.save()
			contact.post = new_post
			contact.telephone = form.cleaned_data['telephone']
			contact.email = form.cleaned_data['email']
			c = form.cleaned_data['city']
			if c == None:
				c = form.cleaned_data['city_new']
			new_city, created = City.objects.get_or_create(city = c)
			if created:
				new_city.save()
			s = form.cleaned_data['street']
			if s == None:
				s = form.cleaned_data['street_new']
			new_street, created = Street.objects.get_or_create(city = new_city, street = s)
			if created:
				new_street.save()
			contact.street = new_street
			contact.building = form.cleaned_data['building']
			contact.apartment = form.cleaned_data['apartment']
			contact.save()
			return HttpResponseRedirect('http://127.0.0.1:8000/contactBook/')
		else: 
			return render(request, 'add.html', {'form': form, 'error_message': "Something wrong"})
	else:
		#context = {'form': ContactForm}
		return HttpResponseRedirect('http://127.0.0.1:8000/contactBook/add')
		#return render(request, 'add.html', context)

def search_surname(request):
	context = {'form': SearchFormSurname()}
	return render(request, 'search.html', context)

def search_job(request):
	context = {'form': SearchFormJob()}
	return render(request, 'search.html', context)

def search_telephone(request):
	context = {'form': SearchFormTelephone()}
	return render(request, 'search.html', context)

def search_list_surname(request):
	if request.method == 'POST':
		form = SearchFormSurname(request.POST)
		if form.is_valid():
			if form.cleaned_data['search'] == 'all':
				context = {'lis': Contact.objects.all()}
			else:
				lis = Contact.objects.all().filter(surname = form.cleaned_data['search'])
				context = {'lis': lis}
			return render(request, 'search_list.html', context)
	return HttpResponseRedirect('http://127.0.0.1:8000/contactBook/search/')

def search_list_job(request):
	if request.method == 'POST':
		form = SearchFormJob(request.POST)
		if form.is_valid():
			lis = Contact.objects.all().filter(job = Job.objects.get(job = form.cleaned_data['search']).pk)
			context = {'lis': lis}
			return render(request, 'search_list.html', context)
	return HttpResponseRedirect('http://127.0.0.1:8000/contactBook/search/job/')

def search_list_telephone(request):
	if request.method == 'POST':
		form = SearchFormTelephone(request.POST)
		if form.is_valid():
			lis = Contact.objects.all().filter(telephone = form.cleaned_data['search'])
			context = {'lis': lis}
			return render(request, 'search_list.html', context)
	return HttpResponseRedirect('http://127.0.0.1:8000/contactBook/search/telephone/')

def edit(request, id):
	#form = EditForm(instance = Contact.objects.get(pk = id))
	contact = Contact.objects.get(pk = id)
	form = ContactForm(initial = {'surname': contact.surname, 'name' : contact.name, 'patronymic' : contact.patronymic, 'gender' : contact.gender, 'birthday' : contact.birthday, 'email' : contact.email, 'telephone' : contact.telephone, 'job_new' : contact.job.job, 'post_new' : contact.post.post, 'city_new' : contact.street.city.city, 'street_new' : contact.street.street, 'building' : contact.building, 'apartment' : contact.apartment})
	context = {'form': form, 'error_massage': "Измените необходимые поля"}
	return render(request, 'edit.html', context)

def save_changes(request, id):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			contact = Contact.objects.get(pk = id)
			contact.surname = form.cleaned_data['surname']
			contact.name = form.cleaned_data['name']
			contact.patronymic = form.cleaned_data['patronymic']
			contact.gender = form.cleaned_data['gender']
			contact.birthday = form.cleaned_data['birthday']
			j = form.cleaned_data['job']
			if j == None:
				j = form.cleaned_data['job_new']
			new_job, created = Job.objects.get_or_create(job = j)
			if created:
				new_job.save()
			contact.job = new_job
			p = form.cleaned_data['post']
			if p == None:
				p = form.cleaned_data['post_new']
			new_post, created = Post.objects.get_or_create(post = p)
			if created:
				new_post.save()
			contact.post = new_post
			contact.telephone = form.cleaned_data['telephone']
			contact.email = form.cleaned_data['email']
			c = form.cleaned_data['city']
			if c == None:
				c = form.cleaned_data['city_new']
			new_city, created = City.objects.get_or_create(city = c)
			if created:
				new_city.save()
			s = form.cleaned_data['street']
			if s == None:
				s = form.cleaned_data['street_new']
			new_street, created = Street.objects.get_or_create(city = new_city, street = s)
			if created:
				new_street.save()
			contact.street = new_street
			contact.building = form.cleaned_data['building']
			contact.apartment = form.cleaned_data['apartment']
			contact.save()
			return HttpResponseRedirect('http://127.0.0.1:8000/contactBook/')
		else: 
			return render(request, 'edit.html', {'form': form, 'error_message': "Something wrong"})
	else:
		#context = {'form': ContactForm}
		return HttpResponseRedirect('http://127.0.0.1:8000/contactBook/edit_id='+id)
	
	
	
	
	
	