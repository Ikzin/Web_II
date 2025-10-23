from django.urls import path
from . import views 

urlpatterns = [

    path('', views.home, name='home'),
    path('login/', views.view_login, name='login'),
    path('logout/', views.view_logout, name='logout'),

    path('autores/', views.lista_autores, name='lista_autores'),
    path('autores/novo/', views.autor_create, name='autor_create'),
    path('autores/editar/<int:id>/', views.autor_update, name='autor_update'),
    path('autores/excluir/<int:id>/', views.autor_delete, name='autor_delete'),
    
    path('categorias/', views.lista_categorias, name='lista_categorias'),
    path('categorias/nova/', views.categoria_create, name='categoria_create'),
    path('categorias/editar/<int:id>/', views.categoria_update, name='categoria_update'),
    path('categorias/excluir/<int:id>/', views.categoria_delete, name='categoria_delete'),

    path('editoras/', views.lista_editoras, name='lista_editoras'),
    path('editoras/nova/', views.editora_create, name='editora_create'),
    path('editoras/editar/<int:id>/', views.editora_update, name='editora_update'),
    path('editoras/excluir/<int:id>/', views.editora_delete, name='editora_delete'),

    path('livros/', views.lista_livros, name='lista_livros'),
    path('livros/novo/', views.livro_create, name='livro_create'),
    path('livros/editar/<int:id>/', views.livro_update, name='livro_update'),
    path('livros/excluir/<int:id>/', views.livro_delete, name='livro_delete'),

]