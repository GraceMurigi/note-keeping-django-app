from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView

# import model 
from .models import Note
# import form 
from .forms import NoteForm
# Create your views here.

class IndexView(ListView):
	model = Note
	template_name = 'notes/index.html'
	queryset = Note.objects.all()

	# template_name = 'notes/index.html'
	# context_object_name = 'latest_notes'

	# def get_queryset(self): 
	# 	"""return the last six notes"""
	# 	return Note.objects.filter().order_by('-id')[:5]



# create and save a new note 
def add_note(request):
	if request.method == 'POST':
		form = NoteForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/notes/')
	else: 
		form = NoteForm()
	return render(request, 'notes/create-note.html', {'form': form})




# class IndexView(generic.ListView):
# 	model = Note
# 	template_name = 'notes/index.html'
# 	context_object_name = 'latest_notes'

	# def get_queryset(self): 
	# 	"""return the last five notes"""
	# 	return Note.objects.filter(
	# 		pub)