from django import forms
from .models import University, Group, Student

class UniversityForm(forms.ModelForm):
    class Meta:
        model = University
        fields = ['name', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['university', 'name']
        widgets = {
            'university': forms.Select(attrs={'class': 'form-select'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['group', 'first_name', 'last_name', 'photo']
        widgets = {
            'group': forms.Select(attrs={'class': 'form-select'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
