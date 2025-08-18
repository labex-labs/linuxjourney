---
lang: "pt"
title: "Instalação do Kernel"
meta_description: "Aprenda como instalar e gerenciar kernels Linux. Descubra as versões do kernel, use `uname -r` e os comandos apt. Comece sua jornada no kernel Linux!"
meta_keywords: "kernel Linux, instalar kernel, uname -r, apt dist-upgrade, gerenciamento de kernel, tutorial Linux, Linux para iniciantes, guia Linux"
---

## Lesson Content

Ok, agora que tiramos todo esse material chato do caminho, vamos falar sobre como realmente instalar e modificar kernels. Você pode instalar vários kernels em seu sistema; lembra-se da nossa lição sobre o processo de inicialização? No nosso menu GRUB, podemos escolher qual kernel inicializar.

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

E então é só reiniciar no kernel que você instalou. Simples, certo? Mais ou menos. Você também precisará instalar outros pacotes Linux, como `linux-headers`, `linux-image-generic`, etc. Você também pode especificar o número da versão, então o comando acima pode parecer: **`sudo apt install 3.19.0-43-generic`**

Alternativamente, se você quiser apenas a versão atualizada do kernel, basta usar `dist-upgrade`; ele realiza atualizações para todos os pacotes em seu sistema:

```bash
sudo apt dist-upgrade
```

Existem muitas versões diferentes de kernel. Algumas são usadas como LTS (Long Term Support), algumas são as mais recentes e melhores. A compatibilidade pode ser muito diferente entre as versões do kernel, então você pode querer experimentar diferentes kernels.

## Exercise

1. Descubra qual versão do kernel você tem.
2. Pesquise as diferentes versões de kernels disponíveis.

## Quiz Question

Como você vê a versão do kernel do seu sistema?

## Quiz Answer

uname -r
