from django import forms

class LoginForms(forms.Form):
  email = forms.CharField(
    label = 'E-mail',
    required = True,
    max_length = 150,
    widget = forms.EmailInput(
      attrs = {
        'class': 'form-control',
        'placeholder': 'Ex.: gustavo@gmail.com'
      }
    )
  )
  senha = forms.CharField(
    label = 'Senha',
    required = True,
    max_length = 70,
    widget = forms.PasswordInput(
      attrs = {
        'class': 'form-control',
        'placeholder': 'Digite sua senha'
      }
    )
  )

class CadastroForms(forms.Form):
  email = forms.CharField(
    label = 'E-mail',
    required = True,
    max_length = 150,
    widget = forms.EmailInput(
      attrs = {
        'class': 'form-control',
        'placeholder': 'Ex.: gustavo@gmail.com'
      }
    )
  ) 
  senha_1 = forms.CharField(
    label = 'Senha',
    required = True,
    max_length = 70,
    widget = forms.PasswordInput(
      attrs = {
        'class': 'form-control',
        'placeholder': 'Digite sua senha'
      }
    )
  )
  senha_2 = forms.CharField(
    label = 'Senha',
    required = True,
    max_length = 70,
    widget = forms.PasswordInput(
      attrs = {
        'class': 'form-control',
        'placeholder': 'Digite novamente sua senha'
      }
    )
  )

  def clean_confirmacao_senha(self):
    senha_1 = self.cleaned_data.get('senha_1')
    senha_2 = self.cleaned_data.get('senha_2')

    if senha_1 and senha_2:
      if senha_1 != senha_2:
          raise forms.ValidationError('As senhas não são iguais')
      else:
        return senha_2