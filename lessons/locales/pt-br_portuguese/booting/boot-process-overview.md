# Visão geral do processo de inicialização

## Conteúdo da lição

Agora que conseguimos um bom entendimento de alguns dos componentes importantes do Linux, vamos incluí-los, aprendendo como o sistema é inicializado. Quando você liga sua máquina, ela faz algumas coisas legais, como mostrar a tela do logotipo, passar por algumas mensagens diferentes e, em seguida, no final, você é solicitado com uma janela de login. Bem, na verdade, há uma tonelada de coisas acontecendo entre quando você aperta o botão liga / desliga e quando você faz o login e nós discutiremos sobre isso neste curso.

O processo de inicialização do Linux pode ser dividido em 4 estágios simples:

<b> 1. BIOS </ b>

O BIOS (significa "Sistema Básico de Entrada / Saída") inicializa o hardware e garante, com um autoteste de inicialização (POST), que todo o hardware está pronto. O trabalho principal da BIOS é carregar o bootloader.

<b> 2. Bootloader </ b>

O bootloader carrega o kernel na memória e então inicia o kernel com um conjunto de parâmetros do kernel. Um dos bootloaders mais comuns é o GRUB, que é um padrão universal do Linux.

<b> 3. Kernel </ b>

Quando o kernel é carregado, ele imediatamente inicializa dispositivos e memória. O principal trabalho do kernel é carregar o processo init.

<b> 4. Init </ b>

Lembre-se de que o processo de inicialização é o primeiro processo iniciado, o init inicia e interrompe o processo de serviço essencial no sistema. Existem três implementações principais do init nas distribuições do Linux. Vamos passar por cima deles brevemente e depois mergulhar neles em outro curso.

Aqui está a explicação (muito) simples do processo de inicialização do Linux. Vamos entrar em mais detalhes sobre esses estágios nas próximas lições.

## Exercício

Reinicialize seu sistema e veja se você consegue identificar cada etapa à medida que sua máquina é inicializada.

## Questionário

Qual é o último estágio no processo de inicialização do Linux?

## Resposta do questionário

init
