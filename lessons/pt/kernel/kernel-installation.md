---
index: 4
lang: "pt"
title: "Instalação do Kernel"
meta_title: "Instalação do Kernel - Kernel"
meta_description: "Aprenda como instalar e gerenciar kernels Linux. Descubra versões de kernel, use `uname -r` e comandos apt. Comece sua jornada no kernel Linux!"
meta_keywords: "kernel Linux, instalar kernel, uname -r, apt dist-upgrade, gerenciamento de kernel, tutorial Linux, Linux para iniciantes, guia Linux"
---

## Lesson Content

Ok, agora que tiramos todo aquele material chato do caminho, vamos falar sobre como realmente instalar e modificar kernels. Você pode instalar vários kernels em seu sistema; lembra da nossa lição sobre o processo de boot? No nosso menu GRUB, podemos escolher qual kernel inicializar.

Para ver qual versão do kernel você tem em seu sistema, use o seguinte comando:

```bash
$ uname -r
3.19.0-43-generic
```

O comando `uname` imprime informações do sistema; a opção `-r` imprimirá a versão de lançamento do kernel.

Você pode instalar o kernel Linux de diferentes maneiras: você pode baixar o pacote fonte e compilar a partir do código-fonte, ou pode instalá-lo usando ferramentas de gerenciamento de pacotes.

```bash
sudo apt install linux-generic-lts-vivid
```

E então é só reiniciar no kernel que você instalou. Simples, certo? Mais ou menos. Você também precisará instalar outros pacotes Linux, como `linux-headers`, `linux-image-generic`, etc. Você também pode especificar o número da versão, então o comando acima pode ser: **`sudo apt install 3.19.0-43-generic`**

Alternativamente, se você quiser apenas a versão atualizada do kernel, basta usar `dist-upgrade`; ele realiza atualizações em todos os pacotes do seu sistema:

```bash
sudo apt dist-upgrade
```

Existem muitas versões diferentes de kernel. Algumas são usadas como LTS (Long Term Support), outras são as mais recentes e melhores. A compatibilidade pode ser muito diferente entre as versões do kernel, então você pode querer experimentar diferentes kernels.

## Exercise

A prática leva à perfeição! Aqui estão alguns laboratórios práticos para reforçar sua compreensão do gerenciamento do kernel Linux e tarefas relacionadas de administração do sistema:

1. **[Personalizar o Menu de Inicialização GRUB2 no Linux](https://labex.io/pt/labs/comptia-customize-the-grub2-boot-menu-in-linux-590859)** - Pratique a modificação do menu de inicialização GRUB2, o que é essencial ao gerenciar várias versões de kernel e selecionar qual inicializar.
2. **[Gerenciar Módulos do Kernel no Linux](https://labex.io/pt/labs/comptia-manage-kernel-modules-in-linux-590865)** - Aprenda a listar, inspecionar, carregar e descarregar módulos do kernel, um aspecto fundamental do gerenciamento do kernel e da compreensão de como o hardware interage com seu sistema.
3. **[Instalação de Software no Linux](https://labex.io/pt/labs/linux-software-installation-on-linux-18005)** - Ganhe experiência prática com vários métodos para instalar e gerenciar software, incluindo o uso de gerenciadores de pacotes, que é uma forma comum de instalar e atualizar kernels.

Esses laboratórios o ajudarão a aplicar os conceitos de gerenciamento de kernel, processos de inicialização e gerenciamento de pacotes em cenários reais, construindo confiança com a administração do sistema.

## Quiz Question

Como você vê a versão do kernel do seu sistema?

## Quiz Answer

uname -r
