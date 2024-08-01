from django import forms
from traveluser import models

class ConfirmForm(forms.ModelForm):
      class Meta:
          model = models.Confirm_booking
          fields = '__all__'
          exclude = ('user','package','transaction')
          
class PaymentForm(forms.ModelForm):
    class Meta:
        model = models.Transaction
        fields = '__all__'
        exclude = ('user','package',)
        