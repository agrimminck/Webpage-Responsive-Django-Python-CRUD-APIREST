from django.db import models
from django.conf import settings

class Game(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100, verbose_name="name")
    genre=models.CharField(max_length=100, verbose_name="genre")
    #available_to_be_played=models.BooleanField()
    image=models.ImageField(upload_to=settings.MEDIA_ROOT, verbose_name="image", null=True)
    description=models.TextField(max_length=500, verbose_name='description', null=True)
    
