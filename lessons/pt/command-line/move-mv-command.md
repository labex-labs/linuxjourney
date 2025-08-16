---
lang: "pt"
title: "mv (Mover)"
description: "Aprenda a usar o comando Linux mv para mover e renomear arquivos/diretórios. Entenda suas opções e evite sobrescrições. Comece sua jornada no Linux!"
keywords: "comando mv, Linux mv, mover arquivos Linux, renomear arquivos Linux, tutorial Linux, iniciante, guia Linux"
---

## Lesson Content

Usado para mover arquivos e também renomeá-los. Bastante semelhante ao comando `cp` em termos de flags e funcionalidade.

Você pode renomear arquivos assim:

```bash
mv oldfile newfile
```

Ou você pode realmente mover um arquivo para um diretório diferente:

```bash
mv file2 /home/pete/Documents
```

E mover mais de um arquivo:

```bash
mv file_1 file_2 /somedirectory
```

Você também pode renomear diretórios:

```bash
mv directory1 directory2
```

Assim como `cp`, se você `mv` um arquivo ou diretório, ele sobrescreverá qualquer coisa no mesmo diretório. Então você pode usar a flag `-i` para ser solicitado antes de sobrescrever qualquer coisa.

```bash
mv -i directory1 directory2
```

Digamos que você quisesse que `mv` um arquivo sobrescrevesse o anterior. Você também pode fazer um backup desse arquivo, e ele simplesmente renomeará a versão antiga com um `~`.

```bash
mv -b directory1 directory2
```

## Exercise

Renomeie um arquivo e, em seguida, mova esse arquivo para um diretório diferente.

## Quiz Question

Como você renomeia um arquivo chamado `cat` para `dog`?

## Quiz Answer

mv cat dog
