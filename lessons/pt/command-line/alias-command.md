---
index: 18
lang: "pt"
title: "alias"
meta_title: "alias - Linha de Comando"
meta_description: "Aprenda como criar e gerenciar aliases Linux para comandos comuns. Descubra a configuração de alias temporário e permanente em .bashrc. Melhore sua eficiência na linha de comando!"
meta_keywords: "alias Linux, alias bash, comando unalias, .bashrc, tutorial Linux, linha de comando, Linux para iniciantes, guia Linux"
---

## Lesson Content

Às vezes, digitar comandos pode ser muito repetitivo, ou se você precisar digitar um comando longo muitas vezes, é melhor ter um alias que você possa usar para isso. Para criar um alias para um comando, você simplesmente especifica um nome de alias e o define para o comando.

```bash
alias foobar='ls -la'
```

Agora, em vez de digitar `ls -la`, você pode digitar `foobar`, e ele executará esse comando — muito legal. Lembre-se de que este comando não salvará seu alias após a reinicialização, então você precisará adicionar um alias permanente em:

```plaintext
~/.bashrc
```

ou arquivos semelhantes se você quiser que ele persista após a reinicialização.

Você pode remover aliases com o comando `unalias`:

```bash
unalias foobar
```

## Exercise

Embora não haja laboratórios específicos para este tópico, recomendamos explorar o abrangente [Caminho de Aprendizagem Linux](https://labex.io/pt/learn/linux) para praticar habilidades e conceitos relacionados ao Linux.

## Quiz Question

Qual comando é usado para criar um alias?

## Quiz Answer

alias
