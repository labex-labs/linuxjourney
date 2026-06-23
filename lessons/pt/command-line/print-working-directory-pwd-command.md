---
index: 2
lang: "pt"
title: "pwd (Imprimir Diretório Atual)"
meta_title: "pwd (Imprimir Diretório Atual) - Linha de Comando"
meta_description: "Aprenda o comando Linux pwd, o que significa imprimir o diretório atual e como caminhos absolutos mostram sua localização atual no sistema de arquivos."
meta_keywords: "comando pwd, linux pwd, imprimir diretório atual, diretório atual linux, caminho absoluto, sistema de arquivos linux, árvore de diretórios"
---

## Lesson Content

No Linux, arquivos e diretórios são organizados em uma hierarquia chamada sistema de arquivos. Antes de você poder se mover com confiança, é preciso saber onde você está. O comando `pwd` responde a essa pergunta imprimindo seu diretório de trabalho atual.

### A Árvore de Diretórios no Linux

Todo o sistema de arquivos começa a partir de um único diretório de nível superior chamado diretório raiz, representado por uma barra (/). A partir da raiz, a árvore de diretórios se ramifica em subdiretórios, que podem conter arquivos e mais subdiretórios.

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

### Entendendo os Caminhos de Arquivos

A localização de qualquer arquivo ou diretório é descrita pelo seu caminho. Um caminho é uma sequência de diretórios que leva de um ponto de partida a um destino específico.

Por exemplo, se você tem uma pasta chamada `pete` dentro de `/home`, e uma pasta `Movies` dentro de `pete`, o caminho completo é:

```plaintext
/home/pete/Movies
```

Um caminho que começa com `/` é um caminho absoluto porque começa no diretório raiz. Um caminho como `Movies` é relativo porque depende da sua localização atual.

### Qual é o Significado Completo de PWD no Linux?

O significado completo de `pwd` é "print working directory" (imprimir diretório de trabalho). Seu diretório de trabalho é o diretório onde seu shell está atualmente localizado. Comandos que usam caminhos relativos começam a partir dessa localização.

### Usando o Comando pwd

Para encontrar seu diretório atual, digite `pwd` e pressione Enter.

```bash
$ pwd
/home/pete
```

A saída é um caminho absoluto. Neste exemplo, o shell está atualmente no diretório home do usuário `pete`.

### Por que o pwd é Útil

Use `pwd` quando:

- Você está seguindo instruções e precisa confirmar sua localização.
- Um comando falhou porque um caminho de arquivo estava errado.
- Você navegou por vários diretórios e perdeu a noção de onde está.
- Você quer copiar o caminho do diretório atual para outro comando.

Por exemplo:

```bash
$ pwd
/home/pete/projects
$ ls
app.py  README.md
```

Isso indica que `app.py` e `README.md` estão localizados em `/home/pete/projects`.

### Perguntas Comuns

**O pwd altera alguma coisa?** Não. `pwd` apenas imprime informações.

**Por que a saída é diferente no meu sistema?** Seu nome de usuário, diretório home e localização atual podem ser diferentes.

**Qual é a diferença entre pwd e cd?** `pwd` mostra onde você está. `cd` muda onde você está.

## Exercise

Practice makes perfect! Here are some hands-on labs to reinforce your understanding of Linux file system navigation and identifying your current location:

1. **[Linux pwd Command: Directory Displaying](https://labex.io/pt/labs/linux-linux-pwd-command-directory-displaying-209734)** - This lab provides a focused overview and practical usage of the `pwd` command, directly aligning with the lesson's introduction to finding your current directory.
2. **[Linux Directory Navigation](https://labex.io/pt/labs/linux-directory-navigation-387844)** - Put your basic Linux command-line skills to the test by navigating through various directories, solidifying your understanding of paths and the file system structure.
3. **[Linux cd Command: Directory Changing](https://labex.io/pt/labs/linux-linux-cd-command-directory-changing-209733)** - Learn to efficiently navigate your file system using the `cd` command, understanding different techniques for changing directories and exploring the file structure.

These labs will help you apply the concepts of file system hierarchy and navigation in real scenarios and build confidence with essential Linux commands.

## Quiz Question

Qual comando é usado para descobrir o diretório em que você está atualmente? (Por favor, responda em inglês, usando apenas o nome do comando em letras minúsculas.)

## Quiz Answer

pwd
