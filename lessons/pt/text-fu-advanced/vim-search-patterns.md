---
title: "Padrões de Busca do Vim"
description: "Aprenda os padrões de busca do Vim: busca para frente (/) e para trás (?). Navegue pelos resultados com 'n' e 'N'. Melhore suas habilidades no Vim hoje!"
keywords: "busca Vim, comandos Vim, editor de texto Linux, tutorial Vim, guia Vim, Vim para iniciantes"
---

## Lesson Content

Para procurar uma expressão, basta digitar a tecla `/` e depois o seu termo de busca enquanto estiver em uma sessão Vim. Depois de pressionar Enter, você pode pressionar `n` para avançar ou `N` para retroceder nos resultados da sua busca.

```plaintext
My pretty file is very pretty.

/pretty

will find the pretty words in the text file.
```

O comando de busca `?` irá procurar o arquivo de texto para trás. Assim, no exemplo anterior, o último "pretty" apareceria primeiro.

```plaintext
My pretty file is very pretty.

?pretty

will find the pretty words in the text file.
```

## Exercise

Brinque com a tecla de busca. Abra um arquivo de texto no Vim com: `vim [textfile]` e comece a procurar!

## Quiz Question

Qual tecla é usada para pesquisar no Vim?

## Quiz Answer

/
