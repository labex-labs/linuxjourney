---
lesson_id: "fedora"
course_id: "getting-started"
lang: "pt"
order_index: 6
title: "Fedora"
description: "Aprenda como o Fedora oferece tecnologias Linux atuais por meio de um projeto comunitário ligado à Red Hat."
meta_title: "Distribuição Linux Fedora"
meta_description: "Saiba o que é a distribuição Linux Fedora, sua relação com o Red Hat, como funciona o gerenciamento de pacotes DNF e por que o Fedora é popular entre desenvolvedores e usuários de desktop."
meta_keywords: "fedora linux, distribuição linux fedora, o que é fedora, fedora red hat, lançamentos fedora, gerenciamento de pacotes dnf, distribuição linux"
---

## O que é o Fedora?

O Fedora é uma distribuição Linux orientada pela comunidade e patrocinada pela Red Hat. É conhecido por disponibilizar tecnologias modernas, uma experiência de desktop refinada e um forte suporte para desenvolvedores e usuários técnicos.

O Fedora tem a reputação de evoluir mais rapidamente do que distribuições mais conservadoras, mantendo o foco na qualidade e usabilidade. Esse equilíbrio o torna atraente para usuários que desejam um sistema Linux moderno sem precisar construir tudo do zero.

:::single-choice{#identify-fedora-project-model} Qual afirmação descreve corretamente o Projeto Fedora?

::option[É uma versão descontinuada do Red Hat Enterprise Linux]{#discontinued-rhel explanation="O Fedora é uma distribuição ativa com lançamentos próprios. Ele é upstream do RHEL, não uma versão obsoleta do RHEL."}
::option[É uma distribuição mantida por um único fabricante de hardware]{#hardware-maintained explanation="O Fedora colabora com fabricantes, mas seu desenvolvimento é orientado pela comunidade e patrocinado pela Red Hat."}
::option[É um projeto comunitário patrocinado pela Red Hat]{#community-sponsored .correct explanation="O Fedora é construído por uma comunidade com patrocínio e apoio da Red Hat. Ele continua sendo uma distribuição comunitária distinta."}
:::

## Por que o Fedora se destaca

O Fedora se destaca porque frequentemente adota novos recursos do Linux antes de distribuições focadas em empresas. Isso o torna atraente para desenvolvedores, colaboradores de código aberto e usuários de desktop que desejam um sistema atualizado com fortes vínculos com o desenvolvimento upstream.

Também é conhecido por oferecer uma experiência padrão limpa. O Fedora Workstation é especialmente popular entre desenvolvedores que buscam um desktop moderno, ferramentas atuais e bom suporte para containers, virtualização e outros fluxos de trabalho de desenvolvimento.

:::single-choice{#match-fedora-user} Qual objetivo de usuário combina melhor com o Fedora Workstation?

::option[Manter uma versão corporativa inalterada por muitos anos]{#long-enterprise-lifecycle explanation="Um ciclo corporativo longo e conservador se aproxima mais do papel do RHEL. O Fedora segue um ritmo mais rápido de lançamentos e atualizações."}
::option[Usar ferramentas atuais de desenvolvimento em um desktop refinado]{#current-developer-desktop .correct explanation="O Fedora Workstation combina um desktop selecionado com ferramentas atuais para desenvolvimento, containers e virtualização. Isso corresponde diretamente ao objetivo."}
::option[Construir manualmente cada componente a partir do código-fonte]{#fedora-manual-source explanation="O Fedora fornece um sistema completo de pacotes e não exige que tudo seja compilado. Esse objetivo descreve um fluxo mais especializado."}
:::

## Fedora e Red Hat

O Fedora desempenha um papel importante no ecossistema da Red Hat. Novas tecnologias e mudanças geralmente aparecem primeiro no Fedora, e parte desse trabalho influencia posteriormente o Red Hat Enterprise Linux (RHEL). Esse relacionamento ajuda a explicar por que o Fedora parece mais atual, enquanto o RHEL é mais conservador e focado no mercado corporativo.

Se você deseja comparar o Fedora com opções orientadas a empresas, veja [Red Hat Enterprise Linux](https://labex.io/lesson/red-hat-enterprise-linux). Se você ainda está comparando famílias de distribuições, [Escolhendo uma Distribuição Linux](https://labex.io/lesson/choosing-a-linux-distribution) oferece uma visão geral mais ampla.

:::single-choice{#explain-fedora-upstream-role} O que significa a relação upstream do Fedora com o RHEL?

::option[As versões do RHEL são copiadas sem alterações para o Fedora depois]{#rhel-copied-to-fedora explanation="Isso inverte a relação. O Fedora evolui mais rapidamente e serve como fonte upstream, não como cópia posterior do RHEL."}
::option[Fedora e RHEL sempre oferecem versões idênticas de software]{#identical-software-versions explanation="As distribuições têm objetivos e calendários diferentes. O RHEL seleciona e estabiliza tecnologias em vez de acompanhar toda versão do Fedora."}
::option[O trabalho desenvolvido no Fedora pode influenciar o RHEL depois]{#fedora-influences-rhel .correct explanation="O Fedora integra tecnologias novas mais cedo. Parte desse trabalho contribui posteriormente para a plataforma corporativa da Red Hat."}
:::

## Lançamentos do Fedora

O Fedora segue um ciclo de lançamento regular, com dois lançamentos principais na maioria dos anos e cerca de treze meses de suporte para cada versão. Comparado com distribuições mais conservadoras, o Fedora tende a entregar kernels, ambientes de desktop e ferramentas de desenvolvedor mais novos em um ritmo mais rápido.

Isso torna o Fedora uma boa escolha para usuários que desejam software atualizado, mas ainda preferem uma distribuição Linux organizada e convencional em vez de um sistema de lançamento contínuo (rolling-release) mais manual.

:::single-choice{#plan-fedora-upgrades} Que manutenção um usuário do Fedora deve esperar desse modelo de lançamento?

::option[Nenhuma atualização de versão durante a vida útil do computador]{#no-version-upgrades explanation="As versões do Fedora têm suporte limitado. Para continuar amparado, é preciso migrar para versões mais novas ao longo do tempo."}
::option[Atualizações regulares de versão para permanecer em uma versão com suporte]{#regular-release-upgrades .correct explanation="O Fedora lança versões em ritmo relativamente rápido e oferece cerca de treze meses de atualizações. Os usuários devem planejar migrações regulares."}
::option[Mudanças contínuas de pacotes sem versões distintas do sistema]{#no-distinct-releases explanation="O Fedora publica versões principais distintas, em vez de funcionar como um lançamento contínuo convencional. Seus pacotes são atuais, mas as versões ainda importam."}
:::

## Gerenciamento de pacotes

O Fedora usa o formato de pacote RPM e o gerenciador de pacotes DNF para instalar, atualizar e remover softwares. O DNF é uma parte central da experiência do Fedora e é uma das principais ferramentas nas quais os usuários confiam para manter o sistema atualizado.

O gerenciamento de pacotes no Fedora é direto e se encaixa naturalmente na família mais ampla de sistemas Red Hat.

:::single-choice{#identify-fedora-package-tool} Qual ferramenta o Fedora usa para gerenciamento de pacotes em alto nível?

::option[APT]{#fedora-apt-tool explanation="O APT está associado a distribuições baseadas no Debian. O Fedora pertence à família RPM e usa o DNF."}
::option[DNF]{#fedora-dnf-tool .correct explanation="O DNF instala, atualiza e remove pacotes dos repositórios Fedora. Por baixo, os pacotes usam o formato RPM."}
::option[Pacman]{#fedora-pacman-tool explanation="Pacman é o gerenciador usado pelo Arch Linux. A ferramenta de alto nível do Fedora é o DNF."}
:::

## Usos comuns

O Fedora é comumente usado em estações de trabalho de desenvolvedores, desktops técnicos e laptops. É especialmente atraente para usuários que desejam um ambiente Linux moderno para programação, containers, máquinas virtuais e trabalho geral de desktop.

Embora o Fedora também possa ser usado em servidores, sua identidade mais forte é geralmente a de uma distribuição Linux atual e amigável para desenvolvedores.

## O Fedora é amigável para iniciantes?

O Fedora pode ser amigável para iniciantes, mas geralmente é mais adequado para usuários que se sentem confortáveis com um sistema que evolui um pouco mais rápido. É mais fácil de abordar do que distribuições altamente manuais, mas pode parecer menos conservador que o Debian ou menos focado em iniciantes do que o Ubuntu ou o Linux Mint.

Para usuários que desejam uma distribuição Linux moderna e não se importam em aprender um pouco conforme avançam, o Fedora é uma excelente opção.

## Leitura adicional

- [Fedora Workstation](https://fedoraproject.org/workstation/)
- [Documentação do Fedora](https://docs.fedoraproject.org/)
- [Ciclo de vida de lançamento do Fedora](https://docs.fedoraproject.org/en-US/releases/lifecycle/)
- [Grupo de Trabalho do Fedora Workstation](https://docs.fedoraproject.org/en-US/workstation-working-group/)

Para desenvolver habilidades reais em Linux após aprender sobre o Fedora, recomendamos estes cursos do LabEx:

1. **[Início Rápido com Linux](https://labex.io/courses/quick-start-with-linux)** - Cobre fundamentos de Linux que se aplicam a muitas distribuições.
2. **[Prática de Comandos Linux Online](https://labex.io/courses/linux-basic-commands-practice-online)** - Fortaleça hábitos de linha de comando importantes no trabalho diário com Linux.
3. **[Gerenciamento de Pacotes RPM e DNF](https://labex.io/courses/rpm-and-dnf-package-management)** - Pratique conceitos de gerenciamento de pacotes relacionados a RPM e DNF.

## Resumo

Agora você consegue explicar o lugar do Fedora como distribuição atual e comunitária no ecossistema Red Hat.

1. Descrever o modelo comunitário e de patrocínio do Fedora.
2. Reconhecer usuários e fluxos atendidos pelo Fedora Workstation.
3. Explicar a relação upstream do Fedora com o RHEL.
4. Planejar atualizações regulares de versão.
5. Identificar o DNF como gerenciador de pacotes do Fedora.
