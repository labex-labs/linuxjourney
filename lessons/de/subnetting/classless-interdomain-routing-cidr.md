---
lesson_id: "classless-interdomain-routing-cidr"
course_id: "subnetting"
lang: "de"
order_index: 5
title: "CIDR"
description: "Lerne, wie CIDR-Präfixe Adressbereiche, Subnetzgrenzen und aggregierte Routen darstellen."
meta_title: "CIDR – Subnetting"
meta_description: "Eine Anleitung zur CIDR-Notation. Lerne das CIDR-Format, CIDR-Subnetting und die Berechnung von Hosts in deinem Netzwerk kennen."
meta_keywords: "CIDR, CIDR-Subnetting, CIDR-Format, Subnetzmaske, IP-Adressierung, Ubuntu-Server-Subnetz CIDR, Netzwerkpräfix, Linux-Vernetzung"
---

Classless Inter-Domain Routing stellt einen Adressbereich durch eine Präfixlänge dar, statt sich auf historische Adressklassen zu stützen. CIDR ermöglicht variabel große Vergaben, Subnetting und Routenaggregation für IPv4 und IPv6.

## Präfixnotation lesen

In `10.42.3.17/24` bilden die ersten 24 Bit das Netzwerkpräfix, und acht Bits bleiben für Positionen innerhalb des Bereichs. Das kanonische Netzwerk lautet `10.42.3.0/24`; die angegebene Hostadresse kann bei der Konfiguration einer Schnittstelle dennoch zusammen mit dem Präfix geschrieben werden.

:::single-choice{#cidr-prefix-meaning}
Was legt `/24` in einem IPv4-CIDR-Wert fest?

::option[24 führende Netzwerkpräfixbits.]{#cidr-24-prefix-bits .correct explanation="Die verbleibenden acht der 32 IPv4-Bits können innerhalb des Präfixes variieren."}
::option[24 verwendbare Adressen in jedem Subnetz.]{#cidr-24-addresses explanation="Ein `/24` enthält insgesamt 256 Adresswerte."}
::option[Den TCP-Zielport des Netzwerks.]{#cidr-24-port explanation="CIDR und Transportports sind unabhängig."}
:::

## Bereichsgröße berechnen

Das IPv4-Präfix `/23` lässt neun Hostbits und umfasst deshalb `2^9 = 512` Adressen. Das ausgerichtete Präfix `123.12.24.0/23` erstreckt sich über:

```text
first: 123.12.24.0
last:  123.12.25.255
```

Bei herkömmlicher Broadcast-Verwendung ist die erste Adresse die Netzwerkadresse und die letzte der gerichtete Broadcast. Wende die Abkürzung „minus zwei“ für verwendbare Hosts nicht blind auf `/31`-Punkt-zu-Punkt- oder `/32`-Hostrouten an.

:::single-choice{#cidr-23-total}
Wie viele IPv4-Adressen enthält ein `/23` insgesamt?

::option[512]{#cidr-total-512 .correct explanation="Neun veränderliche Bits erzeugen 2^9 Kombinationen."}
::option[23]{#cidr-total-23 explanation="Die Präfixzahl zählt feste Bits und keine Adressen."}
::option[510]{#cidr-total-510 explanation="Dies ist nach Abzug besonderer Endpunkte eine herkömmliche verwendbare Anzahl und nicht die gesamte Bereichsgröße."}
:::

## Ausrichtung prüfen

Ein Präfix muss an seiner Binärgrenze beginnen. Ein `/23` schreitet bei festen früheren Oktetten im dritten Oktett in Zweierblöcken fort. Daher ist `123.12.24.0/23` ausgerichtet, während `123.12.25.0/23` zu demselben Bereich `123.12.24.0/23` kanonisiert wird.

:::single-choice{#cidr-canonical-25}
Was ist das kanonische `/23`-Netzwerk, das `123.12.25.0` enthält?

::option[Nur `123.12.25.0/23`, beginnend bei 25.]{#cidr-25-unaligned explanation="Das letzte Präfixbit gruppiert die Werte des dritten Oktetts in ausgerichteten Paaren."}
::option[`123.12.0.0/23`]{#cidr-third-zero explanation="Dies beschreibt einen anderen `/23`-Bereich."}
::option[`123.12.24.0/23`]{#cidr-24-canonical .correct explanation="Die Werte 24 und 25 im dritten Oktett besitzen dasselbe ausgerichtete 23-Bit-Präfix."}
:::

## Routen aggregieren

CIDR kann ein Aggregat für mehrere zusammenhängende, gleich große und richtig ausgerichtete Präfixe ankündigen. Beispielsweise lassen sich `192.0.2.0/25` und `192.0.2.128/25` zu `192.0.2.0/24` zusammenfassen. Aggregation ist nur sicher, wenn der ankündigende Router das vollständige Aggregat korrekt erreichen kann oder Richtlinien zur Vermeidung von Schleifen und Blackholes besitzt.

:::single-choice{#cidr-aggregate-two-25s}
Welches Aggregat umfasst beide Hälften von `192.0.2.0/24`?

::option[`192.0.2.0/26`]{#cidr-aggregate-26 explanation="Ein `/26` umfasst nur 64 Adressen und ist kleiner als jede Hälfte."}
::option[`192.0.3.0/25`]{#cidr-aggregate-other explanation="Dies liegt außerhalb des angegebenen Adressbereichs."}
::option[`192.0.2.0/24`]{#cidr-aggregate-24 .correct explanation="Die beiden zusammenhängenden ausgerichteten `/25`-Bereiche unterscheiden sich nur im nächsten Bit und besitzen dasselbe `/24`-Präfix."}
:::

## Routing mit längstem Präfix

Wenn sich Routen überschneiden, wählt die Weiterleitung normalerweise die geeignete Route mit dem längsten passenden Präfix. Eine `/24`-Route ist spezifischer als ein sie umfassendes `/16`, während eine Standardroute `/0` nur gewinnt, wenn keine spezifischere geeignete Route vorhanden ist.

:::single-choice{#cidr-route-specificity}
Welche geeignete Route ist für das Ziel `10.42.3.8` spezifischer?

::option[`10.42.3.0/24`]{#cidr-route-24 .correct explanation="Die 24-Bit-Übereinstimmung ist länger und damit spezifischer als `/8`."}
::option[`10.0.0.0/8`]{#cidr-route-8 explanation="Diese Route passt, legt aber weniger Zielbits fest."}
::option[`0.0.0.0/0`]{#cidr-default explanation="Die Standardroute ist das unspezifischste mögliche IPv4-Präfix."}
:::

## Zusammenfassung

Du kannst die CIDR-Notation nun für Adressbereiche und Routenauswahl verwenden.

1. Interpretiere den Schrägstrichwert als Anzahl führender Präfixbits.
2. Berechne die Gesamtbereichsgröße aus den verbleibenden Bits.
3. Kanonisiere ein Präfix auf seine ausgerichtete Netzwerkgrenze.
4. Aggregiere nur zusammenhängende ausgerichtete Bereiche mit gültiger Erreichbarkeit.
5. Bevorzuge bei der Routensuche das längste geeignete Präfix.
