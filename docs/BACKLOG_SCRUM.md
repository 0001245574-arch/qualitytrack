# QualityTrack — Backlog Scrum

Use este arquivo para montar o quadro (Trello, Jira ou GitHub Projects) com as colunas **To Do · In Progress · Testing · Done**. Crie um cartão por história e uma etiqueta por épico.

## Épicos
- **E1 Autenticação**
- **E2 Gestão de Não-Conformidades**
- **E3 Pesquisa e Painel**
- **E4 Qualidade (testes)**
- **E5 Documentação e Entrega**

## Histórias de usuário

| ID | Épico | História | Sprint | Coluna sugerida |
|----|-------|----------|--------|-----------------|
| US01 | E1 | Como inspetor, quero entrar com usuário e senha para acessar os dados com segurança. | 1 | Done |
| US02 | E2 | Como inspetor, quero registrar uma não-conformidade para documentar o defeito encontrado na linha. | 1 | Done |
| US03 | E2 | Como inspetor, quero registrar a ação de contenção para isolar o lote afetado imediatamente. | 1 | Done |
| US04 | E2 | Como analista, quero editar a NC e avançar sua etapa até o encerramento para acompanhar o ciclo da tratativa. | 1 | Done |
| US05 | E2 | Como gestor, quero excluir um registro lançado por engano para manter a base correta. | 1 | Done |
| US06 | E3 | Como analista, quero pesquisar por código, produto ou defeito para localizar ocorrências rapidamente. | 2 | Done |
| US07 | E3 | Como gestor, quero ver indicadores por etapa e a taxa de encerramento para apoiar a melhoria contínua. | 2 | Done |
| US08 | E4 | Como desenvolvedor, quero testes automatizados de back-end e front-end para evitar regressões. | 3 | Done |
| US09 | E5 | Como avaliador, quero o manual técnico com evidências para validar o trabalho. | 3 | Testing |
| US10 | E5 | Como equipe, quero o código no GitHub com branches main, develop e feature para registrar o histórico. | 3 | To Do |

## Critérios de aceite (exemplos)
- **US01:** login correto retorna token; senha errada retorna "Usuário ou senha incorretos".
- **US02:** NC criada recebe código único (NC-...); quantidade menor que 1 é rejeitada.
- **US04:** NC encerrada não pode ser reaberta pela edição comum.
- **US07:** painel mostra total, abertas, críticas, em tratamento, aguardando validação, encerradas e taxa de encerramento.

## Sprints
- **Sprint 1:** estrutura, banco, autenticação e CRUD (US01–US05)
- **Sprint 2:** interface, pesquisa e painel (US06–US07)
- **Sprint 3:** testes, documentação e entrega (US08–US10)
