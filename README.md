Python versão 3+

Instalação:
Linux
* python3 -m venv env
* source env/bin/activate
* source .env

Windows (Necessário usar o Powershell):
* Instalar o sqlite a partir do link https://www.sqlite.org/download.html
* python -m venv env
* env/Scripts/Activate.ps1
* ./env.ps1

A partir deste ponto os passos não dependem do sistema operacional:
Este trecho é executado apenas na instalação
* pip install -r requirements.txt
* flask db init
* flask db migrate
* flask db upgrade
* flask setup

Após tudo configurado, usar o seguinte comando para iniciar o servidor da aplicação
* flask run

* abrir no navegador a url http://localhost:5000

Caso use o Visual Studio Code, é possível instalar a seguinte extensão para visualizar as tabelas no sqlite
https://marketplace.visualstudio.com/items?itemName=cweijan.vscode-mysql-client2