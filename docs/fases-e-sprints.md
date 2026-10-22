# Fases e Sprints — LegalByte Resurrection

## Objetivo

Este documento registra as fases de desenvolvimento e o roadmap de sprints definido para o projeto.

O princípio central é **evolução incremental**: a arquitetura e a complexidade devem amadurecer conforme surgem necessidades reais, evitando overengineering.

---

# Fases do projeto

## Fase 1 — Planejamento

**Status: concluída**

Antes de escrever código:

- [x] README
- [x] Visão do produto
- [x] Requisitos
- [x] Regras de negócio
- [x] Diagramas
- [x] Modelo de banco
- [x] Roadmap
- [x] Backlog
- [x] Issues

---

## Fase 2 — Arquitetura

**Status: em andamento**

Tecnologias previstas:

- [x] Django
- [x] Django REST Framework
- [x] PostgreSQL
- [ ] Docker
- [ ] Redis
- [ ] Celery
- [x] pytest
- [ ] GitHub Actions

> Kubernetes não faz parte do escopo inicial.

A arquitetura deve evoluir conforme as necessidades do projeto, em vez de ser definida de forma excessivamente complexa desde o início.

---

## Fase 3 — Clean Architecture

**Status: planejada / evolução incremental**

A separação arquitetural será introduzida conforme houver necessidade real.

Exemplos previstos:

- `apps/`
  - `users/`
  - outras aplicações de domínio
- `core/`
- `domain/`
- `application/`
- `infrastructure/`

Não é objetivo refatorar tudo antecipadamente. A arquitetura deve amadurecer junto com o sistema.

---

## Fase 4 — REST API

**Status: em andamento**

Objetivos:

- CRUDs necessários
- Autenticação JWT
- Autorização
- Paginação
- Filtros
- Ordenação
- Documentação Swagger/OpenAPI
- Versionamento

---

## Fase 5 — Testes

**Status: em andamento**

Cada feature deve nascer com testes.

Tipos previstos:

- Unit tests
- Integration tests
- API tests

O objetivo é manter cobertura alta e garantir que novas alterações não quebrem funcionalidades existentes.

---

## Fase 6 — Docker

**Status: planejada**

Objetivo:

```bash
docker compose up
```

O ambiente deverá incluir:

- PostgreSQL
- Backend
- Redis, quando necessário
- Nginx posteriormente

---

## Fase 7 — CI/CD

**Status: planejada**

Pipeline inicial:

```text
Push
 ↓
Lint
 ↓
Format
 ↓
Tests
 ↓
Coverage
 ↓
Build Docker
```

Posteriormente:

```text
Merge na main
 ↓
Deploy automático
```

---

## Fase 8 — AWS

**Status: planejada**

Deploy em produção somente depois de o projeto estar funcionando.

Serviços possíveis:

- EC2
- RDS
- S3
- CloudFront
- Route53

Não é necessário utilizar todos.

---

## Fase 9 — Observabilidade

**Status: planejada**

Adicionar:

- Logs
- Health Check
- Metrics
- Error Handling

---

## Fase 10 — Performance

**Status: planejada**

Primeiro medir, depois otimizar.

Possíveis otimizações:

- Redis
- Cache
- Otimização de queries
- Resolução de N+1
- Índices
- `EXPLAIN ANALYZE`

---

## Fase 11 — Features de empresa

**Status: planejada**

Funcionalidades que podem ser adicionadas conforme a evolução do produto:

- Upload de arquivos
- Background jobs
- E-mails
- Webhooks
- Exportação
- Importação
- Rate limiting
- Permissions
- Auditoria
- Soft delete
- Versionamento
- Feature flags

---

# Roadmap de Sprints

## Sprint 0 — Descoberta e planejamento

**Duração:** 1 semana  
**Status: concluída**

### Objetivo

Não escrever código.

### Entregáveis

- [x] README
- [x] Visão do produto
- [x] Roadmap
- [x] Backlog
- [x] Wireframes simples
- [x] Modelo inicial do banco
- [x] Definição das entidades

### Aprendizado

Como iniciar um projeto profissional.

### Pergunta de entrevista

