# -*- coding: utf-8 -*-
from django import forms

class ContactForm(forms.Form):
	surname = forms.CharField(label = u"Фамилия", max_length=30)
	name = forms.CharField(label = 'Имя', max_length = 30)
	patronymic = forms.CharField(label = 'Отчество', max_length = 30)
	CHOICE = (('N', 'не указан'), ('M', 'мужской'), ('W', 'женский'))
	gender = forms.ChoiceField(label = 'Пол', choices = CHOICE, required = False)
	birthday = forms.DateField(label = 'Дата рождения', required = False)
	job = forms.CharField(label = 'Место работы', max_length = 30)
	post = forms.CharField(label = 'Должность', max_length = 30)
	telephone = forms.CharField(label = 'Телефон', max_length = 30)
	email = forms.EmailField(label = 'E-mail', required = False)
	city = forms.CharField(label = 'Город', max_length = 30)
	street = forms.CharField(label = 'Улица', max_length = 30)
	building = forms.CharField(label = 'Дом', max_length = 5, required = False)
	apartment = forms.IntegerField(label = 'Квартира', required = False)
	
class SearchFormSurname(forms.Form):
	surname = forms.CharField(label = 'Введите фамилию', max_length = 30)
	
class SearchFormJob(forms.Form):
	job = forms.CharField(label = 'Введите место работы', max_length = 30)
	
class SearchFormTelephone(forms.Form):
	telephone = forms.CharField(label = 'Введите телефон', max_length = 30)