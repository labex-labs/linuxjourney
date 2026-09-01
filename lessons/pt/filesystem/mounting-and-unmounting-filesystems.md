---
lesson_id: "mounting-and-unmounting-filesystems"
course_id: "filesystem"
lang: "pt"
order_index: 6
title: "mount e umount"
description: "Aprenda a anexar, inspecionar e desanexar sistemas de arquivos com segurança usando origens e pontos de montagem verificados."
meta_title: "mount e umount - O Sistema de Arquivos"
meta_description: "Aprenda a usar os comandos mount e umount no Linux para anexar e desanexar sistemas de arquivos. Este guia aborda montagem de dispositivos, desmontagem segura e uso de UUIDs."
meta_keywords: "mount, umount, sudo umount, umount Linux, desmontar Linux, Debian umount, montar sistema de arquivos, desmontar dispositivo, UUID Linux, ponto de montagem"
---

A montagem anexa um sistema de arquivos a um diretório no namespace visível. A origem pode ser um dispositivo de bloco, uma exportação de rede, um sistema de arquivos virtual, uma origem de bind ou outro objeto específico da implementação. O diretório de destino é chamado de ponto de montagem.

## Preparação e Inspeção de um Ponto de Montagem

Crie um diretório com um nome deliberado quando a política local exigir:

```bash
$ sudo mkdir -p /mnt/mydrive
```

Inspecione-o antes da montagem:

```bash
$ findmnt --target /mnt/mydrive
$ sudo ls -la /mnt/mydrive
```

Montar sobre um diretório não vazio oculta suas entradas existentes atrás do novo sistema de arquivos até a desmontagem; isso não as exclui. Esse comportamento pode confundir aplicações e consumir espaço em disco de forma invisível, portanto use um ponto de montagem vazio e dedicado.

