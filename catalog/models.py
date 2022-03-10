from django.db import models
from django.utils import timezone
from .utils import unique_slug_generator
from django.db.models.signals import pre_save

class ReadingMaterial(models.Model):

    original_title         = models.CharField(max_length=200)
    slug                   = models.SlugField(blank=True, max_length=200, unique=True)
    adapted_title          = models.CharField(max_length=200)
    year_of_publication    = models.DateField('year of publication', default=timezone.now())
    pub_date               = models.DateTimeField('date published', default=timezone.now())
    author                 = models.CharField(max_length=200)
    coutry_of_origin       = models.CharField(max_length=200)
    synopsis               = models.TextField()
    additional_information = models.TextField(default='')
    image                  = models.ImageField(upload_to='catalog/static/catalog/images', null=True, blank=True)
    number                 = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.original_title


class Gender(models.Model):

    reading_material = models.ForeignKey(ReadingMaterial, on_delete=models.CASCADE)
    gender_name = models.CharField(max_length=200)

    def __str__(self):
        return self.gender_name


def product_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
    
pre_save.connect(product_pre_save_receiver, sender=ReadingMaterial)
