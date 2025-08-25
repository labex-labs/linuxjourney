---
index: 4
lang: "pt"
title: "Particionamento de Disco"
meta_title: "Particionamento de Disco - O Sistema de Arquivos"
meta_description: "Aprenda particionamento de disco no Linux usando parted. Entenda como particionar, selecionar, visualizar e redimensionar discos. Comece com este guia para iniciantes!"
meta_keywords: "particionamento de disco Linux, comando parted, fdisk, gparted, tutorial Linux, Linux para iniciantes, gerenciamento de disco, guia Linux"
---

## Lesson Content

Vamos fazer algumas coisas práticas com sistemas de arquivos, trabalhando o processo em uma unidade USB. Se você não tiver uma, não se preocupe, você ainda pode acompanhar as próximas lições.

Primeiro, precisaremos particionar nosso disco. Existem muitas ferramentas disponíveis para fazer isso:

- fdisk - ferramenta básica de particionamento de linha de comando; não suporta GPT
- parted - esta é uma ferramenta de linha de comando que suporta particionamento MBR e GPT
- gparted - esta é a versão GUI do parted
- gdisk - fdisk, mas não suporta MBR, apenas GPT

Vamos usar o parted para fazer nosso particionamento. Digamos que eu conecte o dispositivo USB e vejamos que o nome do dispositivo é /dev/sdb2.

### Iniciar parted

```bash
sudo parted
```

Você entrará na ferramenta parted; aqui você pode executar comandos para particionar seu dispositivo.

### Selecionar o dispositivo

```bash
select /dev/sdb2
```

Para selecionar o dispositivo com o qual você trabalhará, selecione-o pelo nome do dispositivo.

### Visualizar tabela de partição atual

```plaintext
(parted) print
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

Aqui você verá as partições disponíveis no dispositivo. Os pontos de **início** e **fim** são onde as partições ocupam espaço no disco rígido; você vai querer encontrar um bom local de início e fim para suas partições.

### Particionar o dispositivo

```bash
mkpart primary 123 4567
```

Agora, basta escolher um ponto de início e fim e criar a partição; você precisará especificar o tipo de partição dependendo da tabela que você usou.

### Redimensionar uma partição

Você também pode redimensionar uma partição se não tiver espaço.

```bash
resize 2 1245 3456
```

Selecione o número da partição e, em seguida, os pontos de início e fim para onde você deseja redimensioná-la.

Parted é uma ferramenta muito poderosa, e você deve ter cuidado ao particionar seus discos.

## Exercise

Prática leva à perfeição! Aqui estão alguns laboratórios práticos para reforçar sua compreensão sobre particionamento de disco e gerenciamento de sistemas de arquivos no Linux:

1. [Gerenciar Partições e Sistemas de Arquivos Linux](https://labex.io/pt/labs/comptia-manage-linux-partitions-and-filesystems-590845) - Neste laboratório, você aprenderá a gerenciar partições de disco e sistemas de arquivos no Linux. Você usará o fdisk para criar uma nova partição, formatá-la com ext4, montá-la, configurar a montagem persistente em /etc/fstab e criar uma partição swap, tudo em um disco virtual secundário seguro.

Este laboratório o ajudará a aplicar os conceitos de particionamento de disco e gerenciamento de sistemas de arquivos em um cenário real e a construir confiança com essas habilidades essenciais de administração Linux.

## Quiz Question

Qual é o comando parted para criar uma partição?

## Quiz Answer

mkpart
