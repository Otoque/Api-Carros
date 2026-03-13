🚗 API de Carros Aleatórios
Esta é uma API desenvolvida em Python utilizando FastAPI e SQLAlchemy. O projeto permite o gerenciamento de uma base de dados de veículos, com foco em retornar veículos aleatórios e detalhes técnicos, incluindo informações sobre o fabricante vinculadas via relacionamento de banco de dados.

🚀 Funcionalidades
Listagem Completa: Retorna todos os carros cadastrados.

Carro Aleatório: Sorteia um veículo do banco de dados e retorna seus dados técnicos junto com as informações do fabricante (JOIN).

Busca por Filtros: Permite buscar carros por marca ou modelo.

Cadastro: Endpoint para salvar novos veículos e seus respectivos fabricantes.

🛠️ Tecnologias Utilizadas
FastAPI: Framework moderno e rápido para construção de APIs.

SQLAlchemy: ORM para mapeamento e manipulação do banco de dados.

SQLite: Banco de dados relacional (arquivo local) para desenvolvimento.

Pydantic: Validação de dados e criação de schemas.

Uvicorn: Servidor ASGI para rodar a aplicação.

📥 Como baixar e usar o projeto
1. Clonar o repositório
Abra o seu terminal e rode:

Bash
git clone https://github.com/Otoque/Api-Carros/tree/main
cd NOME_DO_REPOSITORI

2. Criar e Ativar o Ambiente Virtual (Virtualenv)
Para manter as dependências organizadas e não afetar seu sistema:

No Linux/Mac:

Bash
python3 -m venv venv
source venv/bin/activate
No Windows:

Bash
python -m venv venv
venv\Scripts\activate

3. Instalar as Dependências
Com o ambiente virtual ativado, instale os pacotes necessários:

Bash
pip install -r requirements.txt

4. Rodar a API
Execute o servidor Uvicorn:

Bash
uvicorn api:app --reload
A API estará disponível em: http://127.0.0.1:8000

📖 Documentação e Testes
O FastAPI gera automaticamente uma documentação interativa. Com a API rodando, acesse:

Swagger UI: http://127.0.0.1:8000/docs (Para testar os endpoints visualmente).

Redoc: http://127.0.0.1:8000/redoc (Documentação detalhada).

Exemplo de Resposta (GET /carros/aleatorio)
JSON
{
  "modelo": "330i",
  "marca": "BMW",
  "anoModelo": 2004,
  "fabricante_obj": {
    "nomeFabricante": "Regensburg Plant",
    "cidadeFabricante": "Regensburg",
    "paisFabricante": "Alemanha"
  }
}
📝 Licença
Este projeto está sob a licença MIT. Sinta-se livre para usar e modificar.
