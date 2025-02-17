# details/forms.py


from django import forms

from myproject.details.models import Detail


class DetailForm(forms.ModelForm):
    class Meta:
        model = Detail
        fields = ['name', 'description']
