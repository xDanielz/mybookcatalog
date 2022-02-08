from django.views import generic
from .models import ReadingMaterial

class IndexView(generic.ListView):
    template_name = 'catalog/index.html'
    paginate_by = 2
    model = ReadingMaterial


class DetailView(generic.DetailView):
    model = ReadingMaterial
    template_name = 'catalog/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
