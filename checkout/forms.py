from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('forename', 'surname', 'email',
                  'phone', 'address1', 'address2', 'town', 'county', 'country',
                  'postcode',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'forename': 'Forename',
            'surname': 'Surname',
            'email': 'Email Address',
            'phone': 'Phone Number',
            'address1': 'Street Address 1',
            'address2': 'Street Address 2',
            'town': 'Town or City',
            'county': 'County',
            'postcode': 'Postal Code',
        }

        self.fields['forename'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
