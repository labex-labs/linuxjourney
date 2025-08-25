---
index: 2
lang: "pt"
title: "Processo de Inicialização: BIOS"
meta_title: "Processo de Inicialização: BIOS - Inicialize o Sistema"
meta_description: "Aprenda sobre o processo de inicialização do Linux, BIOS e MBR. Entenda como seu sistema inicia com este guia para iniciantes. Explore os conceitos de UEFI!"
meta_keywords: "processo de inicialização Linux, BIOS, MBR, UEFI, tutorial Linux, bootloader, Linux para iniciantes, inicialização do sistema"
---

## Lesson Content

### BIOS

O primeiro passo no processo de inicialização do Linux é o BIOS, que realiza verificações de integridade do sistema. O BIOS é um firmware mais comum em computadores compatíveis com IBM PC, o tipo dominante de computadores atualmente. Você provavelmente já usou o firmware do BIOS para alterar a ordem de inicialização dos seus discos rígidos, verificar a hora do sistema, o endereço MAC da sua máquina, etc. O principal objetivo do BIOS é encontrar o bootloader do sistema.

Assim, uma vez que o BIOS inicializa o disco rígido, ele procura o bloco de inicialização para descobrir como inicializar o sistema. Dependendo de como você particiona seu disco, ele procurará o Master Boot Record (MBR) ou GPT. O MBR está localizado no primeiro setor do disco rígido, os primeiros 512 bytes. O MBR contém o código para carregar outro programa em algum lugar do disco; este programa, por sua vez, carrega nosso bootloader.

Agora, se você particionou seu disco com GPT, a localização do bootloader muda um pouco.

### UEFI

Existe outra forma de inicializar seu sistema em vez de usar o BIOS, que é com UEFI (significa "Unified Extensible Firmware Interface"). O UEFI foi projetado para ser o sucessor do BIOS; a maioria do hardware atual vem com firmware UEFI integrado. As máquinas Macintosh usam inicialização EFI há anos, e o Windows moveu a maioria de suas coisas para a inicialização UEFI. O formato GPT foi projetado para uso com EFI. Você não precisa necessariamente de EFI se estiver inicializando um disco GPT. O primeiro setor de um disco GPT é reservado para um "MBR protetor" para possibilitar a inicialização de uma máquina baseada em BIOS.

O UEFI armazena todas as informações sobre a inicialização em um arquivo `.efi`. Este arquivo é armazenado em uma partição especial chamada EFI System Partition no hardware. Dentro desta partição, ele conterá o bootloader. O UEFI vem com muitas melhorias em relação ao firmware BIOS tradicional. No entanto, como estamos usando Linux, a maioria de nós está usando BIOS. Portanto, todas essas lições seguirão essa premissa.

## Exercise

A prática leva à perfeição! Aqui estão alguns laboratórios práticos para reforçar sua compreensão do gerenciamento de usuários e grupos no Linux:

1. **[Gerenciar Contas de Usuário Linux com useradd, usermod e userdel](https://labex.io/pt/labs/comptia-manage-linux-user-accounts-with-useradd-usermod-and-userdel-590837)** - Pratique o ciclo de vida completo da administração de usuários, desde a criação e segurança de novas contas até a modificação e exclusão delas.
2. **[Gerenciar Grupos Linux com groupadd, usermod e groupdel](https://labex.io/pt/labs/comptia-manage-linux-groups-with-groupadd-usermod-and-groupdel-590836)** - Obtenha experiência prática com utilitários de linha de comando para administração de grupos, incluindo a criação de novos grupos, a modificação de associações de usuários e a remoção de grupos.
3. **[Configurar Contas de Usuário e Privilégios Sudo no Linux](https://labex.io/pt/labs/comptia-configure-user-accounts-and-sudo-privileges-in-linux-590856)** - Aprenda técnicas essenciais para gerenciar contas de usuário e privilégios sudo para aumentar a segurança de um sistema Linux.

Esses laboratórios o ajudarão a aplicar os conceitos em cenários reais e a construir confiança com o gerenciamento de usuários e grupos no Linux.

## Quiz Question

O que o BIOS carrega?

## Quiz Answer

bootloader
