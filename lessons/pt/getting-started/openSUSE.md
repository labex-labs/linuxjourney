---
lesson_id: "openSUSE"
course_id: "getting-started"
lang: "pt"
order_index: 10
title: "openSUSE"
description: "Aprenda como o openSUSE oferece lançamentos regulares e contínuos com as ferramentas de administração Zypper e YaST."
meta_title: "Distribuição Linux openSUSE"
meta_description: "Saiba o que é a distribuição Linux openSUSE, as diferenças entre Leap e Tumbleweed, como funciona o gerenciamento de pacotes RPM e por que o YaST destaca o openSUSE."
meta_keywords: "distribuição opensuse, distribuição linux opensuse, o que é opensuse, opensuse leap, opensuse tumbleweed, yast, gerenciamento de pacotes rpm"
---

## O que é o openSUSE?

O openSUSE é uma distribuição Linux de longa data, conhecida pela sua flexibilidade, ferramentas de administração robustas e múltiplas opções de lançamento. É um projeto comunitário com reputação de ser polido e capaz, tanto em desktops quanto em sistemas técnicos.

Uma das razões pelas quais o openSUSE se destaca é que ele oferece caminhos diferentes para usuários diferentes. Alguns usuários desejam uma base estável, enquanto outros preferem um modelo de lançamento contínuo (rolling release) mais ágil.

## Leap e Tumbleweed

O openSUSE é conhecido por duas abordagens principais de lançamento: Leap e Tumbleweed. O Leap é a opção mais conservadora, voltada para usuários que buscam estabilidade e um modelo de lançamento tradicional. O Tumbleweed é um lançamento contínuo para usuários que desejam softwares mais recentes entregues de forma contínua.

Essa divisão confere ao openSUSE uma flexibilidade incomum. Os usuários podem escolher o estilo que melhor lhes convém, em vez de mudar completamente para uma família de distribuição diferente.

