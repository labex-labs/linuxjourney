---
lang: "pt"
title: "Visão Geral do Processo de Inicialização"
meta_title: "Visão Geral do Processo de Inicialização - Inicializar o Sistema"
meta_description: "Aprenda os estágios do processo de inicialização do Linux: BIOS, bootloader, kernel e init. Entenda como o Linux inicia desde o ligar até o login. Guia essencial para iniciantes em Linux."
meta_keywords: "processo de inicialização do Linux, BIOS, bootloader, kernel, init, tutorial de Linux, guia de Linux, iniciante"
---

## Lesson Content

Agora que temos uma boa compreensão de alguns dos componentes importantes do Linux, vamos juntá-los aprendendo sobre como o sistema inicializa. Quando você liga sua máquina, ela faz algumas coisas interessantes, como mostrar a tela do logotipo, exibir algumas mensagens diferentes e, no final, você é solicitado com uma janela de login. Bem, na verdade, há uma tonelada de coisas acontecendo entre o momento em que você aperta o botão de energia e o momento em que você faz login, e discutiremos isso neste curso.

O processo de inicialização do Linux pode ser dividido em 4 estágios simples:

### 1. BIOS

O BIOS (significa "Basic Input/Output System") inicializa o hardware e garante, com um Power-on Self-Test (POST), que todo o hardware está pronto para uso. O principal trabalho do BIOS é carregar o bootloader.

### 2. Bootloader

O bootloader carrega o kernel na memória e, em seguida, inicia o kernel com um conjunto de parâmetros do kernel. Um dos bootloaders mais comuns é o GRUB, que é um padrão universal do Linux.

### 3. Kernel

Quando o kernel é carregado, ele imediatamente inicializa dispositivos e memória. O principal trabalho do kernel é carregar o processo init.

### 4. Init

Lembre-se, o processo init é o primeiro processo que é iniciado. O Init inicia e para processos de serviço essenciais no sistema. Existem três implementações principais de init em distribuições Linux. Abordaremos elas brevemente e depois nos aprofundaremos nelas em outro curso.

Aí está, a explicação (muito) simples do processo de inicialização do Linux. Entraremos em mais detalhes sobre esses estágios nas próximas lições.

## Exercise

Reboot your system and see if you can spot each step as your machine boots up.

## Quiz Question

Qual é o último estágio no processo de inicialização do Linux?

## Quiz Answer

init
