---
lesson_id: "creating-filesystems"
course_id: "filesystem"
lang: "pt"
order_index: 5
title: "Criação de Sistemas de Arquivos"
description: "Aprenda a verificar o dispositivo de bloco de destino e criar um sistema de arquivos com ferramentas específicas do formato."
meta_title: "Criação de Sistemas de Arquivos - O Sistema de Arquivos"
meta_description: "Aprenda a criar um sistema de arquivos em uma partição Linux usando o comando mkfs. Este guia aborda gerenciamento de discos, formatação com ext4 e etapas essenciais do particionamento Linux."
meta_keywords: "mkfs, criar sistema de arquivos, ext4, particionamento Linux, tutorial Linux, Linux para iniciantes, gerenciamento de discos, formatar disco Linux"
---

Criar um sistema de arquivos grava novas estruturas de alocação e metadados em um dispositivo de bloco. Essa é uma etapa destrutiva de inicialização, não apenas uma alteração de rótulo. Use somente armazenamento descartável para praticar e mantenha um backup testado antes de formatar um dispositivo que já tenha contido dados valiosos.

## Compreensão de `mkfs`

`mkfs` normalmente é uma interface que encaminha a operação a um programa específico do sistema de arquivos, como `mkfs.ext4`, `mkfs.xfs` ou `mkfs.btrfs`. Um comando genérico possui este formato:

```bash
$ sudo mkfs -t ext4 /dev/VERIFIED-PARTITION
```

O marcador só deve ser substituído após a verificação. A sintaxe equivalente específica do formato normalmente é:

```bash
$ sudo mkfs.ext4 /dev/VERIFIED-PARTITION
```

As opções compatíveis, os padrões, os conjuntos de recursos e as solicitações de confirmação de sobrescrita diferem entre as implementações. Leia o manual local do formatador exato, em vez de presumir que todos os backends de `mkfs` se comportem da mesma forma.

