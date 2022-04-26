from django import forms
from motherearth.web import models


class FilterForm(forms.ModelForm):
    object_list = forms.queryset = models.Type.objects.all()

