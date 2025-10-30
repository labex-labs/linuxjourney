---
index: 1
lang: "de"
title: "IPv4"
meta_title: "IPv4 - Subnetting"
meta_description: "Entdecken Sie den besten Weg, Linux-Netzwerke zu lernen, indem Sie IPv4-Adressen verstehen. Dieser Leitfaden für Anfänger behandelt die IP-Struktur und wie Sie Ihre IP über die Kommandozeile finden."
meta_keywords: "IPv4, IP-Adresse, Linux für Anfänger, bester Weg, Linux zu lernen, Linux-Kommandozeile für Anfänger, ifconfig, ip addr, Netzwerk Grundlagen"
---

## Lesson Content

Jedes Gerät, das mit einem Netzwerk verbunden ist, verfügt über eine eindeutige Adresse, bekannt als IP-Adresse (Internet Protocol). Für diesen Kurs konzentrieren wir uns auf IPv4-Adressen, den häufigsten Typ, dem Sie begegnen werden. Ihr Verständnis ist ein Kernbestandteil beim Erlernen der Netzwerktechnik unter Linux.

Eine IPv4-Adresse ist eine 32-Bit-Zahl, die typischerweise in einem für Menschen lesbaren Format dargestellt wird, wie dieses:

```
204.23.124.23
```

Diese Adresse besteht aus zwei unterschiedlichen Teilen: dem **Netzwerkanteil**, der das spezifische Netzwerk identifiziert, in dem sich das Gerät befindet, und dem **Hostanteil**, der das spezifische Gerät in diesem Netzwerk identifiziert.

### Die Struktur einer IP-Adresse

Eine IPv4-Adresse ist in vier durch Punkte getrennte Abschnitte unterteilt. Jeder Abschnitt wird als **Oktett** bezeichnet. In der Informatik ist ein Oktett eine Gruppe von 8 Bits, und da 8 Bits 1 Byte entsprechen, ist eine IPv4-Adresse 4 Bytes lang. Diese Struktur ist grundlegend, und ihre Beherrschung ist eine der `besten Ressourcen, um die Linux-Befehlszeile für Anfänger` im Bereich Netzwerktechnik zu erlernen.

### Finden Ihrer IP-Adresse unter Linux

Für jeden `Anfänger in Linux` ist eine der ersten Aufgaben, die IP-Adresse des Systems zu finden. Dies können Sie mithilfe von Befehlszeilentools tun.

Der traditionelle Befehl hierfür ist `ifconfig`. Obwohl er auf vielen Systemen noch vorhanden ist, gilt er als veraltet.

```bash
pete@icebox:~$ ifconfig -a
eth0      Link encap:Ethernet  HWaddr 1d:3a:32:24:4d:ce
          inet addr:192.168.1.129  Bcast:192.168.1.255  Mask:255.255.255.0
          inet6 addr: fd60::21c:29ff:fe63:5cdc/64 Scope:Link
```

In der obigen Ausgabe ist die IPv4-Adresse `192.168.1.129`.

### Der moderne Ansatz mit ip addr

Der `beste Weg, Linux`-Netzwerktechnik heute zu erlernen, beinhaltet die Verwendung des modernen `ip`-Befehls. Der Befehl `ip addr` hat `ifconfig` ersetzt und ist der Standard auf den meisten aktuellen Linux-Distributionen.

```bash
pete@icebox:~$ ip addr show
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 1d:3a:32:24:4d:ce brd ff:ff:ff:ff:ff:ff
    inet 192.168.1.129/24 brd 192.168.1.255 scope global dynamic eth0
       valid_lft 85646sec preferred_lft 85646sec
```

Hier finden Sie dieselbe IPv4-Adresse, `192.168.1.129`, aufgeführt neben `inet` für die Schnittstelle `eth0`.

## Exercise

Üben Sie Ihre Fähigkeiten mit diesen praktischen Labs, um Ihr Verständnis von IP-Adressierung und Netzwerkerkennung unter Linux zu festigen:

1. **[MAC- und IP-Adressen unter Linux identifizieren](https://labex.io/de/labs/comptia-identify-mac-and-ip-addresses-in-linux-592731)** - Üben Sie die Verwendung des Befehls `ip a`, um Netzwerkadressinformationen, einschließlich IPv4- und IPv6-Adressen, auf einem Linux-System zu identifizieren.
2. **[IP-Adress-Typen und Erreichbarkeit unter Linux erkunden](https://labex.io/de/labs/comptia-explore-ip-address-types-and-reachability-in-linux-592780)** - Erkunden Sie verschiedene IP-Adress-Typen und testen Sie die Netzwerkerreichbarkeit mit Befehlen wie `ping` und `ip a`.
3. **[IP-Subnetting und Binärkonvertierung im Linux-Terminal durchführen](https://labex.io/de/labs/comptia-perform-ip-subnetting-and-binary-conversion-in-the-linux-terminal-592782)** - Meistern Sie IP-Subnetting und Binärkonvertierung, unerlässlich für ein tieferes Verständnis der Struktur von IP-Adressen und Netzwerken auf Bit-Ebene.

Diese Labs helfen Ihnen, die Konzepte der IP-Adressierung in realen Szenarien anzuwenden und Vertrauen in die Netzwerkkonfiguration und Fehlerbehebung unter Linux aufzubauen.

## Quiz Question

Wie viele Bytes hat eine IPv4-Adresse?

## Quiz Answer

4
