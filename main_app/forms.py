from django.forms import ModelForm
from .models import Gift

class GiftForm(ModelForm):
    class Meta:
        model = Gift
        fields = ['date', 'name']