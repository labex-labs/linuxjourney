---
index: 1
lang: "pt"
title: "diretório /dev"
meta_title: "/dev directory - Dispositivos"
meta_description: "Aprenda sobre o diretório /dev no Linux, onde os arquivos de dispositivo são armazenados. Entenda os nós de dispositivo e como interagir com eles. Explore /dev com ls. Guia para iniciantes em Linux."
meta_keywords: "diretório /dev, arquivos de dispositivo Linux, nós de dispositivo, tutorial Linux, ls /dev, iniciante Linux, guia Linux"
---

## Lesson Content

Quando você conecta um dispositivo à sua máquina, ele geralmente precisa de um driver de dispositivo para funcionar corretamente. Você pode interagir com drivers de dispositivo por meio de arquivos de dispositivo ou nós de dispositivo; estes são arquivos especiais que se parecem com arquivos comuns. Como esses arquivos de dispositivo são como arquivos comuns, você pode usar programas como `ls`, `cat`, etc., para interagir com eles. Esses arquivos de dispositivo são geralmente armazenados no diretório `/dev`. Vá em frente e execute `ls` no diretório `/dev` do seu sistema; você verá uma grande quantidade de arquivos de dispositivo que estão no seu sistema.

```bash
ls /dev
```

Alguns desses dispositivos você já usou e interagiu, como `/dev/null`. Lembre-se de quando enviamos a saída para `/dev/null`, o kernel sabe que este dispositivo recebe toda a nossa entrada e simplesmente a descarta, então nada é retornado.

Antigamente, se você quisesse adicionar um dispositivo ao seu sistema, você adicionaria o arquivo de dispositivo em `/dev` e provavelmente esqueceria dele. Bem, repita isso algumas vezes, e você pode ver onde havia um problema. O diretório `/dev` ficaria cheio de arquivos de dispositivo estáticos de dispositivos que você já havia atualizado, parado de usar, etc. Os dispositivos também são atribuídos a arquivos de dispositivo na ordem em que o kernel os encontra. Assim, se a cada vez que você reiniciava seu sistema, os dispositivos poderiam ter arquivos de dispositivo diferentes dependendo de quando foram descobertos.

Felizmente, não usamos mais esse método. Agora temos algo que usamos para adicionar e remover dinamicamente dispositivos que estão sendo usados no sistema, e discutiremos isso nas próximas lições.

## Exercise

A prática leva à perfeição! Aqui estão alguns laboratórios práticos para reforçar sua compreensão dos dispositivos de hardware e sua interação com o sistema Linux:

1. **[Explorar Dispositivos de Hardware no Linux](https://labex.io/pt/labs/comptia-explore-hardware-devices-in-linux-590861)** - Neste laboratório, você aprenderá as habilidades essenciais para explorar, identificar e inspecionar dispositivos de hardware em um ambiente Linux. Você ganhará experiência prática com poderosas utilidades de linha de comando para entender como o sistema operacional interage com os componentes físicos.

Este laboratório o ajudará a aplicar os conceitos de interação de dispositivos em cenários reais e a construir confiança no gerenciamento de hardware no Linux.

## Quiz Question

Onde os arquivos de dispositivo são armazenados no sistema?

## Quiz Answer

/dev
