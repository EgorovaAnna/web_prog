# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
#from django.forms import ModelForm
from contactBook.models import Contact, Job, Post, City, Street

class ContactForm(forms.Form):
	surname = forms.CharField(label = u'Фамилия', max_length = 30)
	name = forms.CharField(label = 'Имя', max_length = 30)
	patronymic = forms.CharField(label = 'Отчество', max_length = 30)
	CHOICE = (('N', 'не указан'), ('M', 'мужской'), ('W', 'женский'))
	gender = forms.ChoiceField(label = 'Пол', choices = CHOICE, required = False)
	birthday = forms.DateField(label = 'Дата рождения', required = False, help_text = 'гггг-мм-дд')
	#job = forms.CharField(label = 'Место работы', max_length = 30)
	job = forms.ModelChoiceField(label = 'Место работы', queryset = Job.objects.all())
	#post = forms.CharField(label = 'Должность', max_length = 30)
	post = forms.ModelChoiceField(label = 'Должность', queryset = Post.objects.all())
	telephone = forms.CharField(label = 'Телефон', max_length = 30)
	email = forms.EmailField(label = 'E-mail', required = False)
	#city = forms.CharField(label = 'Город', max_length = 30)
	city = forms.ModelChoiceField(label = 'Город', queryset = City.objects.all())
	#street = forms.CharField(label = 'Улица', max_length = 30)
	street = forms.ModelChoiceField(label = 'Улица', queryset = Street.objects.all())
	building = forms.CharField(label = 'Дом', max_length = 5, required = False)
	apartment = forms.IntegerField(label = 'Квартира', required = False)
	
class SearchFormSurname(forms.Form):
	search = forms.CharField(label = 'Введите фамилию', max_length = 30)
	
class SearchFormJob(forms.Form):
	search = forms.CharField(label = 'Введите место работы', max_length = 30)
	
class SearchFormTelephone(forms.Form):
	search = forms.CharField(label = 'Введите телефон', max_length = 30)
	
#class EditForm(ModelForm):
#	class Meta:
#		model = Contact
#		fields = ['surname', 'name', 'patronymic', 'gender', 'birthday', 'job', 'post', 'telephone', 'email', 'city', 'street', 'building', 'apartment']


class EditForm(forms.Form):
	def __init__(self, contact):
		surname = forms.CharField(label = u"Фамилия", max_length=30, initial = contact.surname)
		name = forms.CharField(label = 'Имя', max_length = 30, initial = contact.name)
		patronymic = forms.CharField(label = 'Отчество', max_length = 30, initial = contact.patronymic)
		CHOICE = (('N', 'не указан'), ('M', 'мужской'), ('W', 'женский'))
		gender = forms.ChoiceField(label = 'Пол', choices = CHOICE, required = False, initial = contact.gender)
		birthday = forms.DateField(label = 'Дата рождения', required = False, initial = contact.birthday)
		job = forms.CharField(label = 'Место работы', max_length = 30, initial = contact.job)
		post = forms.CharField(label = 'Должность', max_length = 30, initial = contact.post)
		telephone = forms.CharField(label = 'Телефон', max_length = 30, initial = contact.telephone)
		email = forms.EmailField(label = 'E-mail', required = False, initial = contact.email)
		city = forms.CharField(label = 'Город', max_length = 30, initial = contact.city)
		street = forms.CharField(label = 'Улица', max_length = 30, initial = contact.street)
		building = forms.CharField(label = 'Дом', max_length = 5, required = False, initial = contact.building)
		apartment = forms.IntegerField(label = 'Квартира', required = False, initial = contact.apartment)
		super(EditForm, self).__init__()
		
	