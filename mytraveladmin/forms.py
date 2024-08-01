from django import forms
from mytraveladmin import models


class CategoriesForm(forms.ModelForm):
      class Meta:    
          model = models.Categories
          fields = '__all__'
        #   exclude = ('user',)

class PackagesForm(forms.ModelForm):
      class Meta:    
          model = models.Packages
          fields = '__all__'
          exclude = ('user',)
