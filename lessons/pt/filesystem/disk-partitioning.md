---
lesson_id: "disk-partitioning"
course_id: "filesystem"
lang: "pt"
order_index: 4
title: "Particionamento de Disco"
description: "Aprenda um fluxo baseado em verificação para inspecionar, criar e redimensionar limites de partições com `parted`."
meta_title: "Particionamento de Disco - O Sistema de Arquivos"
meta_description: "Aprenda a particionar discos no Linux com o comando parted. Este guia aborda como visualizar partições com `sudo parted -l`, criá-las e redimensioná-las, além de apresentar o GParted."
meta_keywords: "particionamento de disco Linux, comando parted, sudo parted -l, GParted, fdisk, gerenciamento de discos, criar partição, redimensionar partição, guia Linux"
---

A edição de partições altera o mapa que define os limites do armazenamento. Um dispositivo, início ou fim incorreto pode tornar dados existentes inacessíveis ou sobrescrever metadados essenciais. Pratique somente em um disco virtual descartável e mantenha um backup separado e testado antes de modificar um armazenamento valioso.

## Escolha de uma Ferramenta

Algumas ferramentas comuns são:

- `fdisk`, um editor de partições para terminal do util-linux compatível com MBR e GPT
- `parted`, um editor para terminal e scripts compatível com GPT, MBR e outros formatos de tabela
- `gdisk`, um editor interativo voltado ao GPT
- GParted, uma interface gráfica para partições e sistemas de arquivos

O suporte das ferramentas evolui, portanto use o manual local e a documentação da distribuição. Uma interface gráfica não torna seguras as operações destrutivas; ela ainda altera os mesmos metadados do disco.

