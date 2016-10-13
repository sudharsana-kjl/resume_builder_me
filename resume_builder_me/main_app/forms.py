from django import forms

#from django.forms import inlineformset_factory, BaseInlineFormSet
from django.forms import inlineformset_factory

from .models import Resume, Project, Gpa

class ResumeForm(forms.ModelForm):

    class Meta:
        model = Resume
        exclude = ('user',)
        #fields = ('__all__')



ProjectFormSet = inlineformset_factory(Resume, Project, fields=('title','detail','start_date','end_date'),max_num=4,extra=4)

GpaFormSet = inlineformset_factory(Resume, Gpa, fields=('sem_no','gpa'),max_num = 8,extra =8)