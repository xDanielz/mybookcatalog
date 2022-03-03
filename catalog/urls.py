from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('gender/all', views.AllbooksView.as_view(), name='all'),
    path('<slug:slug>/', views.DetailView.as_view(), name='detail'),
    path('gender/<str:gender>/', views.ResultView, name='result')
]