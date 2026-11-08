# QualityTrack

Sistema web acadêmico para inspeção de qualidade e gestão de não-conformidades industriais. Aplicação SPA React + API REST FastAPI + SQLite.

## Funcionalidades
- Autenticação demonstrativa com token Bearer.
- CRUD de não-conformidades com código único, produto, linha, defeito, severidade, status, quantidade, responsável, ações e link de evidência.
- Pesquisa por código, título, produto e tipo de defeito.
- Painel com indicadores por status, ocorrências críticas e taxa de encerramento.
- Validação de entrada e regra que impede reabrir NC encerrada pela edição comum.

## Execução local — Windows PowerShell
**API**
```powershell
cd backend
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
Copy-Item .env.example .env
uvicorn app.main:app --reload
```
Documentação: http://127.0.0.1:8000/docs

**Frontend** (novo terminal)
```powershell
cd frontend
npm install
npm run dev
```
Acesse http://localhost:5173. Login demonstrativo: `admin` / `Quality@123`.

## Testes
```powershell
cd backend
pytest -v
```
Em outro terminal:
```powershell
cd frontend
npm install
npm test
npm run build
```

## Segurança e limites
Credenciais são exclusivamente demonstrativas. O usuário `admin` está codificado para facilitar avaliação acadêmica; substitua por persistência de usuários, controle de papéis, segredo forte, HTTPS, logs e política de sessão antes de qualquer uso real. Evidências acadêmicas devem ser capturadas após executar o sistema; não declare testes ou cobertura sem executá-los.

## Documentação
Manual em `docs/manual-tecnico/CONTEUDO_MANUAL.md`; diagramas Mermaid em `docs/diagramas/`. Preencha identificação acadêmica e insira capturas reais antes da entrega.
