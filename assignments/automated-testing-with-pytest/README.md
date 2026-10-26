# 📘 Atividade: Automated Testing with Pytest

## 🎯 Objetivo

Escreva testes automatizados para uma API FastAPI usando `pytest` e `TestClient`. Você vai verificar respostas HTTP, dados retornados, validação de entrada e os comportamentos de operações CRUD.

## 📝 Tarefas

### 🛠️ Testar respostas básicas da API

#### Descrição

Instale as dependências com `python -m pip install fastapi pytest httpx` e execute os testes do código inicial com `python -m pytest -v assignments/automated-testing-with-pytest/starter-code.py`. Complete o teste de verificação de saúde e crie um teste para a listagem de atividades.

#### Requisitos

O programa concluído deve:

- Verificar que `GET /health` responde com status HTTP 200 e o JSON `{"status": "ok"}`.
- Verificar que `GET /items` responde com status HTTP 200 e retorna a atividade inicial.
- Usar as fixtures `client` e asserções do pytest para conferir as respostas.

### 🛠️ Testar busca e erros HTTP

#### Descrição

Adicione testes para consultar uma atividade existente pelo identificador e para solicitar um identificador que não existe.

#### Requisitos

O programa concluído deve:

- Verificar que `GET /items/1` retorna status HTTP 200 e os dados da atividade de exemplo.
- Verificar que `GET /items/999` retorna status HTTP 404.
- Conferir tanto o status HTTP quanto os dados relevantes da resposta.

### 🛠️ Testar operações CRUD e validação

#### Descrição

Complete a suíte testando criação, atualização e exclusão de atividades, além da validação de um corpo de requisição inválido.

#### Requisitos

O programa concluído deve:

- Verificar que `POST /items` cria uma atividade e responde com status HTTP 201.
- Verificar que `PUT /items/{item_id}` atualiza uma atividade existente e retorna os dados atualizados.
- Verificar que `DELETE /items/{item_id}` responde com status HTTP 204 e que a atividade deixa de existir.
- Verificar que uma requisição inválida para criar uma atividade responde com status HTTP 422.
- Garantir que cada teste começa com os dados iniciais usando a fixture fornecida.
