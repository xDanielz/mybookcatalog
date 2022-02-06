from django.db import models

class ReadingMaterial(models.Model):
    original_title = models.CharField(max_length=200)
    adapted_title = models.CharField(max_length=200)
    first_publication_date = models.DateTimeField('date published')
    author = models.CharField(max_length=200)
    coutry_of_origin = models.CharField(max_length=200)
    synopsis = models.TextField()
