---
index: 1
lang: "de"
title: "IPv4"
meta_title: "IPv4 - Subnetting"
meta_description: "Beginnen Sie Ihre Reise mit unserem kompletten Linux-Tutorial zu IPv4-Adressen. Dieser Leitfaden für Linux-Anfänger ist der beste Weg, um Linux-Netzwerke zu erlernen, einschließlich IP-Struktur und wesentlicher Befehlszeilentools wie ip addr."
meta_keywords: "IPv4, IP-Adresse, Linux für Anfänger, bester Weg, Linux zu lernen, komplettes Linux-Tutorial, bester kostenloser Linux-Kurs online, kostenlose Linux-Zertifizierungskurse, Linux-Netzwerke, ifconfig, ip addr"
---

## Lesson Content

Jedes Gerät in einem Netzwerk hat eine eindeutige Kennung, die als IP-Adresse (Internet Protocol) bezeichnet wird. Diese Lektion, ein wichtiger Teil unseres `kompletten Linux-Tutorials`, konzentriert sich auf IPv4-Adressen – den häufigsten Typ, dem Sie begegnen werden. Für jeden `Linux-Anfänger` ist das Verständnis von IPv4 ein entscheidender erster Schritt in die Welt der Netzwerke.

### Warum IPv4 unerlässlich ist

Das Lernen über IPv4 ist grundlegend für jeden, der es ernst meint mit Systemadministration oder Netzwerkmanagement. Es bildet das Rückgrat der meisten Netzwerkkommunikation. Dieser Leitfaden bietet den `besten Weg, Linux-Netzwerke` von Grund auf zu erlernen. Obwohl dies keines dieser `kostenlosen Linux-Zertifizierungskurse` ist, ist die Beherrschung dieser Grundlagen ein wichtiger Schritt in Richtung professioneller Zertifizierung.

### IPv4-Adressstruktur

Eine IPv4-Adresse ist eine 32-Bit-Zahl, wird aber normalerweise in einem für Menschen lesbaren Format angezeigt, wie diesem:

```
204.23.124.23
```

Diese Adresse hat zwei Hauptteile: den **Netzwerkanteil**, der das Netzwerk identifiziert, und den **Hostanteil**, der das spezifische Gerät in diesem Netzwerk identifiziert. Die Adresse ist in vier durch Punkte getrennte Abschnitte unterteilt, wobei jeder Abschnitt ein **Oktett** genannt wird. Ein Oktett ist eine Gruppe von 8 Bits, was bedeutet, dass eine IPv4-Adresse 4 Bytes (32 Bits) lang ist. Das Verständnis dieser Struktur ist entscheidend für die Netzwerkkonfiguration und Fehlerbehebung.

### So finden Sie Ihre IP-Adresse

Eine der ersten Aufgaben für jeden Linux-Benutzer ist es, die IP-Adresse seines Systems zu finden. Dies können Sie mit einfachen Befehlszeilentools tun. Der traditionelle Befehl hierfür ist `ifconfig`. Obwohl er auf vielen Systemen noch zu finden ist, gilt er als veraltet.

```bash
pete@icebox:~$ ifconfig -a
eth0      Link encap:Ethernet  HWaddr 1d:3a:32:24:4d:ce
          inet addr:192.168.1.129  Bcast:192.168.1.255  Mask:255.255.255.0
          inet6 addr: fd60::21c:29ff:fe63:5cdc/64 Scope:Link
```

In der obigen Ausgabe ist die IPv4-Adresse `192.168.1.129`.

### Verwendung des ip addr-Befehls

Die moderne und empfohlene Methode verwendet den `ip`-Befehl. Der Befehl `ip addr` hat `ifconfig` ersetzt und ist der Standard auf den meisten aktuellen Linux-Distributionen. Er liefert detailliertere Informationen und ist das Werkzeug, auf dessen Erlernen Sie sich konzentrieren sollten.

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

Üben Sie Ihre Fähigkeiten mit diesen praktischen Labs, um Ihr Verständnis von IP-Adressierung und Netzwerkerkennung in Linux zu festigen:

1. **[MAC- und IP-Adressen in Linux identifizieren](https://labex.io/de/labs/comptia-identify-mac-and-ip-addresses-in-linux-592731)** - Üben Sie die Verwendung des Befehls `ip a`, um Netzwerkadressinformationen, einschließlich IPv4- und IPv6-Adressen, auf einem Linux-System zu identifizieren.
2. **[IP-Adress-Typen und Erreichbarkeit in Linux erkunden](https://labex.io/de/labs/comptia-explore-ip-address-types-and-reachability-in-linux-592780)** - Erkunden Sie verschiedene IP-Adress-Typen und testen Sie die Netzwerkerreichbarkeit mit Befehlen wie `ping` und `ip a`.
3. **[IP-Subnetting und Binärkonvertierung im Linux-Terminal durchführen](https://labex.io/de/labs/comptia-perform-ip-subnetting-and-binary-conversion-in-the-linux-terminal-592782)** - Meistern Sie IP-Subnetting und Binärkonvertierung, was für ein tieferes Verständnis der Struktur von IP-Adressen und Netzwerken auf Bit-Ebene unerlässlich ist.

Diese Labs helfen Ihnen, die Konzepte der IP-Adressierung in realen Szenarien anzuwenden und Vertrauen in die Netzwerkkonfiguration und Fehlerbehebung unter Linux aufzubauen.

## Quiz Question

Wie viele Bytes hat eine IPv4-Adresse?

## Quiz Answer

4
