---
title: "IPv4"
description: "Erfahren Sie mehr über IPv4-Adressen, ihre Struktur und wie Sie Ihre IP mit ifconfig finden. Verstehen Sie die Grundlagen der Netzwerktechnik für Linux-Anfänger."
keywords: "IPv4, IP-Adresse, ifconfig, Netzwerk-Grundlagen, Linux-Netzwerk, Anfänger, Tutorial, Anleitung"
---

## Lesson Content

Wir wissen also, dass Netzwerk-Hosts eine eindeutige Adresse haben, unter der sie gefunden werden können. Diese Adressen werden als IP-Adressen bezeichnet. Eine IPv4-Adresse sieht etwa so aus:

```
204.23.124.23
```

Diese Adresse enthält tatsächlich zwei Teile: den Netzwerkanteil, der uns sagt, in welchem Netzwerk sie sich befindet, und den Host-Anteil, der uns sagt, welcher Host in diesem Netzwerk es ist. In diesem Kurs werden wir uns hauptsächlich mit IPv4-Adressen befassen, die Sie üblicherweise sehen werden, wenn von IP-Adressen die Rede ist.

Eine IP-Adresse wird durch Punkte in Oktette unterteilt. Eine IPv4-Adresse besteht also aus 4 Oktetten. Wenn Sie ein wenig Informatikkenntnisse haben, ist ein Oktett 8 Bit, und 8 Bit entsprechen tatsächlich 1 Byte, daher bezeichnen wir eine IPv4-Adresse auch als 4 Bytes. Wir verwenden Bits häufig, wenn wir mit Subnetzen und IP-Adressen arbeiten.

Sie können Ihre IP-Adresse mit dem Befehl `ifconfig -a` anzeigen:

```bash
pete@icebox:~$ ifconfig -a
eth0      Link encap:Ethernet  HWaddr 1d:3a:32:24:4d:ce
          inet addr:192.168.1.129  Bcast:192.168.1.255  Mask:255.255.255.0
          inet6 addr: fd60::21c:29ff:fe63:5cdc/64 Scope:Link
```

Wie Sie sehen können, ist meine IPv4-Adresse: 192.168.1.129

## Exercise

Finden Sie Ihre IP-Adresse mit `ifconfig`.

## Quiz Question

Wie viele Bytes hat eine IPv4-Adresse?

## Quiz Answer

4
