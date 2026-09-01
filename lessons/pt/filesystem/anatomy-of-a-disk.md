---
lesson_id: "anatomy-of-a-disk"
course_id: "filesystem"
lang: "pt"
order_index: 3
title: "Anatomia de um Disco"
description: "Aprenda como dispositivos de bloco, tabelas de partições, partições e sistemas de arquivos formam camadas distintas de armazenamento."
meta_title: "Anatomia de um Disco - O Sistema de Arquivos"
meta_description: "Conheça a anatomia de um disco no Linux. Este guia explica como as tabelas de partições MBR e GPT informam ao sistema operacional a organização das partições e como os sistemas de arquivos se relacionam com elas."
meta_keywords: "disco no Linux, partições Linux, tipos de partições Linux, organização de partições do disco, MBR, GPT, tabela de partições, sistema de arquivos"
---

Um dispositivo de armazenamento é exposto como um dispositivo de bloco, como `/dev/sda` ou `/dev/nvme0n1`. Ele pode conter uma tabela de partições, cujas entradas descrevem regiões expostas como dispositivos de bloco filhos. Uma partição pode então conter um sistema de arquivos, uma assinatura de swap, um membro de RAID, um contêiner de criptografia, um volume físico de volumes lógicos ou outro formato de dados.

Essas camadas são independentes: nem todo disco possui uma tabela de partições, nem toda partição contém um sistema de arquivos e um sistema de arquivos pode residir em um volume lógico ou em um dispositivo inteiro.

## Tabelas de Partições e Limites

Uma tabela de partições registra posições iniciais, comprimentos, identificadores de tipos e atributos específicos do esquema. O kernel a lê para criar dispositivos de bloco de partições, como `/dev/sda1` ou `/dev/nvme0n1p1`.

Em layouts comuns, os limites das partições não devem se sobrepor. O espaço fora de todas as entradas é considerado não alocado pela tabela de partições, embora ainda possa conter assinaturas ou dados antigos. Alterar uma tabela não move automaticamente o conteúdo dos sistemas de arquivos para corresponder aos novos limites.

