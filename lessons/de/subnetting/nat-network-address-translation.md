---
index: 6
lang: "de"
title: "NAT"
meta_title: "NAT - Subnetting"
meta_description: "Erfahren Sie mehr über NAT (Network Address Translation) in Linux, wie es funktioniert und welche Rolle es bei der Netzwerksicherheit spielt. Verstehen Sie private vs. öffentliche IPs. Linux-Netzwerkanleitung."
meta_keywords: "NAT, Network Address Translation, Linux-Netzwerk, private IP, öffentliche IP, Linux-Tutorial, Anfängerleitfaden"
---

## Lesson Content

Wir haben NAT (Network Address Translation) schon einmal erwähnt, aber nicht näher darauf eingegangen. Wenn wir an unserem Netzwerk arbeiten, bedeutet das, dass das Internet unsere IP-Adresse sehen kann? Nicht ganz.

NAT lässt ein Gerät wie unseren Router als Vermittler zwischen dem Internet und einem privaten Netzwerk agieren. So ist nur eine einzige, eindeutige IP-Adresse erforderlich, um eine ganze Gruppe von Computern darzustellen.

Stellen Sie sich NAT wie eine Empfangsdame in einem großen Büro vor. Wenn jemand Sie kontaktieren möchte, kennt er nur die Nummer des gesamten Büros. Die Empfangsdame müsste dann Ihre Durchwahlnummer suchen und den Anruf an Sie weiterleiten.

### Wie funktioniert es?

Ein einfacher Fall würde so aussehen:

1. Patty möchte sich mit `www.google.com` verbinden, also sendet ihr Gerät diese Anfrage über den Router.
2. Der Router nimmt diese Anfrage entgegen und öffnet seine eigene Verbindung zu google.com, dann sendet er Pattys Anfrage, sobald eine Verbindung hergestellt ist.
3. Der Router ist der Vermittler zwischen Patty und `www.google.com`. Google weiß nichts über Patty; stattdessen sieht es nur den Router.

NAT und die Paketweiterleitung im Allgemeinen können ziemlich kompliziert werden, aber wir werden nicht auf die Einzelheiten eingehen.

## Exercise

Übung macht den Meister! Hier sind einige praktische Übungen, um Ihr Verständnis von Netzwerkadressierung und Konnektivität zu vertiefen, die grundlegend für das Verständnis von Konzepten wie NAT sind:

1. **[MAC- und IP-Adressen in Linux identifizieren](https://labex.io/de/labs/linux-identify-mac-and-ip-addresses-in-linux-592731)** - Üben Sie die Verwendung des Befehls `ip a`, um Netzwerkinformationen, einschließlich IPv4- und IPv6-Adressen, auf einem Linux-System zu identifizieren.
2. **[IP-Adressierung in Linux verwalten](https://labex.io/de/labs/linux-manage-ip-addressing-in-linux-592736)** - Lernen Sie, die IP-Adressierung durch Konfigurieren statischer und dynamischer IPs zu verwalten und die Netzwerkkonfiguration zu überprüfen, was zum Verständnis beiträgt, wie Geräte ihre Adressen erhalten.
3. **[IP-Adresstypen und Erreichbarkeit in Linux erkunden](https://labex.io/de/labs/linux-explore-ip-address-types-and-reachability-in-linux-592780)** - Erkunden Sie verschiedene IP-Adresstypen (privat, öffentlich, Multicast) und testen Sie die Netzwerk-Erreichbarkeit, um einen praktischen Kontext dafür zu erhalten, wie NAT zwischen internen und externen Adressen unterscheidet.

Diese Labs helfen Ihnen, die Konzepte in realen Szenarien anzuwenden und Vertrauen in die Netzwerkkonfiguration und Fehlerbehebung unter Linux aufzubauen.

## Quiz Question

Was wird verwendet, um eine einzelne private Adresse dem Internet gegenüber darzustellen?

## Quiz Answer

NAT
