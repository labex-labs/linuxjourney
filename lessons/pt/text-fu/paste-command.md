---
title: "paste"
description: "Aprenda a usar o comando Linux paste para mesclar linhas de arquivos. Descubra delimitadores e combine arquivos com este tutorial essencial do comando Linux."
keywords: "comando paste Linux, tutorial comando paste, mesclar linhas de arquivo, comandos Linux, Linux para iniciantes, guia Linux"
---

## Lesson Content

O comando `paste` é semelhante ao comando `cat`; ele mescla linhas em um arquivo. Vamos criar um novo arquivo com o seguinte conteúdo:

```
sample2.txt
The
quick
brown
fox
```

Vamos combinar todas essas linhas em uma única linha:

```bash
paste -s sample2.txt
```

O delimitador padrão para `paste` é TAB, então agora há uma linha com TABs separando cada palavra.

Vamos mudar este delimitador (`-d`) para algo um pouco mais legível:

```bash
paste -d ' ' -s sample2.txt
```

Agora tudo deve estar em uma linha delimitada por espaços.

## Exercise

Try to paste multiple files together. What happens?

## Quiz Question

Qual flag você usa com `paste` para fazer com que tudo fique em uma única linha?

## Quiz Answer

-s