:::single-choice{#anatomy-disk-partition-table-role} O que informa ao sistema operacional onde as partições do disco começam e terminam?

::option[O diretório de trabalho atual do shell.]{#anatomy-disk-shell-directory explanation="Um caminho do shell não tem função nos limites das partições em disco."}
::option[A tabela de partições do disco.]{#anatomy-disk-table-boundaries .correct explanation="As entradas das partições descrevem regiões que o kernel pode expor como dispositivos de bloco filhos."}
::option[O grupo primário da conta do usuário.]{#anatomy-disk-user-group explanation="As credenciais de contas não definem a geometria nem o layout das partições do disco."}
:::

## Particionamento MBR

O esquema legado DOS/MBR armazena sua tabela principal no primeiro setor lógico. Ele possui quatro entradas principais. Uma delas pode descrever uma partição estendida, que funciona como contêiner para uma série encadeada de partições lógicas, permitindo mais de quatro regiões utilizáveis.

Com endereços de setores de 32 bits e setores lógicos de 512 bytes, o MBR alcança um limite frequentemente citado de cerca de 2 TiB. O endereçamento exato depende do tamanho do setor e do suporte das ferramentas. O MBR também não possui as cópias redundantes do cabeçalho e da tabela nem os GUIDs por partição do GPT.

:::single-choice{#anatomy-disk-mbr-more-than-four} Qual estrutura do MBR permite mais de quatro partições utilizáveis?

::option[Uma partição de journal contendo mais entradas principais.]{#anatomy-disk-mbr-journal explanation="O journaling do sistema de arquivos não tem relação com as quatro entradas da tabela MBR."}
::option[Uma partição estendida contendo partições lógicas.]{#anatomy-disk-mbr-extended .correct explanation="Uma entrada principal pode definir um contêiner estendido, dentro do qual as partições lógicas são encadeadas."}
::option[Um superbloco do sistema de arquivos que renumera as entradas.]{#anatomy-disk-mbr-superblock explanation="Os metadados de um sistema de arquivos não ampliam a tabela de partições do disco."}
:::

## Particionamento GPT

A GUID Partition Table, ou GPT, usa endereços de blocos lógicos de 64 bits e normalmente armazena um cabeçalho e uma matriz de entradas principais perto do início, além de cópias de backup perto do fim do disco. Um MBR protetor ajuda a impedir que softwares antigos compatíveis apenas com MBR tratem o disco como vazio.

Cada entrada GPT inclui um GUID de tipo de partição e um GUID exclusivo da partição; portanto, o GPT não possui apenas um tipo de partição. A quantidade de entradas disponíveis é determinada pela tabela alocada e pelas ferramentas, geralmente muito superior a quatro, sem partições estendidas ou lógicas.

O GPT normalmente é usado em discos de boot UEFI, mas o particionamento e o modo de inicialização do firmware são conceitos distintos. Um sistema UEFI também precisa dos arquivos de boot apropriados e de uma EFI System Partition; somente o GPT não torna um disco inicializável.

:::single-choice{#anatomy-disk-gpt-identifiers} Quais identificadores uma entrada de partição GPT inclui?

::option[Um GUID de tipo e um GUID exclusivo da partição.]{#anatomy-disk-gpt-guids .correct explanation="O tipo descreve o uso pretendido, enquanto o GUID exclusivo identifica aquela entrada específica de partição."}
::option[Somente um tipo universal compartilhado por todas as partições GPT.]{#anatomy-disk-gpt-one-type explanation="O GPT define muitos GUIDs de tipo para diferentes finalidades de partições."}
::option[O UID e o GID de login do usuário que a criou.]{#anatomy-disk-gpt-user-ids explanation="Os identificadores de contas do sistema de arquivos não são campos de identidade de partições GPT."}
:::

## Estruturas de Sistemas de Arquivos São Específicas do Formato

Após o particionamento, uma ferramenta de criação de sistemas de arquivos grava as estruturas definidas por aquele sistema. Muitos formatos possuem conceitos como superblocos, metadados de alocação, registros de diretórios e extensões ou blocos de dados, mas seu layout, sua redundância e sua terminologia são diferentes.

Por exemplo, os sistemas de arquivos ext usam inodes e grupos de blocos, enquanto outros sistemas organizam metadados por diferentes árvores ou estruturas de alocação. Não aplique um diagrama simplificado de “bloco de boot, um superbloco, tabela de inodes e blocos de dados” a todos os sistemas de arquivos.

:::single-choice{#anatomy-disk-filesystem-layer} Criar uma partição cria automaticamente um sistema de arquivos dentro dela?

::option[Não; formatá-la ou atribuir-lhe outro uso explícito é uma etapa separada.]{#anatomy-disk-partition-not-filesystem .correct explanation="A tabela de partições apenas define uma região de blocos; seu conteúdo permanece independente."}
::option[Sim; toda partição é formatada automaticamente como ext4.]{#anatomy-disk-auto-ext4 explanation="As ferramentas de particionamento não criam universalmente um sistema de arquivos ext4."}
::option[Sim; as entradas GPT são, por si só, diretórios montados.]{#anatomy-disk-gpt-mounted explanation="Uma entrada de partição descreve o armazenamento e não é um ponto de montagem de sistema de arquivos."}
:::

## Inspeção do Layout Atual

Use visualizações somente para leitura antes de qualquer modificação:

```bash
$ lsblk -o NAME,PATH,TYPE,SIZE,PTTYPE,PARTTYPE,FSTYPE,MOUNTPOINTS
$ sudo parted --list
```

`PTTYPE` descreve o esquema detectado da tabela de partições, `PARTTYPE` identifica um tipo de partição e `FSTYPE` informa uma assinatura de conteúdo detectada. A detecção é um indício, não uma garantia de que o conteúdo esteja íntegro ou seja seguro montá-lo.

Os nomes dos dispositivos podem mudar, e assinaturas antigas podem confundir a detecção. Confirme modelo, número de série, tamanho, transporte, links persistentes, montagens ativas, swap, RAID, LVM, criptografia e backups antes de abrir qualquer ferramenta de particionamento no modo de escrita.

:::single-choice{#anatomy-disk-lsblk-fields} Qual campo de `lsblk` diferencia o conteúdo detectado de um sistema de arquivos do esquema da tabela de partições?

::option[`FSTYPE`]{#anatomy-disk-fstype .correct explanation="`FSTYPE` informa um sistema de arquivos detectado ou outra assinatura de conteúdo reconhecida, enquanto `PTTYPE` informa o esquema da tabela."}
::option[`NAME`]{#anatomy-disk-name-field explanation="`NAME` identifica a entrada de dispositivo de bloco do kernel e não indica especificamente o formato do conteúdo."}
::option[`SIZE`]{#anatomy-disk-size-field explanation="O tamanho informa a capacidade, não o tipo do sistema de arquivos."}
:::

Use o laboratório [Gerenciamento de Partições e Sistemas de Arquivos Linux](https://labex.io/labs/comptia-manage-linux-partitions-and-filesystems-590845) somente em armazenamento descartável para praticar essas camadas.

## Resumo

Agora você sabe separar os metadados do layout do disco dos formatos de dados armazenados nele.

1. Identifique dispositivos inteiros e seus dispositivos filhos de partições.
2. Relacione as partições estendidas do MBR ao limite legado de quatro entradas.
3. Relacione o GPT a tabelas redundantes e GUIDs por partição.
4. Trate a criação do sistema de arquivos como algo separado da criação da partição.
5. Inspecione cada camada de armazenamento e consumidor ativo antes de realizar alterações.
