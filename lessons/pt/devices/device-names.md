---
lesson_id: "device-names"
course_id: "devices"
lang: "pt"
order_index: 3
title: "Nomes de Dispositivos"
description: "Aprenda como o Linux nomeia dispositivos de armazenamento, partições, dispositivos lógicos e links persistentes comuns."
meta_title: "Nomes de Dispositivos - Dispositivos"
meta_description: "Conheça os nomes comuns de dispositivos Linux para armazenamento e periféricos. Este guia explica a convenção dos discos SCSI, como sda, e pseudodispositivos como /dev/null."
meta_keywords: "nomes de dispositivos Linux, nome de dispositivo Linux, significado de sda, primeira partição segundo disco SCSI, /dev, dispositivos SCSI, pseudodispositivos, dispositivos PATA"
---

Os nomes de dispositivos Linux refletem o subsistema e o driver do kernel que apresentam uma interface, nem sempre o conector físico indicado no hardware. Aprenda os padrões comuns, mas descubra o mapeamento real do sistema atual antes de alterar o armazenamento.

## Nomes de Discos da Camada SCSI

Os discos apresentados pela camada de discos SCSI normalmente usam nomes `sd`. Isso inclui muitos discos SCSI, SATA, de armazenamento USB e virtuais:

- `/dev/sda`: um disco inteiro
- `/dev/sdb`: outro disco inteiro
- `/dev/sda3`: partição 3 de `/dev/sda`
- `/dev/sdb1`: partição 1 de `/dev/sdb`

As letras refletem a enumeração, não uma identidade permanente. Adicionar um controlador, alterar a ordem do firmware ou conectar um dispositivo pode mudar qual disco recebe determinada letra.

