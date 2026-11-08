# QUALITYTRACK — Manual Técnico

**Sistema de Inspeção de Qualidade e Registro de Não-Conformidades**  
Versão acadêmica 1.0 · Novembro de 2026

> Documento de referência. Substitua os campos de identificação acadêmica e acrescente capturas reais do ambiente executado antes da entrega.

## 1. INTRODUÇÃO E ESCOPO
### 1.1 Descrição do cenário industrial selecionado
O cenário selecionado é a inspeção de qualidade e o registro de não-conformidades em uma linha de montagem de componentes eletrônicos. Defeitos como solda fria, componente invertido, trinca e dimensões fora de tolerância podem chegar à expedição quando os apontamentos são feitos em planilhas isoladas. A ausência de rastreabilidade dificulta a contenção do lote e a análise de causas.
### 1.2 Objetivos do sistema e resolução do problema
O QualityTrack centraliza o registro, classificação, contenção, correção e encerramento das ocorrências. Cada registro recebe código único, produto, linha, tipo de defeito, severidade, quantidade afetada, responsável, descrição e referência opcional de evidência. O painel consolida o volume por etapa e a taxa de encerramento.
### 1.3 Levantamento de requisitos
**Regras de negócio:** RN01 cada NC recebe código único; RN02 quantidade afetada deve ser maior que zero; RN03 severidade deve ser Baixa, Média, Alta ou Crítica; RN04 status segue Aberta, Em tratamento, Aguardando validação e Encerrada; RN05 ocorrência encerrada não pode ser reaberta pela edição comum; RN06 somente usuário autenticado acessa dados operacionais.

**Requisitos funcionais:** RF01 autenticar usuário; RF02 cadastrar NC; RF03 listar, pesquisar e consultar NC; RF04 editar dados, ações e status; RF05 excluir registro; RF06 apresentar indicadores agregados; RF07 registrar ação de contenção, ação corretiva e link de evidência.

**Requisitos não funcionais:** RNF01 API REST documentada por OpenAPI; RNF02 validação de entrada com Pydantic; RNF03 autenticação com token assinado e senha derivada por PBKDF2; RNF04 interface responsiva; RNF05 persistência relacional e separação de camadas; RNF06 testes automatizados reproduzíveis.

## 2. GESTÃO E ARQUITETURA
### 2.1 Metodologia ágil
Planejamento sugerido em três Sprints: Sprint 1 — estrutura, banco, autenticação e CRUD; Sprint 2 — interface, filtros e painel; Sprint 3 — testes, correções, documentação e implantação. Quadro Scrum: To Do (diagramas, evidências e revisão final), In Progress (integração UI/API durante desenvolvimento), Testing (testes unitários, integração e interface), Done (funcionalidades validadas). Atualize o quadro com evidências reais da equipe.
### 2.2 Fluxo de versionamento
Estratégia GitFlow simplificada: `main` contém versões estáveis; `develop` integra funcionalidades; `feature/nome-da-funcionalidade` recebe alterações isoladas. Após revisão e testes, a feature é mesclada em develop; versão validada é promovida para main com tag `v1.0.0`. Commits recomendados: `feat:`, `fix:`, `test:`, `docs:`.
### 2.3 Arquitetura de software adotada
Arquitetura SPA/API desacoplada. React apresenta telas e consome endpoints REST. FastAPI Controller recebe e valida requisições; Service aplica regras; Repository concentra acesso SQLAlchemy; SQLite persiste os registros. O token Bearer protege endpoints privados. Diagrama: `docs/diagramas/arquitetura.mmd`.
### 2.4 Modelagem de dados
MER/DER: entidade `NonConformity` (não-conformidade), identificada por `id` e código único `code`. A entidade possui atributos de identificação do desvio, produto, linha, tipo, severidade, status, quantidade, descrição, ações, responsável, evidência e datas. Nesta versão o modelo é deliberadamente enxuto e não possui entidades relacionadas; uma evolução poderá normalizar produto, usuário, lote e histórico de status em tabelas próprias. Diagrama: `docs/diagramas/der.mmd`.

**Dicionário de dados:** `id` inteiro PK; `code` texto único; `title` texto obrigatório; `product` texto obrigatório; `production_line` texto obrigatório; `defect_type` texto obrigatório; `severity` enum; `status` enum; `quantity` inteiro positivo; `description` texto obrigatório; `containment_action` texto opcional; `corrective_action` texto opcional; `responsible` texto obrigatório; `evidence_url` texto opcional; `created_at` e `updated_at` data/hora.

