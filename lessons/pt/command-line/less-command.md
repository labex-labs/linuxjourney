---
index: 8
lang: "pt"
title: "less"
meta_title: "less - Linha de Comando"
meta_description: "Aprenda a usar o comando 'less' do Linux para visualização e navegação eficientes de arquivos de texto. Domine a paginação, pesquisa e saída com este guia amigável para iniciantes."
meta_keywords: "comando less, Linux less, visualizar arquivos de texto, navegar arquivos, tutorial Linux, Linux para iniciantes, guia Linux"
---

## Lesson Content

Se você está visualizando arquivos de texto maiores do que uma saída simples, `less` é mais. (Existe na verdade um comando chamado `more` que faz algo semelhante, o que é irônico.) O texto é exibido de forma paginada, para que você possa navegar por um arquivo de texto página por página.

Vá em frente e veja o conteúdo de um arquivo com `less`. Uma vez que você esteja no comando `less`, você pode realmente usar outros comandos de teclado para navegar no arquivo.

```bash
less /home/pete/Documents/text1
```

Use os seguintes comandos para navegar através de `less`:

- `q` - Usado para sair de `less` e voltar para o seu shell.
- `Page up`, `Page down`, `Up` e `Down` - Navegue usando as teclas de seta e as teclas de página.
- `g` - Move para o início do arquivo de texto.
- `G` - Move para o final do arquivo de texto.
- `/search` - Você pode procurar por texto específico dentro do documento de texto. Prefacie as palavras que você deseja pesquisar com `/`.
- `h` - Se você precisar de uma pequena ajuda sobre como usar `less` enquanto estiver em `less`, use a ajuda.

## Exercise

Execute `less` em um arquivo, depois suba e desça as páginas do arquivo. Tente procurar por uma palavra específica. Navegue rapidamente para o início ou o fim do arquivo.

Para prática interativa com o comando `less`, experimente este laboratório interativo:

- [Linux less Command: File Paging](https://labex.io/pt/labs/linux-linux-less-command-file-paging-214301)

## Quiz Question

Como você sai de um comando `less`?

## Quiz Answer

q
