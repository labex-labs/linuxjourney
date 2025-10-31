---
index: 7
lang: "de"
title: "IPv6"
meta_title: "IPv6 - Subnetting"
meta_description: "Eine Anfängeranleitung für das IPv6-Protokoll. Erfahren Sie, warum IPv6 entwickelt wurde, wie es sich von IPv4 unterscheidet, und verstehen Sie die Grundlagen seines Adressierungsschemas für moderne Linux-Netzwerke."
meta_keywords: "IPv6, IPv4, IP-Adresse, Linux-Netzwerke, Netzwerkprotokolle, Internetprotokoll, Adressknappheit, Anfänger, Tutorial, Leitfaden"
---

## Lesson Content

Jedes Gerät, das sich mit dem Internet verbindet, von Ihrem Server bis zu Ihrem Smartphone, benötigt eine eindeutige IP-Adresse zur Kommunikation. Die am weitesten verbreitete Version, IPv4, bietet eine begrenzte Anzahl von Adressen, ein Limit, das wir in unserer zunehmend vernetzten Welt schnell erreichen. Dieses Problem ist als IPv4-Adressknappheit bekannt.

### Was ist IPv6?

Um dieses Problem zu lösen, entwickelte das Internet Engineering Task Force (IETF) eine neue Version des Internetprotokolls: IPv6. Der Hauptzweck von IPv6 besteht darin, den verfügbaren Pool an IP-Adressen drastisch zu erweitern und so sicherzustellen, dass das Internet weiter wachsen und Milliarden neuer Geräte aufnehmen kann. Es beinhaltet auch andere Verbesserungen des Netzwerkprotokolls.

### IPv4 vs IPv6

Obwohl IPv6 entwickelt wurde, um die Einschränkungen von IPv4 zu beheben, ist seine Einführung schrittweise erfolgt. Es soll IPv4 nicht sofort ersetzen. Stattdessen sind die beiden Netzwerkprotokolle so konzipiert, dass sie koexistieren und sich gegenseitig ergänzen. Viele Netzwerke arbeiten heute im "Dual-Stack"-Modus und unterstützen gleichzeitig sowohl IPv4 als auch IPv6. Wenn Sie mit IPv4 vertraut sind, werden Ihnen die Kernkonzepte von IPv6 leicht fallen.

### Verständnis von IPv6-Adressen

Der bedeutendste Unterschied, den Sie bemerken werden, ist das Adressformat. Eine IPv4-Adresse ist eine 32-Bit-Zahl, die typischerweise als vier Dezimalzahlen dargestellt wird, getrennt durch Punkte (z. B. `192.168.1.1`). Im Gegensatz dazu ist eine IPv6-Adresse eine 128-Bit-Zahl, die in Hexadezimalform geschrieben und durch Doppelpunkte getrennt ist.

Hier ist, wie eine typische IPv6-Adresse aussieht:

```plaintext
2dde:1235:1256:3:200:f8ed:fe23:59cf
```

Dieses längere Format ermöglicht eine weitaus größere Anzahl eindeutiger IP-Adressen und sichert die Zukunft der Internetkonnektivität.

## Exercise

Um die Konzepte von IPv6 zu beherrschen, ist Übung unerlässlich. Hier sind einige praktische Labs, um Ihr Verständnis der IPv6-Adressierung und ihrer Interaktion mit IPv4 in einer Linux-Umgebung zu festigen:

1. **[IPv6-Adressen in Linux konfigurieren und überprüfen](https://labex.io/de/labs/comptia-configure-and-verify-ipv6-addresses-in-linux-592858)** - Üben Sie die Zuweisung statischer IPv6-Adressen und testen Sie die Konnektivität mit den Befehlen `ip` und `ping6`.
2. **[IPv6-DNS-Abfragen in Linux durchführen](https://labex.io/de/labs/comptia-perform-ipv6-dns-lookups-in-linux-592862)** - Lernen Sie, nach AAAA-Einträgen abzufragen und die IPv6-DNS-Auflösung mithilfe von `dig`, `nslookup` und `ping6` zu überprüfen.
3. **[Einen IPv4-zu-IPv6 6to4-Tunnel in Linux konfigurieren](https://labex.io/de/labs/comptia-configure-an-ipv4-to-ipv6-6to4-tunnel-in-linux-592867)** - Sammeln Sie praktische Erfahrungen beim Einrichten eines 6to4-Tunnels, um IPv6-Konnektivität über ein bestehendes IPv4-Netzwerk zu ermöglichen.

Diese Labs helfen Ihnen, die Konzepte von IPv6 in realen Szenarien anzuwenden und Vertrauen in die Netzwerkkonfiguration und Fehlerbehebung aufzubauen.

## Quiz Question

Wie lautet der Name des IP-Protokolls, das entwickelt wurde, um die Anzahl der verfügbaren Adressen für Hosts im Internet zu erhöhen? Bitte antworten Sie auf Englisch mit dem gebräuchlichen Namen des Protokolls und achten Sie auf die Groß-/Kleinschreibung.

## Quiz Answer

IPv6
