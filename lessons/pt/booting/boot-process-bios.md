---
index: 2
lang: "pt"
title: "Processo de Inicialização: BIOS"
meta_title: "Processo de Inicialização: BIOS - Inicializar o Sistema"
meta_description: "Aprenda sobre o processo de inicialização do Linux, BIOS e MBR. Entenda como seu sistema inicia com este guia amigável para iniciantes. Explore os conceitos de UEFI!"
meta_keywords: "processo de inicialização do Linux, BIOS, MBR, UEFI, tutorial de Linux, bootloader, Linux para iniciantes, inicialização do sistema"
---

## Lesson Content

### BIOS

O primeiro passo no processo de inicialização do Linux é o BIOS, que realiza verificações de integridade do sistema. O BIOS é um firmware mais comum em computadores compatíveis com IBM PC, o tipo dominante de computadores atualmente. Você provavelmente já usou o firmware BIOS para alterar a ordem de inicialização de seus discos rígidos, verificar a hora do sistema, o endereço MAC da sua máquina, etc. O principal objetivo do BIOS é encontrar o bootloader do sistema.

Então, uma vez que o BIOS inicializa o disco rígido, ele procura o bloco de inicialização para descobrir como iniciar o sistema. Dependendo de como você particiona seu disco, ele procurará o Master Boot Record (MBR) ou GPT. O MBR está localizado no primeiro setor do disco rígido, os primeiros 512 bytes. O MBR contém o código para carregar outro programa em algum lugar do disco; este programa, por sua vez, carrega nosso bootloader.

Agora, se você particionou seu disco com GPT, a localização do bootloader muda um pouco.

### UEFI

Existe outra maneira de inicializar seu sistema em vez de usar o BIOS, e essa é com UEFI (que significa "Unified Extensible Firmware Interface"). O UEFI foi projetado para ser o sucessor do BIOS; a maioria do hardware atual vem com firmware UEFI integrado. As máquinas Macintosh usam a inicialização EFI há anos, e o Windows moveu a maioria de suas coisas para a inicialização UEFI. O formato GPT foi projetado para uso com EFI. Você não precisa necessariamente de EFI se estiver inicializando um disco GPT. O primeiro setor de um disco GPT é reservado para um "MBR protetor" para possibilitar a inicialização de uma máquina baseada em BIOS.

O UEFI armazena todas as informações sobre a inicialização em um arquivo `.efi`. Este arquivo é armazenado em uma partição especial chamada EFI System Partition no hardware. Dentro desta partição, ele conterá o bootloader. O UEFI vem com muitas melhorias em relação ao firmware BIOS tradicional. No entanto, como estamos usando Linux, a maioria de nós está usando BIOS. Portanto, todas essas lições seguirão essa premissa.

## Exercise

Entre no menu do seu BIOS e veja se você tem a inicialização UEFI ativada.

## Quiz Question

O que o BIOS carrega?

## Quiz Answer

bootloader
