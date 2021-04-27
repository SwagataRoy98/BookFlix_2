from django import forms


class SearchForm(forms.Form):
    search_by_author = forms.CharField(max_length=200)
    search_by_title = forms.CharField(max_length=300)