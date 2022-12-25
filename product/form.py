from django import forms

from product.models import Category

orders = (
    ('', 'Order By'),
    ('created_date', 'Newest'),
    ('-created_date', 'Oldest'),
    ('-price', 'Expensive'),
    ('price', 'Cheapest'),
    ('favorites', 'Most Favorites'),
)


class FilterForm(forms.Form):
    name = forms.CharField(label='', required=False,
                           widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'search'}))

    category = forms.ModelChoiceField(queryset=Category.objects.all()
                                      , label='', empty_label='All Category', required=False
                                      , widget=forms.Select(
            attrs={'class': 'form-select', 'onchange': 'c_form.submit()'}))

    order = forms.ChoiceField(choices=orders, required=False, label=''
                              , widget=forms.Select(attrs={'class': 'form-select', 'onchange': 'c_form.submit()'}))

    available = forms.BooleanField(label='Just Available Products', required=False,
                                   widget=forms.CheckboxInput(
                                       attrs={'class': '', 'onchange': 'c_form.submit()'}))
