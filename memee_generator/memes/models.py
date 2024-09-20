from django.db import models

class Meme(models.Model):
    image = models.ImageField(upload_to='memes/')
    top_text = models.CharField(max_length=100)
    bottom_text = models.CharField(max_length=100)

# Create your models here.
