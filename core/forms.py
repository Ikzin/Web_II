from django import forms
from .models import Autor, Categoria, Editora, Livro
from django.contrib.auth.forms import AuthenticationForm

class AutorForm(forms.ModelForm):
    
    class Meta:
        model = Autor  
        fields = ['nome', 'biografia']

class CategoriaForm(forms.ModelForm):

    class Meta:
        model = Categoria
        fields = ['nome']

class EditoraForm(forms.ModelForm):
    
    class Meta:
        model = Editora
        fields = ['nome', 'site']

class LivroForm(forms.ModelForm):
    
    autor = forms.ModelChoiceField(
        queryset=Autor.objects.all().order_by('nome'),
        label="Autor"
    )
    
    editora = forms.ModelChoiceField(
        queryset=Editora.objects.all().order_by('nome'),
        label="Editora"
    )
    
    categorias = forms.ModelMultipleChoiceField(
        queryset=Categoria.objects.all().order_by('nome'),
        label="Categorias"
    )

    class Meta:
        model = Livro
        fields = [
            'titulo', 
            'autor', 
            'editora', 
            'categorias', 
            'isbn', 
            'data_publicacao', 
            'capa' 
        ]
        
        widgets = {
            'data_publicacao': forms.DateInput(attrs={'type': 'date'}),
        }

class CustomLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(CustomLoginForm, self).__init__(*args, **kwargs)
        
        self.fields['username'].widget.attrs.update({
            'class': 'form-control mb-3', 
            'placeholder': 'Usuário'
        })
        self.fields['password'].widget.attrs.update({
            'class': 'form-control mb-3',
            'placeholder': 'Senha'
        })