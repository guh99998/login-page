from django.urls import path
from autenticacao.views import index

urlpatterns = [
  path('', index, name='index'),
]