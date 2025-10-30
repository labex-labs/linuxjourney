---
index: 11
lang: "pt"
title: "Navegação de Buffer Emacs"
meta_title: "Navegação de Buffer Emacs - Text-Fu Avançado"
meta_description: "Aprenda os comandos de navegação de buffer do Emacs. Alterne, feche e divida buffers eficientemente com este tutorial de Emacs para iniciantes. Melhore seu fluxo de trabalho!"
meta_keywords: "navegação de buffer Emacs, comandos Emacs, C-x b, C-x k, tutorial Linux, guia Emacs, Emacs para iniciantes"
---

## Lesson Content

Para se mover entre buffers (ou arquivos que você está visitando), use os seguintes comandos:

### Trocar buffers

```
C-x b - switch buffer
C-x right arrow - right-cycle through buffer
C-x left arrow - left-cycle through buffer
```

### Fechar o buffer

```
C-x k
```

### Dividir o buffer atual

```
C-x 2
```

Isso permite que você veja múltiplos buffers em uma única tela. Para se mover entre esses buffers, use: C-x o

### Definir um único buffer como a tela atual

```
C-x 1
```

Se você já usou um multiplexador de terminal como `screen` ou `tmux`, os comandos de buffer parecerão muito familiares.

## Exercise

A prática leva à perfeição! Aqui estão alguns laboratórios práticos para reforçar sua compreensão sobre como navegar e manipular arquivos de texto e buffers:

1. **[Editar Arquivos de Texto no Linux com Vim e Nano](https://labex.io/pt/labs/comptia-edit-text-files-in-linux-with-vim-and-nano-591076)** - Pratique a criação, edição, salvamento e navegação de texto dentro dos editores Vim e Nano, que são cruciais para trabalhar com buffers.
2. **[Comando cat do Linux: Concatenação de Arquivos](https://labex.io/pt/labs/linux-linux-cat-command-file-concatenating-210986)** - Aprenda a visualizar, concatenar e manipular arquivos de texto, aplicando diretamente como você pode interagir com o conteúdo do buffer.
3. **[Visualizando Arquivos de Log e Configuração no Linux](https://labex.io/pt/labs/linux-viewing-log-and-configuration-files-in-linux-387914)** - Pratique o uso de comandos como `cat`, `more` e `less` para visualizar e navegar eficientemente em arquivos de texto, simulando cenários do mundo real de exame de conteúdo semelhante a buffer.

Esses laboratórios o ajudarão a aplicar os conceitos em cenários reais e a construir confiança na manipulação de arquivos de texto e buffers no Linux.

## Quiz Question

Como você encerra um buffer?

## Quiz Answer

C-x k
