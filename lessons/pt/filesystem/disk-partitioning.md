---
index: 4
lang: "pt"
title: "Particionamento de Disco"
meta_title: "Particionamento de Disco - O Sistema de Arquivos"
meta_description: "Aprenda particionamento de disco Linux com o comando parted. Este guia aborda como visualizar partições com `sudo parted -l`, criá-las e redimensioná-las. Também apresenta o gparted, uma alternativa gráfica popular."
meta_keywords: "Particionamento de disco Linux, comando parted, sudo parted -l, gparted, alternativa gparted windows, fdisk, gerenciamento de disco, criar partição, redimensionar partição, guia Linux"
---

## Lesson Content

Esta lição fornece um guia prático para gerenciar sistemas de arquivos particionando um disco, como uma unidade USB. Se você não tiver uma unidade sobressalente, ainda pode acompanhar para entender os conceitos.

Primeiro, precisaremos particionar nosso disco. Existem muitas ferramentas disponíveis para esta tarefa:

- **fdisk**: Uma ferramenta básica de particionamento de linha de comando; não suporta GPT.
- **parted**: Uma poderosa ferramenta de linha de comando que suporta particionamento MBR e GPT.
- **gparted**: A versão gráfica do `parted`. Para usuários que preferem uma interface visual, `gparted` é uma ferramenta intuitiva, frequentemente considerada uma ótima `gparted windows alternative`.
- **gdisk**: Semelhante ao `fdisk`, mas suporta apenas GPT.

Usaremos o `parted` para nossos exemplos.

### Listando Partições Existentes

Antes de fazer alterações, é crucial identificar seu disco e seu layout atual. Uma maneira rápida de fazer isso é com o comando `sudo parted -l`, que lista as tabelas de partição para todos os dispositivos de bloco conectados.

```bash
sudo parted -l
```

Este comando ajuda você a encontrar o nome de dispositivo correto, como `/dev/sdb`, antes de começar a modificá-lo.

### Iniciando o Modo Interativo

Para começar a fazer alterações, inicie o `parted` no modo interativo. Vamos supor que seu dispositivo de destino seja `/dev/sdb`.

```bash
sudo parted
```

Você entrará no shell da ferramenta `parted`, onde poderá executar comandos para gerenciar as partições do seu dispositivo.

### Selecionando um Dispositivo

Uma vez dentro do shell `parted`, você deve selecionar o disco que deseja modificar. Tenha muito cuidado ao escolher o correto para evitar perda de dados.

```bash
select /dev/sdb
```

### Visualizando a Tabela de Partição

Use o comando `print` para exibir a tabela de partição do disco selecionado.

```plaintext
(parted) print
Model: ATA VBOX HARDDISK (scsi)
Disk /dev/sdb: 10.7GB
Sector size (logical/physical): 512B/512B
Partition Table: msdos
Disk Flags:

Number  Start   End     Size    Type      File system  Flags
 1      1049kB  10.7GB  10.7GB  primary   ext4         boot
```

Esta saída mostra as partições disponíveis no dispositivo. As colunas **Start** e **End** indicam onde cada partição está localizada no disco.

### Criando uma Partição

O comando `mkpart` cria uma nova partição. Você precisa especificar o tipo de partição (ex: `primary`), um tipo de sistema de arquivos opcional, e os pontos de início e fim.

```bash
mkpart primary ext4 1MB 5000MB
```

Este comando cria uma partição primária formatada com ext4, começando em 1MB e terminando em 5000MB.

### Redimensionando uma Partição

Você também pode redimensionar uma partição existente com o comando `resize`. Você precisará do número da partição e dos novos pontos de início e fim.

```bash
resize 1 1MB 8000MB
```

Este comando redimensiona a partição número 1 para terminar na marca de 8000MB.

`parted` é uma ferramenta muito poderosa. Sempre verifique duas vezes seus comandos antes de executá-los para evitar perda acidental de dados.

## Exercise

A prática leva à perfeição! Aqui estão alguns laboratórios práticos para reforçar sua compreensão de particionamento de disco Linux e gerenciamento de sistemas de arquivos:

1. [Gerenciar Partições e Sistemas de Arquivos Linux](https://labex.io/pt/labs/comptia-manage-linux-partitions-and-filesystems-590845) - Neste laboratório, você aprenderá a gerenciar partições de disco e sistemas de arquivos no Linux. Você usará o fdisk para criar uma nova partição, formatá-la com ext4, montá-la, configurar a montagem persistente em /etc/fstab e criar uma partição swap, tudo em um disco virtual secundário seguro.

Este laboratório o ajudará a aplicar os conceitos de particionamento de disco e gerenciamento de sistemas de arquivos em um cenário real e a construir confiança com essas habilidades essenciais de administração Linux.

## Quiz Question

Qual é o comando `parted` para criar uma partição? (Por favor, responda em inglês, prestando atenção à sensibilidade de maiúsculas e minúsculas).

## Quiz Answer

mkpart
