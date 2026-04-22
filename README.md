# 🌦️ Weather ETL Pipeline

Pipeline de dados **ETL (Extract, Transform, Load)** para coleta, processamento e armazenamento de dados meteorológicos, utilizando **Python, Apache Airflow, PostgreSQL e Docker**.

---

## 📌 Visão Geral

Este projeto implementa um pipeline automatizado que:

- **Extrai** dados meteorológicos de uma API externa
- **Transforma** os dados (limpeza, padronização e estruturação)
- **Carrega** os dados em um banco relacional para análise

O objetivo é simular um fluxo de engenharia de dados, com orquestração, persistência e organização.

---

## 🧱 Arquitetura

```
          +-------------------+
          |   Weather API     | 
          +-------------------+
                    ↓
          +-------------------+
          |     Extract       | Python
          +-------------------+
                    ↓
          +-------------------+
          |    Transform      | Python
          +-------------------+
                    ↓
          +-------------------+
          |       Load        |
          |   PostgreSQL DB   | 
          +-------------------+
                    ↓
          +-------------------+
          |    Orquestração   | Apache Airflow
          +-------------------+
          Infra: Docker 
```

---

## ⚙️ Tecnologias Utilizadas

- **Python** → lógica do pipeline
- **Apache Airflow** → orquestração de DAGs
- **PostgreSQL** → armazenamento dos dados
- **Docker & Docker Compose** → containerização
- **Requests / Pandas** → manipulação de dados

---

## 📂 Estrutura do Projeto

```bash
.
├── dags/ #dags e tasks do airflow                 
├── src/ #scripts python de etl 
├── .gitignore   
├── README.md          
├── docker-compose.yaml #infra do airflow e postgres   
├── main.py #srcipt de teste para execução manual local                   
├── project.toml #dependências e requisitos        
└── uv.lock
```

---

## 🔄 Pipeline ETL

### 1. Extract (Extração)
- Consome dados de uma API meteorológica
- Realiza requisições HTTP
- Retorna dados em formato JSON

### 2. Transform (Transformação)
- Limpeza de dados
- Conversão de tipos
- Tratamento de valores nulos
- Estruturação em DataFrame

### 3. Load (Carga)
- Conexão com PostgreSQL
- Inserção e armazenamento dos dados em tabelas

---

## 🚀 Como Executar o Projeto

### 1. Clone o repositório

```bash
git clone https://github.com/LucasgPetry/pipeline-etl-weather.git
cd pipeline-etl-weather
```

---

### 2. Configure as variáveis de ambiente

Crie um arquivo `.env` com:

```env
POSTGRES_USER=seu_usuario
POSTGRES_PASSWORD=sua_senha
POSTGRES_DB=weather_db
POSTGRES_HOST=postgres

API_KEY=sua_api_key
```

---

### 3. Suba os containers

```bash
docker compose up -d
```

---

### 4. Acesse o Airflow

- URL: http://localhost:8080  
- Usuário/Senha: definidos no `docker-compose`

---

### 5. Execute a DAG

- Ative a DAG no painel do Airflow
- Execute manualmente ou aguarde o agendamento

---

## 📄 Licença

Este projeto está sob a licença MIT.

---

## 👨‍💻 Autor

Lucas Petry  
https://github.com/LucasgPetry 

Créditos destinados a: @vbluuiza  
Esse projeto foi realizado como forma de estudo com fonte: https://youtu.be/I8qPqbXQBDU?si=_CYXG2YNU-A9C9BC
