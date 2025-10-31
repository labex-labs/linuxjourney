---
index: 9
lang: "pt"
title: "Uso do Disco"
meta_title: "Uso do Disco - O Sistema de Arquivos"
meta_description: "Aprenda a verificar o uso do disco e o espaço livre no Linux com os comandos df e du. Este guia aborda como analisar o espaço em disco, incluindo o uso de inodes com df -i linux, e como encontrar quais arquivos estão ocupando espaço."
meta_keywords: "comando df, comando du, uso de disco Linux, verificar espaço livre, df -i linux, gerenciamento de disco, tutorial Linux, utilização de disco, uso do sistema de arquivos"
---

## Lesson Content

Gerenciar o espaço em disco é uma tarefa fundamental para qualquer usuário ou administrador Linux. Dois comandos essenciais para este propósito são `df` e `du`. Vamos explorar como usá-los para monitorar a utilização do seu disco de forma eficaz.

### Verificando o Espaço do Sistema de Arquivos com df

O comando `df` (disk free - disco livre) relata a quantidade de espaço em disco usada e disponível nos seus sistemas de arquivos montados atualmente. Ele fornece uma visão geral do seu armazenamento.

Para obter um relatório em formato legível por humanos (ex: GB, MB, KB), use a flag `-h`:

```bash
pete@icebox:~$ df -h
Filesystem      Size  Used Avail Use% Mounted on
/dev/sda1       6.2G  2.3G  3.6G  40% /
```

Esta saída mostra o dispositivo do sistema de arquivos, o tamanho total, o espaço usado, o espaço disponível, a porcentagem de uso e onde ele está montado.

### Analisando o Uso de Inodes

Além do espaço em blocos, os sistemas de arquivos também usam inodes para armazenar metadados sobre arquivos (como permissões, propriedade e localização). Em raras ocasiões, você pode ficar sem inodes mesmo tendo espaço livre em disco. Para verificar o uso de inodes, você pode usar o comando `df -i`. Executar `df -i` no Linux oferece uma imagem clara da alocação de inodes.

```bash
pete@icebox:~$ df -i
Filesystem      Inodes  IUsed   IFree IUse% Mounted on
/dev/sda1      4128768 128768 4000000    4% /
```

### Resumindo o Uso de Diretórios com du

Quando você percebe que um disco está ficando cheio, você vai querer identificar quais arquivos ou diretórios estão consumindo mais espaço. Para esta tarefa, o comando `du` (disk usage - uso de disco) é a ferramenta perfeita.

Executar `du` sem argumentos mostra o uso de disco para cada subdiretório na sua localização atual. Usar a flag `-h` fornece um resumo legível por humanos:

```bash
du -h
```

Você também pode especificar um caminho, como `du -h /home/pete`, para analisar um diretório específico. Executá-lo no diretório raiz (`du -h /`) pode gerar muitas saídas, então é frequentemente melhor verificar diretórios específicos que você suspeita serem grandes.

### df vs du Um Resumo Rápido

A sintaxe para `df` e `du` é tão semelhante que pode ser fácil confundi-los. Aqui está uma maneira simples de lembrar a diferença:

- Use `df` para verificar quanto **d**isco está **l**ivre (disk **f**ree) nos seus sistemas de arquivos.
- Use `du` para verificar o **u**so de **d**isco (disk **u**sage) de arquivos e diretórios específicos.

## Exercise

A prática leva à perfeição! Aqui estão alguns laboratórios práticos para reforçar sua compreensão sobre gerenciamento e utilização de espaço em disco no Linux:

1. **[Gerenciar Partições e Sistemas de Arquivos Linux](https://labex.io/pt/labs/comptia-manage-linux-partitions-and-filesystems-590845)** - Pratique a criação, formatação e montagem de sistemas de arquivos, que são as estruturas subjacentes relatadas por `df` e `du`.
2. **[Criar e Ativar um Arquivo de Swap no Linux](https://labex.io/pt/labs/comptia-create-and-activate-a-swap-file-in-linux-590858)** - Aprenda a gerenciar a memória virtual em disco, um aspecto crítico do gerenciamento de recursos do sistema que afeta o espaço em disco.

Estes laboratórios ajudarão você a aplicar os conceitos em cenários reais e a ganhar confiança no gerenciamento de recursos de disco.

## Quiz Question

Qual comando é usado para mostrar quanto espaço está livre no seu disco? Responda em letras minúsculas em inglês.

## Quiz Answer

df
