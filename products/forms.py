from django import forms
from .models import Product, WineOrigin, WineColour


# Create a new class to extend the built-in forms.model form
class ProductForm(forms.ModelForm):

    # Defines the model and the fields we want to include
    class Meta:
        model = Product
        # Include all the fields
        fields = '__all__'

    # Override the init method to make some changes to the fields
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Get wine origins and colours to show in form using friendly names
        # categories = Category.objects.all()
        wine_origin = WineOrigin.objects.all()
        wine_colour = WineColour.objects.all()
        # friendly_names = [(c.id, c.get_friendly_name()) for c in categories]
        # origin_friendly_names = [(wo.id, wo.get_friendly_name()) for wo in wine_origin]
        # colour_friendly_names = [(wc.id, wc.get_friendly_name()) for wc in wine_colour]

        # self.fields['category'].choices = friendly_names
        # self.fields['wine_origins'].choices = origin_friendly_names
        # self.fields['wine_colours'].choices = colour_friendly_names

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'rounded-0'
