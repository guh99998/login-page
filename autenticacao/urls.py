from django.urls import path
from autenticacao.views import login, singup, members

urlpatterns = [
  path('', login, name='login'),
  path('cadastro', singup, name='singup'),
  path('members/', members, name='members'),
]