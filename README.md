# Dicadm App

## Introdução

**Dicadm App** é uma aplicação web voltada para estudantes de administração que tem como objetivo ser uma fonte de pesquisa para os jovens estudantes e pequenos empresários.
Serão mais de **300 termos** que foram coletados de livros e Internet. Caso encontre algum erro e/ou tenha dicas, sugestões ou críticas, entre em contato :).
Inicialmente a aplicação foi pensada para ser um dicionário de termos técnicos da administração, que aos poucos seriam adicionados funções como divulgações de vagas de estágios, dicas sobre áreas da administração, dicas sobre o mercado de trabalho em Teresina/PI, criação de uma aplicação para smartphones Android, e etc.

## Imagens

![Início](_design/screenshot/home.png "Página inicial")

![Sobre](_design/screenshot/about.png "Página sobre")

![Dicionário](_design/screenshot/dictionary.png "Página de pesquisa")

## Tecnologias utilizadas

* [Python](https://www.python.org/) 3.5
* [Django](https://www.djangoproject.com/) 1.10
* [Bootstrap](http://getbootstrap.com/) 3.3

## Outros requisitos

* [model-mommy](https://pypi.python.org/pypi/model_mommy) 1.2.6
* [six](https://pypi.python.org/pypi/six) 1.10.0
* [whitenoise](https://pypi.python.org/pypi/whitenoise) 3.2.2

## Para testar

1. Clone o projeto para a sua máquina local:

`https://github.com/VictorHolanda21/dicadm_django.git`

2. Entre no diretório do projeto:

`cd dicadm_django`

3. Crie um ambiente virtual no python:

`virtualenv -p python3 vdicadm`

4. Ative o ambiente:

`source vdicadm/bin/activate`

5. Instale as dependências:
 
 `pip install -r requirements.txt`

6. Execute as migrações:

`./manage.py migrate `

7. Popule o banco de dados:

`./manage.py shell < seed.py`

8. Teste a aplicação:

`./manage.py test`

A aplicação não está 100% testada.

9. Rode o servidor:

`./manage.py runserver 0:8000`

## Visite

* Github [código fonte](https://github.com/VictorHolanda21/dicadm_django);
* Demo [projeto](https://victorholanda21.pythonanywhere.com/)

## Etapas do projeto

- [x] Início: primeiras views e rotas
- [x] App Dictionary
- [x] Refatorar código, tema
- [x] Pesquisa de termos
- [x] Paginação de resultados
- [x] Refatorar código, tema (2)
- [ ] Acesso de usuários
- [ ] Adicionar função "gostei"
- [ ] Api para aplicativo mobile
- [ ] Adicionar função "favoritos"
