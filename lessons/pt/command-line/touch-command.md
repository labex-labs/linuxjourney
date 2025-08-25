---
index: 5
lang: "pt"
title: "touch"
meta_title: "touch - Linha de Comando"
meta_description: "Aprenda a usar o comando Linux touch para criar novos arquivos e atualizar carimbos de data/hora. Este guia para iniciantes ajuda você a entender o gerenciamento de arquivos."
meta_keywords: "comando touch, criar arquivos, tutorial Linux, carimbos de data/hora de arquivos, Linux para iniciantes, guia Linux, comandos básicos"
---

## Lesson Content

Vamos aprender a criar alguns arquivos. Uma maneira muito simples é usar o comando `touch`. O `touch` permite criar novos arquivos vazios.

```bash
touch mysuperduperfile
```

E pronto, novo arquivo!

O `touch` também é usado para alterar os carimbos de data/hora em arquivos e diretórios existentes. Experimente: faça um `ls -l` em um arquivo e anote o carimbo de data/hora, depois use `touch` nesse arquivo, e ele atualizará o carimbo de data/hora.

Existem muitas outras maneiras de criar arquivos que envolvem outras coisas como redirecionamento e editores de texto, mas abordaremos isso no curso de Manipulação de Texto.

## Exercise

A prática leva à perfeição! Aqui estão alguns laboratórios práticos para reforçar sua compreensão sobre a criação e gerenciamento de objetos do sistema de arquivos:

1. **[Comando Linux mkdir: Criação de Diretórios](https://labex.io/pt/labs/linux-linux-mkdir-command-directory-creating-209739)** - Aprenda como usar o comando `mkdir` no Linux para criar diretórios, definir permissões e organizar seu sistema de arquivos. Isso o ajudará a entender o conceito mais amplo de criação de novos itens no sistema de arquivos.
2. **[Configurando uma Nova Estrutura de Projeto](https://labex.io/pt/labs/linux-setting-up-a-new-project-structure-387859)** - Pratique suas habilidades de gerenciamento de diretórios Linux criando uma estrutura de projeto específica e navegando por ela usando comandos essenciais como `mkdir` e `cd`.

Esses laboratórios o ajudarão a aplicar os conceitos de criação e organização do sistema de arquivos em cenários reais e a construir confiança com os comandos Linux.

## Quiz Question

Como você cria um arquivo chamado `myfile`?

## Quiz Answer

touch myfile