from django.db import models
from django.utils import timezone

class Post(models.Model):
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	title = models.CharField(max_length=400)
	text_opis = models.TextField()
	text = models.TextField()
	image = models.ImageField(upload_to = 'image/')
	published_date = models.DateTimeField(auto_now_add=True)
	

	def publish_car(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title
		