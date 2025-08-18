---
lang: "pt"
title: "Diretório /dev"
meta_description: "Aprenda sobre o diretório /dev no Linux, onde os arquivos de dispositivo são armazenados. Entenda os nós de dispositivo e como interagir com eles. Explore /dev com ls. Guia para iniciantes em Linux."
meta_keywords: "diretório /dev, arquivos de dispositivo Linux, nós de dispositivo, tutorial Linux, ls /dev, Linux para iniciantes, guia Linux"
---

## Lesson Content

Quando você conecta um dispositivo à sua máquina, ele geralmente precisa de um driver de dispositivo para funcionar corretamente. Você pode interagir com drivers de dispositivo através de arquivos de dispositivo ou nós de dispositivo; estes são arquivos especiais que se parecem com arquivos comuns. Como esses arquivos de dispositivo são como arquivos comuns, você pode usar programas como `ls`, `cat`, etc., para interagir com eles. Esses arquivos de dispositivo são geralmente armazenados no diretório `/dev`. Vá em frente e use `ls` no diretório `/dev` do seu sistema; você verá uma grande quantidade de arquivos de dispositivo que estão no seu sistema.

```bash
ls /dev
```

Alguns desses dispositivos você já usou e interagiu, como `/dev/null`. Lembre-se de que quando enviamos a saída para `/dev/null`, o kernel sabe que este dispositivo pega toda a nossa entrada e simplesmente a descarta, então nada é retornado.

Antigamente, se você quisesse adicionar um dispositivo ao seu sistema, você adicionaria o arquivo de dispositivo em `/dev` e provavelmente esqueceria dele. Bem, repita isso algumas vezes, e você pode ver onde havia um problema. O diretório `/dev` ficaria desordenado com arquivos de dispositivo estáticos de dispositivos que você há muito tempo atualizou, parou de usar, etc. Os dispositivos também são atribuídos a arquivos de dispositivo na ordem em que o kernel os encontra. Então, se toda vez que você reiniciava seu sistema, os dispositivos poderiam ter arquivos de dispositivo diferentes dependendo de quando foram descobertos.

Felizmente, não usamos mais esse método. Agora temos algo que usamos para adicionar e remover dinamicamente dispositivos que estão sendo usados no sistema, e discutiremos isso nas próximas lições.

## Exercise

Verifique o conteúdo do diretório `/dev`. Você reconhece algum dispositivo familiar?

## Quiz Question

Onde os arquivos de dispositivo são armazenados no sistema?

## Quiz Answer

/dev
