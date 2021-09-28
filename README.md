Instalação:
Linux
* python3 -m venv env
* source env/bin/activate
* source .env

Windows (Powershell):
* python -m venv env
* env/Scripts/Activate.ps1
* ./env.ps1

A partir deste ponto os passos não dependem do sistema operacional:
* pip install -r requirements.txt
* flask db init
* flask db migrate
* flask db upgrade
* flask run


Uso:
* source env/bin/activate  (Caso ainda não esteja ativo)
* python run.py
* abrir no navegador a url http://localhost:5000
