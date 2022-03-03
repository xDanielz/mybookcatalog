from django.contrib import admin

from .models import ReadingMaterial, Gender


class GenderInline(admin.TabularInline):
    
    model = Gender
    extra = 1


class ReadingMaterialAdmin(admin.ModelAdmin):

    fieldsets = [
        ('Title',            {'fields': ['original_title', 'adapted_title', 'slug']}),
        ('Date information', {'fields': ['pub_date', 'year_of_publication'], 'classes': ['collapse']}),
        ('Author',           {'fields': ['author', 'coutry_of_origin']}),
        ('About',            {'fields': ['synopsis', 'additional_information', 'number']}),
        ('Cover',             {'fields': ['image']})
    ]

    inlines = [GenderInline]
    list_display = ('original_title', 'adapted_title', 'pub_date')
    list_filter = ['pub_date', 'author', ]
    search_fields = ['original_title', 'adapted_title']

admin.site.register(ReadingMaterial, ReadingMaterialAdmin)
