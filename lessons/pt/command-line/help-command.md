---
lang: "pt"
title: "ajuda"
description: "Aprenda a usar o comando 'help' no Bash para assistência rápida na linha de comando. Entenda os comandos integrados e encontre opções para programas Linux."
keywords: "comando help Linux, Bash help, ajuda linha de comando, comandos Linux, Linux para iniciantes, tutorial Linux, tutorial Bash"
---

## Lesson Content

O Linux possui algumas ótimas ferramentas integradas para ajudar você a entender como usar um comando ou verificar quais flags estão disponíveis para um comando. Uma ferramenta, `help`, é um comando Bash integrado que fornece ajuda para outros comandos Bash (por exemplo, `echo`, `logout`, `pwd`).

```bash
help echo
```

Isso lhe dará uma descrição e as opções que você pode usar quando quiser executar `echo`. Para outros programas executáveis, é convenção ter uma opção chamada `--help` ou algo similar.

```bash
echo --help
```

Nem todos os desenvolvedores que distribuem executáveis seguirão este padrão, mas é provavelmente sua melhor chance de encontrar alguma ajuda sobre um programa.

## Exercise

Execute `help` nos comandos `echo`, `logout` e `pwd`.

## Quiz Question

Como você obtém ajuda rápida na linha de comando para comandos Bash integrados?

## Quiz Answer

help
