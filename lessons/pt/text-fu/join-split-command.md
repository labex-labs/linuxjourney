---
title: "join e split"
description: "Aprenda a usar os comandos 'join' e 'split' do Linux para manipulação de arquivos. Entenda como combinar arquivos por campos comuns e dividir arquivos grandes de forma eficiente. Obtenha exemplos práticos e dicas."
keywords: "comando Linux join, comando Linux split, manipulação de arquivos, tutorial Linux, linha de comando, Linux para iniciantes, guia Linux"
---

## Lesson Content

O comando `join` permite unir vários arquivos por um campo comum:

Digamos que eu tivesse dois arquivos que queria unir:

```plaintext
file1.txt
1 John
2 Jane
3 Mary

file2.txt
1 Doe
2 Doe
3 Sue
```

```bash
$ join file1.txt file2.txt
1 John Doe
2 Jane Doe
3 Mary Sue
```

Percebe como ele uniu meus arquivos? Eles são unidos pelo primeiro campo por padrão, e os campos precisam ser idênticos. Se não forem, você pode classificá-los. Neste caso, os arquivos são unidos via 1, 2, 3.

Como uniríamos os seguintes arquivos?

```plaintext
file1.txt
John 1
Jane 2
Mary 3

file2.txt
1 Doe
2 Doe
3 Sue
```

Para unir este arquivo, você precisa especificar quais campos está unindo. Neste caso, queremos o campo 2 em `file1.txt` e o campo 1 em `file2.txt`, então o comando seria assim:

```bash
$ join -1 2 -2 1 file1.txt file2.txt
1 John Doe
2 Jane Doe
3 Mary Sue
```

`-1` refere-se a `file1.txt` e `-2` refere-se a `file2.txt`. Bem legal. Você também pode dividir um arquivo em diferentes arquivos com o comando `split`:

```bash
split somefile
```

Isso o dividirá em diferentes arquivos. Por padrão, ele os dividirá assim que atingirem um limite de 1000 linhas. Os arquivos são nomeados `x**` por padrão.

## Exercise

Una dois arquivos com um número diferente de linhas em cada arquivo. O que acontece?

## Quiz Question

Qual comando você usaria para unir arquivos chamados `cat`, `dog`, `cow`?

## Quiz Answer

join cat dog cow
