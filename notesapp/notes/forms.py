# create forms from models 
from django.forms import ModelForm, Textarea, TextInput
# customize wording of user facing interfaces
from django.utils.translation import gettext_lazy as _

from .models import Note



# Note form 
class NoteForm(ModelForm):
	class Meta:
		model = Note
		# exclude = ['pub_date']
		fields = '__all__'
		widgets = {
			'note_title':TextInput(attrs={'class':'form-control'}),
			'note_text':Textarea(attrs={'class':'form-control','placeholder':'Type your note here'}), 
		}
		
		labels = {
			'note_title': _('Title'),
			'note_text': _('Note')
		}
