from django import forms
from .models import Review


# Create a new class to extend the built-in forms.model form
class ReviewForm(forms.ModelForm):

    # Defines the model and the fields we want to include
    class Meta:
        model = Review
        # Include all the fields
        fields = '__all__'

    # Override the init method to make some changes to the fields
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)

    #     for field_name, field in self.fields.items():
    #         field.widget.attrs['class'] = 'rounded-0'
