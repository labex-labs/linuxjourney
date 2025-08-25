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

A localização desses arquivos e diretórios é referida como caminhos. Se você tivesse uma pasta chamada `home` com uma pasta dentro dela chamada `pete` e outra pasta nessa pasta chamada `Movies`, esse caminho seria assim: `/home/pete/Movies`. Bem simples, não é?

A navegação do sistema de arquivos, muito parecido com a vida real, é útil se você sabe onde está e para onde está indo. Para ver onde você está, você pode usar o comando `pwd`. Este comando significa "print working directory" (imprimir diretório de trabalho) e apenas mostra em qual diretório você está. Observe que o caminho deriva do diretório raiz.

```bash
pwd
```

Onde você está? Onde estou? Experimente.

## Exercise

A prática leva à perfeição! Aqui estão alguns laboratórios práticos para reforçar sua compreensão da navegação do sistema de arquivos Linux e da identificação de sua localização atual:

1. **[Comando Linux pwd: Exibição de Diretório](https://labex.io/pt/labs/linux-linux-pwd-command-directory-displaying-209734)** - Este laboratório oferece uma visão geral focada e uso prático do comando `pwd`, alinhando-se diretamente com a introdução da lição sobre como encontrar seu diretório atual.
2. **[Navegação de Diretório Linux](https://labex.io/pt/labs/linux-directory-navigation-387844)** - Coloque suas habilidades básicas de linha de comando Linux à prova navegando por vários diretórios, solidificando sua compreensão de caminhos e da estrutura do sistema de arquivos.
3. **[Comando Linux cd: Mudança de Diretório](https://labex.io/pt/labs/linux-linux-cd-command-directory-changing-209733)** - Aprenda a navegar eficientemente em seu sistema de arquivos usando o comando `cd`, entendendo diferentes técnicas para mudar de diretório e explorar a estrutura de arquivos.

Esses laboratórios o ajudarão a aplicar os conceitos de hierarquia e navegação do sistema de arquivos em cenários reais e a construir confiança com comandos Linux essenciais.

## Quiz Question

Como faço para descobrir em qual diretório você está atualmente?

## Quiz Answer

pwd