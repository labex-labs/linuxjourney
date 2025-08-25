---
index: 9
lang: "pt"
title: "Uso do Disco"
meta_title: "Uso do Disco - O Sistema de Arquivos"
meta_description: "Aprenda como verificar o uso do disco e o espaço livre no Linux usando os comandos df e du. Entenda suas diferenças e quando usar cada um. Tutorial de gerenciamento de disco Linux."
meta_keywords: "comando df, comando du, uso do disco Linux, verificar espaço livre, tutorial Linux, Linux para iniciantes, gerenciamento de disco, guia Linux"
---

## Lesson Content

Existem algumas ferramentas que você pode usar para ver a utilização de seus discos:

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

A prática leva à perfeição! Aqui estão alguns laboratórios práticos para reforçar sua compreensão do gerenciamento e utilização do espaço em disco no Linux:

1. **[Gerenciar Partições e Sistemas de Arquivos Linux](https://labex.io/pt/labs/comptia-manage-linux-partitions-and-filesystems-590845)** - Pratique a criação, formatação e montagem de sistemas de arquivos, que são as estruturas subjacentes relatadas por `df` e `du`.
2. **[Criar e Ativar um Arquivo Swap no Linux](https://labex.io/pt/labs/comptia-create-and-activate-a-swap-file-in-linux-590858)** - Aprenda a gerenciar a memória virtual em disco, um aspecto crítico do gerenciamento de recursos do sistema que impacta o espaço em disco.

Esses laboratórios o ajudarão a aplicar os conceitos em cenários reais e a construir confiança no gerenciamento de recursos de disco.

## Quiz Question

Qual comando é usado para mostrar quanto espaço está livre em seu disco?

## Quiz Answer

df