:::single-choice{#device-names-sdb-first-partition}
No padrão de nomes `sd`, qual caminho indica a partição 1 de `/dev/sdb`?

::option[`/dev/sda2`]{#device-names-sda-two explanation="Esse caminho indica a partição 2 do disco atualmente chamado `/dev/sda`."}
::option[`/dev/sdbp1`]{#device-names-sdb-p-one explanation="O separador `p` é usado em padrões cujo nome base já termina em um dígito, não em nomes `sd` comuns."}
::option[`/dev/sdb1`]{#device-names-sdb-one .correct explanation="Para discos `sd`, o número da partição é acrescentado diretamente ao nome do disco inteiro."}
:::

## Nomes que Terminam em Dígitos

Alguns nomes de dispositivos inteiros já contêm dígitos, portanto os nomes de suas partições usam `p` como separador:

- `/dev/nvme0n1`: namespace NVMe 1 no controlador 0
- `/dev/nvme0n1p2`: partição 2 desse namespace
- `/dev/mmcblk0`: um dispositivo de bloco MMC
- `/dev/mmcblk0p1`: partição 1 desse dispositivo

Os dispositivos NVMe normalmente não são chamados `/dev/sdX`; eles usam a convenção de nomes do subsistema NVMe.

:::single-choice{#device-names-nvme-partition}
Qual caminho indica a partição 2 de `/dev/nvme0n1`?

::option[`/dev/nvme0n1p2`]{#device-names-nvme-p-two .correct explanation="Os nomes de partições NVMe inserem `p` antes do número da partição."}
::option[`/dev/nvme0n12`]{#device-names-nvme-no-p explanation="Sem um separador, os dígitos finais seriam ambíguos em relação ao número do namespace."}
::option[`/dev/sda2`]{#device-names-nvme-sda explanation="Essa é uma partição de disco da camada `sd` e não nomeia o namespace NVMe especificado."}
:::

## Dispositivos de Bloco Lógicos e Virtuais

O Linux também cria dispositivos de bloco que não correspondem individualmente a um disco físico:

- `/dev/dm-N` para dispositivos do device mapper, muitas vezes acompanhados de links descritivos em `/dev/mapper/`
- `/dev/mdN` para arranjos RAID de software do Linux
- `/dev/loopN` para arquivos comuns associados como dispositivos de bloco loop

Partições, camadas de criptografia, RAID, volumes lógicos e sistemas de arquivos formam uma pilha. Use ferramentas como `lsblk` para visualizar as relações entre pais e filhos, em vez de deduzir a pilha apenas pelo nome.

:::single-choice{#device-names-device-mapper-link}
Qual local normalmente fornece links descritivos para dispositivos do device mapper?

::option[`/dev/mapper/`]{#device-names-mapper-directory .correct explanation="Aplicações do device mapper, como LVM e criptografia de disco, normalmente expõem links nomeados nesse diretório."}
::option[`/dev/null/`]{#device-names-null-directory explanation="`/dev/null` é um dispositivo de caractere, não um diretório de dispositivos de bloco mapeados."}
::option[`/proc/partitions/mapper/`]{#device-names-proc-mapper explanation="Esse não é o caminho normal dos links de nomes do device mapper."}
:::

## Links Persistentes de Armazenamento

O gerenciamento de dispositivos no espaço do usuário cria links em `/dev/disk/`, normalmente agrupados como:

- `by-id` para identificadores de hardware ou transporte
- `by-uuid` para UUIDs de sistemas de arquivos
- `by-label` para rótulos de sistemas de arquivos
- `by-partuuid` para UUIDs de tabelas de partições
- `by-path` para caminhos dependentes da topologia

Escolha um identificador que corresponda ao que precisa permanecer estável. O UUID de um sistema de arquivos identifica o sistema de arquivos, não necessariamente o disco físico abaixo dele. Clonar um sistema de arquivos pode duplicar seu UUID, portanto verifique a exclusividade antes de depender dele.

:::single-choice{#device-names-persistent-config}
Por que links em `/dev/disk/by-id/` muitas vezes são preferíveis a `/dev/sdX` em configurações específicas de dispositivos?

::option[Eles tornam gravações destrutivas automaticamente reversíveis.]{#device-names-by-id-reversible explanation="Um nome estável não fornece snapshots, backups nem proteção contra gravação."}
::option[Eles convertem um dispositivo de bloco em um arquivo comum.]{#device-names-by-id-regular explanation="A entrada é um link simbólico que ainda aponta para um nó de dispositivo de bloco."}
::option[Eles são derivados da identidade do dispositivo, não da ordem atual de enumeração.]{#device-names-by-id-stable .correct explanation="O destino do link pode mudar enquanto o link baseado em identidade permanece associado ao mesmo dispositivo reconhecido."}
:::

## Nomes de Pseudodispositivos

Nomes como `/dev/null`, `/dev/zero` e `/dev/urandom` descrevem pseudodispositivos do kernel, não armazenamento físico. `/dev/null` descarta gravações e retorna fim de arquivo nas leituras; `/dev/zero` fornece bytes zero; `/dev/urandom` fornece bytes do gerador de números aleatórios do kernel.

:::single-choice{#device-names-zero-read}
O que a leitura de `/dev/zero` produz?

::option[Uma lista de dispositivos de armazenamento não utilizados.]{#device-names-zero-storage-list explanation="Esse é um dispositivo de caractere que produz bytes, não um comando de descoberta."}
::option[Um fluxo de bytes com valor zero.]{#device-names-zero-bytes .correct explanation="O pseudodispositivo zero retorna bytes nulos nas leituras solicitadas."}
::option[Fim de arquivo imediato, como na leitura de `/dev/null`.]{#device-names-zero-eof explanation="`/dev/zero` continua produzindo bytes, enquanto as leituras de `/dev/null` retornam fim de arquivo."}
:::

Use o laboratório [Exploração de Dispositivos de Hardware no Linux](https://labex.io/labs/comptia-explore-hardware-devices-in-linux-590861) para comparar nomes, links persistentes e relações exibidas por `lsblk` antes de tentar trabalhar com partições.

## Resumo

Agora você sabe interpretar nomes comuns de armazenamento do Linux sem tratá-los como identidades permanentes.

1. Leia `sdXNUMBER` como uma partição de disco `sd`.
2. Use `pNUMBER` quando o nome do dispositivo inteiro já terminar em um dígito.
3. Reconheça dispositivos lógicos como device mapper, RAID e dispositivos loop.
4. Prefira links persistentes escolhidos de acordo com a identidade necessária.
5. Diferencie nomes de armazenamento de pseudodispositivos do kernel.
