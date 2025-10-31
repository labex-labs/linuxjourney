---
index: 4
lang: "pt"
title: "Processo de Inicialização: Kernel"
meta_title: "Processo de Inicialização: Kernel - Inicializando o Sistema"
meta_description: "Explore o processo de inicialização do kernel Linux. Aprenda como o initramfs carrega drivers de um sistema de arquivos temporário para montar a partição raiz final. Entenda as etapas desde o carregamento do kernel até a execução do init."
meta_keywords: "raiz de inicialização, initramfs, inicialização do kernel, partição de boot, initramfs ubuntu, /etc/default/grub, processo de boot Linux, sistema de arquivos raiz, inicialização do kernel"
---

## Lesson Content

Uma vez que o carregador de boot (bootloader) carregou o kernel na memória e passou os parâmetros necessários, o kernel assume o controle do sistema. Vamos explorar o que acontece a seguir.

### Inicialização do Kernel e o Initramfs

Um desafio clássico durante a inicialização é que o kernel precisa de drivers para acessar os dispositivos de hardware, mas esses drivers geralmente residem em um dispositivo de armazenamento ao qual o kernel ainda não consegue acessar. Para resolver isso, o Linux usa um sistema de arquivos raiz temporário.

Em sistemas mais antigos, isso era tratado por um `initrd` (initial RAM disk). O kernel carregava esta imagem de disco, encontrava os drivers necessários e, em seguida, mudava para o sistema de arquivos raiz real. Sistemas modernos, incluindo distribuições como o Ubuntu, usam `initramfs` (initial RAM filesystem). Diferente do `initrd`, o `initramfs` é um arquivo `cpio` que é descompactado em um sistema de arquivos temporário diretamente na memória. Essa abordagem é mais eficiente, pois evita a sobrecarga de criar e montar um dispositivo de bloco. O `initramfs` contém apenas os módulos essenciais que o kernel precisa para acessar a partição de boot real (`boot partition`) e outro hardware.

### Montagem do Sistema de Arquivos Raiz de Boot

Com os drivers carregados do `initramfs`, o kernel agora pode localizar e montar o sistema de arquivos raiz de boot principal (`boot root`). A localização deste sistema de arquivos é tipicamente passada como um parâmetro pelo carregador de boot, o que pode ser configurado em arquivos como `/etc/default/grub`.

Primeiro, o kernel monta a partição raiz de boot (`boot root`) em modo somente leitura. Esta é uma medida de segurança que permite que a utilidade `fsck` (verificação do sistema de arquivos) seja executada e verifique a integridade do sistema de arquivos sem arriscar a corrupção de dados. Após a conclusão bem-sucedida da verificação, o kernel remonta o sistema de arquivos em modo leitura-escrita.

Finalmente, com o sistema de arquivos raiz totalmente disponível, o kernel inicia o primeiro programa em espaço de usuário: `init`. Este programa é responsável por colocar o restante do sistema online.

## Exercise

Prática leva à perfeição! Aqui está um laboratório prático para reforçar sua compreensão do processo de boot do Linux:

- **[Personalizar o Menu de Boot GRUB2 no Linux](https://labex.io/pt/labs/comptia-customize-the-grub2-boot-menu-in-linux-590859)** - Aprenda a modificar o menu de boot do GRUB2, incluindo a alteração do tempo limite e da entrada padrão, e a aplicar essas alterações. Este laboratório ajudará você a entender como o carregador de boot pode ser configurado.

Este laboratório ajudará você a aplicar os conceitos em um cenário real e a ganhar confiança com a configuração de boot do Linux.

## Quiz Question

What is used in modern systems to load a temporary root filesystem? Please answer in English, using only lowercase letters.

## Quiz Answer

initramfs
