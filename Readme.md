# Projeto do Desafio da TechnoTech Natal

Um projeto Django utilizando Python e Docker Compose

## Para rodar:

1 - Crie uma venv usando o python
```
$ python -m venv workvenv
$ source workvenv/bin/activate
```

2 - procure o arquivo `requiriments.txt` na pasta python code e execute:
```
pip3 install -r requirements.txt
```

3 - Instale o django por meio do requirements.txt

4 - Execute o projeto

```
python manage.py makemigrations --noinput
python manage.py migrate --noinput
python manage.py runserver
```
ou se preferir execute:
```
./start_update.sh
```

Template HTML:

1 - acesse a pasta reacttemplate

2 - dentro da subpasta template-projeto, execute:
```
npm install
npm run dev
```

Para mais informações sobre o desenrolar do projeto, acesse o relatorio.md na pasta test_codes
----------------------------------------
## Patrocinio:
- TecnoTech Natal
- Hostingator
- Jerimun Jobs
- GruPy RN
