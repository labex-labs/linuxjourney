---
lesson_id: "linux-history"
course_id: "getting-started"
lang: "pt"
order_index: 1
title: "História do Linux"
description: "Aprenda como o UNIX, o GNU e o kernel Linux contribuíram para os sistemas Linux modernos."
meta_title: "História do Linux - Primeiros Passos"
meta_description: "Comece sua jornada no Linux explorando sua história. Aprenda sobre suas origens no UNIX, o projeto GNU e a criação do kernel Linux por Linus Torvalds."
meta_keywords: "história do linux, jornada linux, UNIX, projeto GNU, Linus Torvalds, kernel Linux, Linux para iniciantes"
---

Bem-vindo à sua **Jornada Linux**! Se você está pronto para mergulhar no poderoso mundo do Linux, veio ao lugar certo. Meu nome é Penguin Pete e serei seu guia. Para começar, vamos conhecer uma breve **história do Linux**.

## Os predecessores do Linux

Para entender como o Linux foi criado, precisamos voltar a 1969, quando Ken Thompson e Dennis Ritchie, dos Laboratórios Bell, desenvolveram o sistema operacional UNIX. Mais tarde, ele foi reescrito na linguagem de programação C, o que o tornou portátil e favoreceu sua ampla adoção.

![Linha do tempo do Unix](https://file.labex.io/images/ed9c245d-e8be-4287-bf34-67750b042542.jpg)

:::single-choice{#understand-unix-portability} Qual foi um resultado importante da reescrita do UNIX em C?

::option[Ele se tornou o kernel livre criado para o sistema GNU.]{#unix-became-gnu-kernel explanation="O UNIX surgiu antes do projeto GNU e não era o kernel do GNU. Mais tarde, o GNU começou a desenvolver um kernel separado chamado Hurd."}
::option[Ele ficou mais fácil de transferir entre diferentes sistemas de hardware.]{#portable-across-hardware .correct explanation="Escrever o UNIX em C aumentou sua portabilidade. Essa característica ajudou o sistema a se difundir além do hardware original."}
::option[Ele se tornou um shell de comandos usado apenas nos Laboratórios Bell.]{#unix-became-shell explanation="O UNIX é um sistema operacional, não apenas um shell. Sua reescrita em C favoreceu a adoção fora dos Laboratórios Bell."}
:::

Mais de uma década depois, Richard Stallman iniciou o projeto GNU. GNU é um acrônimo recursivo de "GNU's Not UNIX", e seu objetivo era criar um sistema operacional semelhante ao UNIX, totalmente livre e de código aberto. O projeto produziu muitos componentes essenciais e a Licença Pública Geral GNU (GPL), mas seu próprio kernel, o GNU Hurd, ainda não estava pronto para uso geral quando o Linux surgiu.

:::single-choice{#identify-gnu-missing-component} Qual componente importante do GNU ainda não estava pronto quando o Linux surgiu?

::option[Um kernel pronto para uso em produção]{#gnu-kernel .correct explanation="O GNU já havia produzido muitos componentes do sistema, mas seu próprio kernel, o GNU Hurd, ainda não estava pronto para uso geral."}
::option[Uma licença de software livre]{#gnu-license explanation="O projeto GNU já havia criado a Licença Pública Geral GNU. O componente ausente era um kernel utilizável."}
::option[Ferramentas essenciais do sistema]{#gnu-tools explanation="O GNU já havia produzido muitas ferramentas essenciais. Seu kernel continuava sendo a principal parte inacabada do sistema."}
:::

## O papel do kernel

O kernel é o componente central de um sistema operacional. Ele atua como uma ponte que permite a comunicação entre hardware e software. O kernel gerencia recursos do sistema, como CPU, memória e dispositivos periféricos. Além das ferramentas e dos aplicativos usados pelas pessoas, um sistema operacional completo precisa desse núcleo responsável pelos recursos.

:::single-choice{#recognize-kernel-role} Qual responsabilidade pertence ao kernel do sistema operacional?

::option[Escrever todos os comandos digitados no shell]{#write-shell-commands explanation="Pessoas ou scripts fornecem os comandos do shell. O kernel disponibiliza os recursos de baixo nível necessários quando os programas executam esses comandos."}
::option[Escolher a licença de cada aplicativo instalado]{#choose-software-licenses explanation="Autores e distribuidores escolhem as licenças dos aplicativos. Essa escolha não é uma tarefa de gerenciamento de recursos do kernel."}
::option[Gerenciar a CPU, a memória e os dispositivos conectados]{#manage-system-resources .correct explanation="O kernel gerencia os recursos de hardware e os disponibiliza ao software. Tempo de CPU, memória e dispositivos são exemplos centrais."}
:::

## O nascimento do kernel Linux

Chegamos então a 1991, quando um estudante finlandês chamado Linus Torvalds começou a desenvolver um novo kernel como projeto pessoal. Esse kernel passou a ser conhecido como kernel Linux. Depois que o Linux foi lançado como software livre, em 1992, ele pôde ser combinado ao sistema GNU quase completo para formar um sistema operacional livre completo, comumente chamado GNU/Linux. Esse marco foi um momento decisivo na **história do Linux**.

![Linus Torvalds em 2018](https://file.labex.io/images/3e1311fd-b8ca-45e7-8d02-9aac6377bb36.jpg)

_Linus Torvalds em 2018 (Fonte: [Wikipedia](https://en.wikipedia.org/wiki/Linus_Torvalds))_

:::single-choice{#identify-linux-kernel-creator} Quem começou a desenvolver o kernel Linux em 1991?

::option[Richard Stallman]{#richard-stallman explanation="Richard Stallman iniciou o projeto GNU. O GNU forneceu muitos componentes do sistema, mas foi Linus Torvalds quem começou o kernel Linux."}
::option[Dennis Ritchie]{#dennis-ritchie explanation="Dennis Ritchie ajudou a desenvolver o UNIX e a linguagem C. O projeto do kernel Linux foi iniciado mais tarde por Linus Torvalds."}
::option[Linus Torvalds]{#linus-torvalds .correct explanation="Linus Torvalds iniciou o projeto do kernel em 1991. Esse projeto se tornou o kernel Linux."}
:::

Para continuar sua **jornada Linux**, experimente estes laboratórios práticos para treinar comandos fundamentais e ganhar confiança no ambiente de linha de comando.

1. **[Introdução ao Linux](https://labex.io/labs/linux-getting-started-with-linux-446315)** - Comece sua jornada no Linux aprendendo comandos essenciais do terminal, como `echo`, `date` e cálculos básicos. Ideal para iniciantes.
2. **[Seu Primeiro Laboratório Linux](https://labex.io/labs/linux-your-first-linux-lab-270253)** - Este laboratório introdutório apresenta o clássico programa "Hello, World!" no Linux e ensina alguns comandos fundamentais.
3. **[Crie uma Saudação de Terminal Personalizada](https://labex.io/labs/linux-create-personalized-terminal-greeting-446322)** - Um desafio rápido e divertido para usar comandos básicos do terminal Linux e criar uma mensagem de boas-vindas.

## Resumo

Agora você consegue explicar como o UNIX, o GNU e o kernel Linux contribuíram para os sistemas Linux modernos.

1. Descrever por que a portabilidade do UNIX foi importante.
2. Identificar o kernel como o principal componente que faltava ao GNU.
3. Explicar o papel do kernel no gerenciamento dos recursos do sistema.
4. Identificar Linus Torvalds como o criador do kernel Linux.
