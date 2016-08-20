from django import forms

#from django.forms import inlineformset_factory, BaseInlineFormSet
from django.forms import inlineformset_factory

from .models import Resume, Project

class ResumeForm(forms.ModelForm):

    class Meta:
        model = Resume
        fields = ('__all__')

#class ProjectForm(forms.ModelForm):

#	class Meta:
#		model = Project
#		fields = ('__all__')

ProjectFormSet = inlineformset_factory(Resume, Project, fields=('title','detail','start_date','end_date'),max_num=4,extra=4)

#class CustomInlineFormSet(BaseInlineFormSet):
#	def clean(self):
#		super(CustomInlineFormSet,self).clean()
