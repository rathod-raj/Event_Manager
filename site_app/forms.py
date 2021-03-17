from django import forms
from site_app.models import ignisdata

class AlldataForm(forms.ModelForm):
   class Meta:
       model = ignisdata 
       fields = ("event_name", "data", "location", "image")