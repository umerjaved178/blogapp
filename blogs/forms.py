from django import forms 
from django.forms import ModelForm

from .models import *

class FormClass(ModelForm):
	class Meta:
		model=	BlogDataBase
		fields=	'__all__'
