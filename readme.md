Disclaimer: This is an API for an Events Subscription Platform developed in NLW Connect 3-Day Course.

# 🌐 Event API Flask

## Características
- API RESTful desenvolvida com Flask  
- Gerenciamento de eventos (CRUD)  
- Integração com banco de dados (Usado DBeaver nos testes)  
- Funcionamento de localhost usando POSTMAN  

---

## Requisitos
- Python 3.8+  
- Flask  
- SQLAlchemy
-----------------
- Aplicação SQL (Exemplo: DBeaver) 
- Aplicação pra envio de GET/POST no host (Exemplo: Postman) 

---

## Instalação

### Clone este repositório:
```bash
git clone https://github.com/felipemchdev/Event_API_Flask.git
cd Event_API_Flask
```
### Crie um Ambiente Virtual
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
.\venv\Scripts\activate   # Windows
```
### Instale as dependências:
```bash
pip install -r requirements.txt
```
### Execute a Aplicação:
```bash
python app.py
```
### Acesse a API usando:
```
http://localhost:5000/
```

## Estrutura do Projeto:

- app.py: Script principal da aplicação

- models.py: Definição dos modelos de dados

- routes.py: Definição das rotas da API

- requirements.txt: Dependências do projeto

- README.md: Documentação do projeto

