from django import forms
from .models import storeItem


class AddItem(forms.ModelForm):
  class Meta:
    model = storeItem
    fields = ["name", "desc", "image"]
    labels = {'name': "Name", "desc": "Description", "image": "Image"}