:::single-choice{#creating-filesystems-mkfs-role} O que `mkfs -t ext4 TARGET` solicita?

::option[A montagem de um sistema de arquivos existente sem alterá-lo.]{#creating-filesystems-mount-existing explanation="A montagem é uma operação separada; mkfs inicializa os metadados no dispositivo."}
::option[A criação de estruturas do sistema de arquivos ext4 no destino.]{#creating-filesystems-create-ext4 .correct explanation="A interface seleciona a implementação de formatação ext4 para o dispositivo de bloco especificado."}
::option[Uma listagem de todos os sistemas de arquivos atualmente montados.]{#creating-filesystems-list-mounted explanation="O inventário de montagens somente para leitura é realizado por ferramentas como `findmnt`."}
:::

## Verificação de Todas as Camadas de Armazenamento

Antes de formatar, identifique o destino por modelo, número de série, tamanho, topologia, link persistente e função pretendida:

```bash
$ lsblk -o NAME,PATH,TYPE,SIZE,MODEL,SERIAL,FSTYPE,UUID,MOUNTPOINTS
$ findmnt --real
$ sudo wipefs --no-act /dev/VERIFIED-PARTITION
```

`wipefs --no-act` informa as assinaturas reconhecidas sem apagá-las. Verifique também o uso por swap, LVM, RAID, criptografia, máquinas virtuais, contêineres e aplicações. Um dispositivo pode estar ativo mesmo que `MOUNTPOINTS` esteja vazio.

Desmonte ou desative todas as camadas relevantes por meio de suas próprias ferramentas. Verifique novamente a identidade imediatamente antes de executar o formatador, pois os nomes de enumeração podem mudar.

:::single-choice{#creating-filesystems-wipefs-no-act} O que `wipefs --no-act TARGET` fornece nesse fluxo de trabalho?

::option[Um relatório somente para leitura das assinaturas reconhecidas.]{#creating-filesystems-signature-report .correct explanation="O modo no-act ajuda a revelar assinaturas existentes de sistemas de arquivos, tabelas de partições, RAID ou outras sem removê-las."}
::option[Um novo sistema de arquivos vazio e pronto para montagem.]{#creating-filesystems-wipefs-formats explanation="A inspeção das assinaturas não inicializa um novo sistema de arquivos."}
::option[Uma garantia de que nenhum processo esteja usando o destino.]{#creating-filesystems-wipefs-no-users explanation="O uso deve ser verificado separadamente nas montagens e em toda a pilha de armazenamento."}
:::

## Seleção Deliberada do Sistema de Arquivos

Escolha um tipo compatível com a distribuição, o ambiente de boot, as ferramentas de backup, as ferramentas de reparo e a carga de trabalho. Considere os limites necessários, snapshots, checksums, cotas, camadas de criptografia, comportamento de expansão ou redução e acesso entre plataformas.

Não selecione um formato apenas por ser popular. Por exemplo, ext4, XFS e Btrfs possuem diferentes recursos operacionais e procedimentos de recuperação. Um dispositivo removível destinado à interoperabilidade pode exigir outro formato, com semânticas diferentes para permissões Unix.

:::single-choice{#creating-filesystems-type-choice} Qual é uma base adequada para selecionar o tipo de sistema de arquivos?

::option[O nome mais curto de digitar.]{#creating-filesystems-shortest-name explanation="O tamanho do comando não indica nada sobre durabilidade, recursos ou suporte."}
::option[A promessa de que nenhuma falha futura de armazenamento ocorrerá.]{#creating-filesystems-no-failure explanation="Nenhum sistema de arquivos elimina falhas de hardware nem a necessidade de backups."}
::option[As necessidades da carga de trabalho junto com ferramentas compatíveis de backup, boot e recuperação.]{#creating-filesystems-supported-workflow .correct explanation="O formato deve atender aos requisitos técnicos e à capacidade do ambiente de operá-lo e recuperá-lo."}
:::

## Rótulos, UUIDs e Verificação

Os formatadores normalmente geram um UUID de sistema de arquivos e muitas vezes podem definir um rótulo legível. Use rótulos suficientemente exclusivos para o ambiente e garanta que sistemas de arquivos clonados não mantenham identificadores conflitantes quando forem montados juntos.

Após a criação bem-sucedida, inspecione sem montar:

```bash
$ lsblk -f /dev/VERIFIED-PARTITION
$ sudo blkid /dev/VERIFIED-PARTITION
```

Registre o UUID para a configuração posterior da montagem. Criar um sistema de arquivos não o monta, não cria diretórios de aplicações, não restaura backups nem o torna persistente após a inicialização.

:::single-choice{#creating-filesystems-after-mkfs} O que continua sendo uma etapa separada após a criação de um sistema de arquivos?

::option[Montá-lo em um diretório pretendido.]{#creating-filesystems-mount-separate .correct explanation="A formatação grava as estruturas do sistema de arquivos, enquanto a montagem o associa à árvore visível de diretórios."}
::option[Atribuir qualquer capacidade ao dispositivo de bloco.]{#creating-filesystems-capacity explanation="A partição ou o dispositivo lógico subjacente já fornece a capacidade que está sendo formatada."}
::option[Criar o diretório `/dev` do kernel desde o início.]{#creating-filesystems-create-dev explanation="O gerenciamento de nós de dispositivos é independente da formatação de um destino."}
:::

Use o laboratório [Gerenciamento de Partições e Sistemas de Arquivos Linux](https://labex.io/labs/comptia-manage-linux-partitions-and-filesystems-590845) somente no disco secundário descartável do laboratório.

## Resumo

Agora você sabe descrever a criação de sistemas de arquivos como uma operação destrutiva verificada.

1. Trate `mkfs` como uma interface para ferramentas específicas do formato.
2. Verifique a identidade persistente, as assinaturas e todos os consumidores ativos.
3. Selecione um sistema de arquivos usando requisitos de suporte e recuperação.
4. Inspecione o tipo, o rótulo e o UUID gerados antes da montagem.
