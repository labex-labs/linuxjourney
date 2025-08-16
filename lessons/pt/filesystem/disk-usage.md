---
title: "Uso do Disco"
description: "Aprenda a verificar o uso do disco e o espaço livre no Linux usando os comandos df e du. Entenda suas diferenças e quando usar cada um. Tutorial de gerenciamento de disco Linux."
keywords: "comando df, comando du, uso do disco Linux, verificar espaço livre, tutorial Linux, Linux para iniciantes, gerenciamento de disco, guia Linux"
---

## Lesson Content

Existem algumas ferramentas que você pode usar para ver a utilização dos seus discos:

```bash
pete@icebox:~$ df -h
Filesystem     1K-blocks    Used Available Use% Mounted on
/dev/sda1       6.2G  2.3G  3.6G  40% /
```

O comando `df` mostra a utilização dos seus sistemas de arquivos atualmente montados. A flag `-h` fornece um formato legível por humanos. Você pode ver qual é o dispositivo e quanta capacidade é usada e disponível.

Digamos que seu disco esteja ficando cheio e você queira saber quais arquivos ou diretórios estão ocupando esse espaço; para isso, você pode usar o comando **du**.

```bash
du -h
```

Isso mostra o uso do disco do diretório atual em que você está. Você pode dar uma olhada no diretório raiz com `du -h /`, mas isso pode ficar um pouco confuso.

Ambos os comandos são tão semelhantes na sintaxe que pode ser difícil lembrar qual usar. Para verificar quanto do seu **disco** está **livre**, use `df`. Para verificar o **uso do disco**, use `du`.

## Exercise

Verifique o uso do disco e o espaço livre com `du` e `df`.

## Quiz Question

Qual comando é usado para mostrar quanto espaço está livre no seu disco?

## Quiz Answer

df
