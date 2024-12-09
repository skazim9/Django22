from django import forms
from .models import Product, Category

forbidden = ['казино', 'криптовалюта', 'крипта', 'биржа',
             'дешево', 'бесплатно', 'обман', 'полиция', 'радар']


class ProductForm(forms.Form):
    class Meta:
        model = Product
        fields = ['title', 'content', 'image', 'created_at', 'publication_sign', 'count_of_views']
        fields = ['name', 'description', 'image', 'category', 'price']

    def clean_name(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')

        if any(word in name.lower() for word in forbidden):
            raise forms.ValidationError("Название не должно содержать запрещенные слова.")
        return name

    def clean_description(self):
        cleaned_data = super().clean()
        description = cleaned_data.get('description')

        if any(word in description.lower() for word in forbidden):
            raise forms.ValidationError("Название не должно содержать запрещенные слова.")
        return description


class CategorytForm(forms.Form):
    class Meta:
        model = Category
        fields = ['name', 'description']