---
lesson_id: "make-directory-mkdir-command"
course_id: "command-line"
lang: "pt"
order_index: 12
title: "mkdir (Criar Diretório)"
description: "Aprenda a criar diretórios únicos, múltiplos e aninhados com as opções de mkdir."
meta_title: "mkdir (Criar Diretório) - Linha de Comando"
meta_description: "Aprenda o comando mkdir do Linux com exemplos para criar um ou vários diretórios, diretórios pais aninhados e definir permissões."
meta_keywords: "comando mkdir, mkdir Linux, criar diretório Linux, criar pasta Linux, mkdir -p, mkdir -m, diretórios aninhados"
---

O comando `mkdir`, abreviação de make directory, cria diretórios para organizar arquivos e outros diretórios.

A sintaxe básica é:

```bash
mkdir [OPTIONS] DIRECTORY...
```

## Criação de um Diretório

Forneça um caminho para criar um diretório. Este exemplo cria `documents` no diretório de trabalho atual:

```bash
$ mkdir documents
```

Se já existir uma entrada chamada `documents`, `mkdir` informará um erro em vez de substituí-la. Use `ls -ld documents` para inspecionar a entrada existente.

:::single-choice{#create-one-directory} Qual comando cria um diretório chamado `documents` no diretório de trabalho atual?

::option[`mkdir documents`]{#mkdir-documents .correct explanation="`mkdir` cria o diretório solicitado no caminho relativo `documents`."}
::option[`touch documents`]{#touch-documents explanation="`touch` cria um arquivo comum vazio quando o caminho está ausente. Ele não cria um diretório."}
::option[`cd documents`]{#cd-documents explanation="`cd` tenta entrar em um diretório existente. Ele não cria um diretório ausente."}
:::

## Criação de Vários Diretórios

Liste vários caminhos para criar vários diretórios em um único comando:

```bash
$ mkdir books paintings
```

:::single-choice{#create-separate-directories} Qual comando cria dois diretórios irmãos chamados `books` e `paintings`?

::option[`mkdir books/paintings`]{#nested-paintings explanation="Esse caminho descreve `paintings` dentro de `books`, não dois diretórios irmãos. Ele também falha se `books` estiver ausente."}
::option[`mkdir "books paintings"`]{#spaced-directory explanation="As aspas combinam as palavras em um único caminho; portanto, esse comando solicita um só diretório cujo nome contém um espaço."}
::option[`mkdir books paintings`]{#two-directories .correct explanation="Operandos separados instruem `mkdir` a criar `books` e `paintings` como dois diretórios."}
:::

## Criação de Diretórios Pais Ausentes

Sem uma opção, `mkdir books/hemingway/favorites` falha quando um diretório intermediário está ausente. Acrescente `-p` para criar os diretórios pais que faltam ao longo do caminho:

```bash
$ mkdir -p books/hemingway/favorites
```

Esse comando cria as partes ausentes do caminho. Ele também não informa um erro apenas porque o diretório final já existe, embora outros erros, como permissões insuficientes, ainda possam ocorrer.

:::single-choice{#create-nested-path} Nenhuma parte de `projects/app/src` existe. Qual comando cria o caminho completo de diretórios?

::option[`mkdir -p projects/app/src`]{#mkdir-parents .correct explanation="A opção `-p` cria cada diretório pai ausente antes de criar o diretório final."}
::option[`mkdir projects/app/src`]{#mkdir-no-parents explanation="Sem `-p`, `mkdir` não consegue criar `src` quando os diretórios intermediários não existem."}
::option[`mkdir -m projects/app/src`]{#mkdir-mode-missing explanation="A opção `-m` exige um argumento de modo e não solicita a criação dos diretórios pais ausentes."}
:::

## Definição do Modo Inicial

Use `-m MODE` para especificar as permissões de um novo diretório:

```bash
$ mkdir -m 755 public
```

Você estudará os modos de permissão mais adiante. Neste exemplo, o modo `755` concede ao proprietário permissões de leitura, gravação e pesquisa, enquanto o grupo e os demais recebem permissões de leitura e pesquisa.

Acrescente `-v` para mostrar uma mensagem para cada diretório criado:

```bash
$ mkdir -pv projects/app/src
mkdir: created directory 'projects'
mkdir: created directory 'projects/app'
mkdir: created directory 'projects/app/src'
```

:::single-choice{#set-directory-mode} Qual comando cria `public` com o modo de permissão `755`?

::option[`mkdir -p 755 public`]{#parents-755 explanation="A opção `-p` trata as palavras restantes como caminhos de diretórios; portanto, esse comando não define o modo de permissão `755`."}
::option[`mkdir -v 755 public`]{#verbose-755 explanation="A opção `-v` mostra mensagens de criação. Ela não interpreta `755` como um modo de permissão."}
::option[`mkdir -m 755 public`]{#mode-public .correct explanation="A opção `-m` recebe o modo solicitado, e `public` é o caminho do diretório que será criado."}
:::

Para praticar a criação e a organização de diretórios, experimente estes laboratórios:

1. **[Comando mkdir do Linux: Criação de Diretórios](https://labex.io/labs/linux-linux-mkdir-command-directory-creating-209739)** — Aprenda a usar `mkdir` para criar diretórios, definir permissões e organizar o sistema de arquivos. O laboratório aborda o uso básico e avançado, incluindo diretórios aninhados.
2. **[Configuração da Estrutura de um Novo Projeto](https://labex.io/labs/linux-setting-up-a-new-project-structure-387859)** — Pratique o gerenciamento de diretórios criando uma estrutura de projeto específica e navegando por ela com comandos essenciais como `mkdir` e `cd`.

## Resumo

Agora você sabe criar estruturas de diretórios com nomes, diretórios pais e modos escolhidos conscientemente.

1. Crie um ou mais diretórios em um único comando.
2. Reconheça um erro causado por um caminho já existente.
3. Crie diretórios pais ausentes com `-p`.
4. Defina o modo de um novo diretório com `-m`.
