from django import forms
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout

class PropertyForm(forms.Form):
	address_digit = forms.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(9)])
	property_type = forms.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(2)])

	# def __init__(self, *args, **kwargs):
	# 	super(PropertyForm, self).__init__(*args, **kwargs)
	# 	self.helper = FormHelper()
	# 	self.helper.field_class = 'input-group'
