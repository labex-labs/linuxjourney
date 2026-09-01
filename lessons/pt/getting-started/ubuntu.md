---
lesson_id: "ubuntu"
course_id: "getting-started"
lang: "pt"
order_index: 5
title: "Ubuntu"
description: "Aprenda como o Ubuntu combina a base do Debian com opções acessíveis para desktop, servidor e lançamentos."
meta_title: "Ubuntu Linux"
meta_description: "Saiba o que é o Ubuntu Linux, por que é popular, como funciona seu modelo de lançamento e gerenciamento de pacotes, e por que é amplamente utilizado em desktops, laptops e servidores."
meta_keywords: "ubuntu linux, distribuição ubuntu, o que é ubuntu, lançamentos ubuntu, gerenciamento de pacotes ubuntu, ubuntu baseado em debian, distribuição linux"
---

## O que é o Ubuntu?

O Ubuntu é uma das distribuições Linux mais utilizadas. Desenvolvido pela Canonical, é baseado no Debian e conhecido pelo seu design acessível, grande comunidade de utilizadores e amplo suporte a hardware e software.

O Ubuntu tornou-se um ponto de partida comum para pessoas que desejam aprender Linux sem começar por uma configuração mais manual ou avançada. É utilizado em computadores pessoais, sistemas de desenvolvimento, plataformas em nuvem e servidores, o que lhe confere um alcance que poucas outras distribuições conseguem igualar.