## 3. DESENVOLVIMENTO E CODIFICAÇÃO
### 3.1 Tecnologias e frameworks
Back-end: Python 3.10+, FastAPI, Pydantic, SQLAlchemy e Uvicorn. Front-end: React 18, Vite e CSS responsivo. Banco de dados: SQLite no protótipo acadêmico. Testes: Pytest, HTTPX, Vitest e Testing Library.
### 3.2 Padrões de projeto aplicados
Repository abstrai consultas e persistência; Service centraliza regras de negócio; Controller coordena HTTP e dependências; schemas DTO validam entradas e saídas. SRP é aplicado separando responsabilidades; DIP é favorecido pela injeção do repositório no serviço; OCP é favorecido pela extensão de camadas sem acoplar regra de negócio ao HTTP. Os demais princípios SOLID devem ser reavaliados conforme expansão do domínio.
### 3.3 Medidas de segurança implementadas
A API exige Bearer token nos endpoints de dados; o token é assinado com HMAC-SHA256 e possui expiração. A senha demonstrativa é derivada com PBKDF2-HMAC-SHA256 e salt aleatório. Pydantic valida tipos, limites e comprimentos. CORS permite origens configuradas. O front-end não concatena valores em SQL; SQLAlchemy utiliza parâmetros. Para produção: HTTPS obrigatório, segredo fora do repositório, usuário em tabela com política de senha, rotação de token, controle de perfis, logs, rate limiting, política de retenção e revisão de segurança. A autenticação atual usa usuário demonstrativo em memória e não substitui gestão de identidade de produção.

## 4. PLANO E EXECUÇÃO DE TESTES
### 4.1 Testes de back-end
Cinco testes unitários cobrem delegação da listagem, consulta existente, resposta 404, cálculo do dashboard e exclusão. Dois testes de integração exercitam criação/leitura e atualização/exclusão por HTTP com banco SQLite de teste. Executar `cd backend` e `pytest -v`. Registrar a saída real e cobertura após instalar `pytest-cov` se a disciplina exigir percentual de cobertura; não declarar percentual sem relatório executado.
### 4.2 Testes de front-end
Quatro testes com Vitest/Testing Library verificam renderização do login, envio do formulário de autenticação, abertura do formulário de cadastro e acessibilidade básica dos campos com rótulos e botão identificáveis. Os testes verificam elementos visíveis. Executar `cd frontend`, `npm install` e `npm test`.
### 4.3 Relatório de bugs e planos de correção
Durante a homologação, preencher tabela com: ID, descrição, severidade, passos para reproduzir, resultado esperado, resultado obtido, correção, responsável e situação. Não foram inventados bugs ou resultados de execução neste documento; registrar os achados reais da execução local.

## 5. GUIA OPERACIONAL E IMPLANTAÇÃO
### 5.1 Requisitos de infraestrutura
Computador com Windows 10/11, macOS ou Linux; Python 3.10+, Node.js 18+ e Git. Para demonstração local: 2 núcleos de CPU, 4 GB RAM e espaço livre para dependências e banco. Portas padrão: 8000 (API) e 5173 (Vite). SQLite grava arquivo local.
### 5.2 Variáveis de ambiente e configuração
Copiar `backend/.env.example` para `backend/.env`. Configurar `DATABASE_URL`, `SECRET_KEY`, `ACCESS_TOKEN_MINUTES` e `CORS_ORIGINS`. Não publicar `.env` nem usar a chave de exemplo em produção. No front-end, `VITE_API_URL` pode apontar para a URL da API.
### 5.3 Roteiro de deploy passo a passo
Back-end: criar ambiente virtual, instalar `requirements.txt`, configurar `.env` e iniciar `uvicorn app.main:app --host 0.0.0.0 --port 8000`. Front-end: executar `npm install` e `npm run build`; publicar `frontend/dist` em servidor web estático configurando `VITE_API_URL` para a API. Em produção, usar proxy HTTPS, CORS restrito, segredo forte, banco gerenciado e processo de migração de schema (Alembic recomendado).
### 5.4 Backup, restauração e rollback
Parar gravações ou usar backup consistente do SQLite. Copiar `backend/qualitytrack.db` para local protegido, datado e com acesso restrito. Restaurar substituindo o arquivo com a aplicação parada e validar `/health` e consultas. Manter cópias versionadas e testar restauração periodicamente. Rollback de aplicação: voltar à tag estável anterior; backup do banco antes de alterações de schema. Em implantação real, usar backup automatizado e política de retenção.

## Evidências que devem ser inseridas
1. Tela de login; 2. dashboard com dados de demonstração; 3. lista de NC; 4. formulário de cadastro; 5. edição de NC; 6. resposta de endpoint na documentação `/docs`; 7. execução dos testes; 8. quadro Scrum; 9. repositório Git com branches e commits. Use capturas feitas após executar o projeto. Não utilize imagens ilustrativas como se fossem prints reais do sistema.

## Identificação acadêmica
Aluno(a): [preencher] · Curso: [preencher] · Disciplina: [preencher] · Professor(a): [preencher] · Instituição: [preencher] · Data: [preencher]
