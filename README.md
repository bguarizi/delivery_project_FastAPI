# Plataforma de Delivery - Projeto teste usando FastAPI

Este projeto tem por objetivo simular um ambiente de delivery no qual uma loja pode realizar a venda de seus produtos. O projeto inclui:

- Criação de cadastro para novos usuários
- Realização de login via swagger ou API (como o projeto não conta ainda com uma interface frontend, os testes devem ser realizados via swagger - página /docs)
- Deleção de usuários
- Criação e deleção de um pedido
- Adição e remoção de itens em um pedido
- Listar pedidos ativos do usuário
- Cancelamento de pedido (desistência)
- Finalização de pedido (conclusão/entrega do pedido)

* O sistema executa criptografia de senha para os cadastros criados e possui bloqueio de acesso de algumas rotas para usuários logados e para usuários adm.

* Hoje não há bloqueio sobre a criação de usuários adm, qualquer usuário pode criar seu acesso como admin.

## Instalação

Para instalar o projeto, siga estes passos:

1. Clone o repositório em sua máquina e acesse a pasta do projeto:

    ```bash
    git clone https://github.com/bguarizi/delivery_project_FastAPI.git
    cd delivery_project_FastAPI/
    ```

3. Crie uma virtual environment:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

4. Acesse o repositório baixado e instale o requirements.txt:

    ```bash
    pip install -r requirements.txt
    ```

5. Execute o import e a migração do banco de dados:

    ```bash
    ./venv/bin/python -c "import sqlite3; sqlite3.connect('database/banco.db')"
    ./venv/bin/alembic upgrade head
    ```
6. Altere o arquivo .env.exemple:

Ajuste o arquivo para conter os dados indicados e renomeie-o para ".env"

7. Inicie o projeto:

    ```bash
    uvicorn main:app --reload
    ```

    Acesse a URL indicada no terminal com /docs no final para acessar as rotas da aplicação: http://127.0.0.1:8000/docs







