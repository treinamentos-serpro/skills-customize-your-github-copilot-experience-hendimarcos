# 📘 Atividade: Building REST APIs with FastAPI

## 🎯 Objetivo

Crie uma API REST para gerenciar atividades de estudo usando FastAPI. Você praticará rotas HTTP, validação de dados com modelos Pydantic, operações CRUD e respostas com códigos de status apropriados.

## 📝 Tarefas

### 🛠️ Configurar a API e criar uma rota de verificação

#### Descrição

Use o código inicial para configurar a aplicação FastAPI e criar uma rota que confirme que a API está funcionando. Instale as dependências com `python -m pip install fastapi uvicorn` e execute o servidor com `python -m uvicorn starter-code:app --reload`.

#### Requisitos

O programa concluído deve:

- Criar uma instância FastAPI chamada `app`.
- Implementar `GET /health` com uma resposta JSON que indique que o serviço está funcionando.
- Permitir consultar a documentação interativa da API em `/docs`.

### 🛠️ Consultar atividades de estudo

#### Descrição

Defina um modelo Pydantic para uma atividade de estudo e implemente rotas para listar as atividades e consultar uma atividade pelo identificador.

#### Requisitos

O programa concluído deve:

- Representar cada atividade com `id`, `title`, `subject` e `completed`.
- Implementar `GET /items` para retornar a lista de atividades.
- Implementar `GET /items/{item_id}` para retornar uma atividade pelo identificador.
- Responder com status HTTP 404 quando o identificador solicitado não existir.

### 🛠️ Gerenciar atividades de estudo

#### Descrição

Complete a API implementando operações para criar, atualizar e excluir atividades. Use os modelos Pydantic do código inicial para validar os dados recebidos no corpo das requisições.

#### Requisitos

O programa concluído deve:

- Implementar `POST /items` para criar uma atividade e responder com status HTTP 201.
- Implementar `PUT /items/{item_id}` para atualizar uma atividade existente.
- Implementar `DELETE /items/{item_id}` para excluir uma atividade e responder com status HTTP 204.
- Responder com status HTTP 404 ao tentar atualizar ou excluir uma atividade inexistente.
- Permitir testar as rotas e os códigos de resposta pela documentação em `/docs`.
