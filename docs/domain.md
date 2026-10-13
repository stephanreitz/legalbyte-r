# Domain

Este documento define a linguagem e o modelo de domínio da LegalByte.

Código, documentação e regras de negócio devem usar os mesmos termos. Quando uma funcionalidade introduzir um conceito de negócio novo, este documento deve ser atualizado.

---

## Visão

A LegalByte é uma plataforma de automação jurídica para escritórios de advocacia.

O objetivo é reduzir o tempo gasto em tarefas operacionais e repetitivas, para que advogados e estagiários se concentrem em atividades que exigem análise jurídica.

O modelo é centrado em Solicitações (Requests). O usuário não interage diretamente com automações. Ele solicita que a plataforma resolva um problema. A implementação usada para atender essa solicitação é um detalhe interno da aplicação.

---

## Princípios

Toda nova funcionalidade deve:

- Automatizar ou simplificar uma atividade recorrente do fluxo jurídico.
- Reduzir tempo operacional e erros humanos.
- Produzir um resultado claro e útil para o usuário.
- Permanecer independente das demais automações sempre que possível.

---

## Modelo conceitual

```text
Office
  ↓
Users
  ↓
Requests
  ↓
Tasks
  ↓
Automations
  ↓
Output
```

---

## Glossário

### Office (Escritório)

Cliente da plataforma. Agrupa usuários e suas solicitações.

Exemplos: Marchiori, Sachet, Barros & Dias Advogados; Escritório XPTO.

### User (Usuário)

Pessoa autorizada a usar a plataforma. Pertence a um único escritório e cria solicitações.

Perfis iniciais:

- Advogado
- Estagiário

Outros papéis (Administrador, Gestor etc.) poderão existir no futuro.

### Request (Solicitação)

Intenção do usuário. Toda interação relevante começa com uma solicitação.

Exemplos: filtrar uma planilha; protocolar um lote de processos; buscar informações em documentos; gerar um relatório.

A Request é o Aggregate Root do domínio. Ela armazena parâmetros e entradas, acompanha o processamento, consolida resultados e apresenta o status geral ao usuário.

Status da Request:

- Pendente
- Em processamento
- Concluída
- Concluída parcialmente
- Falhou

### Task

Unidade de trabalho necessária para atender uma Request. Uma Request pode gerar uma, dezenas ou centenas de Tasks.

Cada Task tem o próprio ciclo de vida e o próprio status. Os logs pertencem às Tasks, para informar o que foi executado, o que falhou e por quê.

### Automation (Automação)

Mecanismo capaz de executar uma Task. Não é o centro do domínio: é um dos mecanismos usados para atender uma Request.

Exemplos: Filtro de Publicações Irrelevantes; Protocolos Automatizados; Análise de Planilhas; Busca Inteligente em Documentos.

Novos mecanismos podem surgir sem alterar o conceito central do sistema.

### Input

Dados fornecidos pelo usuário: arquivos (XLSX, CSV, PDF, DOCX) ou parâmetros informados na interface.

### Output

Resultado produzido pela plataforma: planilha, PDF, relatório, mensagem ou arquivo compactado.

### Publicação

Conceito específico da automação Filtro de Publicações Irrelevantes. Cada publicação é um registro da planilha enviada pelo usuário, classificado como relevante ou irrelevante segundo as regras da automação.

---

## Fluxo principal

```text
Office
  ↓
User
  ↓
Cria uma Request
  ↓
Fornece Input
  ↓
A Request gera uma ou mais Tasks
  ↓
Automations executam as Tasks
  ↓
A Request consolida o Output
  ↓
O usuário faz o download
```

---

## Fora do escopo

A LegalByte não substitui o sistema de gestão (CRM/ERP) do escritório.

Atua como plataforma complementar de automações e poderá, no futuro, integrar-se a sistemas já existentes.
