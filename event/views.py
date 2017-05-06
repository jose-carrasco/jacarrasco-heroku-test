# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from models import Event
from forms import *

def home(request):
	events = Event.objects.all().order_by('-id')
	return render(request, 'home.html', {'events': events})


def event_details(request, id):
	event = get_object_or_404(Event, id=id)
	return render(request, 'details.html', {'event': event})


def event_add(request,):	
	form = EventForm()

	if request.method == 'POST':
		form = EventForm(request.POST)
		if form.is_valid():
			event = form.save(commit=True)
			url = reverse('event:event_details', kwargs={'id': event.id})
			return HttpResponseRedirect(url)
	return render(request, 'add.html', {'form': form})


def event_edit(request, id):
	event = get_object_or_404(Event, id=id)
	form = EventEditForm(instance=event)

	if request.method == 'POST':
		form = EventEditForm(request.POST, instance=event)
		if form.is_valid():
			event = form.save(commit=True)
			url = reverse('event:event_details', kwargs={'id': event.id})
			return HttpResponseRedirect(url)

	return render(request, 'edit.html', {'event': event, 'form': form})

def event_delete(request, id):
	event = get_object_or_404(Event, id=id)
	form = EventDeleteForm()

	if request.method == 'POST':
		form = EventDeleteForm(request.POST)
		if form.is_valid():
			event.delete()
			return HttpResponseRedirect(reverse('event:home'))

	return render(request, 'delete.html', {'event': event, 'form': form})