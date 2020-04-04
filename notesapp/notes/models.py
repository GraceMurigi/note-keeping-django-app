from django.db import models


# Create your models here.
class Note(models.Model):
	note_title = models.CharField(max_length =200)
	note_text = models.CharField(max_length = 1000)
	# pub_date = models.DateTimeField()

	
	def __str__(self):
		return self.note_text


