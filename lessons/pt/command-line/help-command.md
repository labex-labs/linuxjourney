---
index: 15
lang: "pt"
title: "ajuda"
meta_title: "ajuda - Linha de Comando"
meta_description: "Descubra como usar o comando help do Linux para assistência rápida no seu terminal. Este tutorial Bash explica como obter ajuda para comandos internos do shell e usar a flag --help para outros programas Linux."
meta_keywords: "comando help Linux, ajuda Bash, ajuda linha de comando, comandos Linux, Linux para iniciantes, tutorial Linux, tutorial Bash, built-in shell, assistência linha de comando"
---

## Lesson Content

Ao trabalhar na linha de comando do Linux, você frequentemente precisará de um lembrete rápido de como um comando funciona ou quais opções ele aceita. Felizmente, o Linux fornece excelentes ferramentas de ajuda para a linha de comando diretamente no terminal.

### O Comando 'help' para Built-ins do Bash

Uma das ferramentas mais diretas é o `help`, um comando que é construído diretamente no shell Bash. Ele é especificamente projetado para fornecer informações sobre outros comandos built-in do Bash. Um comando built-in faz parte do próprio shell, não sendo um programa separado. Exemplos incluem `echo`, `cd` e `pwd`.

Para usar o **comando help do Linux**, basta digitar `help` seguido pelo nome do comando built-in.

```bash
help echo
```

Isso exibirá um resumo do comando `echo`, sua sintaxe e uma lista de opções disponíveis. Esta é a maneira mais rápida de obter assistência para funções específicas do shell.

### A Flag --help para Programas Executáveis

Para a maioria dos outros programas executáveis que não são built-in no shell, o comando `help` não funcionará. Em vez disso, uma convenção comum é fornecer uma flag `--help`. Esta opção sinaliza ao programa para imprimir um resumo de uso e, em seguida, sair.

```bash
ls --help
```

Embora a maioria dos desenvolvedores siga este padrão, ele não é universal. No entanto, tentar a flag `--help` é geralmente o melhor primeiro passo para encontrar ajuda para um programa desconhecido. É uma habilidade fundamental para quem está aprendendo sobre **comandos Linux**.

## Exercise

Embora não haja laboratórios específicos para este tópico, recomendamos explorar o abrangente [Trilha de Aprendizagem do Linux](https://labex.io/pt/learn/linux) para praticar habilidades e conceitos relacionados ao Linux.

## Quiz Question

Como você obtém ajuda rápida na linha de comando para comandos built-in do Bash? (Por favor, forneça o nome único do comando em inglês e em minúsculas.)

## Quiz Answer

help
