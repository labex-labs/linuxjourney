---
index: 2
lang: "pt"
title: "pwd (Print Working Directory)"
meta_title: "pwd (Print Working Directory) - Linha de Comando"
meta_description: "Aprenda a usar o comando 'pwd' no Linux para imprimir seu diretório de trabalho atual. Entenda os caminhos do sistema de arquivos Linux e a navegação para iniciantes."
meta_keywords: "comando pwd, diretório Linux, diretório atual, caminho Linux, tutorial Linux, Linux para iniciantes, guia Linux"
---

## Lesson Content

Tudo no Linux é um arquivo. À medida que você se aprofunda no Linux, você entenderá isso, mas por enquanto, apenas tenha isso em mente. Cada arquivo é organizado em uma árvore de diretórios hierárquica. O primeiro diretório no sistema de arquivos é apropriadamente chamado de diretório raiz. O diretório raiz tem muitas pastas e arquivos, que podem armazenar mais pastas e arquivos, etc. Aqui está um exemplo de como a árvore de diretórios se parece:

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

A localização desses arquivos e diretórios é referida como caminhos. Se você tivesse uma pasta chamada `home` com uma pasta dentro dela chamada `pete` e outra pasta nessa pasta chamada `Movies`, esse caminho se pareceria com isto: `/home/pete/Movies`. Bem simples, não é?

A navegação do sistema de arquivos, assim como na vida real, é útil se você sabe onde está e para onde está indo. Para ver onde você está, você pode usar o comando `pwd`. Este comando significa "print working directory" (imprimir diretório de trabalho) e ele apenas mostra em qual diretório você está. Observe que o caminho se origina do diretório raiz.

```bash
pwd
```

Onde você está? Onde estou? Experimente.

## Exercise

Para prática prática com o comando `pwd`, experimente este laboratório interativo:

- [Linux pwd Command: Directory Displaying](https://labex.io/pt/labs/linux-linux-pwd-command-directory-displaying-209734)

## Quiz Question

Como faço para descobrir em qual diretório você está atualmente?

## Quiz Answer

pwd
