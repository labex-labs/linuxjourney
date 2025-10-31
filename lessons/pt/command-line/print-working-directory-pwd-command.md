---
index: 2
lang: "pt"
title: "pwd (Imprimir Diretório de Trabalho)"
meta_title: "pwd (Imprimir Diretório de Trabalho) - Linha de Comando"
meta_description: "Domine o comando pwd do Linux para exibir seu diretório atual. Esta lição explica o significado completo de pwd no Linux e como navegar na árvore de diretórios."
meta_keywords: "linux pwd, diretório atual linux, árvore de diretórios linux, significado de pwd linux, imprimir diretório de trabalho, caminho linux, navegação linux, comandos básicos"
---

## Lesson Content

No Linux, um conceito central é que tudo é tratado como um arquivo. Esses arquivos são organizados dentro de uma estrutura hierárquica conhecida como sistema de arquivos. Entender essa estrutura é fundamental para navegar em seu sistema de forma eficaz.

### A Árvore de Diretórios no Linux

Todo o sistema de arquivos começa a partir de um único diretório de nível superior chamado diretório raiz, representado por uma barra normal (`/`). A partir da raiz, a **árvore de diretórios no linux** ramifica-se em vários subdiretórios, que podem conter arquivos e mais subdiretórios.

Aqui está um exemplo simplificado de como essa estrutura se parece:

```plaintext
/
|-- bin
|   |-- file1
|   |-- file2
|-- etc
|   |-- file3
|   `-- directory1
|       |-- file4
|       `-- file5
|-- home
|-- var
```

### Entendendo os Caminhos de Arquivo

A localização de qualquer arquivo ou diretório é descrita pelo seu caminho. Um caminho é uma sequência de diretórios que leva de um ponto de partida a um destino específico. Por exemplo, se você tem uma pasta chamada `pete` dentro do diretório `/home`, e uma pasta `Movies` dentro de `pete`, o caminho completo seria `/home/pete/Movies`.

### Qual é a Forma Completa de PWD no Linux?

Ao navegar no sistema de arquivos, é essencial saber sua localização atual. O comando para isso é `pwd`. A **forma completa de pwd no linux** é "print working directory" (imprimir diretório de trabalho). Seu único propósito é exibir o caminho completo do diretório em que você está atualmente, começando pela raiz (`/`).

### Usando o Comando linux pwd

Para encontrar seu **diretório atual linux**, basta digitar o comando **linux pwd** e pressionar Enter. Ele imprime o caminho absoluto para sua localização presente na linha de comando.

```bash
pwd
```

Onde você está? Onde estou? Tente para ver seu próprio diretório de trabalho atual.

## Exercise

A prática leva à perfeição! Aqui estão alguns laboratórios práticos para reforçar sua compreensão da navegação no sistema de arquivos Linux e da identificação de sua localização atual:

1.  **[Comando Linux pwd: Exibição de Diretório](https://labex.io/pt/labs/linux-linux-pwd-command-directory-displaying-209734)** - Este laboratório fornece uma visão focada e uso prático do comando `pwd`, alinhando-se diretamente com a introdução da lição sobre como encontrar seu diretório atual.
2.  **[Navegação de Diretório Linux](https://labex.io/pt/labs/linux-directory-navigation-387844)** - Coloque suas habilidades básicas de linha de comando Linux à prova, navegando por vários diretórios, solidificando sua compreensão de caminhos e da estrutura do sistema de arquivos.
3.  **[Comando Linux cd: Mudança de Diretório](https://labex.io/pt/labs/linux-linux-cd-command-directory-changing-209733)** - Aprenda a navegar eficientemente em seu sistema de arquivos usando o comando `cd`, entendendo diferentes técnicas para mudar de diretório e explorar a estrutura de arquivos.

Esses laboratórios ajudarão você a aplicar os conceitos de hierarquia e navegação do sistema de arquivos em cenários reais e a ganhar confiança com comandos essenciais do Linux.

## Quiz Question

Qual comando é usado para encontrar o diretório em que você está atualmente? (Por favor, responda em inglês, usando apenas o nome do comando em minúsculas.)

## Quiz Answer

pwd
