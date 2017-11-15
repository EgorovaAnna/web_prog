# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import RequestContext, loader

def main(request):
	context = {}
	return render(request, 'main.html', context)

def search(request):
	context = {}
	return render(request, 'search_choice.html', context)

def add(request):
	context = {}
	return render(request, 'add.html', context)

def search_surname(request):
	context = {}
	return render(request, 'search_choice.html', context)