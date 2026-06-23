---
index: 12
lang: "pt"
title: "mkdir (Criar Diretório)"
meta_title: "mkdir (Criar Diretório) - Linha de Comando"
meta_description: "Aprenda o comando mkdir do Linux com exemplos para criar um diretório, múltiplos diretórios, diretórios aninhados e definir permissões."
meta_keywords: "comando mkdir, linux mkdir, criar diretório linux, fazer diretório linux, mkdir -p, mkdir -m, criar pasta linux"
---

## Lesson Content

À medida que você trabalha com arquivos, precisará organizá-los em diretórios. A ferramenta principal para essa tarefa é o comando `mkdir`, que significa criar diretório.

A sintaxe básica é:

```bash
mkdir [OPTIONS] DIRECTORY...
```

### Criando um Diretório Único

O uso mais básico do `mkdir` é criar um único diretório novo. Se o diretório ainda não existir, este comando o cria no seu local atual.

```bash
$ mkdir documents
```

### Criando Múltiplos Diretórios

Você também pode criar vários diretórios de uma vez listando seus nomes, separados por espaços. Esta é uma forma eficiente de configurar várias pastas rapidamente.

```bash
$ mkdir books paintings
```

### Criando Diretórios Aninhados

Às vezes, você precisa criar um diretório e seus diretórios pai simultaneamente. A opção `-p` é perfeita para isso. Ela evita erros caso os diretórios pai não existam.

```bash
$ mkdir -p books/hemingway/favorites
```

Este único comando cria `books`, `hemingway` e `favorites` se eles ainda não existirem.

### Definindo Permissões do Diretório

Use `-m` para definir permissões ao criar um diretório.

```bash
$ mkdir -m 755 public
```

Você aprenderá mais sobre permissões depois, mas este exemplo cria um diretório que o proprietário pode escrever e os outros podem ler e acessar.

### Opções Comuns do mkdir

- `-p`: Cria diretórios pai conforme necessário.
- `-m MODE`: Define permissões para o novo diretório.
- `-v`: Exibe uma mensagem para cada diretório criado.

Exemplo:

```bash
$ mkdir -pv projects/app/src
mkdir: created directory 'projects'
mkdir: created directory 'projects/app'
mkdir: created directory 'projects/app/src'
```

### Perguntas Comuns

**Por que o mkdir diz "File exists"?** Um arquivo ou diretório com esse nome já existe. Use `ls` para inspecioná-lo.

**Como criar diretórios aninhados?** Use `mkdir -p parent/child/grandchild`.

**O mkdir pode criar arquivos?** Não. Use `touch` para criar arquivos vazios.

## Exercise

A prática leva à perfeição! Aqui estão alguns laboratórios práticos para reforçar seu entendimento sobre criação e gerenciamento de diretórios:

1. **[Comando Linux mkdir: Criando Diretórios](https://labex.io/pt/labs/linux-linux-mkdir-command-directory-creating-209739)** - Aprenda a usar o comando `mkdir` no Linux para criar diretórios, definir permissões e organizar seu sistema de arquivos. Este laboratório cobre uso básico e avançado, incluindo criação de diretórios aninhados.
2. **[Configurando uma Nova Estrutura de Projeto](https://labex.io/pt/labs/linux-setting-up-a-new-project-structure-387859)** - Pratique suas habilidades de gerenciamento de diretórios no Linux criando uma estrutura específica de projeto e navegando por ela usando comandos essenciais como `mkdir` e `cd`.

Esses laboratórios ajudarão você a aplicar os conceitos em cenários reais e ganhar confiança na criação e organização de diretórios no Linux.

## Quiz Question

Qual comando é usado para criar um diretório? Por favor, responda usando apenas o comando em inglês minúsculo.

## Quiz Answer

mkdir
