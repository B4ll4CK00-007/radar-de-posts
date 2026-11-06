@echo off
REM Publica o site do Radar de Posts no GitHub + ativa o GitHub Pages.
REM Rode:  publicar.cmd   (ou clique duas vezes no arquivo)
setlocal
cd /d "%~dp0"

echo [1/4] Publicando o repositorio...
gh repo create radar-de-posts --public --source=. --remote=origin --push
if errorlevel 1 (
  echo       Falhou. Se o repositorio ja existir, tentando de novo...
  gh repo create radar-de-posts --public --source=. --remote=origin --push --force
)
if errorlevel 1 (
  echo.
  echo NAO FOI POSSIVEL PUBLICAR. Verifique se voce esta logado: gh auth status
  pause
  exit /b 1
)

echo [2/4] Ativando o GitHub Pages...
echo {"build_type":"legacy","source":{"branch":"main","path":"/"}} | gh api -X POST repos/B4ll4CK00-007/radar-de-posts/pages --input -

echo [3/4] Consultando a URL publica...
set URL=
for /f "delims=" %%u in ('gh api repos/B4ll4CK00-007/radar-de-posts/pages --jq .html_url 2^>nul') do set URL=%%u

echo [4/4] Concluido.
echo.
echo  Site do app .............. https://b4ll4ck00-007.github.io/radar-de-posts/
echo  Politica de Privacidade .. https://b4ll4ck00-007.github.io/radar-de-posts/privacidade.html
echo  Termos de Servico ........ https://b4ll4ck00-007.github.io/radar-de-posts/termos.html
echo  Exclusao de dados ........ https://b4ll4ck00-007.github.io/radar-de-posts/exclusao.html
echo.
echo  A primeira compilacao do Pages leva cerca de 1 minuto.
echo  Copie e cole a mensagem acima aqui no chat para eu preencher o formulario da Meta.
pause
