---
index: 8
lang: "pt"
title: "less"
meta_title: "less - Linha de Comando"
meta_description: "Aprenda a usar o comando 'less' do Linux para visualização e navegação eficientes de arquivos de texto. Domine a paginação, pesquisa e saída com este guia amigável para iniciantes."
meta_keywords: "comando less, Linux less, visualizar arquivos de texto, navegar arquivos, tutorial Linux, Linux para iniciantes, guia Linux"
---

## Lesson Content

Se você está visualizando arquivos de texto maiores que uma saída simples, `less` é mais. (Na verdade, existe um comando chamado `more` que faz algo semelhante, então isso é irônico.) O texto é exibido de forma paginada, para que você possa navegar por um arquivo de texto página por página.

Continue e veja o conteúdo de um arquivo com `less`. Uma vez que você esteja no comando `less`, você pode realmente usar outros comandos de teclado para navegar no arquivo.

```bash
less /home/pete/Documents/text1
```

Use os seguintes comandos para navegar através de `less`:

- `q` - Usado para sair de `less` e voltar para o seu shell.
- `Page up`, `Page down`, `Up` e `Down` - Navegue usando as teclas de seta e as teclas de página.
- `g` - Move para o início do arquivo de texto.
- `G` - Move para o final do arquivo de texto.
- `/search` - Você pode pesquisar por texto específico dentro do documento de texto. Preceda as palavras que você deseja pesquisar com `/`.
- `h` - Se você precisar de uma pequena ajuda sobre como usar `less` enquanto estiver em `less`, use a ajuda.

## Exercise

A prática leva à perfeição! Aqui estão alguns laboratórios práticos para reforçar sua compreensão sobre a visualização e navegação de arquivos de texto no Linux:

1. **[Comando Linux less: Paginação de Arquivos](https://labex.io/pt/labs/linux-linux-less-command-file-paging-214301)** - Aprenda o comando 'less' do Linux para visualização e navegação eficientes de arquivos de texto, incluindo pesquisa, números de linha e correspondência de padrões.
2. **[Comando Linux more: Rolagem de Arquivos](https://labex.io/pt/labs/linux-linux-more-command-file-scrolling-214299)** - Aprenda o comando 'more' do Linux para visualização eficiente de arquivos de texto, cobrindo o uso básico, iniciando de linhas específicas e personalizando a exibição.
3. **[Visualizando Arquivos de Log e Configuração no Linux](https://labex.io/pt/labs/linux-viewing-log-and-configuration-files-in-linux-387914)** - Aprenda habilidades essenciais da linha de comando Linux para visualizar e navegar eficientemente em arquivos de texto, incluindo logs do sistema e arquivos de configuração, usando comandos como `cat`, `more` e `less`.

Esses laboratórios o ajudarão a aplicar os conceitos em cenários reais e a construir confiança na manipulação e navegação de arquivos de texto.

## Quiz Question

Como você sai de um comando `less`?

## Quiz Answer

q