---
title: "dd"
description: "Aprenda o comando Linux dd para cópia de dados e criação de imagens de disco. Entenda suas opções como if, of e bs. Comece sua jornada de gerenciamento de dados Linux!"
keywords: "comando dd, Linux dd, copiar dados, imagem de disco, tutorial Linux, iniciante, guia, backup de dados"
---

## Lesson Content

A ferramenta `dd` é super útil para converter e copiar dados. Ela lê a entrada de um arquivo ou fluxo de dados e a escreve em um arquivo ou fluxo de dados.

Considere o seguinte comando:

```bash
dd if=/home/pete/backup.img of=/dev/sdb bs=1024
```

Este comando está copiando o conteúdo de `backup.img` para `/dev/sdb`. Ele copiará os dados em blocos de 1024 bytes até que não haja mais dados para serem copiados.

- `if=file` - Arquivo de entrada; lê de um arquivo em vez da entrada padrão.
- `of=file` - Arquivo de saída; escreve para um arquivo em vez da saída padrão.
- `bs=bytes` - Tamanho do bloco; ele lê e escreve essa quantidade de bytes de dados por vez. Você pode usar diferentes métricas de tamanho denotando o tamanho com um `k` para kilobyte, `m` para megabyte, etc., então 1024 bytes é 1k.
- `count=number` - Número de blocos a copiar.

Você verá alguns comandos `dd` que usam a opção `count`. Geralmente, com `dd`, se você quiser copiar um arquivo de 1 megabyte, você geralmente vai querer que esse arquivo tenha 1 megabyte quando a cópia for concluída. Digamos que você execute o seguinte comando:

```bash
dd if=/home/pete/backup.img of=/dev/sdb bs=1M count=2
```

Nosso arquivo `backup.img` tem 10M; no entanto, estamos dizendo neste comando para copiar 1M 2 vezes, então apenas 2M estão sendo copiados, deixando nossos dados copiados incompletos. `count` pode ser útil em muitas situações, mas se você estiver apenas copiando dados, você pode praticamente omitir `count` e até mesmo `bs` nesse caso. Se você realmente quiser otimizar suas transferências de dados, então você vai querer começar a usar essas opções.

`dd` é extremamente poderoso; você pode usá-lo para fazer backups de qualquer coisa, incluindo discos rígidos inteiros, restaurar imagens de disco e muito mais. Tenha cuidado, essa ferramenta poderosa pode ter um preço se você não tiver certeza do que está fazendo.

## Exercise

Use o comando `dd` para fazer um backup do seu drive e defina a saída para um arquivo `.img`.

## Quiz Question

Qual é a opção `dd` para o tamanho do bloco?

## Quiz Answer

bs
