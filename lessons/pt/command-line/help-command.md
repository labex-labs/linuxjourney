---
index: 15
lang: "pt"
title: "help"
meta_title: "help - Linha de Comando"
meta_description: "Aprenda como obter ajuda na linha de comando do Linux com o Bash help, saída --help, páginas man e type para comandos internos do shell e comandos externos."
meta_keywords: "comando help linux, ajuda bash, ajuda linha de comando, --help, comando interno shell, comando man, comando type"
---

## Lesson Content

Ao trabalhar na linha de comando do Linux, você frequentemente precisará de um lembrete rápido de como um comando funciona ou quais opções ele aceita. O Linux oferece várias ferramentas de ajuda diretamente no terminal.

### O Comando 'help' para Comandos Internos do Bash

Uma das ferramentas mais diretas é o `help`, um comando incorporado diretamente no shell Bash. Ele é especificamente projetado para fornecer informações sobre outros comandos internos do Bash. Um comando interno faz parte do próprio shell, não é um programa separado. Exemplos incluem `echo`, `cd` e `pwd`.

Para usar o `help`, digite-o seguido do nome do comando interno.

```bash
$ help echo
```

Isso exibirá um resumo do comando `echo`, sua sintaxe e uma lista de opções disponíveis. Esta é a maneira mais rápida de obter assistência para funções específicas do shell.

### A Flag --help para Programas Executáveis

Para a maioria dos outros programas executáveis que não são internos do shell, o comando `help` não funcionará. Em vez disso, uma convenção comum é fornecer a flag `--help`. Esta opção indica ao programa para imprimir um resumo de uso e então sair.

```bash
$ ls --help
```

Embora a maioria dos desenvolvedores siga esse padrão, ele não é universal. Tentar `--help` geralmente é um bom primeiro passo para um programa desconhecido.

### Encontrando o Tipo do Comando

Se você não tem certeza se um comando é um interno do Bash ou um programa externo, use `type`.

```bash
$ type cd
cd is a shell builtin
$ type ls
ls is /usr/bin/ls
```

Isso ajuda você a escolher entre `help cd`, `ls --help` ou `man ls`.

### Escolhendo a Ferramenta de Ajuda Certa

- Use `help COMMAND` para comandos internos do Bash como `cd`, `echo` e `history`.
- Use `COMMAND --help` para um resumo rápido de muitos comandos externos.
- Use `man COMMAND` para páginas de manual detalhadas.
- Use `whatis COMMAND` para uma descrição em uma linha.

### Perguntas Comuns

**Por que `help ls` não funciona?** `ls` geralmente é um programa externo, não um comando interno do Bash. Tente `ls --help` ou `man ls`.

**Por que `--help` não funciona para todos os comandos?** É uma convenção, não uma regra rígida.

**Qual é a maneira mais rápida de verificar um comando?** Tente `COMMAND --help` para comandos externos e `help COMMAND` para comandos internos do Bash.

## Exercise

Embora não existam laboratórios específicos para este tópico, recomendamos explorar o abrangente [Linux Learning Path](https://labex.io/pt/learn/linux) para praticar habilidades e conceitos relacionados ao Linux.

## Quiz Question

Como você obtém ajuda rápida na linha de comando para comandos internos do Bash? (Por favor, forneça o nome do comando único em inglês e em letras minúsculas.)

## Quiz Answer

help
