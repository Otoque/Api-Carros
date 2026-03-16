# 🚗 API de Carros

API REST desenvolvida em **Python** utilizando **FastAPI** para fornecer informações detalhadas sobre veículos.

O projeto foi criado com o objetivo de disponibilizar um conjunto de dados estruturados sobre carros, incluindo informações técnicas do veículo, dados do motor, combustível e fabricante.

A API permite consultar carros cadastrados em um banco de dados e retornar essas informações de forma simples através de endpoints HTTP.

---

# 📌 Objetivo do Projeto

Este projeto foi desenvolvido para praticar conceitos importantes de desenvolvimento backend, incluindo:

- Criação de APIs REST
- Modelagem de banco de dados
- Relacionamentos entre tabelas
- Organização de código backend
- Integração entre API e aplicações frontend

---

# 🛠️ Tecnologias Utilizadas

O projeto foi desenvolvido utilizando as seguintes tecnologias:

- **Python**
- **FastAPI**
- **SQLAlchemy**
- **SQLite**
- **Pydantic**
- **Uvicorn**

---

# 📂 Estrutura do Projeto

Api-Carros<br>
│<br>
├── api.py # Arquivo principal da API<br>
├── carros.db # Banco de dados SQLite com os dados dos carros<br>
├── requirements.txt # Dependências do projeto<br>
├── .gitignore<br>
└── README.md<br>

---

# ⚙️ Como executar o projeto localmente

### 1️⃣ Clone o repositório

git clone https://github.com/Otoque/Api-Carros.git

---

### 2️⃣ Entre na pasta do projeto

cd Api-Carros

---

### 3️⃣ Crie um ambiente virtual

python -m venv venv

---

### 4️⃣ Ative o ambiente virtual

Linux / Mac

source venv/bin/activate

Windows

/venv/bin/Scripts/activate

---

### 5️⃣ Instale as dependências

pip install -r requirements.txt

---

## 6️⃣ Execute a API:

uvicorn api:app --reload

---

### 7️⃣ Acesse a API

http://127.0.0.1:8000

---

# 📖 Documentação da API

O FastAPI gera automaticamente uma interface de documentação interativa.

Swagger UI:

http://127.0.0.1:8000/docs

Nela é possível:

- testar os endpoints
- visualizar respostas
- enviar requisições diretamente pelo navegador

---

# 🔎 Endpoints da API

## Listar todos os carros

GET /carros

Retorna todos os carros cadastrados no banco de dados.

---

## Buscar um carro aleatório

GET /carros/aleatorio

Retorna um carro aleatório do banco de dados.

---

# 📊 Estrutura dos Dados

Cada carro possui informações como:

- VIN (identificação do veículo)
- Marca
- Modelo
- Ano do modelo
- Série e versão
- Tipo de veículo

Além disso, a API retorna informações técnicas do motor:

- Modelo do motor
- Configuração do motor
- Número de cilindros
- Potência (HP e KW)
- Cilindrada

Também são retornados dados de combustível:

- Combustível principal
- Combustível secundário

---

# 🏭 Fabricante

Cada carro está associado a um fabricante contendo informações como:

- Nome do fabricante
- Cidade
- Estado
- País

O relacionamento entre carros e fabricantes é feito através de **chaves estrangeiras no banco de dados**.

---

# 🗄️ Banco de Dados

O projeto utiliza **SQLite** como banco de dados.

O banco possui duas tabelas principais:

- **Carros**
- **Fabricantes**

Cada fabricante pode possuir vários carros associados.

---

# 🚀 Possíveis Melhorias Futuras

Algumas melhorias que podem ser implementadas no projeto:

- Endpoint para buscar carros por marca
- Endpoint para buscar carros por ano
- Paginação de resultados
- Autenticação na API
- Deploy com banco de dados externo (PostgreSQL)
- Interface frontend consumindo a API

---

# 👨‍💻 Autor

Projeto desenvolvido por **Nicolas Tavares**.

---

# 📄 Licença

Este projeto é livre para uso educacional e estudos.
