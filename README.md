# Projeto: Biblioteca Virtual (Django)

Este projeto é um sistema de gerenciamento de biblioteca pessoal, desenvolvido em Django como atividade acadêmica.

##  Funcionalidades Principais

* **Autenticação:** Sistema de login e logout personalizado. As páginas de gerenciamento são protegidas.
* **CRUD de Livros:** Cadastro, leitura, atualização e exclusão de livros, incluindo upload de imagem da capa.
* **CRUD de Autores:** Gerenciamento completo de autores.
* **CRUD de Editoras:** Gerenciamento completo de editoras.
* **CRUD de Categorias:** Gerenciamento completo de categorias.
* **Paginação:** Todas as páginas de listagem usam o Paginator do Django.
* **Dashboard:** Página inicial com estatísticas (total de livros, autores, etc.) e livros adicionados recentemente.

## Tecnologias Utilizadas

* Python
* Django
* Bootstrap 5 (para o front-end)
* SQLite3 (banco de dados padrão)
* Git & GitHub

---

## Modelo Relacional

O sistema é construído em torno de 5 modelos principais (mais o modelo `User` padrão do Django), que se relacionam para formar a estrutura da biblioteca.

### 1. User (Padrão do Django)
A tabela padrão do Django para autenticação.
* `id` (Chave Primária)
* `username`
* `password`
* ... (outros campos de autenticação)

### 2. Leitor
Estende o `User` padrão com informações específicas do leitor.
* `id` (Chave Primária)
* `usuario` (Relação **Um-para-Um** com `User`): Cada usuário do sistema é um único leitor.

### 3. Autor
Armazena os autores dos livros.
* `id` (Chave Primária)
* `nome`
* `biografia`

### 4. Categoria
Armazena os gêneros/categorias dos livros (ex: Ficção, Biografia).
* `id` (Chave Primária)
* `nome`

### 5. Editora
Armazena as editoras dos livros.
* `id` (Chave Primária)
* `nome`
* `site`

### 6. Livro (O Modelo Central)
O `Livro` é o modelo principal que se conecta a quase todos os outros.
* `id` (Chave Primária)
* `titulo`
* `isbn`
* `data_publicacao`
* `capa` (Caminho para a imagem de capa)
* `autor` (Relação **Muitos-para-Um** com `Autor`): Um livro tem um autor, mas um autor pode ter muitos livros.
* `editora` (Relação **Muitos-para-Um** com `Editora`): Um livro tem uma editora, mas uma editora pode ter muitos livros.
* `categorias` (Relação **Muitos-para-Muitos** com `Categoria`): Um livro pode pertencer a várias categorias, e uma categoria pode conter vários livros.

## [cite_start]Como Rodar o Projeto (Instruções) 

Siga estas instruções para rodar o projeto em sua máquina local.

**1. Clonar o Repositório:**
```bash
git clone [https://github.com/Ikzin/Web_II.git](https://github.com/SEU-USUARIO/projeto-biblioteca-django.git)
cd projeto-biblioteca-django




