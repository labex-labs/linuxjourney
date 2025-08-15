# Processo de inicialização: bootloader

## Conteúdo da lição

As principais responsabilidades do bootloader são:

<ul>
<li> Inicializar um sistema operacional, ele também pode ser usado para inicializar sistemas operacionais não-Linux </ li>
<li> Selecionar um kernel para usar </ li>
<li> Especificar os parâmetros do kernel </ li>
</ ul>

O bootloader mais comum para o Linux é o GRUB, provavelmente você está usando em seu sistema. Existem muitos outros gerenciadores de inicialização que você pode usar, como o LILO, efilinux, coreboot, SYSLINUX e muito mais. No entanto, estaremos apenas trabalhando com o GRUB como nosso gerenciador de inicialização.

Então sabemos que o principal objetivo do bootloader é carregar o kernel, mas onde ele encontra o kernel? Para encontrá-lo, precisamos examinar nossos parâmetros do kernel. Os parâmetros podem ser encontrados indo para o menu GRUB na inicialização usando a tecla 'e'. Se você não tem o GRUB não se preocupe, nós vamos passar pelos parâmetros de inicialização que você verá:

<ul>
<li> initrd - Especifica a localização do disco RAM inicial (falaremos mais sobre isso na próxima lição).</ li>
<li> BOOT_IMAGE - Aqui é onde a imagem do kernel está localizada </ li>
<li> root - A localização do sistema de arquivos raiz, o kernel procura dentro deste local para encontrar o init. É frequentemente representado pelo seu UUID ou pelo nome do dispositivo, como / dev / sda1. </ li>
<li> ro - Este parâmetro é bastante padrão, monta o sistema de arquivos como modo somente leitura. </ li>
<li> quiet - Isso é adicionado para que você não veja as mensagens de exibição que estão acontecendo em segundo plano durante a inicialização. </ li>
<li> splash - Isso permite que a tela inicial seja exibida. </ li>
</ ul>

## Exercício

Se você tem o GRUB como seu bootloader, entre no menu GRUB com 'e' e dê uma olhada nas configurações.

## Questionário

Qual parâmetro do kernel faz com que você não veja as mensagens de inicialização?

## Resposta do questionário

quiet
