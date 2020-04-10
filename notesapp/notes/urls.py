from django.urls import path 

from notes.views import NoteListView, NoteCreateView, NoteEditView, NoteDeleteView

app_name = 'notes'

urlpatterns = [
	path('', NoteListView.as_view(), name='note-list'),
	path('add/', NoteCreateView.as_view(), name='create-note'),
	path('<int:pk>/update/', NoteEditView.as_view(), name='edit-note'), 
	path('<int:pk>/delete/', NoteDeleteView.as_view(), name='delete-note')
] 