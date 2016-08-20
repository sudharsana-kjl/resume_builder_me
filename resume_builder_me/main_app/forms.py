from django import forms

#from django.forms import inlineformset_factory, BaseInlineFormSet
from django.forms import inlineformset_factory

from .models import Resume, Project

class ResumeForm(forms.ModelForm):

    class Meta:
        model = Resume
        fields = ('__all__')



ProjectFormSet = inlineformset_factory(Resume, Project, fields=('title','detail','start_date','end_date'),max_num=4,extra=4)

