from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('genero/todos', views.AllbooksView.as_view(), name='all'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('genero/<str:gender>/', views.ResultView, name='result')
]