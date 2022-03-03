from email.policy import HTTP
import unicodedata
from django.http import Http404

from django.views import generic
from .models import ReadingMaterial, Gender
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render


_genders = {}
for gen in Gender.objects.all():
    key = unicodedata.normalize('NFD', gen.gender_name)
    key = ''.join(c for c in key if not unicodedata.combining(c)) 
    _genders.setdefault(key.lower().replace(' ', '+'), gen.gender_name.upper())


class IndexView(generic.ListView):
    template_name = 'catalog/index.html'
    context_object_name = 'genders'
    
    def get_queryset(self):
        return _genders


class AllbooksView(generic.ListView):
    template_name = 'catalog/allbooks.html'
    model = ReadingMaterial
    paginate_by = 2


class DetailView(generic.DetailView):
    queryset = ReadingMaterial.objects.all()
    template_name = 'catalog/detail.html'

    def get_object(self):
        slug = self.kwargs.get('slug')
        
        try:
            instance = ReadingMaterial.objects.get(slug=slug)
        except ReadingMaterial.DoesNotExist:
            raise Http404("Não encontrado")
        except ReadingMaterial.MultipleObjectsReturned:
            qs = ReadingMaterial.objects.filter(slug=slug)
            instance = qs.first()

        return instance

    



def ResultView(request, gender):
    books = []

    for o in ReadingMaterial.objects.all():
        for g in o.gender_set.all():
            gen = unicodedata.normalize('NFD', g.gender_name)
            gen = ''.join(c for c in gen if not unicodedata.combining(c))
            if gender.replace('+', ' ') == gen:
                books.append(o)

    paginator = Paginator(books, 2)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'catalog/result.html', {'gender': _genders[gender], 'page_obj': page_obj})
    

