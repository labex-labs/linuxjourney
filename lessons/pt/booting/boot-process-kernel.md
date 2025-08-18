---
lang: "pt"
title: "Processo de Inicialização: Kernel"
meta_title: "Processo de Inicialização: Kernel - Inicializar o Sistema"
meta_description: "Aprenda sobre o processo de inicialização do Linux, inicialização do kernel e o papel do initramfs. Entenda como o kernel monta o sistema de arquivos raiz. Guia do processo de inicialização do Linux."
meta_keywords: "processo de inicialização do Linux, inicialização do kernel, initramfs, initrd, sistema de arquivos raiz, tutorial de Linux, Linux para iniciantes, guia de Linux"
---

## Lesson Content

Agora que nosso bootloader passou os parâmetros necessários, vamos ver como ele inicia:

### Initrd vs Initramfs

Existe um pequeno problema de "ovo ou galinha" quando falamos sobre a inicialização do kernel. O kernel gerencia o hardware do nosso sistema; no entanto, nem todos os drivers estão disponíveis para o kernel durante a inicialização. Então, dependemos de um sistema de arquivos raiz temporário que contém apenas os módulos essenciais que o kernel precisa para acessar o restante do hardware. Em versões mais antigas do Linux, essa tarefa era dada ao initrd (initial ramdisk). O kernel montava o initrd, obtinha os drivers de inicialização necessários e, quando terminava de carregar tudo o que precisava, substituía o initrd pelo sistema de arquivos raiz real. Atualmente, temos algo chamado initramfs; este é um sistema de arquivos raiz temporário que é construído no próprio kernel para carregar todos os drivers necessários para o sistema de arquivos raiz real, então não há mais a necessidade de localizar o arquivo initrd.

### Mounting the root filesystem

Agora o kernel tem todos os módulos necessários para criar um dispositivo raiz e montar a partição raiz. Antes de prosseguir, a partição raiz é montada inicialmente em modo somente leitura para que o fsck possa ser executado com segurança e verificar a integridade do sistema. Posteriormente, ele remonta o sistema de arquivos raiz em modo leitura-gravação. Em seguida, o kernel localiza o programa init e o executa.

## Exercise

No exercises for this lesson.

## Quiz Question

O que é usado em sistemas modernos para carregar um sistema de arquivos raiz temporário?

## Quiz Answer

initramfs
