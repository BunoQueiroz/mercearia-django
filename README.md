# Mercadinho
![em desenvolvimento](https://img.shields.io/badge/STATUS-EM%20DESENVOLVIMENTO-brightgreen)

# 🔨Ferramentas Utilizadas
* Django 4.1.3
* Bootstrap 5.2.2
* Postgresql 6.8

# Funcionalidades
* Renderização de páginas web
* Sistema de mensagens
* Cadastro de usuários no banco de dados
* Autenticação e login de usuário
* Dashboard para clientes logados
* Atualização de dados dos clientes
* Alteração de senha dos clientes
* Página para exibição dos produtos conforme sua categoria
* Mostrar detalhes de cada compra dos clientes
* Validação de formulários
* Landing Page básica para cada produto
* Envio de email

# Para Utilizar o projeto em seu computador realize os seguintes comandos:
LEMBRE-SE:
* Você precisa de algum banco de dados para utilizar todos os recursos do projeto sem ocorrer falhas
<br>
<br>

Crie uma pasta pasta:
```
mkdir my-project
```
E entre nela, assim:
```
cd my-project
```

No seu terminal *git bash* digite:
``` 
git clone https://github.com/BunoQueiroz/mercearia-django.git .
```

E em seguida, crie um ambiente virtual:

* COMANDO WINDOWS
```
virtualenv venv
```

* COMANDO LINUX / MAC

```
venv venv
```

Entre no ambiente:

* COMANDO WINDOWS
```
venv/Scripts/activate
```

* COMANDO LINUX / MAC

```
source venv/bin/activate
```

Instale as bibliotecas necessárias:

DJANGO :
```
pip install -r requirements.txt
```

BOOTSTRAP :
```
npm install
```

*Por fim crie, na raiz do seu projeto um arquivo .env e defina dentro dele suas variáveis de ambiente.*

Para Similar seu banco de dados ao projeto rode o comando:

```
python manage.py migrate
```

Depois de tudo isso, rode o comando:

```
python manage.py runserver
```
E seja feliz ; )

*Dúvidas ou  erros fale diretamente comigo, boa sorte com tudo*