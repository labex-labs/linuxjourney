---
title: "Anatomia de um Disco"
description: "Aprenda sobre particionamento de disco Linux, MBR vs. GPT e estrutura de filesystem. Entenda partições, tabelas e como organizar dados. Comece com este guia para iniciantes!"
keywords: "particionamento de disco Linux, MBR, GPT, estrutura de filesystem, partições Linux, iniciante, tutorial, guia"
---

## Lesson Content

Discos rígidos podem ser subdivididos em partições, essencialmente criando múltiplos dispositivos de bloco. Lembre-se de exemplos como `/dev/sda1` e `/dev/sda2`. `/dev/sda` é o disco inteiro, mas `/dev/sda1` é a primeira partição nesse disco. As partições são extremamente úteis para separar dados, e se você precisar de um determinado filesystem, pode facilmente criar uma partição em vez de fazer com que o disco inteiro seja de um único tipo de filesystem.

### Partition Table

Todo disco terá uma partition table. Esta tabela informa ao sistema como o disco está particionado. Esta tabela informa onde as partições começam e terminam, quais partições são inicializáveis, quais setores do disco são alocados para qual partição, etc. Existem dois esquemas principais de partition table usados: Master Boot Record (MBR) e GUID Partition Table (GPT).

### Partition

Os discos são compostos por partições que nos ajudam a organizar nossos dados. Você pode ter várias partições em um disco, e elas não podem se sobrepor. Se houver espaço não alocado para uma partição, ele é conhecido como free space. Os tipos de partições dependem da sua partition table. Dentro de uma partição, você pode ter um filesystem ou dedicar uma partição a outras coisas como swap (chegaremos a isso em breve).

_MBR_

- Partition table tradicional, era usada como padrão
- Pode ter partições primary, extended e logical
- MBR tem um limite de quatro partições primary
- Partições adicionais podem ser criadas transformando uma partição primary em uma partição extended (pode haver apenas uma partição extended em um disco). Então, dentro da partição extended, você adiciona partições logical. As partições logical são usadas como qualquer outra partição. Estranho, eu sei.
- Suporta discos de até 2 terabytes

_GPT_

- GUID Partition Table (GPT) está se tornando o novo padrão para particionamento de disco
- Tem apenas um tipo de partição, e você pode criar muitas delas
- Cada partição tem um ID globalmente único (GUID)
- Usado principalmente em conjunto com o boot baseado em UEFI (entraremos em detalhes em outro curso)

### Filesystem Structure

Sabemos da nossa lição anterior que um filesystem é uma coleção organizada de arquivos e diretórios. Em sua forma mais simples, é composto por um banco de dados para gerenciar arquivos e os próprios arquivos; no entanto, vamos entrar em um pouco mais de detalhes.

- Boot block - Está localizado nos primeiros setores do filesystem, e não é realmente usado pelo filesystem. Em vez disso, contém informações usadas para inicializar o sistema operacional. Apenas um boot block é necessário para o sistema operacional. Se você tiver várias partições, elas terão boot blocks, mas muitos deles não são usados.
- Super block - Este é um único bloco que vem depois do boot block, e contém informações sobre o filesystem, como o tamanho da inode table, o tamanho dos logical blocks e o tamanho do filesystem.
- Inode table - Pense nisso como o banco de dados que gerencia nossos arquivos (temos uma lição inteira sobre inodes, então não se preocupe). Cada arquivo ou diretório tem uma entrada única na inode table, e ela contém várias informações sobre o arquivo.
- Data blocks - Estes são os dados reais para os arquivos e diretórios.

Vamos dar uma olhada nas diferentes partition tables. Abaixo está um exemplo de uma partição usando a partition table MBR (msdos). Você pode ver as partições primary, extended e logical na máquina.

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

Este exemplo é GPT, usando apenas um ID único para as partições.

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

Execute **parted -l** em sua máquina e avalie seus resultados.

## Quiz Question

Qual tipo de partição é usado para criar mais de 4 partições no esquema de particionamento MBR?

## Quiz Answer

extended
