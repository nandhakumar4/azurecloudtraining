
from django import forms
from app.models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('name','email','address','jobrole','gender','it','cse','ece','mech','eee')
        
    
 