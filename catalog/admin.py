from django.contrib import admin
from .models import ReadingMaterial, Gender


class ReadingMaterialAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Title',            {'fields': ['original_title', 'adapted_title']}),
        ('Date information', {'fields': ['pub_date', 'year_of_publication']}),
        ('Author',           {'fields': ['author', 'coutry_of_origin']}),
        ('About',            {'fields': ['synopsis', 'additional_information', 'number']})
    ]


admin.site.register(ReadingMaterial)
