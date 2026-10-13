# Decisions

Este documento registra decisões de produto tomadas durante o desenvolvimento.

Seu objetivo é preservar o contexto das escolhas realizadas.

---

## 001 - O domínio será centrado em Requests

Data: 2026-08-05

### Contexto

Inicialmente o domínio estava sendo modelado em torno de Executions.

Após a análise do fluxo de negócio percebeu-se que o usuário nunca pensa em "execuções".

Ele faz solicitações para que a plataforma resolva um problema.

### Decisão

A entidade central do domínio passa a ser Request.

A plataforma poderá utilizar uma ou mais Tasks, Automations ou outros mecanismos para atender cada Request.

Esses detalhes permanecem internos ao sistema.

### Motivação

Modelar o domínio utilizando a linguagem do negócio.

### Consequências

- O domínio fica desacoplado da implementação.
- A arquitetura torna-se mais flexível.
- Novos mecanismos poderão ser adicionados futuramente sem alterar o conceito central da plataforma.
