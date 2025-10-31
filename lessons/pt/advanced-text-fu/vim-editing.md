---
index: 7
lang: "pt"
title: "Edição no Vim"
meta_title: "Edição no Vim - Text-Fu Avançado"
meta_description: "Um tutorial Vim para iniciantes sobre comandos essenciais de edição. Aprenda a deletar, alterar, copiar (yank) e colar texto no editor de texto Vim para melhorar seu fluxo de trabalho no Linux."
meta_keywords: "Edição Vim, comandos Vim, editor de texto Linux, tutorial Vim, guia Vim, Vim para iniciantes, comando dd, deletar Vim"
---

## Lesson Content

Editar texto no Vim é um recurso poderoso que se baseia na combinação de operadores e movimentos do modo Normal. Essa abordagem permite que você exclua, altere, copie (yank) e cole (put) texto de forma eficiente. Antes de executar qualquer comando, pressione `Esc` para garantir que você esteja no modo Normal.

### Entendendo Operadores e Movimentos do Vim

A essência da edição no Vim é a fórmula: `operador + movimento`. Um operador é uma ação (como `d` para deletar), e um movimento é um deslocamento (como `w` para palavra). Por exemplo, `dw` combina o operador de deletar com o movimento de palavra para deletar uma palavra. Você também pode usar contadores para repetir uma ação, como `2dw` para deletar duas palavras.

### Deletando Texto no Vim

O operador de deletar é `d`. É um dos comandos Vim mais comuns para manipulação de texto.

- `x` – Deleta o caractere diretamente sob o cursor.
- `dw` – Deleta do cursor até o início da próxima palavra.
- `d$` – Deleta do cursor até o final da linha atual.
- `dd` – O comando `dd` deleta a linha inteira atual.
- `3dd` – Deleta três linhas, começando pela linha atual.

### Alterando Texto

O operador de alterar, `c`, funciona de forma semelhante ao deletar, mas coloca você no modo de Inserção após executar a ação. Isso é útil para substituir texto.

- `cw` – Altera o texto do cursor até o final da palavra.
- `c$` – Altera o texto do cursor até o final da linha.
- `cc` – Altera a linha inteira atual.

### Copiando e Colando no Vim

No Vim, copiar é chamado de "yanking" (operador `y`), e colar é chamado de "putting".

- `yw` – Yanks (copia) uma palavra.
- `yy` – Yanks (copia) a linha inteira atual.
- `p` – Puts (cola) o texto copiado após o cursor ou na linha de baixo.
- `P` – Puts (cola) o texto antes do cursor ou na linha de cima.

### Outros Comandos de Edição Úteis

Este guia Vim não estaria completo sem alguns outros comandos úteis.

- `r{char}` – Substitui o caractere único sob o cursor pelo caractere especificado.
- `R` – Entra no modo de Substituição, permitindo sobrescrever texto continuamente até pressionar `Esc`.
- `J` – Junta a linha atual com a próxima.
- `.` – Repete a última alteração que você fez, um comando muito poderoso e eficiente.

Combinar operadores com diferentes movimentos desbloqueia todo o potencial deste editor de texto Linux. Por exemplo, `d}` deleta até o próximo parágrafo, e `caw` altera "uma palavra" (a palavra sob o cursor, incluindo qualquer espaço circundante).

## Exercise

Para colocar seu conhecimento em prática, recomendamos o seguinte laboratório prático. Ele o ajudará a dominar os comandos de edição fundamentais discutidos neste tutorial Vim.

1. **[Editar Arquivos de Texto no Linux com Vim e Nano](https://labex.io/pt/labs/comptia-edit-text-files-in-linux-with-vim-and-nano-591076)** - Pratique a criação de arquivos, edição de texto, salvamento de arquivos e navegação com vi/vim e nano. Este laboratório o ajudará a aplicar conceitos como deletar, alterar, yanking e putting texto em cenários reais.

## Quiz Question

Qual comando deleta a linha atual no Vim? (Por favor, responda em inglês, prestando atenção à sensibilidade a maiúsculas e minúsculas).

## Quiz Answer

dd
