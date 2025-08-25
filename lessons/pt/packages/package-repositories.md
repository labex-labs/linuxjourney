---
index: 2
lang: "pt"
title: "Repositórios de Pacotes"
meta_title: "Repositórios de Pacotes - Pacotes"
meta_description: "Aprenda sobre repositórios de pacotes Linux e como eles gerenciam software. Descubra como encontrar e adicionar fontes de pacotes como /etc/apt/sources.list para fácil instalação."
meta_keywords: "repositórios de pacotes Linux, lista de fontes apt, /etc/apt/sources.list, pacotes Linux, Linux para iniciantes, tutorial Linux, gerenciamento de pacotes"
---

## Lesson Content

Como os pacotes enviados para a internet chegam aos nossos computadores? Você vai para a página de download de cada pacote que deseja e clica em baixar e instalar? Embora você possa fazer isso, há uma solução melhor: repositórios de pacotes. Repositórios são locais de armazenamento central para pacotes. Existem toneladas de repositórios contendo muitos pacotes e, o melhor de tudo, todos eles são encontrados na internet — sem discos de instalação bobos. Sua máquina não sabe onde procurar esses repositórios, a menos que você explicitamente diga a ela onde procurar.

Por exemplo, digamos que eu queira o Docker Software na minha máquina. O Docker gerencia seus próprios repositórios para seus pacotes de contêineres. Dentro deste repositório, existem vários pacotes, como o pacote `docker-ce`, o pacote `docker-ce-cli`, o pacote `containerd.io`, etc. O Docker hospeda este repositório em um link de origem chamado: `https://download.docker.com/linux/ubuntu`

Agora, em vez de ir ao site deles para baixar o pacote diretamente, você pode dizer à sua máquina para encontrar o software Docker a partir do link de origem.

Sua distribuição já vem com fontes pré-aprovadas para obter pacotes, e é assim que ela instala todos os pacotes base que você vê em seu sistema. Em um sistema Debian, este arquivo de fontes é o arquivo `/etc/apt/sources.list`. Sua máquina saberá onde procurar e verificar quaisquer repositórios de origem que você adicionou.

## Exercise

A prática leva à perfeição! Aqui estão alguns laboratórios práticos para reforçar sua compreensão do gerenciamento de pacotes e repositórios Linux:

1. **[Instalação de Software no Linux](https://labex.io/pt/labs/linux-software-installation-on-linux-18005)** - Pratique vários métodos para instalar e gerenciar software em sistemas Ubuntu, incluindo o uso de `apt` e o manuseio de arquivos `.deb`, diretamente relacionados ao conceito de `sources.list`.
2. **[Instalando e Removendo Pacotes](https://labex.io/pt/labs/linux-installing-and-removing-packages-385380)** - Aprenda a atualizar o sistema, instalar e remover pacotes em um sistema baseado em Debian, solidificando sua compreensão de como os gerenciadores de pacotes interagem com os repositórios.
3. **[Consultar e Atualizar Pacotes com YUM no Linux](https://labex.io/pt/labs/rhel-query-and-update-packages-with-yum-in-linux-590869)** - Explore como gerenciar pacotes de software em sistemas Linux baseados em RHEL usando `YUM`, fornecendo uma perspectiva mais ampla sobre o gerenciamento de pacotes em diferentes distribuições.

Esses laboratórios o ajudarão a aplicar os conceitos de repositórios de pacotes e gerenciamento de software em cenários reais e a construir confiança com as tarefas de administração do sistema.

## Quiz Question

Onde está o arquivo de fontes em um sistema Debian?

## Quiz Answer

/etc/apt/sources.list
