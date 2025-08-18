---
index: 2
lang: "pt"
title: "Repositórios de Pacotes"
meta_title: "Repositórios de Pacotes - Pacotes"
meta_description: "Aprenda sobre repositórios de pacotes Linux e como eles gerenciam software. Descubra como encontrar e adicionar fontes de pacotes como /etc/apt/sources.list para fácil instalação."
meta_keywords: "repositórios de pacotes Linux, lista de fontes apt, /etc/apt/sources.list, pacotes Linux, Linux para iniciantes, tutorial de Linux, gerenciamento de pacotes"
---

## Lesson Content

Como os pacotes enviados para a internet chegam aos nossos computadores? Você vai à página de download de cada pacote que deseja e clica em baixar e instalar? Embora você possa fazer isso, há uma solução melhor: repositórios de pacotes. Repositórios são locais de armazenamento central para pacotes. Existem muitos repositórios contendo vários pacotes e, o melhor de tudo, todos eles são encontrados na internet — sem discos de instalação bobos. Sua máquina não sabe onde procurar esses repositórios a menos que você explicitamente diga a ela onde procurar.

Por exemplo, digamos que eu queira o software Docker na minha máquina. A Docker gerencia seus próprios repositórios para seus pacotes de containers. Dentro deste repositório, há múltiplos pacotes, como o pacote docker-ce, o pacote docker-ce-cli, o pacote containerd.io, etc. A Docker hospeda este repositório em um link de origem chamado: `https://download.docker.com/linux/ubuntu`

Agora, em vez de ir ao site deles para baixar o pacote diretamente, você pode dizer à sua máquina para encontrar o software Docker a partir do link de origem.

Sua distribuição já vem com fontes pré-aprovadas para obter pacotes, e é assim que ela instala todos os pacotes base que você vê em seu sistema. Em um sistema Debian, este arquivo de fontes é o arquivo `/etc/apt/sources.list`. Sua máquina saberá procurar lá e verificar quaisquer repositórios de origem que você adicionou.

## Exercise

No exercises for this lesson.

## Quiz Question

Onde está o arquivo de fontes em um sistema Debian?

## Quiz Answer

/etc/apt/sources.list
