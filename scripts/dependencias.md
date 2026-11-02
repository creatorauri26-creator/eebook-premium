# Dependências de reconstrução

- Python 3.10 ou superior; gerador usa apenas biblioteca padrão.
- Pandoc 3.1.11.1 (versão disponível nesta preparação).
- XeLaTeX/TeX Live e fontes Latin Modern.

Em Debian/Ubuntu, com permissões administrativas:

```sh
sudo apt-get update
sudo apt-get install python3 pandoc texlive-xetex texlive-lang-portuguese texlive-fonts-recommended fonts-texgyre fonts-lmodern
```

O pacote Pandoc da distribuição pode ter outra versão. Para reproduzir a ferramenta de referência, instale a versão 3.1.11.1 pela distribuição oficial do Pandoc. Não há dependências pip ou npm. Para uma edição final, registrar em PROGRESSO.md as versões exatas de Python, Pandoc, XeLaTeX e sistema operacional; a distribuição TeX e as fontes também afetam paginação. Esta estrutura não promete PDF idêntico byte a byte em sistemas diferentes.

Verificação: python3 --version, pandoc --version e xelatex --version.
