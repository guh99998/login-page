from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from autenticacao.forms import LoginForms, CadastroForms
from django.contrib.auth.models import User
from django.contrib import auth, messages

def login(request):
  form = LoginForms()

  if request.method == 'POST':
    form = LoginForms(request.POST)

    if form.is_valid():
      email = form['email'].value()
      senha = form['senha'].value()

      usuario = auth.authenticate(
        request,
        username = email,
        password = senha
      )
      if usuario is not None:
        auth.login(request, usuario)
        messages.success(request, 'Logado com sucesso!')
        return redirect('members')
      else:
        messages.error(request, 'Erro ao efetuar login!')
        return redirect('login')
      
  return render(request, 'login.html', {'form': form})

def singup(request):
  form = CadastroForms()

  if request.method == 'POST':
    form = CadastroForms(request.POST)

    if form.is_valid():
      email = form['email'].value()
      senha = form['senha_2'].value()

      if User.objects.filter(email = email).exists():
        messages.error(request, 'O usuário já existe no sistema!')
        return redirect('login')
      
      usuario = User.objects.create_user(
        username = email,
        password = senha
      )
      usuario.save()
      messages.success(request, 'Cadastro efetuado!')
      return redirect('login')

  return render(request, 'singup.html', {'form': form})

@login_required
def members(request):
  return render(request, 'members.html')