---
index: 4
lang: "pt"
title: "Processo de Inicialização: Kernel"
meta_title: "Processo de Inicialização: Kernel - Inicialize o Sistema"
meta_description: "Aprenda sobre o processo de inicialização do Linux, inicialização do kernel e o papel do initramfs. Entenda como o kernel monta o sistema de arquivos raiz. Guia do processo de inicialização do Linux."
meta_keywords: "processo de inicialização Linux, inicialização do kernel, initramfs, initrd, sistema de arquivos raiz, tutorial Linux, Linux para iniciantes, guia Linux"
---

## Lesson Content

Então, agora que nosso bootloader passou os parâmetros necessários, vamos ver como ele inicia:

### Initrd vs Initramfs

Existe um problema de "ovo ou galinha" quando falamos sobre a inicialização do kernel. O kernel gerencia o hardware do nosso sistema; no entanto, nem todos os drivers estão disponíveis para o kernel durante a inicialização. Então, dependemos de um sistema de arquivos raiz temporário que contém apenas os módulos essenciais que o kernel precisa para acessar o resto do hardware. Em versões mais antigas do Linux, essa tarefa era dada ao initrd (initial ramdisk). O kernel montava o initrd, obtinha os drivers de inicialização necessários e, quando terminava de carregar tudo o que precisava, substituía o initrd pelo sistema de arquivos raiz real. Atualmente, temos algo chamado initramfs; este é um sistema de arquivos raiz temporário que é construído no próprio kernel para carregar todos os drivers necessários para o sistema de arquivos raiz real, então não há mais a necessidade de localizar o arquivo initrd.

### Montando o sistema de arquivos raiz

Agora o kernel tem todos os módulos de que precisa para criar um dispositivo raiz e montar a partição raiz. Antes de prosseguir, a partição raiz é montada em modo somente leitura primeiro para que o fsck possa ser executado com segurança e verificar a integridade do sistema. Depois, ele remonta o sistema de arquivos raiz em modo de leitura e escrita. Em seguida, o kernel localiza o programa init e o executa.

## Exercise

A prática leva à perfeição! Aqui está um laboratório prático para reforçar sua compreensão do processo de inicialização do Linux:

- **[Personalizar o Menu de Inicialização GRUB2 no Linux](https://labex.io/pt/labs/comptia-customize-the-grub2-boot-menu-in-linux-590859)** - Aprenda a modificar o menu de inicialização GRUB2, incluindo a alteração do tempo limite e da entrada padrão, e a aplicar essas alterações. Este laboratório o ajudará a entender como o bootloader pode ser configurado.

Este laboratório o ajudará a aplicar os conceitos em um cenário real e a construir confiança com a configuração de inicialização do Linux.

## Quiz Question

O que é usado em sistemas modernos para carregar um sistema de arquivos raiz temporário?

## Quiz Answer

initramfs
