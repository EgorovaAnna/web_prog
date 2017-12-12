# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.template.context_processors import csrf
from contactBook.forms import *
from contactBook.models import *
from django.db.models.query import EmptyQuerySet
import re
import func

def main(request):
	context = {}
	return render(request, 'main.html', context)

def search(request):
	context = {}
	return render(request, 'search_choice.html', context)

def add(request, cts):
	if cts:
		if re.search(r'/', cts):
			cts = cts[0:-1]
		cont = ContactToSave.objects.get(pk = cts)
		form = ContactForm(initial = {'surname': cont.surname, 'name' : cont.name, 'patronymic' : cont.patronymic, 'gender' : cont.gender, 'birthday' : cont.birthday, 'email' : cont.email, 'telephone' : cont.telephone, 'job' : cont.job, 'post' : cont.post, 'city' : cont.city, 'street' : cont.street, 'building' : cont.building, 'apartment' : cont.apartment})
		context = {'form': form, 'cts': cts, 'error_massage': cont.error}
	else:
		form = ContactForm()
		context = {'form': form}
	return render(request, 'add.html', context)

def add_some_doesnt_exist(request, some, id):
	if request.method == 'POST':
		if id:
			if re.search(r'/', id):
				id = id[0:-1]
			cts = ContactToSave.objects.get(pk = id)
			cts = func.initial(request, cts)
		else:
			cts = func.initial(request)
		cts.save()
		if some == 'job+':
			context = {'cts': cts.pk, 'add_string': 'организации', 'some': 'job+', 'form': AddJob(), 'have': Job.objects.all()}
		elif some == 'post+':
			context = {'cts': cts.pk, 'add_string': 'должности', 'some': 'post+', 'form': AddPost(), 'have': Post.objects.all()}
		elif some == 'city+':
			context = {'cts': cts.pk, 'add_string': 'города', 'some': 'city+', 'form': AddCity(), 'have': City.objects.all()}
		elif some == 'street+':
			if request.POST['city'] == '':
				context = {'cts': cts.pk, 'add_string': 'улицы', 'some': 'street+', 'form': AddStreet(), 'have': Street.objects.all().order_by('city'), 'street': True}
			else:
				formcity = request.POST['city']
				context = {'cts': cts.pk, 'add_string': 'улицы', 'some': 'street+', 'form': AddStreetCity(), 'have': Street.objects.filter(city = formcity).order_by('street'), 'street': True}
		return render(request, 'add_some_doesnt_exist.html', context)
				
def add_job(request):
	context = {'add_string': 'организации', 'some': 'job', 'form': AddJob(), 'have': Job.objects.all(), 'street': False}
	return render(request, 'add_new_some.html', context)

def add_post(request):
	context = {'add_string': 'должности', 'some': 'post', 'form': AddPost(), 'have': Post.objects.all(), 'street': False}
	return render(request, 'add_new_some.html', context)

def add_city(request):
	context = {'add_string': 'города', 'some': 'city', 'form': AddCity(), 'have': City.objects.all(), 'street': False}
	return render(request, 'add_new_some.html', context)

def add_street(request):
	context = {'add_string': 'улицы', 'some': 'street', 'form': AddStreet(), 'have': Street.objects.all().order_by('city'), 'street': True}
	return render(request, 'add_new_some.html', context)

def delete(request, id):
	contact = Contact.objects.get(pk = id)
	contact.delete()
	return HttpResponseRedirect('http://127.0.0.1:8000/contactBook/')

def add_new_some(request, some, cts = False):
	if request.method == 'POST':
		start = True
		form = request.POST
		new_job = None
		new_post = None
		new_city = None
		new_street = None
		if cts:
			if re.search(r'/', cts):
				cts = cts[0:-1]
			start = False
			cts = ContactToSave.objects.get(pk = cts)
		if some == 'job' or some == 'job+':
			some = form.get('add')
			new_job, created = Job.objects.get_or_create(job = some)
			if created and re.search(r'[\S]', some):
				new_job.save()
			if not start:
				cts.job = new_job
		if some == 'post' or some == 'post+':
			some = form.get('add')
			new_post, created = Post.objects.get_or_create(post = some)
			if created and re.search(r'[\S]', some):
				new_post.save()
			if not start:
				cts.post = new_post
		if some == 'city' or some == 'city+':
			some = form.get('add')
			new_city, created = City.objects.get_or_create(city = some)
			if created and re.search(r'[\S]', some):
				new_city.save()
			if not start:
				cts.city = new_city
		if some == 'street' or some == 'street+':
			if not start and cts.city:
				some_c = cts.city.pk
			else:
				some_c = form.get('add_c')
			some_s = form.get('add_s')
			new_city = City.objects.get(pk = some_c)
			new_street, created = Street.objects.get_or_create(city = new_city, street = some_s)
			if created and re.search(r'[\S]', some):
				new_street.save()
			if not start:
				cts.city = new_city
				cts.street = new_street
		if start:
			return HttpResponseRedirect('http://127.0.0.1:8000/contactBook/')
		else:
			cts.save()
			return redirect('http://127.0.0.1:8000/contactBook/add/{}/'.format(cts.pk))
	return HttpResponseRedirect('http://127.0.0.1:8000/contactBook/')


def add_new(request, id):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if id and re.search(r'/', id):
			id = id[0:-1]
		if form.is_valid():
			er, contact = func.check(form)
			if er:
				if id:
					cont = ContactToSave.objects.get(pk = id)
					cont = func.initial(request, cont)
				else:
					cont = func.initial(request)
				if er == 'telephone':
					cont.error = "Введите корректный номер телефона"
				elif er == 'street':
					cont.error = "Улицы {} нет в городе {}".format(cont.street.street, cont.city.city)
				cont.save()
				return redirect('add', cont.pk)
			contact.save()
			if id:
				cont = ContactToSave.objects.get(pk = id)
				cont.delete()
			return HttpResponseRedirect('http://127.0.0.1:8000/contactBook/')
		else:
			if id:
				cts = ContactToSave.objects.get(pk = id)
				cts = func.initial(request, cts)
				cts.save()
			else:
				cts = func.initial(request)
				cts.save()
			return redirect('add', cts.pk)
	else:
		return HttpResponseRedirect('http://127.0.0.1:8000/contactBook/add')

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
	contact = Contact.objects.get(pk = id)
	form = ContactForm(initial = {'surname': contact.surname, 'name' : contact.name, 'patronymic' : contact.patronymic, 'gender' : contact.gender, 'birthday' : contact.birthday, 'email' : contact.email, 'telephone' : contact.telephone, 'job' : contact.job, 'post' : contact.post, 'city' : contact.street.city, 'street' : contact.street, 'building' : contact.building, 'apartment' : contact.apartment})
	context = {'form': form, 'error_massage': "Измените необходимые поля", 'id': id}
	return render(request, 'edit.html', context)

def save_changes(request, id):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			contact = Contact.objects.get(pk = id)
			er, contact = func.check(form, contact)
			if er:
				if er == 'telephone':
					error = "Введите корректный номер телефона"
				elif er == 'street':
					error = "Улицы {} нет в городе {}".format(form.cleaned_data['street'].street, form.cleaned_data['city'].city)
				return render(request, 'edit.html', {'form': form, 'error_message': error, 'id': id})
			contact.save()
			return HttpResponseRedirect('http://127.0.0.1:8000/contactBook/')
		else: 
			return render(request, 'edit.html', {'form': form, 'error_message': "Something wrong"})
	else:
		return HttpResponseRedirect('http://127.0.0.1:8000/contactBook/edit_id='+id)
	
	
	
	
	
	