:::single-choice{#identify-ubuntu-base} Qual distribuição fornece a base do Ubuntu?

::option[A distribuição Debian]{#debian-base .correct explanation="O Ubuntu é construído a partir do Debian e herda boa parte de seu modelo de empacotamento. Depois, acrescenta lançamentos, padrões e suporte próprios."}
::option[A distribuição Fedora]{#ubuntu-fedora-base explanation="O Fedora pertence ao ecossistema Red Hat e não forma a base do Ubuntu. O Ubuntu faz parte da família Debian."}
::option[A distribuição Arch]{#ubuntu-arch-base explanation="O Arch Linux é uma distribuição separada, com sistema de pacotes e modelo de lançamento próprios. O Ubuntu é baseado no Debian."}
:::

## Por que o Ubuntu é popular

O Ubuntu é popular porque tenta tornar o Linux prático para o uso diário. Oferece um instalador polido, documentação robusta, lançamentos previsíveis e um grande ecossistema de tutoriais e suporte de terceiros. Para muitos utilizadores, essa combinação torna o Ubuntu uma das distribuições Linux mais fáceis de utilizar.

Outra razão pela qual o Ubuntu é tão visível é que funciona em muitos ambientes. Vê-lo-á em portáteis e desktops, em máquinas virtuais, em servidores e em plataformas em nuvem. Essa ampla adoção reforça a sua reputação como uma distribuição Linux de uso geral.

:::single-choice{#recognize-beginner-support} Qual característica do Ubuntu ajuda mais diretamente um iniciante a resolver problemas?

::option[Compilação manual obrigatória de cada programa instalado]{#manual-compilation explanation="O Ubuntu normalmente oferece software empacotado, sem exigir que todo programa seja compilado à mão. Trabalho adicional de compilação não simplificaria a solução de problemas."}
::option[Documentação extensa e uma grande comunidade de usuários]{#documentation-community .correct explanation="A documentação e as discussões da comunidade oferecem muitos lugares para encontrar explicações e ajuda. Isso reduz a barreira de aprendizagem."}
::option[Orientação limitada apenas a administradores experientes]{#limited-guidance explanation="A visibilidade do Ubuntu se deve em parte à orientação disponível para vários níveis de habilidade. Restringir a ajuda a especialistas iria contra a acessibilidade para iniciantes."}
:::

## Ubuntu e Debian

O Ubuntu é uma distribuição baseada no Debian, o que significa que herda grande parte do seu modelo de gestão de pacotes e abordagem de empacotamento de software do Debian. Se aprender como o `apt` funciona no Ubuntu, esse conhecimento também o ajudará a compreender outros sistemas baseados em Debian.

Ao mesmo tempo, o Ubuntu não é apenas "Debian com um desktop". Tem o seu próprio cronograma de lançamentos, padrões, modelo de suporte e ecossistema. Se deseja compará-lo com outras opções, consulte [Escolher uma Distribuição Linux](https://labex.io/lesson/choosing-a-linux-distribution) ou saiba mais sobre o [Debian](https://labex.io/lesson/debian).

## Lançamentos do Ubuntu

O Ubuntu utiliza dois tipos principais de lançamento. Publica uma nova versão a cada seis meses e, a cada dois anos, um desses lançamentos torna-se uma versão de Suporte de Longo Prazo, ou LTS. Os lançamentos LTS são habitualmente escolhidos para desktops, estações de trabalho e servidores que necessitam de uma base mais estável.

Este modelo de lançamento ajuda a explicar o apelo do Ubuntu. Os utilizadores que desejam uma base fiável escolhem frequentemente a LTS, enquanto os utilizadores que desejam funcionalidades mais recentes podem utilizar os lançamentos intermédios que chegam num cronograma mais rápido.

:::single-choice{#choose-ubuntu-lts} Qual tipo de lançamento do Ubuntu é mais adequado a um sistema que precisa de uma base previsível e duradoura?

::option[Um lançamento intermediário]{#interim-release explanation="Lançamentos intermediários chegam com maior frequência e oferecem novos recursos mais cedo. Seu período de suporte menor não corresponde à prioridade indicada."}
::option[Um lançamento LTS]{#lts-release .correct explanation="Os lançamentos LTS foram concebidos para suporte mais longo e são escolhidos com frequência por sistemas que priorizam uma base confiável."}
::option[Uma atualização de pacote]{#package-update explanation="Uma atualização de pacote altera software dentro de uma versão instalada. Ela não é um dos dois tipos de lançamento do sistema operacional Ubuntu."}
:::

## Gestão de pacotes

Como um sistema baseado em Debian, o Ubuntu utiliza o formato de pacote `.deb` e o gestor de pacotes `apt` para instalar, atualizar e remover software. Isto dá aos utilizadores acesso a um ecossistema de software muito vasto e a um fluxo de trabalho de linha de comandos familiar.

A gestão de pacotes é um dos pontos fortes práticos do Ubuntu, porque combina ferramentas maduras do Debian com um ambiente de software grande e amplamente documentado.

:::single-choice{#identify-ubuntu-package-tool} Qual item é a ferramenta de gerenciamento de pacotes usada para instalar software no Ubuntu?

::option[`.deb`]{#deb-format explanation="`.deb` identifica o formato de pacote usado por sistemas baseados no Debian. Ele não é a ferramenta de linha de comando para gerenciar pacotes."}
::option[`LTS`]{#lts-label explanation="LTS identifica um lançamento com suporte de longo prazo. Ele não instala nem gerencia pacotes de software."}
::option[`apt`]{#ubuntu-apt-tool .correct explanation="O Ubuntu usa `apt` para instalar, atualizar e remover pacotes. A ferramenta trabalha com software no formato `.deb` do Debian."}
:::

## Uso em desktop e servidor

O Ubuntu é utilizado tanto em sistemas desktop como em servidores. No lado do desktop, é conhecido por uma experiência polida baseada em GNOME e padrões relativamente acessíveis. No lado do servidor, é amplamente implementado em desenvolvimento, infraestrutura web e ambientes em nuvem.

Essa variedade torna o Ubuntu atraente para utilizadores que desejam uma distribuição Linux que possa escalar desde a aprendizagem num portátil até à execução de cargas de trabalho em produção.

## Por que os iniciantes escolhem o Ubuntu

O Ubuntu é frequentemente recomendado a iniciantes porque é mais fácil de instalar e solucionar problemas do que muitas outras distribuições Linux. A grande base de utilizadores significa que existem muitos tutoriais, publicações em fóruns e guias disponíveis quando algo corre mal.

Para utilizadores que desejam uma distribuição Linux amigável para iniciantes sem abrir mão da flexibilidade a longo prazo, o Ubuntu continua a ser um dos pontos de partida mais seguros.

## Leitura adicional

- [Ubuntu Desktop](https://ubuntu.com/desktop)
- [Ubuntu Server](https://ubuntu.com/server)
- [Ciclo de lançamento do Ubuntu](https://ubuntu.com/releaseendoflife)
- [Documentação de lançamentos do Ubuntu](https://documentation.ubuntu.com/project/release-team/ubuntu-releases/)

Para continuar a aprender após esta introdução ao Ubuntu, recomendamos estes cursos LabEx:

1. **[Início Rápido com Linux](https://labex.io/courses/quick-start-with-linux)** - Construa uma base prática em fundamentos de Linux e habilidades de linha de comando.
2. **[Linux para Iniciantes](https://labex.io/courses/linux-for-noobs)** - Siga um caminho amigável para iniciantes para compreender o básico do Linux passo a passo.
3. **[Torne-se um Administrador de Sistemas Júnior](https://labex.io/courses/become-a-junior-system-administrator)** - Continue com habilidades práticas de administração Linux quando estiver confortável com o básico.

## Resumo

Agora você consegue explicar como o Ubuntu aproveita o Debian e oferece lançamentos e uma experiência próprios.

1. Identificar o Debian como a base do Ubuntu.
2. Reconhecer características de suporte úteis a iniciantes.
3. Comparar lançamentos LTS e intermediários.
4. Usar `apt` como ferramenta de gerenciamento de pacotes do Ubuntu.
