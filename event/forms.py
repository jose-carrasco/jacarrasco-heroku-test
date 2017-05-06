# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from models import Event

class EventForm(forms.ModelForm):

    def __init__(self, *args, **kw):
        super(EventForm, self).__init__(*args, **kw)        

    class Meta:
        model = Event
        fields = ['name', 'category', 'type', 'place', 'address', 'start_date', 'end_date']

        widgets = {            
            'category': forms.Select(attrs={
                'class': 'select2 form-control',
            }),
            'type': forms.Select(attrs={
                'class': 'select2 form-control',
            }),
            'start_date': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'flatpickr',
                'placeholder': u'Fecha de inicio',
            }),
            'end_date': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'flatpickr',
                'placeholder': u'Fecha de término',
            }),
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre del evento'
            }),
            'place': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Lugar'
            }),
            'address': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Dirección'
            }),            
        }

class EventEditForm(forms.ModelForm):

    def __init__(self, *args, **kw):
        super(EventEditForm, self).__init__(*args, **kw)        

    class Meta:
        model = Event
        fields = ['name', 'category', 'type', 'place', 'address', 'start_date', 'end_date']

        widgets = {            
            'category': forms.Select(attrs={
                'class': 'select2 form-control',
            }),
            'type': forms.Select(attrs={
                'class': 'select2 form-control',
            }),
            'start_date': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'flatpickr',
                'placeholder': u'Fecha de inicio',
            }),
            'end_date': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'flatpickr',
                'placeholder': u'Fecha de término',
            }),
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre del evento'
            }),
            'place': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Lugar'
            }),
            'address': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Dirección'
            }),            
        }

class EventDeleteForm(forms.Form):

    def __init__(self, *args, **kw):
        super(EventDeleteForm, self).__init__(*args, **kw)        


