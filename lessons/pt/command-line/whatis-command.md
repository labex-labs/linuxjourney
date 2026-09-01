---
lesson_id: "whatis-command"
course_id: "command-line"
lang: "pt"
order_index: 17
title: "whatis"
description: "Aprenda a obter descrições concisas das páginas de manual e interpretar seus números de seção."
meta_title: "whatis - Linha de Comando"
meta_description: "Aprenda o comando whatis do Linux com exemplos para obter descrições de uma linha das páginas man e entender várias seções do manual."
meta_keywords: "comando whatis, whatis Linux, descrição de comando Linux, resumo página man, ajuda linha de comando, apropos"
---

Quando você reconhece o nome de um comando, mas esquece sua finalidade, `whatis` pode fornecer um breve lembrete com base no banco de dados das páginas de manual.

## Consulta de um Nome Exato

Forneça um ou mais nomes exatos de tópicos a `whatis`. Cada resultado deriva da seção `NAME` registrada em uma página de manual instalada:

```bash
$ whatis cat
cat (1)              - concatenate files and print on the standard output
```

A saída é uma descrição, não uma lista de opções ou exemplos do comando. Use `man cat` ou `cat --help` quando precisar de mais detalhes.

:::single-choice{#describe-known-command} Você conhece o nome `cat` e quer sua descrição de uma linha na página de manual. Qual comando deve executar?

::option[`man cat`]{#manual-cat explanation="`man cat` abre a página de manual completa. Ele fornece mais do que o lembrete de uma linha solicitado."}
::option[`apropos cat`]{#apropos-cat explanation="`apropos` pesquisa descrições por uma palavra-chave e pode retornar muitos tópicos relacionados. Ele é mais abrangente que uma consulta por nome exato."}
::option[`whatis cat`]{#whatis-cat .correct explanation="`whatis` consulta o nome exato do tópico e mostra sua descrição concisa no banco de dados do manual."}
:::

## Leitura dos Números de Seção

Se o mesmo tópico tiver páginas de manual em várias seções, `whatis` poderá mostrar mais de um resultado:

```bash
$ whatis passwd
passwd (1)           - change user password
passwd (5)           - the password file
```

O número entre parênteses é a seção do manual. Aqui, `passwd(1)` descreve o comando de usuário, e `passwd(5)` descreve um formato de arquivo. Você pode abrir uma delas explicitamente com `man 1 passwd` ou `man 5 passwd`.

:::single-choice{#interpret-whatis-section} Na saída `passwd (5) - the password file`, o que `(5)` identifica?

::option[A quinta opção aceita pelo comando `passwd`.]{#fifth-option explanation="O número não é a posição de uma opção. As opções são documentadas dentro da página de manual selecionada."}
::option[A seção do manual que contém a página do formato de arquivo.]{#section-five .correct explanation="A seção 5 é usada para formatos e convenções de arquivos; portanto, `passwd(5)` se refere a essa seção."}
::option[Cinco páginas de manual que compartilham o nome `passwd`.]{#five-pages explanation="Podem existir vários resultados, mas o valor entre parênteses identifica uma seção, não a quantidade de páginas."}
:::

## Escolha entre whatis, man e apropos

- `whatis NAME`: mostra descrições concisas de um nome exato de tópico do manual.
- `man NAME`: abre uma página de manual completa.
- `apropos KEYWORD`: pesquisa uma palavra-chave nos nomes e nas descrições das páginas.

Por exemplo:

```bash
$ apropos password
```

Use `apropos` quando conhecer a tarefa, mas não o nome do comando. Use `whatis` quando já souber o nome.

:::single-choice{#search-by-purpose} Você não conhece o nome de um comando, mas quer pesquisar a palavra-chave `password` nas descrições dos manuais. Qual comando é adequado?

::option[`apropos password`]{#apropos-password .correct explanation="`apropos` pesquisa a palavra-chave nos nomes e nas descrições das páginas de manual, ajudando a descobrir tópicos relevantes."}
::option[`whatis password`]{#exact-password explanation="`whatis` procura um tópico exato chamado `password`. Ele não é a interface geral de pesquisa por palavra-chave."}
::option[`man password`]{#manual-password explanation="`man` tenta abrir uma página com esse nome de tópico. Ele não realiza a pesquisa solicitada nas descrições."}
:::

## Quando Nenhuma Descrição Aparece

Se `whatis` informar que nada é apropriado, talvez o tópico não possua uma página de manual instalada ou o banco de dados esteja desatualizado. Esse resultado não comprova a inexistência de um executável, alias, função ou comando interno com esse nome. Use `type NAME` para descobrir como o Bash resolve o nome e então escolha a fonte de ajuda apropriada.

:::single-choice{#whatis-versus-type} `whatis deploy` não encontra uma descrição de manual. Qual comando verifica se o Bash resolve `deploy` como alias, função, comando interno ou executável?

::option[`whatis -r deploy`]{#whatis-regex-deploy explanation="Alterar a consulta ao banco de manuais não mostra todos os aliases, funções, comandos internos e resoluções de caminho do Bash."}
::option[`man 5 deploy`]{#manual-five-deploy explanation="Esse comando tenta abrir uma página da seção 5. Ele não determina como o Bash resolve o nome."}
::option[`type deploy`]{#resolve-deploy .correct explanation="O `type` do Bash informa como o shell atual resolve um nome de comando, independentemente de existir uma descrição de manual instalada."}
:::

## Resumo

Agora você sabe obter e interpretar descrições concisas no banco de dados dos manuais.

1. Consulte um tópico exato com `whatis`.
2. Leia a seção do manual mostrada entre parênteses.
3. Use `man` quando precisar da página completa.
4. Use `apropos` quando conhecer uma palavra-chave, mas não o nome.