:::single-choice{#disk-partitioning-fdisk-gpt} Qual afirmação sobre o `fdisk` atual do Linux está correta?

::option[Ele oferece suporte a tabelas de partições MBR e GPT.]{#disk-partitioning-fdisk-supports-gpt .correct explanation="O fdisk atual do util-linux pode editar layouts DOS/MBR e GPT, entre outros."}
::option[Ele pode editar somente GPT e nunca MBR.]{#disk-partitioning-fdisk-only-gpt explanation="O `gdisk`, voltado ao GPT, corresponde melhor a essa descrição; o fdisk oferece suporte a vários tipos de rótulos."}
::option[Ele cria sistemas de arquivos, mas não pode editar entradas de partições.]{#disk-partitioning-fdisk-filesystem-only explanation="Sua finalidade central é visualizar e editar tabelas de partições."}
:::

## Identificação e Inativação do Destino

Comece com um inventário somente para leitura:

```bash
$ lsblk -o NAME,PATH,TYPE,SIZE,MODEL,SERIAL,TRAN,PTTYPE,FSTYPE,MOUNTPOINTS
$ findmnt --real
$ sudo parted --list
```

Confirme o dispositivo inteiro por sua identidade persistente, modelo, número de série, tamanho, transporte e topologia — não apenas por `/dev/sdX`. Em seguida, identifique todos os consumidores: sistemas de arquivos montados, swap, LVM, RAID, criptografia, contêineres, máquinas virtuais, bancos de dados e descritores de arquivos abertos.

Desmonte ou desative todas as camadas relevantes de acordo com seus procedimentos documentados. Não edite a tabela de partições do disco do sistema em execução apenas porque a ferramenta abre com sucesso. Registre a tabela existente em um formato restaurável e confirme que seu backup esteja em outro domínio de falha.

:::single-choice{#disk-partitioning-target-identity} Por que um nome de dispositivo como `/dev/sdb` é insuficiente como única verificação do destino?

::option[O Linux nunca expõe discos inteiros em `/dev`.]{#disk-partitioning-no-whole-disks explanation="Discos inteiros normalmente possuem nós de bloco em `/dev`."}
::option[Os nomes de enumeração podem mudar quando os dispositivos ou a topologia são alterados.]{#disk-partitioning-enumeration-changes .correct explanation="Uma letra é atribuída pela ordem de descoberta e pode indicar outro disco em uma sessão posterior."}
::option[As ferramentas de partições aceitam apenas UUIDs de sistemas de arquivos como operandos.]{#disk-partitioning-only-uuid explanation="Os editores normalmente atuam sobre o caminho de um dispositivo de bloco inteiro após a verificação da identidade."}
:::

## Inspeção de um Dispositivo no `parted`

Abra o dispositivo inteiro verificado explicitamente:

```bash
$ sudo parted /dev/VERIFIED-DISK
```

Depois, selecione unidades de exibição consistentes e mostre a tabela:

```text
(parted) unit MiB
(parted) print free
```

`print free` mostra as entradas atuais e as regiões não alocadas. Os comandos do Parted podem atualizar imediatamente os metadados do disco, sem aguardar uma operação final de “salvar”, portanto trate o prompt interativo como um acesso de escrita ativo.

:::single-choice{#disk-partitioning-print-free} O que `print free` ajuda a exibir no `parted`?

::option[Arquivos que podem ser excluídos para reduzir qualquer sistema de arquivos com segurança.]{#disk-partitioning-free-files explanation="O Parted lê o layout das partições, não a alocação de arquivos dentro do sistema de arquivos."}
::option[Todos os backups armazenados em sistemas remotos.]{#disk-partitioning-remote-backups explanation="O inventário de backups remotos não faz parte do escopo de um editor de partições."}
::option[As entradas de partições existentes e as regiões não alocadas.]{#disk-partitioning-free-regions .correct explanation="Essa visualização ajuda a escolher limites com base na tabela atual e nos espaços restantes."}
:::

## Criação de uma Entrada de Partição

A sintaxe exata de `mkpart` depende do tipo da tabela. Um exemplo de GPT em unidades MiB se parece com este:

```text
(parted) mkpart data ext4 1MiB 5000MiB
```

Esse comando cria uma entrada de partição com um nome, um tipo de conteúdo sugerido, início e fim. Ele **não** cria um sistema de arquivos ext4. A formatação é uma etapa destrutiva separada, realizada somente depois que o kernel reconhece a nova partição pretendida e sua identidade é verificada.

Use o alinhamento recomendado pela ferramenta e entenda se os pontos finais são inclusivos e como são arredondados. Inspecione o resultado com `print` e `lsblk`; não presuma que um limite decimal solicitado foi registrado exatamente.

:::single-choice{#disk-partitioning-mkpart-effect} O que o comando `mkpart` do `parted` cria?

::option[Um sistema de arquivos ext4 montado que contém um diretório pessoal.]{#disk-partitioning-mounted-filesystem explanation="A formatação e a montagem são operações separadas posteriores à criação da partição."}
::option[Um backup completo do conteúdo anterior da partição.]{#disk-partitioning-automatic-backup explanation="Editores de partições não criam automaticamente um backup de recuperação."}
::option[Uma entrada na tabela de partições, sem formatar um sistema de arquivos.]{#disk-partitioning-entry-only .correct explanation="O argumento do tipo de sistema de arquivos influencia os metadados da partição, mas não executa `mkfs`."}
:::

## Redimensionamento de Limites e Conteúdo

`resizepart NUMBER END` move somente o limite final de uma partição. Ele não redimensiona o sistema de arquivos nem outra estrutura armazenada nela.

A ordem é essencial:

- Para expandir, aumente primeiro a partição ou o dispositivo lógico que funciona como contêiner e depois expanda o sistema de arquivos com sua ferramenta compatível.
- Para reduzir, confirme que o sistema de arquivos permite redução, diminua-o primeiro respeitando seus requisitos de funcionamento online ou offline e só então reduza o limite do contêiner sem cruzar o novo fim.

Alguns sistemas de arquivos não podem ser reduzidos. Criptografia, LVM, RAID e layouts aninhados acrescentam mais camadas ordenadas. O kernel também pode se recusar a reler uma tabela alterada enquanto os dispositivos estão ocupados, exigindo uma reinicialização controlada antes que o novo layout possa ser usado.

:::single-choice{#disk-partitioning-shrink-order} Quando um sistema de arquivos permite redução, qual ordem evita cortar dados ativos?

::option[Reduzir primeiro a partição e depois descobrir se o sistema de arquivos cabe.]{#disk-partitioning-shrink-partition-first explanation="Encurtar primeiro o contêiner pode truncar estruturas e dados do sistema de arquivos."}
::option[Reduzir primeiro o sistema de arquivos e depois diminuir o limite da partição que o contém.]{#disk-partitioning-shrink-filesystem-first .correct explanation="O conteúdo deve caber no intervalo menor antes que o dispositivo de bloco externo seja encurtado."}
::option[Excluir a tabela de partições e deixar o sistema de arquivos recriá-la.]{#disk-partitioning-delete-table explanation="Um sistema de arquivos não reconstrói uma tabela de partições segura como parte da redução normal."}
:::

Use o laboratório [Gerenciamento de Partições e Sistemas de Arquivos Linux](https://labex.io/labs/comptia-manage-linux-partitions-and-filesystems-590845) em seu disco virtual secundário designado; não o substitua por um disco do host.

## Resumo

Agora você sabe descrever a edição de partições como uma operação destrutiva em camadas de armazenamento.

1. Selecione uma ferramenta compatível com a tabela e o fluxo de trabalho reais.
2. Verifique a identidade persistente do disco e desative todos os consumidores.
3. Inspecione unidades, entradas e regiões livres antes de gravar.
4. Lembre-se de que `mkpart` não cria um sistema de arquivos.
5. Redimensione o conteúdo interno e os limites externos na ordem segura.
