from django.db import models
from django.utils import timezone

class ReadingMaterial(models.Model):

    original_title = models.CharField(max_length=200)
    adapted_title = models.CharField(max_length=200)
    year_of_publication = models.DateField('year of publication', default=timezone.now())
    pub_date = models.DateTimeField('date published', default=timezone.now())
    author = models.CharField(max_length=200)
    coutry_of_origin = models.CharField(max_length=200)
    synopsis = models.TextField()
    additional_information = models.TextField()
    number = models.IntegerField(default=1)

    def __str__(self):
        return self.original_title


class Gender(models.Model):

    reading_material = models.ForeignKey(ReadingMaterial, on_delete=models.CASCADE)
    gender_name = models.CharField(max_length=200)

    def __str__(self):
        return self.gender_name
    
