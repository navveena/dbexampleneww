from django import forms
from dbexamplenewwapp.models import Employee
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employeefields = "__all__"