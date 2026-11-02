# Projeto de ebook profissional em PDF

Estrutura inicial, sem conteúdo editorial. Leia AGENTS.md, INDICE.md e PROGRESSO.md ao retomar o trabalho.

## Arquivos
- capitulos/: um Markdown por capítulo; .gitkeep preserva a pasta vazia.
- imagens/: imagens finais e registro de origem/licença.
- scripts/gerar_pdf.py: validação e montagem em ordem explícita.
- scripts/capitulos.json: lista ordenada dos caminhos dos capítulos, inicialmente vazia.
- scripts/pdf.yaml: opções tipográficas, metadados e sumário.
- scripts/dependencias.md: ferramentas necessárias.
- INDICE.md: planejamento do índice; PROGRESSO.md: decisões e continuidade.

## Reconstruir
Instale Python 3.10+, Pandoc e XeLaTeX conforme scripts/dependencias.md. Na raiz:

```sh
python3 scripts/gerar_pdf.py --verificar
python3 scripts/gerar_pdf.py
```

O segundo comando só gera o PDF quando houver capítulos no manifesto; sem capítulos, termina com mensagem explicativa. O PDF será salvo em build/ebook.pdf, pasta gerada e ignorada pelo Git. Não há PDF editorial nesta etapa.

Após autorizar a escrita, adicione arquivos como capitulos/01-titulo.md à lista JSON de scripts/capitulos.json na ordem de leitura. Cada arquivo deve ter um título de nível 1. Use caminhos de imagens relativos à raiz, por exemplo imagens/nome.png. Atualize INDICE.md, metadados de scripts/pdf.yaml e PROGRESSO.md. Antes da edição final, confira a aprovação de todos os capítulos.

## Git e GitHub
A estrutura será entregue na branch estrutura-ebook para revisão por pull request. A branch main contém apenas o commit inicial de base, pois o repositório estava vazio. Integre o PR depois de revisar os arquivos.

Após cada etapa aprovada, atualize PROGRESSO.md, revise git diff, adicione os arquivos da etapa, faça commit e envie a branch. Não alterar capítulos aprovados sem autorização nem excluir imagens utilizadas.

Para conferir a publicação desta estrutura:

```sh
git fetch origin
git rev-parse HEAD
git rev-parse origin/estrutura-ebook
git ls-tree -r --name-only origin/estrutura-ebook
git status --short
```

Os dois SHAs devem ser iguais quando estiver na branch estrutura-ebook sem commits locais adicionais. No GitHub, selecione essa branch, confira os arquivos e abra o commit correspondente; confira também a aba Files changed do PR. Após integrar, confira os arquivos em main. Push e presença na branch remota confirmam o backup do código-fonte; integração é uma etapa separada. PDFs finais aprovados devem ser anexados a uma Release, com o commit de origem registrado.
