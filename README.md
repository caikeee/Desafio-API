


Este projeto é uma API Flask para gerenciar esportes, ele utiliza SQLite como banco de dados para armazenar informações.

Siga os passos abaixo para instalar e configurar o projeto:

Clone o repositório:

git clone https://github.com/usuario/desafio-api.git
cd desafio-api

Crie um ambiente virtual (recomendado):

python -m venv venv
source venv\Scripts\activate

Instale as dependências:

pip install -r requirements.txt

Estrutura do Projeto

desafio-api/
│
├── app.py
├── models.py
├── routes.py
├── desafio_api/
│ └── esporte.db
├── requirements.txt
├── README.md
└── config.py

app.py: Arquivo principal que inicia a aplicação Flask.
cliente.py: menu que permite realizar as ações do app
desafio_api/esporte.db: Arquivo do banco de dados SQLite.
README.md: Documentação do projeto.

Como usar:

execute o arquivo 'app.py' para iniciar o aplicativo flask, após isso execute o arquivo cliente, nele tera acesso todas as funções do projeto, podendo criar, listar todas atividades ou listar por ID e deletar atividades.
