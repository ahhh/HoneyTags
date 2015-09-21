from django import forms
from .models import Tag

#class regTagForm(forms.Form):
#	campaign = forms.CharField(label='campaign', max_length=200)
#	title = forms.CharField(label='title', max_length=200)
#	key = forms.CharField(label='keu', max_length=200)
#	type = formsCharField(label='type', max_length=200)

class regTagForm(forms.ModelForm):
	class Meta:
		model = Tag
		fields = ('campaign', 'title', 'key', 'type',)



