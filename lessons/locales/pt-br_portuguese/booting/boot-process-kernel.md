# Processo de inicialização: Kernel

## Conteúdo da lição

Então, agora que o nosso gerenciador de inicialização passou os parâmetros necessários, vamos ver como ele é iniciado:

<b> Initrd vs Initramfs </ b>

Há um problema de galinha e ovo quando falamos sobre a inicialização do kernel. O kernel gerencia nosso hardware de sistemas, porém nem todos os drivers estão disponíveis para o kernel durante a inicialização. Portanto, dependemos de um sistema de arquivos raiz temporário que contém apenas os módulos essenciais que o kernel precisa para chegar ao restante do hardware. Nas versões mais antigas do Linux, esse trabalho era dado ao initrd (disco de RAM inicial). O kernel montaria o initrd, obteria os drivers de boot necessários, então, quando terminasse de carregar tudo o que precisava, ele substituiria o initrd pelo sistema de arquivos raiz real. Hoje em dia, temos algo chamado initramfs, que é um sistema de arquivos raiz temporário embutido no próprio kernel para carregar todos os drivers necessários para o sistema de arquivos raiz real, para que não mais localizemos o arquivo initrd.

<b> Montando o sistema de arquivos raiz </ b>

Agora o kernel tem todos os módulos necessários para criar um dispositivo raiz e montar a partição raiz. Antes de prosseguir, a partição raiz é montada primeiro no modo somente leitura para que o fsck possa ser executado com segurança e verificar a integridade do sistema. Depois disso, ele remonta o sistema de arquivos raiz no modo de leitura e gravação. Então o kernel localiza o programa init e o executa.

## Exercício

Nenhum exercício para esta lição.

## Questionário

O que é usado em sistemas modernos para carregar um sistema de arquivos raiz temporário?

## Resposta do questionário

initramfs
