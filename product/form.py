from django import forms

from product.models import Category


class CategoryFilterForm(forms.Form):
    category = forms.ModelChoiceField(queryset=Category.objects.all()
                                      , label='', empty_label='All Category'
                                      , widget=forms.Select(
            attrs={'class': 'form-select', 'onchange': 'c_form.submit()'}))


class SearchFilterForm(forms.Form):
    name = forms.CharField(label='', required=False,
                           widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'search'}))
