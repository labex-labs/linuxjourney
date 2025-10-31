---
index: 3
lang: "pt"
title: "Anatomia de um Disco"
meta_title: "Anatomia de um Disco - O Sistema de Arquivos"
meta_description: "Explore a anatomia de um disco no Linux. Este guia explica qual componente do disco informa ao SO como o disco está particionado, cobrindo tabelas de partição MBR e GPT, diferentes tipos de partições Linux e como elas são organizadas."
meta_keywords: "disco no linux, partições linux, tipos de partições linux, qual componente do disco informa ao SO como o disco está particionado, o que contém informações sobre como as partições do disco rígido são organizadas, MBR, GPT, tabela de partição, sistema de arquivos"
---

## Lesson Content

Um disco rígido no Linux pode ser subdividido em partições, que funcionam como dispositivos de bloco individuais. Você deve se lembrar de exemplos como /dev/sda1 e /dev/sda2. Aqui, /dev/sda representa o disco inteiro, enquanto /dev/sda1 é a primeira partição nesse disco. As partições são incrivelmente úteis para separar dados. Se você precisar de um sistema de arquivos específico para uma parte do seu armazenamento, poderá criar uma nova partição para ele em vez de formatar o disco inteiro.

### A Tabela de Partição

Então, qual componente de um disco informa ao SO como o disco está particionado? A resposta é a **tabela de partição**. Este componente crucial contém informações sobre como as partições do disco rígido são organizadas. A tabela de partição especifica onde cada partição começa e termina, quais partições são inicializáveis e quais setores do disco são alocados a cada partição. Existem dois esquemas principais de tabela de partição: Master Boot Record (MBR) e GUID Partition Table (GPT).

### Entendendo as Partições Linux

Os discos são compostos por partições que nos ajudam a organizar nossos dados. Você pode ter várias partições em um único disco, mas elas não podem se sobrepor. Qualquer espaço no disco não alocado a uma partição é conhecido como espaço livre. Os tipos de partições Linux disponíveis dependem do esquema de tabela de partição que você usa. Dentro de uma partição, você pode criar um sistema de arquivos ou dedicá-la a outros fins, como espaço de troca (swap).

### Partições MBR

A Master Boot Record (MBR) é o padrão tradicional de tabela de partição.

- Ela suporta partições primárias, estendidas e lógicas.
- O MBR tem um limite de quatro partições primárias.
- Para criar mais partições, uma partição primária deve ser designada como uma partição estendida (apenas uma é permitida por disco). Dentro desta partição estendida, você pode criar várias partições lógicas, que funcionam como qualquer outra partição.
- Ela suporta discos de até 2 terabytes de tamanho.

### Partições GPT

A GUID Partition Table (GPT) é o padrão moderno para particionamento de disco.

- Ela tem apenas um tipo de partição, e você pode criar um grande número delas.
- Cada partição recebe um Identificador Globalmente Único (GUID).
- O GPT é comumente usado com sistemas de inicialização baseados em UEFI.

### Estrutura do Sistema de Arquivos

Como aprendemos anteriormente, um sistema de arquivos é uma coleção organizada de arquivos e diretórios. Em sua essência, ele consiste em um banco de dados para gerenciar arquivos e nos próprios arquivos. Vamos explorar sua estrutura em mais detalhes.

- **Bloco de inicialização (Boot block)**: Localizado nos primeiros setores de um sistema de arquivos, este bloco não é usado pelo sistema de arquivos em si. Em vez disso, ele contém informações usadas para inicializar o sistema operacional. Apenas um bloco de inicialização é necessário por SO. Embora outras partições possam ter blocos de inicialização, eles geralmente ficam sem uso.
- **Superbloco (Superblock)**: Este é um único bloco que segue o bloco de inicialização e contém metadados sobre o sistema de arquivos, como o tamanho da tabela de inodes, o tamanho dos blocos lógicos e o tamanho total do sistema de arquivos.
- **Tabela de inodes (Inode table)**: Este é o banco de dados que gerencia arquivos e diretórios. Cada arquivo ou diretório tem uma entrada exclusiva na tabela de inodes, que armazena vários atributos sobre ele. Abordaremos os inodes em uma lição dedicada.
- **Blocos de dados (Data blocks)**: É aqui que o conteúdo real dos seus arquivos e diretórios é armazenado.

Abaixo está um exemplo de um disco usando a tabela de partição MBR (rotulada como `msdos`). Você pode ver as partições primária, estendida e lógica.

```plaintext
pete@icebox:~$ sudo parted -l
Model: Seagate (scsi)
Disk /dev/sda: 21.5GB
Sector size (logical/physical): 512B/512B
Partition Table: msdos

Number  Start   End     Size    Type      File system     Flags
 1      1049kB  6860MB  6859MB  primary   ext4            boot
 2      6861MB  21.5GB  14.6GB  extended
 5      6861MB  7380MB  519MB   logical   linux-swap(v1)
 6      7381MB  21.5GB  14.1GB  logical   xfs
```

Este segundo exemplo mostra uma tabela de partição GPT, que usa IDs exclusivos para suas partições.

```plaintext
Model: Thumb Drive (scsi)
Disk /dev/sdb: 4041MB
Sector size (logical/physical): 512B/512B
Partition Table: gpt

Number  Start   End     Size     File system  Name        Flags
 1      17.4kB  1000MB  1000MB                first
 2      1000MB  4040MB  3040MB                second
```

## Exercise

Para reforçar sua compreensão sobre particionamento de disco e sistemas de arquivos, recomendamos este laboratório prático:

1. **[Gerenciar Partições e Sistemas de Arquivos Linux](https://labex.io/pt/labs/comptia-manage-linux-partitions-and-filesystems-590845)** - Pratique a criação de novas partições, formatando-as com sistemas de arquivos como ext4, montando-as e configurando a montagem persistente em /etc/fstab.

Este laboratório ajudará você a aplicar conceitos de gerenciamento de disco em cenários do mundo real e a ganhar confiança com o armazenamento Linux.

## Quiz Question

Qual tipo de partição é usado para criar mais de 4 partições no esquema de particionamento MBR? (Por favor, responda em uma única palavra em inglês minúscula.)

## Quiz Answer

extended
