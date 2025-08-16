---
lang: "pt"
title: "grep"
description: "Aprenda a usar o comando grep no Linux para pesquisar padrões de texto em arquivos. Descubra o uso básico, pesquisa que não diferencia maiúsculas de minúsculas e a combinação com outros comandos. Comece sua jornada no Linux!"
keywords: "comando grep, Linux grep, pesquisar arquivos, processamento de texto, tutorial Linux, Linux para iniciantes, guia grep"
---

## Lesson Content

O comando `grep` é possivelmente o comando de processamento de texto mais comum que você usará. Ele permite pesquisar arquivos por caracteres que correspondem a um determinado padrão. E se você quisesse saber se um arquivo existe em um determinado diretório, ou se quisesse ver se uma string foi encontrada em um arquivo? Você certamente não vasculharia cada linha de texto; você usaria o `grep`!

Vamos usar nosso arquivo `sample.txt` como exemplo:

```bash
grep fox sample.txt
```

Você deve ver que o `grep` encontrou "fox" no arquivo `sample.txt`.

Você também pode `grep` padrões que não diferenciam maiúsculas de minúsculas com a flag `-i`:

```bash
grep -i somepattern somefile
```

Para ter ainda mais flexibilidade com o `grep`, você pode combiná-lo com outros comandos usando `|`.

```bash
env | grep -i User
```

Como você pode ver, o `grep` é bastante versátil. Você pode até usar expressões regulares em seu padrão:

```bash
ls /somedir | grep '.txt$'
```

Isso deve retornar todos os arquivos terminados em `.txt` em `somedir`.

## Exercise

Você pode ter ouvido falar de `egrep` ou `fgrep`; estas são chamadas `grep` obsoletas e foram substituídas por `grep -E` e `grep -F`. Leia a manpage do `grep` para saber mais.

## Quiz Question

Qual comando você usa para encontrar um determinado padrão?

## Quiz Answer

grep
