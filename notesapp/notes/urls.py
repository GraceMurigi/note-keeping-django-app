from django.urls import path 

from . import views

app_name = 'notes'

urlpatterns = [
	path('', views.IndexView.as_view(), name='index'),
	path('add/', views.add_note, name='add_note'),
]