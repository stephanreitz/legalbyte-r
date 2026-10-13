# User Flows

Este documento descreve os principais fluxos de utilização da plataforma LegalByte.

Seu objetivo é servir como referência para o desenvolvimento da interface, da API e das regras de negócio.

---

# Fluxo 1 - Login

## Objetivo

Permitir que um usuário autenticado acesse as automações disponíveis na plataforma.

## Fluxo

Usuário informa email e senha.
Clica em Entrar.
Credenciais válidas → Dashboard.
Credenciais inválidas → mensagem de erro.
Campos obrigatórios.

---

# Fluxo 2 - Dashboard

## Objetivo

Apresentar todas as automações disponíveis para o usuário.
As ferramentas disponíveis podem variar de acordo com o usuário.

## Fluxo

Após o login, o usuário é direcionado para a tela principal da LegalByte.
A tela apresenta uma saudação ao usuário.
A tela apresenta a lista de ferramentas disponíveis para aquele usuário.
O usuário pode selecionar uma ferramenta para iniciar uma solicitação.

Cada automação é representada por:

- Nome
- Descrição resumida
- Ícone
  ↓
  Usuário seleciona a automação desejada
  ↓
  Sistema direciona para a tela específica daquela automação

---

# Fluxo 3 - Executar uma Solicitação

## Objetivo

Executar uma solicitação utilizando uma ferramenta da LegalByte.

## Fluxo

Usuário seleciona uma ferramenta no Dashboard
↓
Sistema abre uma nova página específica da ferramenta
↓
Sistema apresenta:
Nome da ferramenta
Explicação sobre a finalidade da ferramenta
Descrição do resultado esperado
Passo a passo de como utilizar corretamente a ferramenta
Inputs necessários para aquela ferramenta
Opções específicas da ferramenta (checkboxes, seletores, etc.)
Campo para upload de um ou mais arquivos
Botão para iniciar a solicitação
↓
Usuário segue as instruções apresentadas
↓
Usuário seleciona as opções disponíveis
↓
Usuário envia os arquivos necessários
↓
Validações antes da execução
O sistema valida:
Se todos os campos obrigatórios foram preenchidos.
Se todas as opções obrigatórias foram selecionadas.
Se pelo menos um arquivo foi enviado, quando necessário.
Se a quantidade de arquivos está dentro dos limites definidos pela ferramenta.
Se os arquivos possuem formatos suportados pela ferramenta.
Se os arquivos atendem aos requisitos específicos da ferramenta.
Se os parâmetros informados são válidos e compatíveis entre si.
Se o usuário possui permissão para utilizar a ferramenta.
Se a solicitação está apta para ser processada.
↓
Dados válidos → solicitação é iniciada
Dados inválidos → sistema informa os problemas encontrados e não inicia a execução
↓
Sistema cria e processa a solicitação
↓
A solicitação pode disparar uma ou mais automações do mesmo tipo
↓
Sistema processa todos os processos relacionados à solicitação
↓
Após a finalização de todos os processos, sistema gera o resultado da solicitação
↓
Sistema apresenta o resultado
↓
Usuário realiza o download do arquivo gerado, normalmente uma planilha

---

## Fluxo 4 - Acompanhar e Finalizar uma Solicitação

### Objetivo

Permitir que o usuário acompanhe o processamento de uma solicitação, visualize o resultado de cada Task e obtenha o resultado final da solicitação.

### Fluxo

Usuário inicia uma solicitação após o preenchimento e validação dos inputs
↓
Sistema direciona o usuário para uma nova página de acompanhamento da solicitação
↓
Sistema apresenta a lista de Tasks relacionadas à solicitação
↓
Cada Task apresenta seu status de processamento
↓
Sistema atualiza os status conforme as Tasks são processadas
↓
Para cada Task concluída com sucesso:

- Sistema informa que o processamento foi concluído.
- Sistema registra o resultado correspondente.
  Para cada Task que falhar:
- Sistema informa que o processamento falhou.
- Sistema apresenta o respectivo motivo da falha.
  ↓
  Sistema aguarda a finalização de todas as Tasks
  ↓
  Todas as Tasks concluídas
  ↓
  Sistema apresenta o resultado consolidado da solicitação
  ↓
  Sistema gera um relatório contendo os resultados das Tasks, relacionando:
- Tasks concluídas com sucesso
- Tasks que falharam
- Motivo da falha de cada Task
  ↓
  Usuário realiza o download do relatório gerado, normalmente uma planilha.

### Observação

O conteúdo específico do resultado pode variar de acordo com a ferramenta utilizada.
Independentemente da ferramenta, toda solicitação deve permitir identificar:

- O que foi processado.
- O que foi concluído com sucesso.
- O que falhou.
- O motivo de cada falha.

---

# Fluxo 4 - Logout

Usuário seleciona "Sair"
↓
Sistema encerra a sessão
↓
Usuário retorna para a tela de login

---

# Fluxo padrão das automações

Independentemente da funcionalidade, toda automação seguirá o mesmo padrão de utilização.

Entrada
↓
Configuração
↓
Execução
↓
Resultado

Este fluxo deve permanecer consistente para proporcionar uma experiência uniforme ao usuário.

---

# MVP

No MVP existirá apenas uma automação disponível:

- Filtro de Publicações Irrelevantes

As demais automações serão adicionadas gradualmente, reutilizando o mesmo fluxo de navegação.
