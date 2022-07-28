from xml.dom import ValidationErr
from django import forms
from django.core.exceptions import ValidationError

from .models import Notes

class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ('title', 'text', 'author')
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control my-5'}),
            'text': forms.Textarea(attrs={'class':'form-control my-5'})
        }
        labels = {
            'text':'Write your phrase here'
        }

    # def clean_title(self): # validando titulo 
    #     title = self.cleaned_data['title']
    #     if 'dream' not in title:
    #         raise ValidationError('We only accept phrases about dream')
    #     return title