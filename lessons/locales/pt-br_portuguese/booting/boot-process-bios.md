# Processo de inicialização: BIOS

## Conteúdo da lição

<b> BIOS </ b>

O primeiro passo no processo de inicialização do Linux é o BIOS que realiza verificações de integridade do sistema. O BIOS é um firmware que é mais comum em computadores compatíveis com IBM PC, o tipo dominante de computadores existentes atualmente. Você provavelmente usou o firmware do BIOS para alterar a ordem de inicialização dos seus discos rígidos(HD), verificar a hora do sistema, o endereço MAC do seu computador, etc. O principal objetivo do BIOS é encontrar o carregador de inicialização do sistema.

Assim, uma vez que o BIOS inicializa o disco rígido, ele procura o bloco de inicialização para descobrir como inicializar o sistema. Dependendo de como você particiona seu disco, ele irá olhar para o registro mestre de inicialização (MBR) ou GPT. O MBR está localizado no primeiro setor do disco rígido, os primeiros 512 bytes. O MBR contém o código para carregar outro programa em algum lugar no disco; este programa, por sua vez, carrega nosso bootloader.

Agora, se você particionou seu disco com o GPT, o local do bootloader muda um pouco.

<b> UEFI </ b>

Existe outra maneira de inicializar o sistema em vez de usar o BIOS e isso é com UEFI (significa "Unified extensible firmware interface" (interface de firmware extensível unificada)). O UEFI foi projetado para ser o sucessor do BIOS, a maioria dos hardwares existentes atualmente vem com firmware UEFI integrado. As máquinas Macintosh vêm usando a inicialização EFI há anos e o Windows moveu todas as suas coisas para a inicialização via UEFI. O formato GPT foi planejado para uso com o EFI. Você não precisa necessariamente da EFI se estiver inicializando um disco GPT. O primeiro setor de um disco GPT é reservado para um "MBR de proteção" para possibilitar a inicialização de uma máquina baseada em BIOS.

UEFI armazena todas as informações sobre inicialização em um arquivo .efi. Este arquivo é armazenado em uma partição especial chamada partição do sistema EFI no hardware. Dentro dessa partição, ele conterá o bootloader. A UEFI vem com muitos aprimoramentos do firmware tradicional do BIOS. No entanto, como estamos usando o Linux, a maioria de nós está usando o BIOS. Então, todas essas lições vão acompanhar essa pretensão.

## Exercício

Vá para o menu do BIOS e veja se você tem a inicialização do UEFI ativada.

## Questionário

O que o BIOS carrega?

## Resposta do questionário

bootloader
