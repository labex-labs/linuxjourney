---
index: 6
lang: "pt"
title: "Inserindo e Anexando Texto no Vim"
meta_title: "Inserir e Anexar Texto no Vim - Técnicas Avançadas"
meta_description: "Aprenda a diferença entre os modos de inserção e anexação do Vim. Domine comandos como 'i', 'a' e 'o' para editar texto eficientemente, anexar conteúdo no vim e adicionar linha no vim."
meta_keywords: "vim anexar, anexar vs inserir vim, vim inserir vs anexar, vim adicionar linha, edição de texto vim, comandos vim, tutorial vim, modo de inserção, modo de anexação"
---

## Lesson Content

No Vim, você trabalhará principalmente em dois modos: o modo Normal para executar comandos e o modo de Inserção (Insert mode) para digitar texto. Para alternar do modo de Inserção de volta para o modo Normal, basta pressionar a tecla `Esc`.

Existem vários comandos para entrar no modo de Inserção, cada um posicionando o cursor em um ponto de partida diferente para a entrada de texto.

### Comandos Básicos de Inserção

A maneira mais fundamental de começar a digitar é com o comando `i`.

- `i` – **i**nsere texto antes da posição atual do cursor.

Este comando alterna para o modo de Inserção, permitindo que você digite diretamente no arquivo.

### Vim Append vs Insert

Um ponto comum de comparação é **vim append vs insert** (vim anexar vs inserir). Embora ambos entrem no modo de Inserção, seus pontos de partida diferem em relação ao cursor. Entender a distinção **vim insert vs append** é fundamental para o movimento e edição eficientes.

- `a` – **a**nexa texto após a posição atual do cursor.
- `I` – **I**nsere texto no início da linha atual.
- `A` – **A**nexa texto no final da linha atual.

Usar `a` em vez de `i` economiza uma tecla (movendo o cursor um espaço para a direita antes de inserir). Da mesma forma, `A` é um atalho poderoso para começar a digitar imediatamente no final de uma linha. Dominar os comandos **vim append** é um passo significativo para melhorar sua velocidade de edição.

### Como Fazer Vim Adicionar Linha

Quando você precisar adicionar novas linhas de texto, não precisa pressionar Enter manualmente no final de uma linha. O Vim fornece comandos dedicados para abrir linhas e entrar imediatamente no modo de Inserção.

- `o` – **o**bre uma nova linha abaixo da linha atual e entra no modo de Inserção.
- `O` – **O**bre uma nova linha acima da linha atual e entra no modo de Inserção.

Esses comandos são extremamente úteis quando você precisa rapidamente **vim add line** (vim adicionar linha) ao codificar ou escrever.

**Dica:** Você pode prefixar esses comandos com um número para repeti-los. Por exemplo, digitar `3o` no modo Normal abrirá três novas linhas em branco abaixo da linha atual e o posicionará no modo de Inserção na primeira dessas novas linhas.

## Exercise

A prática é essencial para dominar o Vim. O laboratório a seguir fornece um ambiente prático para reforçar sua compreensão das capacidades de edição de texto do Vim.

1. **[Editar Arquivos de Texto no Linux com Vim e Nano](https://labex.io/pt/labs/comptia-edit-text-files-in-linux-with-vim-and-nano-591076)** - Pratique criar arquivos, editar texto, salvar arquivos e navegar com vi/vim e nano. Este laboratório o ajudará a dominar as habilidades fundamentais de uso dos modos Normal e de Inserção do Vim.

Aplicar esses conceitos em cenários reais ajudará você a construir confiança na edição de texto no Linux usando o Vim.

## Quiz Question

Qual tecla entra no modo de Inserção antes do cursor? Por favor, responda com uma única letra minúscula em inglês.

## Quiz Answer

i