> Como você planeja um software antes de começar?
> Começo pelo problema, não pela stack. Quero saber quem usa, o que precisa ser verdadeiro no primeiro entregável e o que deliberadamente fica de fora. Isso vira visão, linguagem de domínio, fluxos principais e um backlog pequeno.
> Só então um plano incremental: fatias que dão valor sozinhas, na ordem de risco. Decisões que mudam o modelo (o que é a entidade central, o que o usuário realmente faz) eu registro, para não perder o “porquê”.
> Não desenho a arquitetura final no dia zero. Infra, filas e camadas extra entram quando um requisito real aparecer. Planejar, para mim, é reduzir incerteza o suficiente para começar a construir com segurança — não antecipar os próximos dois anos.

---

## Sprint 1 — Fundação do projeto

**Duração:** 2 semanas  
**Status: concluída**

### Objetivo

Estabelecer a fundação do backend e sua arquitetura inicial.

### Entregáveis

- [x] Django
- [x] Django REST Framework
- [x] PostgreSQL
- [x] Estrutura de pastas
- [x] Configurações
- [x] Usuário
- [x] Autenticação JWT

### Progresso atual

Já foram implementados e testados:

- Projeto Django
- App `users`
- PostgreSQL
- Custom User Model
- E-mail como identificador do usuário
- Configuração do pytest
- Testes do modelo de usuário
- Registro de usuário via API
- Serializer de registro
- View de registro
- Rotas da API

O próximo passo é concluir a autenticação JWT e seus testes.

### Fora do escopo desta sprint

- Upload
- Processamento de arquivos
- Docker
- AWS

### Pergunta de entrevista

> Como você organiza um backend?
> Pelo domínio, não por tecnologia. Cada área de negócio vira um módulo (users, depois o que o produto exigir). Configuração, rotas e settings ficam à parte. Testes fora do código de produção, agrupados por feature.
> A estrutura inicial é a mais simples que atende o requisito atual: modelo, API, autenticação, banco. Uso bibliotecas maduras no lugar de reinventar (por exemplo JWT). Cada fatia nasce com teste; o teste descreve o contrato antes da implementação.
> Quando a lógica cresce ou as responsabilidades se misturam, extraio um service ou uma camada a mais. Não organizo o backend para um sistema hipotético de escala — organizo para o que existe hoje, de um jeito que ainda dá para evoluir sem reescrever tudo.

## Sprint 2 — Upload de planilhas

**Duração:** 2 semanas  
**Status: in progress**

### Objetivo

Permitir que o sistema trabalhe com arquivos enviados pelo usuário.

### Entregáveis

- [ ] Login
- [ ] Upload
- [ ] Armazenamento do arquivo
- [ ] Listagem de uploads

### Observação

Ainda não haverá processamento dos arquivos.

### Aprendizado

- Storage
- Upload
- Organização

### Pergunta de entrevista

> Como você trabalha com arquivos?

---

## Sprint 3 — Primeira feature real

**Status: não iniciada**

Esta é a sprint mais importante do MVP.

### Feature

**Filtro de Publicações**

### Fluxo

```text
Upload
  ↓
Processamento
  ↓
Arquivo final
  ↓
Download
```

### Estratégia

- [ ] Processamento síncrono
- [ ] Sem Celery
- [ ] Sem Redis

A primeira implementação deve ser simples e funcional.

### Pergunta de entrevista

> Como você implementou essa regra de negócio?

---

## Sprint 4 — Testes

**Status: não iniciada**

### Objetivo

Parar de adicionar features e aprofundar a estratégia de testes.

### Entregáveis

- [ ] pytest
- [ ] Testes de API
- [ ] Testes de services
- [ ] Testes de autenticação

### Pergunta de entrevista

> Como você garante que novas alterações não quebram o sistema?

---

## Sprint 5 — Docker

**Status: não iniciada**

### Objetivo

Containerizar o projeto.

### Entregáveis

- [ ] Backend
- [ ] Banco
- [ ] `docker compose up`

### Pergunta de entrevista

> Como outro desenvolvedor roda seu projeto?

---

## Sprint 6 — Refatoração

**Status: não iniciada**

### Objetivo

Revisar o código depois de já existir uma implementação real.

Aplicar somente onde houver necessidade:

- [ ] SOLID
- [ ] Clean Architecture

Não refatorar tudo antecipadamente.

### Pergunta de entrevista

> O que você faria diferente hoje?

