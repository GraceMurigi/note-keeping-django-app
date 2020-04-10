from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView

# import edit views classes
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# urls

# import model 
from .models import Note
# import form 
from .forms import NoteForm


# view to display all notes 
class NoteListView(ListView):
	model = Note
	template_name = 'notes/index.html'
	queryset = Note.objects.all().order_by('-pk')

	# template_name = 'notes/index.html'
	# context_object_name = 'latest_notes'

	# def get_queryset(self): 
	# 	"""return the last six notes"""
	# 	return Note.objects.filter().order_by('-id')[:5]

# create a note 
class NoteCreateView(CreateView):
	model = Note
	form_class = NoteForm
	template_name = 'notes/create-note.html'
	# use namespace to avoid NoReverseMatchError
	success_url = reverse_lazy('notes:note-list')

class NoteEditView(UpdateView):
	model = Note
	form_class = NoteForm
	template_name ='notes/edit-note.html'
	success_url = reverse_lazy('notes:note-list')

class NoteDeleteView(DeleteView):
	model = Note
	success_url = reverse_lazy('notes:note-list')