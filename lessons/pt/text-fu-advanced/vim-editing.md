---
title: "Edição no Vim"
description: "Aprenda os conceitos básicos de edição no Vim: deletar, alterar, copiar e colar texto de forma eficiente. Domine os comandos essenciais do Vim para iniciantes e melhore suas habilidades de edição de texto no Linux."
keywords: "edição Vim, comandos Vim, editor de texto Linux, tutorial Vim, guia Vim, Vim para iniciantes, comando dd, deletar Vim"
---

## Lesson Content

Editar no Vim é feito a partir do modo Normal usando operadores e movimentos. Você pode deletar, alterar, copiar (yank), colar (put) e substituir texto de forma eficiente.

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

Abra um arquivo com `vim [file]` e tente: `dw`, `cw`, `yy` então `p`, `dd`, `J`, e `.` para repetir uma alteração.

## Quiz Question

Qual comando deleta a linha atual no Vim?

## Quiz Answer

dd
