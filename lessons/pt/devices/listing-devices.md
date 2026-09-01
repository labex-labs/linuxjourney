---
lesson_id: "listing-devices"
course_id: "devices"
lang: "pt"
order_index: 6
title: "lsusb, lspci, lsscsi"
description: "Aprenda a inspecionar a topologia USB, funções PCI, dispositivos da camada SCSI e seus drivers ativos."
meta_title: "lsusb, lspci, lsscsi - Dispositivos"
meta_description: "Descubra como listar e inspecionar hardware USB, PCI e SCSI em seu sistema Linux. Este guia aborda os comandos lsusb, lspci e lsscsi, incluindo opções como lsusb -t para visualizar árvores de dispositivos."
meta_keywords: "lsusb, lspci, lsscsi, lsusb -t, listar dispositivos USB, listar dispositivos PCI, listar dispositivos SCSI, hardware Linux, informações de dispositivos"
---

O Linux oferece ferramentas de inventário específicas para barramentos e subsistemas. Cada comando apresenta uma visão diferente, portanto combine seus identificadores, topologia, drivers, caminhos do sysfs e logs, em vez de esperar uma única lista completa do hardware.

## Inspeção de Dispositivos USB

`lsusb` lista os dispositivos USB visíveis pelo subsistema USB:

```bash
$ lsusb
```

A saída normalmente inclui números de barramento e dispositivo, um par de IDs de fornecedor e produto e uma descrição do banco de dados USB local. O endereço numérico de barramento/dispositivo pode mudar após uma reconexão ou reinicialização e não deve ser tratado como uma identidade persistente.

Exiba as relações entre controladores, hubs, portas, interfaces, drivers e velocidades com:

```bash
$ lsusb -t
```

Também há uma saída detalhada dos descritores, mas alguns dados exigem acesso elevado de leitura. Não conceda permissões amplas aos dispositivos USB apenas para evitar mensagens de uma ferramenta de inspeção.

:::single-choice{#listing-devices-usb-tree} Qual comando exibe os dispositivos USB como uma árvore de topologia?

::option[`lspci -k`]{#listing-devices-lspci-tree explanation="Esse comando lista funções PCI e informações de drivers do kernel, não a topologia USB."}
::option[`lsscsi -t`]{#listing-devices-lsscsi-tree explanation="Esse não é o comando de árvore USB apresentado."}
::option[`lsusb -t`]{#listing-devices-lsusb-tree .correct explanation="A opção de árvore mostra os dispositivos abaixo de controladores e hubs, com relações entre portas e interfaces."}
:::

## Inspeção de Funções PCI

`lspci` lista as funções encontradas nos barramentos PCI e PCI Express:

```bash
$ lspci
```

Dispositivos PCIe internos e conectados externamente podem incluir controladores gráficos, de rede, armazenamento, USB, áudio e pontes. Mostre o driver do kernel em uso e os módulos candidatos com:

```bash
$ lspci -k
```

O aparecimento de um controlador PCI nessa lista não comprova que todos os dispositivos atrás dele estejam inicializados ou funcionando. Verifique a associação do driver e os logs do kernel durante a solução de problemas.

:::single-choice{#listing-devices-pci-driver} Qual comando acrescenta informações de drivers do kernel a uma listagem PCI?

::option[`lspci -k`]{#listing-devices-lspci-k .correct explanation="A opção `-k` exibe o driver ativo do kernel e os módulos capazes de controlar cada dispositivo PCI."}
::option[`lsusb -t`]{#listing-devices-usb-not-pci explanation="Esse comando descreve a hierarquia USB e os drivers das interfaces."}
::option[`lsblk -f`]{#listing-devices-lsblk-filesystem explanation="Esse comando informa campos de dispositivos de bloco e sistemas de arquivos, não a associação de drivers PCI."}
:::

## Inspeção de Dispositivos da Camada SCSI

`lsscsi` lista os dispositivos representados pela camada intermediária SCSI do Linux:

```bash
$ lsscsi
```

Isso pode incluir dispositivos SCSI nativos e discos SATA, de armazenamento USB ou virtuais apresentados por camadas compatíveis com SCSI. Os namespaces NVMe normalmente pertencem a outro subsistema e não são inventariados de forma abrangente por `lsscsi`.

Para uma hierarquia orientada ao armazenamento que inclua muitos tipos de dispositivos de bloco, use também `lsblk`:

```bash
$ lsblk -o NAME,TYPE,SIZE,MODEL,SERIAL,TRAN,FSTYPE,MOUNTPOINTS
```

:::single-choice{#listing-devices-lsscsi-scope} O que `lsscsi` lista principalmente?

::option[Exclusivamente todos os namespaces e controladores NVMe.]{#listing-devices-only-nvme explanation="O NVMe usa seu próprio subsistema e suas próprias ferramentas, embora visualizações de blocos relacionadas possam aparecer em outros lugares."}
::option[Somente arquivos cujos nomes terminam em `.scsi`.]{#listing-devices-scsi-extension explanation="O comando consulta interfaces de dispositivos do kernel, não extensões de nomes de arquivos."}
::option[Dispositivos representados pela camada intermediária SCSI do Linux.]{#listing-devices-scsi-mid-layer .correct explanation="O comando informa hosts, destinos, unidades lógicas SCSI e os nós de dispositivos correspondentes, quando disponíveis."}
:::

## Interpretação dos Resultados do Inventário

As descrições muitas vezes vêm de bancos de dados locais de IDs e podem ser genéricas ou desatualizadas. Um dispositivo listado pode não ter um driver funcional, e um ambiente virtualizado pode apresentar hardware emulado ou paravirtual. Relacione os resultados a `udevadm info`, sysfs, `lsblk`, ferramentas de rede e `journalctl -k` ou `dmesg`, de acordo com as permissões e com o problema investigado.

Os utilitários podem ser distribuídos separadamente, normalmente em pacotes como `usbutils`, `pciutils` e `lsscsi`. Quando um comando estiver ausente, use o gerenciador de pacotes da distribuição em vez de baixar substitutos desconhecidos.

:::single-choice{#listing-devices-listed-not-working} Ver um dispositivo em `lspci` comprova que seu driver está ativo e funcionando corretamente?

::option[Não; inspecione também a associação do driver e as mensagens relevantes do kernel.]{#listing-devices-needs-correlation .correct explanation="A enumeração estabelece que uma função PCI está visível, não que a inicialização de nível superior foi bem-sucedida."}
::option[Sim; a enumeração PCI realiza um teste funcional completo.]{#listing-devices-complete-test explanation="A listagem não exercita todas as funções do hardware nem valida o comportamento dos serviços."}
::option[Sim; `lspci` instala automaticamente um driver adequado.]{#listing-devices-installs-driver explanation="O comando é uma ferramenta de inventário e não instala pacotes de drivers."}
:::

Use o laboratório [Exploração de Dispositivos de Hardware no Linux](https://labex.io/labs/comptia-explore-hardware-devices-in-linux-590861) para comparar essas visualizações de subsistemas em um único host controlado.

## Resumo

Agora você sabe selecionar um comando de inventário para o subsistema de dispositivos em questão.

1. Use `lsusb` e `lsusb -t` para identidade e topologia USB.
2. Use `lspci -k` para funções PCI e associação de drivers.
3. Use `lsscsi` para dispositivos da camada SCSI e `lsblk` para a topologia de blocos.
4. Relacione a enumeração aos drivers, ao sysfs e às mensagens do kernel.
