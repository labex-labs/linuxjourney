---
index: 14
lang: "pt"
title: "find"
meta_title: "find - Linha de Comando"
meta_description: "Aprenda o comando find do Linux com exemplos para busca por nome, tipo, tamanho, tempo de modificação e execução de ações em arquivos correspondentes."
meta_keywords: "comando linux find, comando find, encontrar arquivos linux, find por nome, find por tipo, find por tamanho, find mtime, find exec"
---

## Lesson Content

Com inúmeros arquivos em um sistema, pode ser desafiador localizar um específico. O comando `find` pesquisa árvores de diretórios usando critérios como nome, tipo, tamanho e tempo de modificação.

### Usando o comando find

A sintaxe básica é:

```bash
find [PATH] [EXPRESSION]
```

Você especifica o diretório para buscar e os critérios do que está procurando.

Por exemplo, para buscar um arquivo chamado `puppies.jpg` dentro do diretório `/home` e todos os seus subdiretórios, você usaria:

```bash
$ find /home -name puppies.jpg
```

As buscas são recursivas por padrão, então `find /home` procura dentro de `/home` e seus subdiretórios.

### Buscando por Nome e Tipo

Um dos usos mais comuns do `find` é buscar pelo nome do arquivo. A opção `-name` corresponde exatamente ao nome ou por padrões no estilo shell.

```bash
$ find . -name "*.txt"
```

Você também pode especificar o tipo do item que está procurando. A opção `-type` é usada para esse propósito. Por exemplo, se quiser encontrar um diretório em vez de um arquivo, pode usar `d`.

```bash
$ find /home -type d -name MyFolder
```

Neste comando, definimos o tipo como `d` para diretório e estamos buscando um item chamado `MyFolder`. Para buscar especificamente arquivos regulares, você usaria `-type f`.

### Buscando por Tamanho e Tempo

Você pode buscar pelo tamanho do arquivo:

```bash
$ find . -type f -size +10M
$ find . -type f -size -1k
```

O primeiro comando encontra arquivos maiores que 10 megabytes. O segundo encontra arquivos menores que 1 kilobyte.

Você também pode buscar pelo tempo de modificação:

```bash
$ find . -type f -mtime -7
$ find . -type f -mtime +30
```

`-mtime -7` significa modificado nos últimos 7 dias. `-mtime +30` significa modificado há mais de 30 dias.

### Executando Ações nos Resultados

Por padrão, o `find` imprime os caminhos correspondentes. Você pode adicionar ações como `-print`, `-delete` ou `-exec`.

Imprima as correspondências explicitamente:

```bash
$ find . -name "*.log" -print
```

Execute `ls -l` em cada correspondência:

```bash
$ find . -name "*.log" -exec ls -l {} \;
```

O espaço reservado `{}` é substituído por cada caminho correspondente. O ponto e vírgula escapado marca o fim do comando.

Tenha cuidado com ações destrutivas como `-delete`. Primeiro execute a mesma busca sem `-delete` para confirmar as correspondências.

### Opções Comuns do find

- `-name PATTERN`: Corresponde pelo nome do arquivo.
- `-iname PATTERN`: Corresponde pelo nome do arquivo, ignorando maiúsculas e minúsculas.
- `-type f`: Corresponde a arquivos regulares.
- `-type d`: Corresponde a diretórios.
- `-size +10M`: Corresponde a arquivos maiores que 10 megabytes.
- `-mtime -7`: Corresponde a arquivos modificados nos últimos 7 dias.
- `-maxdepth N`: Limita a profundidade da busca do `find`.

### Perguntas Comuns

**Por que o find mostra "Permission denied"?** Seu usuário não pode ler alguns diretórios. Busque em um caminho mais restrito ou use privilégios apropriados.

**Por que devo colocar padrões como "*.txt" entre aspas?** Colocar entre aspas impede que o shell expanda o curinga antes que o `find` o receba.

**O find é recursivo?** Sim. Ele busca em subdiretórios por padrão.

## Exercise

Practice is key to mastering the `find command in linux`. These hands-on labs will help you reinforce your understanding of finding files and directories:

1. **[Linux find Command: File Searching](https://labex.io/pt/labs/linux-linux-find-command-file-searching-219191)** - This lab provides an introduction to the `find` command, a versatile utility for searching and locating files and directories based on various criteria. You'll practice using `find` to locate specific files.
2. **[Discover Critical System Resources](https://labex.io/pt/labs/linux-discover-critical-system-resources-388032)** - Learn essential Linux commands for locating files and executables, including `find`. You'll practice efficiently navigating the file system and discovering critical system resources.

These labs will help you apply the concepts in real scenarios and build confidence with using the `find` command effectively.

## Quiz Question

Qual opção você deve especificar para o comando `find` buscar por nome? Por favor, responda usando apenas a opção em inglês, prestando atenção ao formato requerido (ex.: -option).

## Quiz Answer

-name
