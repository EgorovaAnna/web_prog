# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import RequestContext, loader
from .forms import ContactForm

def main(request):
	context = {}
	return render(request, 'main.html', context)

def search(request):
	context = {}
	return render(request, 'search_choice.html', context)

def add(request):
	context = {'form': ContactForm()}
	return render(request, 'add.html', context)

def add_new(request):
	if request.method == 'post':
		form = ContactForm(request.POST)
		if form.is_valid():
			contact = Contact()
			contact.surname = form.cleaned_data['surname']
			contact.name = form.cleaned_data['name']
			contact.patronymic = form.cleaned_data['patronymic']
			contact.gender = form.cleaned_data['gender']
			contact.birthday = form.cleaned_data['birthday']
			j = form.cleaned_data['job']
			if isinstance(Job.objects.all().filter(job = j), EmptyQuerySet):
				new_job = Job(job = j)
				new_job.save()
				contact.job = new_job
			else:
				contact.job = Job.objects.all().filter(job = j).get(pk = 1)
			p = form.cleaned_data['post']
			if isinstance(Post.objects.all().filter(post = p), EmptyQuerySet):
				new_post = Post(post = p)
				new_post.save()
				contact.post = new_post
			else:
				contact.post = Post.objects.all().filter(post = p).get(pk = 1)
			contact.telephone = form.cleaned_data['telephone']
			contact.email = form.cleaned_data['email']
			c = form.cleaned_data['city']
			if isinstance(City.objects.all().filter(city = c), EmptyQuerySet):
				new_city = City(city = c)
				new_city.save()
				contact.city = new_city
			else:
				contact.city = City.objects.all().filter(city = c).get(pk = 1)
			s = form.cleaned_data['street']
			if isinstance(Street.objects.all().filter(street = s), EmptyQuerySet):
				new_street = Street(street = s)
				new_street.save()
				contact.street = new_street
			else:
				contact.street = Street.objects.all().filter(street = s).get(pk = 1)
			contact.building = form.cleaned_data['building']
			contact.apartment = form.cleaned_data['apartment']
			contact.save()
			return HttpResponseRedirect('/thanks/')
    	else: 
			context = {'form': ContactForm()}
	return render(request, 'add.html', context)

def search_surname(request):
	context = {}
	return render(request, 'search_choice.html', context)

def search_job(request):
	context = {}
	return render(request, 'search_choice.html', context)

def search_telephone(request):
	context = {}
	return render(request, 'search_choice.html', context)