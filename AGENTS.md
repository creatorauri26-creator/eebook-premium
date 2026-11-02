# Instruções permanentes para o Codex

## Continuidade e preservação
1. Nunca depender exclusivamente do histórico da conversa. Antes de trabalhar, ler este arquivo, README.md, INDICE.md e PROGRESSO.md e consultar os arquivos existentes e o Git.
2. Salvar cada capítulo em um arquivo Markdown separado em capitulos/, com nome numerado (01-titulo.md). Só escrever o ebook quando o usuário mandar explicitamente; não iniciar redação por conta própria. A autorização para preparar a estrutura não autoriza escrever conteúdo editorial.
3. Atualizar PROGRESSO.md após cada etapa: trabalho realizado, validação, pendências e próximos passos. Não registrar aprovação sem evidência explícita do usuário.
4. Não substituir nem alterar capítulos aprovados sem autorização explícita. Registrar aprovação, data e commit de referência no progresso; propor revisões em arquivo separado quando necessário.
5. Não excluir imagens utilizadas no projeto. Preservar originais finais em imagens/ e registrar origem, licença e uso em imagens/README.md.
6. Manter versionados scripts, configurações e dependências para reconstruir o PDF. Não guardar segredos no Git.
7. Fazer commits Git após cada etapa aprovada; a criação inicial da estrutura foi solicitada pelo usuário. Não confundir entrega técnica com aprovação editorial.
8. Disponibilizar alterações em branch e pull request no GitHub para revisão e integração. Não integrar PR sem autorização.
9. Só declarar backup concluído após push bem-sucedido, comparação do SHA local/remoto e conferência dos arquivos no commit remoto. Commit local não é backup remoto.

## Fluxo editorial
Tema, público, título e índice editorial ainda dependem de definição. Manter INDICE.md e scripts/capitulos.json na mesma ordem; o manifesto determina a montagem do PDF. Apenas capítulos explicitamente aprovados entram na edição final. Antes de liberar um PDF, revisar visualmente tipografia, margens, imagens, sumário, links e quebras de página. Registrar limitações e validações reais, sem inventar resultados.