:::single-choice{#mount-umount-nonempty-target} O que acontece com os arquivos existentes em um diretório quando outro sistema de arquivos é montado nele?

::option[Eles são copiados automaticamente para o novo sistema de arquivos.]{#mount-umount-copied-files explanation="A montagem altera a associação no namespace e não migra o conteúdo do diretório."}
::option[Eles são apagados permanentemente pelo kernel.]{#mount-umount-erased-files explanation="Os arquivos normalmente reaparecem após a desmontagem, pois foram ocultados, não excluídos."}
::option[Eles ficam ocultos pela montagem até que ela seja desfeita.]{#mount-umount-hidden-files .correct explanation="O diretório subjacente permanece, mas a resolução dos caminhos passa para o sistema de arquivos montado."}
:::

## Montagem de um Sistema de Arquivos Verificado

Após confirmar a identidade da origem, o tipo detectado e o conteúdo esperado, monte explicitamente:

```bash
$ sudo mount -t ext4 /dev/VERIFIED-PARTITION /mnt/mydrive
```

A opção `-t` especifica a implementação do sistema de arquivos. Mount muitas vezes consegue detectar o tipo, mas um tipo explícito e opções revisadas tornam a intenção mais clara. Para conteúdo não confiável ou removível, considere opções restritivas como `ro`, `nosuid`, `nodev` e `noexec` quando forem adequadas à carga de trabalho; cada uma possui limitações e não deve ser tratada como uma sandbox completa.

Verifique o que realmente foi montado:

```bash
$ findmnt --target /mnt/mydrive -o TARGET,SOURCE,FSTYPE,OPTIONS
```

As montagens são específicas do namespace. Uma montagem criada em um contêiner ou namespace privado de serviço pode não aparecer na visão de outro processo.

:::single-choice{#mount-umount-mount-role} O que o comando `mount` faz no fluxo mostrado?

::option[Cria um novo sistema de arquivos e apaga a origem.]{#mount-umount-format-source explanation="A criação do sistema de arquivos é uma operação destrutiva separada realizada por `mkfs`."}
::option[Anexa uma origem de sistema de arquivos a um diretório em um namespace de montagem.]{#mount-umount-attach-filesystem .correct explanation="A resolução dos caminhos abaixo do destino passa então para o sistema de arquivos anexado."}
::option[Altera os limites das partições do disco.]{#mount-umount-change-partitions explanation="A edição da tabela de partições é separada da montagem no namespace."}
:::

## Uso de UUIDs de Sistemas de Arquivos

Nomes de enumeração como `/dev/sdb2` podem mudar. Descubra os identificadores dos sistemas de arquivos com:

```bash
$ lsblk -f
$ sudo blkid
```

Depois, monte um sistema de arquivos verificado pelo UUID:

```bash
$ sudo mount UUID=130b882f-7d79-436d-a096-1e594c92bb76 /mnt/mydrive
```

Um UUID identifica o sistema de arquivos, não necessariamente o disco físico. A reformatação o altera, enquanto a clonagem pode duplicá-lo. Verifique a exclusividade antes de anexar o original e o clone ao mesmo sistema.

:::single-choice{#mount-umount-uuid-benefit} Por que um UUID de sistema de arquivos costuma ser preferível a `/dev/sdX` em configurações persistentes?

::option[Ele impede que qualquer dispositivo de armazenamento apresente falhas.]{#mount-umount-uuid-no-failure explanation="Um identificador não fornece redundância, reparo de integridade nem backup."}
::option[Ele garante que sistemas de arquivos clonados possuam identificadores diferentes.]{#mount-umount-uuid-clone-unique explanation="Um clone no nível dos blocos pode copiar o UUID e criar uma colisão."}
::option[Ele está vinculado à identidade do sistema de arquivos, não à ordem atual de enumeração.]{#mount-umount-uuid-identity .correct explanation="O caminho do dispositivo de bloco pode mudar enquanto os metadados do sistema de arquivos mantêm seu UUID."}
:::

## Desmontagem Segura

Desanexe pelo ponto de montagem exato:

```bash
$ sudo umount /mnt/mydrive
```

O comando se chama `umount`, sem o primeiro `n`. Uma desmontagem bem-sucedida desanexa o sistema de arquivos depois que o kernel conclui as gravações necessárias e as referências permitem a operação. Confirme depois com `findmnt` antes de desconectar o armazenamento.

Uma desmontagem bem-sucedida nem sempre é a última operação necessária para remover uma mídia com segurança. As pilhas de armazenamento dos ambientes gráficos podem oferecer uma ação de ejeção ou desligamento que sincroniza os caches do dispositivo e desabilita um dispositivo USB. Siga o fluxo da plataforma e do hardware.

:::single-choice{#mount-umount-command-name} Qual comando desanexa `/mnt/mydrive`?

::option[`umount /mnt/mydrive`]{#mount-umount-umount-correct .correct explanation="`umount` desanexa o sistema de arquivos montado no destino especificado."}
::option[`unmount /mnt/mydrive`]{#mount-umount-unmount-spelling explanation="O nome do comando padrão omite o primeiro `n`."}
::option[`mkfs /mnt/mydrive`]{#mount-umount-mkfs-target explanation="Mkfs cria estruturas de sistemas de arquivos e nunca deve ser usado para desanexá-los."}
:::

## Diagnóstico de um Sistema de Arquivos Ocupado

A desmontagem falha quando o namespace ainda possui referências ativas, como arquivos abertos, um diretório de trabalho de processo, montagens aninhadas, swap ou outras camadas de armazenamento. Investigue em vez de forçar a operação imediatamente:

```bash
$ findmnt --submounts /mnt/mydrive
$ sudo fuser -vm /mnt/mydrive
```

Mova os shells para fora da árvore, encerre de forma limpa a aplicação responsável e desmonte os filhos antes do pai. As opções de desmontagem preguiçosa e forçada possuem semânticas especializadas e podem deixar referências ativas ou causar perda de dados; use-as apenas com uma justificativa de recuperação documentada.

:::single-choice{#mount-umount-busy-cause} Qual condição pode fazer `umount` informar que um sistema de arquivos está ocupado?

::option[O nome do diretório do ponto de montagem contém letras minúsculas.]{#mount-umount-lowercase explanation="O uso de maiúsculas ou minúsculas no caminho não cria por si só uma referência ativa ao sistema de arquivos."}
::option[Um processo possui seu diretório de trabalho atual dentro da montagem.]{#mount-umount-cwd-busy .correct explanation="O processo mantém uma referência no sistema de arquivos montado, impedindo o desanexo comum."}
::option[O UUID do sistema de arquivos é maior que o nome do dispositivo.]{#mount-umount-uuid-length explanation="O comprimento do identificador não tem relação com as verificações de estado ocupado."}
:::

Use o laboratório [Gerenciamento de Partições e Sistemas de Arquivos Linux](https://labex.io/labs/comptia-manage-linux-partitions-and-filesystems-590845) para praticar no armazenamento descartável designado.

## Resumo

Agora você sabe anexar e desanexar sistemas de arquivos com um escopo verificável.

1. Use um ponto de montagem vazio e dedicado.
2. Verifique a origem, o tipo, as opções e a montagem resultante.
3. Prefira um identificador exclusivo do sistema de arquivos para referências persistentes.
4. Desmonte pelo destino e confirme o desanexo antes da remoção.
5. Diagnostique referências ativas em vez de forçar a desmontagem de um sistema ocupado.