:::single-choice{#choose-opensuse-leap} Qual opção do openSUSE é mais adequada a quem deseja um lançamento tradicional e regular?

::option[Tumbleweed]{#tumbleweed-release explanation="O Tumbleweed é o lançamento contínuo do openSUSE. Ele atende melhor a usuários que priorizam pacotes mais recentes."}
::option[YaST]{#yast-not-release explanation="YaST é uma ferramenta de instalação e configuração, não um modelo de lançamento do openSUSE. Ela pode ser usada para administrar o sistema."}
::option[Leap]{#leap-release .correct explanation="O Leap segue um modelo de lançamentos regulares e enfatiza uma base mais conservadora. Isso corresponde à preferência indicada."}
:::

:::single-choice{#recognize-tumbleweed-model} O que diferencia o Tumbleweed do Leap?

::option[Ele entrega continuamente atualizações testadas de pacotes]{#continuous-tested-updates .correct explanation="O Tumbleweed é um lançamento contínuo que publica snapshots testados. Os usuários recebem software novo sem esperar por uma grande versão regular."}
::option[Ele recebe software apenas por grandes versões fixas]{#fixed-major-releases explanation="Versões regulares fixas descrevem melhor o Leap. O Tumbleweed é atualizado continuamente."}
::option[Ele remove o gerenciamento de pacotes do sistema operacional]{#no-package-management explanation="O Tumbleweed continua gerenciando pacotes e atualizações do sistema. Lançamento contínuo descreve a frequência, não a ausência de gerenciamento."}
:::

## Gerenciamento de pacotes

O openSUSE utiliza o formato de pacote RPM e ferramentas como o `zypper` para instalar, atualizar e remover softwares. Isso o coloca em uma família de pacotes diferente da do Debian e do Ubuntu, que utilizam pacotes `.deb` e o APT.

Compreender as famílias de pacotes é útil ao comparar distribuições Linux. Se você deseja uma comparação mais ampla, consulte [Escolhendo uma Distribuição Linux](https://labex.io/lesson/choosing-a-linux-distribution).

:::single-choice{#identify-zypper-role} Para que o `zypper` é usado no openSUSE?

::option[Selecionar temas de papel de parede do desktop]{#zypper-wallpaper explanation="A aparência do desktop é configurada por ferramentas gráficas. O `zypper` gerencia pacotes de software."}
::option[Instalar, atualizar e remover pacotes de software]{#zypper-package-tool .correct explanation="O `zypper` é a ferramenta de linha de comando do openSUSE para gerenciar pacotes. Ele trabalha com software de repositórios RPM."}
::option[Transformar o Tumbleweed em uma versão fixa do Debian]{#zypper-debian explanation="O gerenciamento de pacotes não transforma o openSUSE em outra família. Leap e Tumbleweed continuam sendo opções do openSUSE."}
:::

## YaST

Uma das características mais conhecidas do openSUSE é o **YaST**. O YaST é uma ferramenta de administração e configuração que ajuda a gerenciar softwares, serviços, armazenamento, rede e outras tarefas do sistema a partir de uma interface central.

Este é um dos principais motivos pelos quais o openSUSE atrai usuários que desejam ferramentas poderosas de administração de sistema sem precisar configurar tudo manualmente.

:::single-choice{#identify-yast-purpose} O que o YaST foi projetado para oferecer?

::option[Um repositório contínuo apenas com os aplicativos mais novos]{#yast-repository explanation="O Tumbleweed oferece o modelo de repositório contínuo. O YaST é uma ferramenta de administração e configuração, não uma ramificação de software."}
::option[Um formato de pacote compartilhado com Debian e Ubuntu]{#yast-package-format explanation="O openSUSE usa pacotes RPM e sistemas Debian usam `.deb`. O próprio YaST não é um formato de pacote."}
::option[Uma interface central para instalação e configuração do sistema]{#yast-administration .correct explanation="O YaST combina a instalação com módulos para configurar várias partes do openSUSE. Ele está disponível em interfaces gráficas e de terminal."}
:::

## Usos comuns

O openSUSE funciona bem em desktops, sistemas de desenvolvimento e estações de trabalho técnicas. Também é atraente para usuários que desejam um controle rigoroso sobre a configuração do sistema, mantendo ferramentas polidas.

Comparado a distribuições mais focadas em iniciantes, o openSUSE frequentemente atrai usuários que desejam um pouco mais de estrutura e visibilidade administrativa.

## Quem deve usar o openSUSE?

O openSUSE é uma opção sólida para usuários que desejam flexibilidade no estilo de lançamento e apreciam ferramentas de gerenciamento poderosas. Ele pode funcionar para iniciantes, especialmente aqueles que gostam de administração gráfica, mas é frequentemente atraente para usuários intermediários e usuários técnicos de desktop.

## Leitura adicional

- [Distribuições Desktop do openSUSE](https://get.opensuse.org/desktop/)
- [Tumbleweed](https://get.opensuse.org/tumbleweed/)
- [Leap](https://get.opensuse.org/leap/)
- [YaST](https://yast.opensuse.org/)

Para continuar após esta introdução ao openSUSE, recomendamos estes cursos do LabEx:

1. **[Início Rápido com Linux](https://labex.io/courses/quick-start-with-linux)** - Aprenda os fundamentos de Linux com prática guiada.
2. **[Prática de Comandos Linux Online](https://labex.io/courses/linux-basic-commands-practice-online)** - Ganhe familiaridade com a linha de comando do Linux.
3. **[Torne-se um Administrador de Sistemas Júnior](https://labex.io/courses/become-a-junior-system-administrator)** - Continue com tópicos mais amplos de administração de sistemas Linux.

## Resumo

Agora você consegue comparar as opções de lançamento do openSUSE e identificar suas principais ferramentas de administração.

1. Escolher entre Leap e Tumbleweed conforme a preferência de lançamento.
2. Explicar como o Tumbleweed entrega atualizações contínuas.
3. Identificar o Zypper como ferramenta de gerenciamento de pacotes.
4. Reconhecer o YaST como interface central de configuração.
