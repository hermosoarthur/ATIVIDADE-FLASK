

# 📚 API de Atividades

## 🧠 Objetivo Geral

Este repositório contém a API de Atividades, desenvolvida com Flask e SQLAlchemy, como parte de uma arquitetura baseada em microsserviços.

## 🧩 Arquitetura

A API de Atividades é um microsserviço que faz parte do sistema School System, sendo responsável exclusivamente pelo gerenciamento das atividades escolares.

⚠️ A API depende da [API de Gerenciamento Escolar](https://github.com/hermosoarthur/API-FLASK), que deve estar em execução para o sistema funcionar corretamente.


A comunicação entre os serviços ocorre via requisições HTTP REST, para validar:


Verificar se professor leciona a turma:  GET professores/{id}/turma/{id}


## 🚀 Tecnologias Utilizadas

Python 3

Flask

SQLAlchemy

SQLite (como banco de dados local)

Requests (para consumo da API externa)

## ▶️ Como Executar a API com Docker

1. **Clone o repositório:**
```bash
git clone https://github.com/hermosoarthur/ATIVIDADE-FLASK
cd ATIVIDADE-FLASK/atividade_service
```                                                                                                                                                                                                     
2. Criar rede com Docker (recomendado):
```bash
docker network create api-network
```
Essa rede será utilizada por todas as APIs que fazem parte do sistema de microsserviços (como as APIs de Gestão e Reservas), permitindo que elas se comuniquem entre si. *(OBS: caso já tenha feito a execução da API de gestão não é necessario criar )*

3. Construa a imagem da API
```bash
docker build -t api-atv .
```
4. Execute o container utilizando a rede criada:
```bash
docker run -d --name api-atv --network api-network -p 5002:5002 api-atv
```
A aplicação estará disponível em: 📍 http://localhost:5002/atividades

## 📡 Endpoints Principais

GET /atividades → Lista todas as atividades

POST /atividades → Cria uma nova atividade

GET /atividades/<id> → Detalha uma atividade


Exemplo de corpo JSON para criação:

```json
{
    "enuciado": "1+1",
    "id": 1,
    "id_professor": 1,
    "id_turma": 2,
    "respostas": "2,dois"
  }
```

# 🔗 Dependência Externa

Certifique-se de que a API de Gerenciamento Escolar esteja rodando em: http://localhost:5000

E que os endpoints GET professores/{id}/turma/{id}  estejam funcionando corretamente, para que a validação seja realizada com sucesso.

## 📦 Estrutura do Projeto

```bash
ATIVIDADE-FLASK/
├──atividade_service/
  ├── app.py                 
  ├── config.py       
  ├── Dockerfile           
  ├── requirements.txt      
  ├── clients/
  │ pessoa_service.py
  ├──controllers/
  │  ├── atividade_controller.py
  ├──models/
  │  ├──atividade_model.py
  ├──instance/
  │  ├──banco.bd
```


# 🛠️ Futuras Melhorias

Validação de conflito de atividades

Integração via fila (RabbitMQ) com outros microsserviços

Autenticação de usuários

Docker Compose para orquestração dos microsserviços


# 🧑‍💻 Autores

Arthur Hermoso

Luana Garrido Moreira Dias

Rafaela Santos Rodrigues

Vitória da Silva Moço

Fanthine Vitoria de Souza
