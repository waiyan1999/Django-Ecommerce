      
from django import forms
from .models import IncomeExpense ,Category

class IncomeExpenseForm(forms.ModelForm):
    class Meta:
        model = IncomeExpense
        fields = ['category', 'task_name', 'amount']
        widgets = {
            'category': forms.Select(attrs={'class': 'form-control'}),
            'task_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter task dddd name'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control','placeholder': 'Enter Amount'} ),
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']     
        
            