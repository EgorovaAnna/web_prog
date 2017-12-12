# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from contactBook.models import *
from contactBook.forms import ContactForm
from django.template import RequestContext, loader
import re

def initial(request, cts = ContactToSave()):
	form = request.POST
	if form.get('birthday'):
		cts.birthday = form.get('birthday')
	if form.get('surname'):
		cts.surname = form.get('surname')
	if form.get('name'):
		cts.name = form.get('name')
	if form.get('patronymic'):
		cts.patronymic = form.get('patronymic')
	if form.get('gender'):
		cts.gender = form.get('gender')
	if form.get('email'):
		cts.email = form.get('email')
	if form.get('telephone'):
		cts.telephone = form.get('telephone')
	if form.get('building'):
		cts.building = form.get('building')
	if form.get('apartment'):
		cts.apartment = form.get('apartment')
	if form.get('job'):
		new_job = Job.objects.get(pk = form.get('job'))
		cts.job = new_job
	if form.get('post'):
		new_post = Post.objects.get(pk = form.get('post'))
		cts.post = new_post
	if form.get('city'):
		new_city = City.objects.get(pk = form.get('city'))
		cts.city = new_city
	if form.get('street'):
		new_street = Street.objects.get(pk = form.get('street'))
		cts.street = new_street
	return cts

def check(form, contact = Contact()):
	contact.surname = form.cleaned_data['surname']
	contact.name = form.cleaned_data['name']
	contact.patronymic = form.cleaned_data['patronymic']
	contact.gender = form.cleaned_data['gender']
	contact.birthday = form.cleaned_data['birthday']
	j = form.cleaned_data['job']
	new_job = Job.objects.get(job = j)
	contact.job = new_job
	p = form.cleaned_data['post']
	new_post = Post.objects.get(post = p)
	contact.post = new_post
	phone = form.cleaned_data['telephone']
	if re.match(r'[+7, 8]{1}[0-9]{10}', phone):
		contact.telephone =  phone
	elif re.match(r'\+?[7, 8][-, (]*\d{3}[-, )]*\d{3}-?\d{2}-?\d{2}', phone):
		contact.telephone = re.findall(r'([+7, \d+])', phone)
	else:
		return 'telephone', None
	contact.email = form.cleaned_data['email']
	c = form.cleaned_data['city']
	new_city = City.objects.get(city = c)
	s = form.cleaned_data['street']
	new_street, created = Street.objects.get_or_create(city = new_city, street = s)
	if created:
		new_street.delete()
		return 'street', None
	contact.street = new_street
	contact.building = form.cleaned_data['building']
	contact.apartment = form.cleaned_data['apartment']
	return False, contact