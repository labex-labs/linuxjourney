---
index: 4
lang: "pt"
title: "ls (Listar Diretórios)"
meta_title: "ls (Listar Diretórios) - Linha de Comando"
meta_description: "Aprenda a usar o poderoso comando ls no Linux. Este guia aborda como listar o conteúdo do diretório, visualizar arquivos ocultos com ls -a, obter listagens detalhadas com ls -l e usar o comando ls -r para ordenação reversa. Uma lição perfeita para dominar o cmd ls."
meta_keywords: "comando ls, listar diretórios, cmd ls, comando ls -r, comando ls, linux ls -r, comando linux ls, arquivos ocultos, comandos Linux, Linux iniciante"
---

## Lesson Content

Agora que sabemos como navegar pelo sistema de arquivos, como podemos descobrir o que está disponível para nós? Sem a ferramenta certa, é como se mover no escuro. Felizmente, o maravilhoso `command linux ls` está aqui para ajudar, listando o conteúdo dos diretórios.

### Uso Básico do Comando ls

Por padrão, o comando `ls` listará os diretórios e arquivos no seu diretório atual. No entanto, você também pode especificar um caminho para listar o conteúdo de um diretório diferente.

```bash
ls
ls /home/pete
```

O `command ls` é uma ferramenta versátil que pode mostrar informações detalhadas sobre os arquivos e diretórios que você está visualizando.

### Visualizando Arquivos Ocultos

Note que nem todos os arquivos em um diretório são visíveis por padrão. No Linux, nomes de arquivos que começam com um ponto (`.`) são ocultos. Você pode visualizá-los usando o `cmd ls` com a flag `-a`, que significa "all" (todos).

```bash
ls -a
```

### Obtendo Informações Detalhadas

Outra flag essencial do `ls` é `-l` para "long" (longo). Esta opção fornece uma lista detalhada de arquivos em formato longo. Isso mostrará informações detalhadas, começando da esquerda: permissões do arquivo, número de links, nome do proprietário, grupo do proprietário, tamanho do arquivo, carimbo de data/hora da última modificação e o nome do arquivo ou diretório.

```bash
ls -l
```

Aqui está um exemplo da saída:

```plaintext
pete@icebox:~$ ls -l
total 80
drwxr-x--- 7 pete penguingroup   4096 Nov 20 16:37 Desktop
drwxr-x--- 2 pete penguingroup   4096 Oct 19 10:46  Documents
drwxr-x--- 4 pete penguingroup   4096 Nov 20 09:30 Downloads
drwxr-x--- 2 pete penguingroup   4096 Oct  7 13:13   Music
drwxr-x--- 2 pete penguingroup   4096 Sep 21 14:02 Pictures
drwxr-x--- 2 pete penguingroup   4096 Jul 27 12:41   Public
drwxr-x--- 2 pete penguingroup   4096 Jul 27 12:41   Templates
drwxr-x--- 2 pete penguingroup   4096 Jul 27 12:41   Videos
```

### Ordenando em Ordem Inversa

Às vezes, você pode querer alterar a ordem de classificação. O `ls -r command` lista arquivos e diretórios em ordem alfabética inversa. A opção `linux ls -r` é particularmente útil quando você deseja ver os últimos itens em uma lista longa primeiro.

```bash
ls -r
```

### Combinando Flags de Comando

Comandos têm flags (também chamadas de argumentos ou opções) para adicionar mais funcionalidade. Como vimos com `-a` e `-l`, você pode combiná-las em um único comando como `ls -la`. A ordem das flags geralmente não importa, então `ls -al` funcionaria identicamente. Você também pode adicionar a flag de reversão: `ls -lar`.

```bash
ls -la
```

## Exercise

A prática leva à perfeição! Aqui está um laboratório prático para reforçar sua compreensão do comando `ls`:

- **[Comando ls do Linux: Listagem de Conteúdo](https://labex.io/pt/labs/linux-linux-ls-command-content-listing-219205)** - Pratique o uso do comando `ls` para listar e analisar eficientemente o conteúdo de arquivos e diretórios. Você aprenderá várias opções para listagens detalhadas, exibição de arquivos ocultos, tamanhos legíveis por humanos e técnicas de ordenação para aprimorar suas habilidades de linha de comando.

Este laboratório o ajudará a aplicar os conceitos em um cenário real e a construir confiança com a listagem de diretórios no Linux.

## Quiz Question

What command would you use to see hidden files? Please answer in English, paying attention to case sensitivity.

## Quiz Answer

ls -a
