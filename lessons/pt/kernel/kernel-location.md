---
index: 5
lang: "pt"
title: "Localização do Kernel"
meta_title: "Localização do Kernel - Kernel"
meta_description: "Aprenda sobre a localização do kernel Linux no diretório /boot, entendendo vmlinuz, initrd e System.map. Explore os arquivos do kernel e gerencie o espaço de forma eficaz."
meta_keywords: "Kernel Linux, diretório /boot, vmlinuz, initrd, System.map, Linux para iniciantes, tutorial de kernel, guia Linux"
---

## Lesson Content

O que acontece quando você instala um novo kernel? Bem, ele realmente adiciona alguns arquivos ao seu sistema; esses arquivos são geralmente adicionados ao diretório `/boot`.

Você verá vários arquivos para diferentes versões do kernel:

- `vmlinuz` - este é o kernel Linux real
- `initrd` - como discutimos antes, o `initrd` é usado como um sistema de arquivos temporário, usado antes de carregar o kernel
- `System.map` - tabela de pesquisa simbólica
- `config` - configurações de configuração do kernel; se você estiver compilando seu próprio kernel, pode definir quais módulos podem ser carregados

Se o seu diretório `/boot` ficar sem espaço, você sempre pode excluir versões antigas desses arquivos ou apenas usar um gerenciador de pacotes. Mas tenha cuidado ao fazer a manutenção neste diretório e não exclua acidentalmente o kernel que você está usando atualmente.

## Exercise

A prática leva à perfeição! Aqui estão alguns laboratórios práticos para reforçar sua compreensão do processo de inicialização do Linux e do gerenciamento do kernel:

1. **[Personalize o Menu de Inicialização GRUB2 no Linux](https://labex.io/pt/labs/comptia-customize-the-grub2-boot-menu-in-linux-590859)** - Pratique a modificação da configuração do GRUB2, o que afeta diretamente como seu sistema Linux inicializa e seleciona as versões do kernel. Este laboratório o ajudará a entender as implicações práticas dos arquivos discutidos no diretório `/boot`.

Este laboratório o ajudará a aplicar os conceitos em cenários reais e a construir confiança com o kernel Linux e o gerenciamento de inicialização.

## Quiz Question

Como é chamada a imagem do kernel em `/boot`?

## Quiz Answer

vmlinuz
