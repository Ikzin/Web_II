from django.shortcuts import render, redirect, get_object_or_404
from .models import Autor, Categoria, Editora, Livro
from django.contrib.auth.models import User
from .forms import AutorForm, CategoriaForm, EditoraForm, LivroForm, CustomLoginForm 
from django.core.paginator import Paginator
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages 


@login_required
def lista_autores(request):
    autores_lista = Autor.objects.all().order_by('nome')
    
    paginator = Paginator(autores_lista, 10) 
    
    page_number = request.GET.get('page')
    
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj
    }
    
    return render(request, 'core/autor_list.html', context)


def autor_create(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        
        if form.is_valid():
            form.save() 
            return redirect('lista_autores')  
    
    else:
        form = AutorForm() 

    context = {
        'form': form
    }
    return render(request, 'core/autor_form.html', context)


def autor_update(request, id):
    autor = get_object_or_404(Autor, id=id)
    
    if request.method == 'POST':
        form = AutorForm(request.POST, instance=autor)
        if form.is_valid():
            form.save()
            return redirect('lista_autores')
            
    else:
        form = AutorForm(instance=autor)

    context = {
        'form': form
    }
    return render(request, 'core/autor_form.html', context)


def autor_delete(request, id):
    autor = get_object_or_404(Autor, id=id)
    
    if request.method == 'POST':
        autor.delete() 
        return redirect('lista_autores') 
    
    context = {
        'autor': autor
    }
    return render(request, 'core/autor_delete_confirm.html', context)

def lista_categorias(request):
    categorias_lista = Categoria.objects.all().order_by('nome')
    paginator = Paginator(categorias_lista, 10) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj
    }
    return render(request, 'core/categoria_list.html', context)


def categoria_create(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_categorias')
    else:
        form = CategoriaForm()
    context = {
        'form': form
    }
    return render(request, 'core/categoria_form.html', context)

def categoria_update(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('lista_categorias')
    else:
        form = CategoriaForm(instance=categoria)
    context = {
        'form': form
    }
    return render(request, 'core/categoria_form.html', context)

def categoria_delete(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    if request.method == 'POST':
        categoria.delete()
        return redirect('lista_categorias')
    context = {
        'categoria': categoria
    }
    return render(request, 'core/categoria_delete_confirm.html', context)

def lista_editoras(request):
    editoras_lista = Editora.objects.all().order_by('nome')
    paginator = Paginator(editoras_lista, 10) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj
    }
    return render(request, 'core/editora_list.html', context)

def editora_create(request):
    if request.method == 'POST':
        form = EditoraForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_editoras')
    else:
        form = EditoraForm()
    context = {
        'form': form
    }
    return render(request, 'core/editora_form.html', context)

def editora_update(request, id):
    editora = get_object_or_404(Editora, id=id)
    if request.method == 'POST':
        form = EditoraForm(request.POST, instance=editora)
        if form.is_valid():
            form.save()
            return redirect('lista_editoras')
    else:
        form = EditoraForm(instance=editora)
    context = {
        'form': form
    }
    return render(request, 'core/editora_form.html', context)

def editora_delete(request, id):
    editora = get_object_or_404(Editora, id=id)
    if request.method == 'POST':
        editora.delete()
        return redirect('lista_editoras')
    context = {
        'editora': editora
    }
    return render(request, 'core/editora_delete_confirm.html', context)

@login_required
def lista_livros(request):
    livros_lista = Livro.objects.all().order_by('titulo')
    paginator = Paginator(livros_lista, 10) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj
    }
    return render(request, 'core/livro_list.html', context)

@login_required
def livro_create(request):
    if request.method == 'POST':
        form = LivroForm(request.POST, request.FILES) 
        if form.is_valid():
            form.save()
            return redirect('lista_livros')
    else:
        form = LivroForm()
    context = {
        'form': form
    }
    return render(request, 'core/livro_form.html', context)

def livro_update(request, id):
    livro = get_object_or_404(Livro, id=id)
    if request.method == 'POST':
        form = LivroForm(request.POST, request.FILES, instance=livro)
        if form.is_valid():
            form.save()
            return redirect('lista_livros')
    else:
        form = LivroForm(instance=livro)
    context = {
        'form': form
    }
    return render(request, 'core/livro_form.html', context)

@login_required
def livro_delete(request, id):
    livro = get_object_or_404(Livro, id=id)
    if request.method == 'POST':
        livro.delete()
        return redirect('lista_livros')
    context = {
        'livro': livro
    }
    return render(request, 'core/livro_delete_confirm.html', context)

def view_login(request):
    if request.user.is_authenticated:
        return redirect('lista_livros')
        
    if request.method == 'POST':
        form = CustomLoginForm(request, data=request.POST)
        
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('lista_livros') 
            else:
                messages.error(request, 'Usuário ou senha inválidos.')
        else:
             messages.error(request, 'Usuário ou senha inválidos.')
            
    form = CustomLoginForm()
    return render(request, 'core/login.html', {'form': form})


def view_logout(request):
    logout(request)
    return redirect('login')

@login_required
def home(request):
    total_livros = Livro.objects.count()
    total_autores = Autor.objects.count()
    total_categorias = Categoria.objects.count()
    
    livros_recentes = Livro.objects.all().order_by('-id')[:6]
    
    context = {
        'total_livros': total_livros,
        'total_autores': total_autores,
        'total_categorias': total_categorias,
        'livros_recentes': livros_recentes,
    }
    
    return render(request, 'core/home.html', context)