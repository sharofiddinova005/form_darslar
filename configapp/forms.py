from django import forms
from. models import  *
class NewsForm(forms.ModelForm):
    title=forms.CharField(max_length=150, label='News',
                          widget=forms.TextInput(attrs={"class": "form-control"}))

    context=forms.CharField(label='Text', required=False, widget=forms.Textarea(attrs={
        "class":"form-control",
        "rows":5
    }))
    photo=forms.ImageField()
    is_bool=forms.BooleanField(label='is bool', initial=True)
    category=forms.ModelChoiceField(empty_label='Categories',
                                    label='Categories', queryset=Category.objects.all(),
                                    widget=forms.Select(attrs={"class":"form-control"}))

class SearchForm(forms.Form):
    title=forms.CharField(max_length=150, label='News',
                          widget=forms.TextInput(attrs={"class": "form-control"}))



class CategoryForm(forms.ModelForm):
    title = forms.CharField(max_length=150, label='Categories',
                            widget=forms.TextInput(attrs={"class": "form-control"}))

    context = forms.CharField(label='Text', required=False, widget=forms.Textarea(attrs={
        "class": "form-control",
        "rows": 5
    }))
    photo = forms.ImageField()
    is_bool = forms.BooleanField(label='is bool', initial=True)
    category = forms.ModelChoiceField(empty_label='Categories',
                                      label='Categories', queryset=Category.objects.all(),
                                      widget=forms.Select(attrs={"class": "form-control"}))


class SearchForm(forms.Form):
    title = forms.CharField(max_length=150, label='Categories',
                            widget=forms.TextInput(attrs={"class": "form-control"}))
