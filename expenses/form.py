from django.forms import ModelForm
from django import forms
from dataclasses import fields
from .models import Expense

class ExpensesForm(ModelForm):
    observations = forms.CharField(widget=forms.Textarea(attrs={"cols":32, "rows": 5, "required":False}))
    class Meta:
        model = Expense
        fields = ['date', 'value', 'description', 'category', 'observations']
    
    
