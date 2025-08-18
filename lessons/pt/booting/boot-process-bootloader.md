---
lang: "pt"
title: "Processo de Inicialização: Bootloader"
meta_description: "Aprenda sobre o bootloader Linux, suas funções e parâmetros comuns do kernel como initrd e root. Entenda o GRUB e otimize seu processo de inicialização Linux."
meta_keywords: "bootloader Linux, GRUB, parâmetros do kernel, initrd, sistema de arquivos root, processo de inicialização Linux, tutorial Linux, Linux para iniciantes"
---

## Lesson Content

As principais responsabilidades do bootloader são:

- Inicializar um sistema operacional; ele também pode ser usado para inicializar sistemas operacionais que não são Linux.
- Selecionar um kernel para usar.
- Especificar parâmetros do kernel.

O bootloader mais comum para Linux é o GRUB; você provavelmente o está usando em seu sistema. Existem muitos outros bootloaders que você pode usar, como LILO, EFILINUX, Coreboot, SYSLINUX e outros. No entanto, trabalharemos apenas com o GRUB como nosso bootloader.

Então, sabemos que o principal objetivo do bootloader é carregar o kernel, mas onde ele encontra o kernel? Para encontrá-lo, precisaremos olhar para os nossos parâmetros do kernel. Os parâmetros podem ser encontrados entrando no menu do GRUB na inicialização usando a tecla 'e'. Se você não tem GRUB, não se preocupe, vamos passar pelos parâmetros de inicialização que você verá:

- `initrd` - Especifica a localização do disco RAM inicial (falaremos mais sobre isso na próxima lição).
- `BOOT_IMAGE` - É onde a imagem do kernel está localizada.
- `root` - A localização do sistema de arquivos root; o kernel procura dentro desta localização para encontrar `init`. É frequentemente representado por seu UUID ou pelo nome do dispositivo, como `/dev/sda1`.
- `ro` - Este parâmetro é bastante padrão; ele monta o sistema de arquivos em modo somente leitura.
- `quiet` - Isso é adicionado para que você não veja as mensagens de exibição que estão acontecendo em segundo plano durante a inicialização.
- `splash` - Isso permite que a tela de splash seja exibida.

## Exercise

Se você tem o GRUB como seu bootloader, entre no menu do GRUB com 'e' e dê uma olhada nas configurações.

## Quiz Question

Qual parâmetro do kernel faz com que você não veja as mensagens de inicialização?

## Quiz Answer

quiet
