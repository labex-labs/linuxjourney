---
lesson_id: "help-command"
course_id: "command-line"
lang: "pt"
order_index: 15
title: "help"
description: "Aprenda a escolher entre a ajuda integrada, a saída de uso do programa e as páginas de manual de um comando."
meta_title: "help - Linha de Comando"
meta_description: "Aprenda a obter ajuda na linha de comando do Linux com help do Bash, saída --help, páginas man e type para comandos internos e externos."
meta_keywords: "comando help Linux, help Bash, ajuda linha de comando, --help, comando interno shell, comando man, comando type"
---

Você não precisa memorizar todas as opções dos comandos. O Bash e muitos programas instalados podem explicar sua sintaxe diretamente no terminal, mas a fonte de ajuda adequada depende do tipo de comando usado.

## Obtenção de Ajuda para Comandos Internos do Bash

O Bash fornece o comando interno `help` para comandos implementados pelo próprio shell. Alguns exemplos são `cd`, `history` e `type`.

Forneça o nome do comando interno como argumento:

```bash
$ help echo
```

A saída descreve a sintaxe e o comportamento do comando interno. Executar `help` sem um argumento lista os comandos internos para os quais o Bash possui ajuda.

:::single-choice{#help-for-bash-cd}
Qual comando exibe a entrada de ajuda do Bash para seu comando interno `cd`?

::option[`cd --help`]{#cd-help-option explanation="Alguns comandos internos podem reconhecer opções, mas a interface de documentação dedicada do Bash é `help` seguido do nome do comando."}
::option[`help cd`]{#help-cd .correct explanation="O comando interno `help` do Bash consulta a documentação do comando interno indicado, neste caso `cd`."}
::option[`type cd`]{#type-cd explanation="`type` explica como o Bash resolve o nome `cd`. Ele identifica o comando, mas não mostra sua entrada de ajuda completa."}
:::

## Solicitação do Resumo de Uso de um Programa

Muitos programas externos seguem a convenção de aceitar `--help` e mostrar um resumo de uso:

```bash
$ ls --help
```

Essa convenção é comum, mas não universal. Leia a saída e o status de encerramento, em vez de presumir que todos os programas aceitam a mesma opção.

:::single-choice{#quick-ls-usage}
Qual comando normalmente mostra um resumo rápido de uso fornecido pelo programa externo `ls`?

::option[`help ls`]{#bash-help-ls explanation="O `help` do Bash documenta comandos internos do shell. Em um sistema comum, ele não fornece a página de uso do programa externo `ls`."}
::option[`ls --help`]{#ls-help .correct explanation="O GNU `ls` segue a convenção comum de `--help` e mostra seu uso e suas opções."}
::option[`type --help ls`]{#type-help-ls explanation="Esse comando pergunta ao comando interno `type` sobre suas próprias opções, em vez de pedir que `ls` explique seu uso."}
:::

## Descoberta de Como o Bash Resolve um Nome

Use `type` para descobrir se o Bash resolve um nome como comando interno, alias, função, palavra-chave ou arquivo executável:

```bash
$ type cd
cd is a shell builtin
$ type ls
ls is /usr/bin/ls
```

O resultado exato pode variar conforme os aliases, as funções, os programas instalados e o `PATH`. Use `type -a NAME` quando quiser que o Bash mostre todas as resoluções conhecidas, não apenas a primeira que usaria.

:::single-choice{#identify-command-resolution}
Você não sabe se `deploy` é um alias, uma função, um comando interno ou um executável. Qual comando do Bash verifica como esse nome é resolvido?

::option[`type deploy`]{#type-deploy .correct explanation="O comando interno `type` informa como o Bash interpreta o nome no ambiente atual do shell."}
::option[`help deploy`]{#help-deploy explanation="`help` procura documentação de comandos internos do Bash. Em geral, ele não identifica aliases, funções e arquivos externos."}
::option[`deploy --help`]{#deploy-help explanation="Esse comando tenta executar o programa e depende de seu próprio suporte à opção. Ele não explica primeiro como o Bash resolveu o nome."}
:::

## Escolha do Nível de Detalhe

- Use `help COMMAND` para um comando interno do Bash.
- Use `COMMAND --help` para obter um resumo rápido de muitos comandos externos.
- Use `man COMMAND` para uma página de manual instalada com documentação mais detalhada.
- Use `whatis COMMAND` para uma descrição de uma linha.

As próximas lições examinam com mais detalhes as páginas de manual e as descrições de uma linha.

:::single-choice{#choose-detailed-manual}
Você precisa de documentação detalhada para o comando externo `ls`, não apenas de um resumo de uso. Qual comando deve tentar?

::option[`man ls`]{#man-ls .correct explanation="`man ls` abre a página de manual instalada, que normalmente oferece uma descrição mais completa da sintaxe, das opções e do comportamento."}
::option[`whatis ls`]{#whatis-ls explanation="`whatis` foi projetado para mostrar descrições concisas das páginas de manual. Ele não fornece a documentação detalhada solicitada."}
::option[`type ls`]{#type-ls explanation="`type` informa como o Bash resolve `ls`. Ele não exibe o manual detalhado do programa."}
:::

## Resumo

Agora você sabe escolher uma fonte de ajuda conforme a maneira como o Bash resolve um comando.

1. Use `help` para comandos internos do Bash.
2. Experimente `--help` para obter o resumo de uso de um programa.
3. Inspecione a resolução de nomes com `type`.
4. Abra a documentação detalhada com `man`.
