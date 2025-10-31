---
index: 12
lang: "pt"
title: "mkdir (Criar Diretório)"
meta_title: "mkdir (Criar Diretório) - Linha de Comando"
meta_description: "Aprenda a usar o comando mkdir no Linux para criar um novo diretório. Este guia abrange o comando criar pasta Linux, incluindo como criar múltiplos diretórios e diretórios pais a partir do prompt de comando."
meta_keywords: "criar diretório linux, comando mkdir no linux, criar diretório no linux, comando criar diretório prompt, comando criar pasta linux, mkdir, criar diretório, linux"
---

## Lesson Content

Ao trabalhar com arquivos, você precisará organizá-los em diretórios. A principal ferramenta para essa tarefa é o comando `mkdir`, que significa "Make Directory" (Criar Diretório). Este comando permite que você **crie um diretório no Linux** diretamente do seu terminal ou **prompt de comando**.

### Criando um Único Diretório

O uso mais básico do **comando mkdir no Linux** é criar um novo diretório. Se o diretório ainda não existir, este comando o criará em sua localização atual. Por exemplo, para criar um diretório chamado `documents`:

```bash
mkdir documents
```

### Criando Múltiplos Diretórios

Você também pode criar vários diretórios de uma vez, listando seus nomes, separados por espaços. Esta é uma maneira eficiente de configurar várias pastas rapidamente.

```bash
mkdir books paintings
```

### Criando Diretórios Aninhados

Às vezes, você precisa criar um diretório e seus diretórios pais simultaneamente. A opção `-p` (parent/pai) é perfeita para isso. Este recurso poderoso do **comando para criar pasta no Linux** evita erros se os diretórios pais não existirem. Por exemplo, para criar o diretório `favorites` dentro de `hemmingway`, que está dentro de `books`:

```bash
mkdir -p books/hemmingway/favorites
```

Este único comando cria `books`, `hemmingway` e `favorites` se eles ainda não existirem, demonstrando uma capacidade chave quando você precisa **criar um diretório no Linux**.

## Exercise

A prática leva à perfeição! Aqui estão alguns laboratórios práticos para reforçar sua compreensão da criação e gerenciamento de diretórios:

1. **[Comando mkdir do Linux: Criação de Diretório](https://labex.io/pt/labs/linux-linux-mkdir-command-directory-creating-209739)** - Aprenda a usar o comando `mkdir` no Linux para criar diretórios, definir permissões e organizar seu sistema de arquivos. Este laboratório cobre o uso básico e avançado, incluindo a criação de diretórios aninhados.
2. **[Configurando uma Nova Estrutura de Projeto](https://labex.io/pt/labs/linux-setting-up-a-new-project-structure-387859)** - Pratique suas habilidades de gerenciamento de diretórios no Linux criando uma estrutura de projeto específica e navegando por ela usando comandos essenciais como `mkdir` e `cd`.

Estes laboratórios ajudarão você a aplicar os conceitos em cenários reais e a ganhar confiança na criação e organização de diretórios no Linux.

## Quiz Question

Qual comando é usado para criar um diretório? Por favor, responda usando apenas o comando em inglês minúsculo.

## Quiz Answer

mkdir
