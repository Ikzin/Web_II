from django.db import models
from django.db import models
from django.contrib.auth.models import User 

class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Editora(models.Model):
    nome = models.CharField(max_length=100)
    site = models.URLField(blank=True, null=True) 

    def __str__(self):
        return self.nome

class Autor(models.Model):
    nome = models.CharField(max_length=255)
    biografia = models.TextField(blank=True) 
    
    def __str__(self):
        return self.nome

class Livro(models.Model):
    autor = models.ForeignKey(Autor, on_delete=models.PROTECT)
    editora = models.ForeignKey(Editora, on_delete=models.PROTECT)
    categorias = models.ManyToManyField(Categoria)

    titulo = models.CharField(max_length=255)
    data_publicacao = models.DateField(null=True, blank=True)
    isbn = models.CharField(max_length=13, unique=True, help_text="Número de 13 dígitos do ISBN")
    
    capa = models.ImageField(upload_to='capas_livros/', blank=True, null=True)

    def __str__(self):
        return f"{self.titulo} ({self.autor.nome})"

class Leitor(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    telefone = models.CharField(max_length=15, blank=True)
    livros_favoritos = models.ManyToManyField(Livro, blank=True, related_name='favoritado_por')

    def __str__(self):
        return self.usuario.username
