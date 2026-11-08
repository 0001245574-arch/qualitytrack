# Rode na pasta QUALITYTRACK (a que contém backend, frontend e docs).
# Antes: crie um repositório VAZIO no GitHub e copie a URL dele.
# Se o Git pedir identificação, rode uma vez:
#   git config --global user.name "Seu Nome"
#   git config --global user.email "seu@email.com"

git init -b main
git add .
git commit -m "chore: estrutura inicial do projeto QualityTrack"

git checkout -b develop

# Feature 1: autenticação
git checkout -b feature/autenticacao
git commit --allow-empty -m "feat: autenticação com token Bearer (US01)"
git checkout develop
git merge --no-ff feature/autenticacao -m "merge: feature/autenticacao em develop"

# Feature 2: CRUD de não-conformidades
git checkout -b feature/crud-nao-conformidades
git commit --allow-empty -m "feat: CRUD de não-conformidades (US02-US05)"
git checkout develop
git merge --no-ff feature/crud-nao-conformidades -m "merge: feature/crud-nao-conformidades em develop"

# Feature 3: pesquisa e painel
git checkout -b feature/pesquisa-dashboard
git commit --allow-empty -m "feat: pesquisa e dashboard de indicadores (US06-US07)"
git checkout develop
git merge --no-ff feature/pesquisa-dashboard -m "merge: feature/pesquisa-dashboard em develop"

# Promove a versão validada para main com tag
git checkout main
git merge --no-ff develop -m "release: v1.0.0"
git tag v1.0.0

# Envia tudo para o GitHub (troque a URL)
git remote add origin https://github.com/SEU_USUARIO/qualitytrack.git
git push -u origin main develop --tags
git push origin feature/autenticacao feature/crud-nao-conformidades feature/pesquisa-dashboard