---

## Sprint 7 — Deploy

**Status: não iniciada**

### Objetivo

Colocar o sistema no ar.

Possibilidades:

- [ ] EC2
- [ ] Nginx
- [ ] Gunicorn

### Fora do escopo

- Kubernetes
- Terraform
- ECS

### Pergunta de entrevista

> Como colocar um Django em produção?

---

## Sprint 8 — GitHub Actions

**Status: não iniciada**

### Objetivo

Automatizar a qualidade do código.

### Pipeline

```text
Push
 ↓
Lint
 ↓
Testes
 ↓
Build
```

Deploy ainda será manual.

### Pergunta de entrevista

> Como você automatiza qualidade?

---

## Sprint 9 — Deploy automático

**Status: não iniciada**

### Objetivo

Automatizar o deploy.

### Fluxo

```text
Merge na main
 ↓
Deploy
```

### Pergunta de entrevista

> Como funciona seu pipeline?

---

## Sprint 10 — Performance

**Status: não iniciada**

### Objetivo

Medir antes de otimizar.

### Possíveis atividades

- [ ] Identificar gargalos
- [ ] Índices
- [ ] Cache
- [ ] Otimização

### Pergunta de entrevista

> Como você melhora performance?

---

## Sprint 11 — Próxima feature

**Status: não iniciada**

### Objetivo

Adicionar outra automação ou funcionalidade relevante.

Possibilidades:

- [ ] OCR
- [ ] Processador de PDFs
- [ ] Integração
- [ ] Dashboard

A escolha será feita conforme a evolução do produto.

---

# Princípio de evolução incremental

A arquitetura não deve ser tratada como uma sprint isolada.

A evolução esperada é:

- **Sprint 1:** estrutura simples e organizada (`apps`, `core`, `config`), sem exageros.
- **Sprint 3:** quando a lógica de processamento crescer, extrair `services.py` ou um caso de uso dedicado.
- **Sprint 6:** quando surgirem responsabilidades misturadas, introduzir interfaces, injeção de dependências ou separação mais clara entre domínio e infraestrutura.
- **Sprint 10:** revisar decisões tomadas no início e refatorar apenas o que realmente se tornou um problema.

Esse fluxo representa melhor a realidade de projetos profissionais: a arquitetura amadurece conforme os requisitos evoluem.

---

# O que deliberadamente não faz parte do roadmap inicial

Evitar tecnologias que adicionariam complexidade sem necessidade real:

- Kubernetes
- Microserviços
- Kafka
- RabbitMQ
- Event Sourcing
- CQRS
- Elasticsearch
- Terraform
- Helm
- Prometheus

O objetivo é construir um produto real com a complexidade adequada para um desenvolvedor pleno, e não fazer o projeto parecer uma infraestrutura de uma empresa de centenas de engenheiros.

---

# Status atual

**Sprint atual: Sprint 1 — Fundação do projeto**

### Concluído

- Sprint 0 inteira
- Django
- DRF
- PostgreSQL
- Estrutura inicial
- Configurações
- Custom User Model
- E-mail como identificador
- pytest
- Testes do modelo
- Endpoint de registro
- Serializer
- View
- URLs
- Testes existentes passando

### Próximo passo

**Concluir autenticação JWT e seus testes.**

### Depois

1. Sprint 2 — Upload de planilhas
2. Sprint 3 — Filtro de Publicações
3. Sprint 4 — Testes
4. Sprint 5 — Docker
5. Sprint 6 — Refatoração
6. Sprint 7 — Deploy
7. Sprint 8 — GitHub Actions
8. Sprint 9 — Deploy automático
9. Sprint 10 — Performance
10. Sprint 11 — Próxima feature

---

## Sprint 12 — Refinamentos e segurança

**Status: não iniciada**

### Objetivo

Verificar a necessidade dos pontos listados a baixo.
Entender e estudar o que cada uma significa e suas importância.
Sendo realmente necessário, implementar da forma mais simples e adequada possível.
Não basta fazer, é necessário entender porque fazer e como fazer.

### Ponto a verificar

- [ ] Identificar gargalos
- [ ] Índices
- [ ] Cache
- [ ] Otimização

### Pergunta de entrevista

> Essas questões respondem qual pergunta? Segurança? O que mais?
