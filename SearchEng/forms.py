from django import forms

class SearchForm(forms.Form):
    base_query = forms.CharField(max_length=100)
