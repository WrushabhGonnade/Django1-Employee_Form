from django import forms

from Emp_app.models import Employee_Table


class Employee_Form(forms.ModelForm):
    class Meta:
        model=Employee_Table
        fields="__all__"