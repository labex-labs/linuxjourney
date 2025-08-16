---
title: "pwd (Imprimir Diretório de Trabalho)"
description: "Aprenda a usar o comando 'pwd' no Linux para imprimir seu diretório de trabalho atual. Entenda os caminhos do sistema de arquivos Linux e a navegação para iniciantes."
keywords: "comando pwd, diretório Linux, diretório atual, caminho Linux, tutorial Linux, Linux para iniciantes, guia Linux"
---

## Lesson Content

Tudo no Linux é um arquivo. À medida que você se aprofunda no Linux, você entenderá isso, mas por enquanto, apenas tenha isso em mente. Cada arquivo é organizado em uma árvore de diretórios hierárquica. O primeiro diretório no filesystem é apropriadamente chamado de diretório raiz. O diretório raiz tem muitas pastas e arquivos, que podem armazenar mais pastas e arquivos, etc. Aqui está um exemplo de como a árvore de diretórios se parece:

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

A localização desses arquivos e diretórios é referida como paths. Se você tivesse uma pasta chamada `home` com uma pasta dentro dela chamada `pete` e outra pasta nessa pasta chamada `Movies`, esse path se pareceria com isto: `/home/pete/Movies`. Bem simples, não é?

A navegação do filesystem, assim como na vida real, é útil se você sabe onde está e para onde está indo. Para ver onde você está, você pode usar o comando `pwd`. Este comando significa "print working directory" e ele apenas mostra em qual diretório você está. Observe que o path deriva do diretório raiz.

```bash
pwd
```

Onde você está? Onde estou? Experimente.

## Exercise

No exercises for this lesson.

## Quiz Question

Como faço para descobrir em qual diretório você está atualmente?

## Quiz Answer

pwd
