---
index: 7
lang: "pt"
title: "Edição Vim"
meta_title: "Edição Vim - Text-Fu Avançado"
meta_description: "Aprenda os conceitos básicos de edição do Vim: deletar, alterar, copiar e colar texto de forma eficiente. Domine os comandos essenciais do Vim para iniciantes e melhore suas habilidades de edição de texto no Linux."
meta_keywords: "edição Vim, comandos Vim, editor de texto Linux, tutorial Vim, guia Vim, Vim para iniciantes, comando dd, deletar Vim"
---

## Lesson Content

A edição no Vim é feita a partir do modo Normal usando operadores e movimentos. Você pode deletar, alterar, copiar (yank), colar (put) e substituir texto de forma eficiente.

- Pressione `Esc` para garantir que você esteja no modo Normal antes de usar esses comandos.

Exclusões (operador `d`):

- `x` – deleta o caractere sob o cursor
- `dw` – deleta do cursor até o início da próxima palavra
- `d$` – deleta do cursor até o final da linha
- `dd` – deleta a linha atual
- Contagens se aplicam: `3dd` deleta três linhas; `2dw` deleta duas palavras

Alterações (operador `c`, deleta e então entra no modo Insert):

- `cw` – altera a palavra a partir do cursor
- `c$` – altera até o final da linha
- `cc` – altera a linha inteira

Yank e Put (copiar/colar):

- `yw` – copia a palavra
- `yy` – copia a linha atual
- `p` – cola (put) após o cursor ou abaixo da linha
- `P` – cola (put) antes do cursor ou acima da linha

Substituir e outras edições úteis:

- `r{char}` – substitui o caractere sob o cursor por `{char}`
- `R` – entra no modo Replace para sobrescrever texto
- `J` – une a linha atual com a próxima linha
- `.` – repete a última alteração

Combine operadores com movimentos para ter poder: `d}` deleta até o próximo parágrafo; `caw` altera “uma palavra” (palavra sob o cursor incluindo o espaço circundante).

## Exercise

A prática leva à perfeição! Aqui está um laboratório prático para reforçar sua compreensão da edição de texto no Vim:

1. **[Editar Arquivos de Texto no Linux com Vim e Nano](https://labex.io/pt/labs/comptia-edit-text-files-in-linux-with-vim-and-nano-591076)** - Pratique a criação de arquivos, edição de texto, salvamento de arquivos e navegação com vi/vim e nano. Este laboratório o ajudará a dominar os comandos de edição fundamentais discutidos, como deletar, alterar, copiar e colar texto.

Este laboratório o ajudará a aplicar os conceitos em cenários reais e a construir confiança na edição de texto no Linux.

## Quiz Question

Qual comando deleta a linha atual no Vim?

## Quiz Answer

dd
