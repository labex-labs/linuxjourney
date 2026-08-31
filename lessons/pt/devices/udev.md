---
lesson_id: "udev"
course_id: "devices"
lang: "pt"
order_index: 5
title: "udev"
description: "Aprenda como o udev processa eventos de dispositivos do kernel para aplicar políticas, permissões e links persistentes."
meta_title: "udev - Dispositivos"
meta_description: "Aprenda sobre o udev, como ele gerencia dinamicamente os arquivos de dispositivos Linux e como usar udevadm. Entenda a criação de nós de dispositivos."
meta_keywords: "udev, udevadm, gerenciamento de dispositivos Linux, arquivos de dispositivos, tutorial Linux, Linux para iniciantes, regras udev, guia Linux"
---

O kernel Linux informa alterações de dispositivos ao espaço do usuário por meio de uevents. Em muitas distribuições atuais, `systemd-udevd` processa esses eventos usando regras udev e um banco de dados de dispositivos. Junto com o `devtmpfs` preenchido pelo kernel, isso produz as propriedades, permissões, atributos e links simbólicos que as aplicações observam em `/dev`.

## Do Evento do Kernel à Política do Dispositivo

Quando um dispositivo é adicionado, alterado, movido ou removido, o udev pode:

- ler atributos do sysfs e propriedades do evento
- aplicar políticas de proprietário, grupo e modo a um nó de dispositivo
- adicionar links simbólicos estáveis, como `/dev/disk/by-id/...`
- marcar dispositivos para outros serviços
- executar um processamento auxiliar de escopo restrito

O kernel continua responsável pelo dispositivo real e por seu driver. Excluir um nó de `/dev` não remove fisicamente o hardware, e criar manualmente um nó com `mknod` não faz um hardware sem suporte existir nem associa um driver a ele.

:::single-choice{#udev-kernel-event-input}
O que normalmente aciona o processamento do udev para uma alteração de dispositivo?

::option[Uma atualização dos repositórios de pacotes realizada pelo APT.]{#udev-apt-refresh explanation="As atualizações dos metadados de pacotes não têm relação com o processamento de eventos ativos de dispositivos."}
::option[Um usuário renomeando manualmente todos os arquivos em `/dev`.]{#udev-manual-renaming explanation="A política dinâmica é orientada por eventos do kernel e regras, não por uma renomeação manual em massa."}
::option[Um uevent do kernel que descreve a ação do dispositivo.]{#udev-kernel-uevent .correct explanation="O udev recebe eventos de dispositivos do kernel e aplica as regras correspondentes no espaço do usuário."}
:::

## Locais e Precedência das Regras

As regras normalmente ficam em:

- `/usr/lib/udev/rules.d/` para regras fornecidas por fornecedores ou pacotes
- `/run/udev/rules.d/` para regras voláteis em tempo de execução
- `/etc/udev/rules.d/` para a política local do administrador

Os arquivos são processados na ordem lexical dos nomes, e arquivos com o mesmo nome em diretórios de maior prioridade substituem versões de menor prioridade, conforme a implementação do udev instalada. As regras locais devem usar um nome de arquivo deliberado e corresponder a propriedades estáveis, não a nomes de enumeração.

Uma regra pode afetar todos os dispositivos correspondentes, portanto teste seu escopo cuidadosamente. Não edite diretamente regras de pacotes quando uma substituição local ou uma regra suplementar for apropriada.

:::single-choice{#udev-local-rules-directory}
Qual diretório é destinado às regras udev locais persistentes do administrador?

::option[`/proc/udev/rules.d/`]{#udev-proc-rules explanation="O procfs não fornece o diretório local persistente de regras."}
::option[`/etc/udev/rules.d/`]{#udev-etc-rules .correct explanation="A política local pertence a `/etc`, separada das regras de fornecedores gerenciadas por pacotes."}
::option[`/dev/udev/rules.d/`]{#udev-dev-rules explanation="`/dev` contém objetos voltados a dispositivos em tempo de execução, não configurações persistentes de regras."}
:::

## Inspeção de um Dispositivo com `udevadm`

Consulte as propriedades do udev para um nó existente:

```bash
$ udevadm info --query=all --name=/dev/sda
```

Use um nó que exista no sistema atual. `udevadm info --attribute-walk --name=...` pode exibir atributos ao longo da cadeia de pais no sysfs, o que ajuda a construir uma regra. `udevadm monitor --kernel --udev --property` observa eventos do kernel e eventos processados; ele pode expor identificadores de dispositivos, portanto trate adequadamente a saída capturada.

:::single-choice{#udev-info-purpose}
O que `udevadm info --query=all --name=/dev/sda` solicita?

::option[Uma regravação destrutiva da tabela de partições do disco.]{#udev-info-partition-write explanation="A consulta é uma operação de inspeção e não formata nem reparticiona o armazenamento."}
::option[A instalação pela Internet de um driver ausente do kernel.]{#udev-info-install-driver explanation="A inspeção com udevadm não funciona como um gerenciador de downloads de pacotes."}
::option[As propriedades conhecidas pelo udev para o nó de dispositivo indicado.]{#udev-info-properties .correct explanation="O comando info consulta o banco de dados de dispositivos e as informações associadas do sysfs."}
:::

## Aplicação Cuidadosa das Alterações de Regras

Recarregar os arquivos de regras afeta o processamento dos eventos futuros; isso não reconstrói automaticamente o estado de todos os dispositivos existentes. Acionar eventos manualmente pode afetar muitos dispositivos e serviços, portanto restrinja o destino e consulte a documentação do `udevadm` instalado. Um comando de teste pode simular a avaliação de regras, mas talvez não reproduza todos os efeitos colaterais de um evento real.

Faça backup das regras locais, valide a sintaxe, observe um único dispositivo de teste conhecido e mantenha um caminho de recuperação antes de alterar permissões ou nomes. Evite trabalhos demorados diretamente no processamento de eventos do udev; delegue-os a um serviço apropriado.

:::single-choice{#udev-reload-effect}
O que a recarga das regras udev altera principalmente?

::option[A forma como os eventos posteriores correspondentes de dispositivos são processados.]{#udev-future-events .correct explanation="A recarga atualiza as regras em memória; ainda é necessário que ocorra um evento ou que ele seja acionado deliberadamente para um dispositivo ser reavaliado."}
::option[A conexão física de todos os dispositivos conectados.]{#udev-physical-wiring explanation="Carregar regras de software não pode alterar conexões de hardware."}
::option[Todos os nós de dispositivos existentes, independentemente de eventos ou correspondências.]{#udev-all-existing explanation="Uma recarga por si só não garante a reavaliação imediata de todos os dispositivos atuais."}
:::

Use o laboratório [Exploração de Dispositivos de Hardware no Linux](https://labex.io/labs/comptia-explore-hardware-devices-in-linux-590861) para relacionar propriedades de `udevadm`, caminhos do sysfs e links de `/dev` em um ambiente controlado.

## Resumo

Agora você sabe situar o udev entre os eventos do kernel e a política de dispositivos no espaço do usuário.

1. Relacione uevents e atributos do sysfs à correspondência das regras udev.
2. Diferencie os locais de regras de fornecedores, de tempo de execução e locais.
3. Inspecione propriedades e o fluxo de eventos com `udevadm`.
4. Recarregue e acione regras somente com um escopo restrito e testado.
