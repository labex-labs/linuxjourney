---
lesson_id: "subnetting-cheats"
course_id: "subnetting"
lang: "de"
order_index: 4
title: "Subnetting-Kurzverfahren"
description: "Lerne kompakte Binär- und Blockgrößenverfahren zur Prüfung von IPv4-Subnetzberechnungen."
meta_title: "Subnetting-Kurzverfahren – Subnetting"
meta_description: "Beherrsche Subnetting mit kompakten Verfahren zur Binärumwandlung. Verwende die Folge 128+64+32+16+8+4+2+1, um IP-Adressen schnell zwischen Dezimal- und Binärdarstellung umzuwandeln."
meta_keywords: "Subnetting, Binärumwandlung, IP-Adresse, Netzwerk, Linux-Vernetzung, 128+64+32+16+8+4+2+1, Dezimal zu Binär, Subnetzberechnung, Tutorial, Anleitung"
---

Subnetzrechner sind nützlich, doch einige wenige Binärmuster erleichtern die Prüfung ihrer Ausgabe. Diese Verfahren sind Kontrollen und kein Ersatz für die Bestätigung der tatsächlichen Vergabe- und Routingrichtlinie.

## Bitwerte eines Oktetts

Ein IPv4-Oktett verwendet diese Stellenwerte:

```text
bit:    1   1   1   1   1  1  1  1
value: 128  64  32  16   8  4  2  1
```

Die Summe aller acht Werte ergibt 255. Dezimal 192 ist `128 + 64`, daher lautet seine Binärdarstellung `11000000`.

:::single-choice{#subnet-cheats-binary-192} Wie lautet Dezimal 192 in achtstelliger Binärdarstellung?

::option[`11000000`]{#subnet-cheats-192-correct .correct explanation="Die Stellen 128 und 64 sind gesetzt, die übrigen Stellen null."}
::option[`10101000`]{#subnet-cheats-168 explanation="Dieses Muster entspricht 168."}
::option[`11111111`]{#subnet-cheats-255 explanation="Alle acht gesetzten Stellen ergeben 255."}
:::

## Häufige Masken innerhalb eines Oktetts

Zusammenhängende Präfixbits ergeben eine kurze Maskenfolge:

```text
bits set: 0    1    2    3    4    5    6    7    8
decimal:  0  128  192  224  240  248  252  254  255
```

`/19` enthält beispielsweise 16 vollständige Präfixbits sowie drei Bits im dritten Oktett. Die Maske lautet daher `255.255.224.0`.

:::single-choice{#subnet-cheats-prefix-19} Welche Maske entspricht IPv4-`/19`?

::option[`255.255.224.0`]{#subnet-cheats-mask-19 .correct explanation="Sechzehn vollständige Bits plus drei weitere ergeben 255, 255 und 224."}
::option[`255.255.19.0`]{#subnet-cheats-literal-19 explanation="Eine Präfixlänge ist eine Bitanzahl und kein dezimales Maskenoktett."}
::option[`255.255.255.19`]{#subnet-cheats-tail-19 explanation="Dies ist keine zusammenhängende 19-Bit-Maske."}
:::

## Blockgrößen

Subtrahiere im ersten Maskenoktett, das nicht 255 ist, den Maskenwert von 256, um die Subnetzschrittweite zu erhalten. Eine `/27`-Maske endet auf 224 und ergibt die Blockgröße `256 - 224 = 32`. Die Grenzen im letzten Oktett sind daher 0, 32, 64, 96, 128, 160, 192 und 224.

Die Adresse `198.51.100.77/27` liegt im Block von 64 bis 95.

:::single-choice{#subnet-cheats-77-network} Wie lautet die Netzwerkadresse für `198.51.100.77/27`?

::option[`198.51.100.32`]{#subnet-cheats-network-32 explanation="Dieser Block umfasst im letzten Oktett die Werte 32 bis 63."}
::option[`198.51.100.77`]{#subnet-cheats-network-77 explanation="Die Adresse enthält Hostbits und ist keine Blockgrenze."}
::option[`198.51.100.64`]{#subnet-cheats-network-64 .correct explanation="Der bei 64 beginnende `/27`-Block umfasst 64 bis 95."}
:::

## Ein beliebiges Oktett umwandeln

Wähle zur Umwandlung von Dezimal 123 jeweils die größten verbleibenden Werte, ohne die Zahl zu überschreiten:

```text
123 = 64 + 32 + 16 + 8 + 2 + 1
    = 01111011
```

Wandle zurück, indem du nur die Stellenwerte addierst, deren Bits eins sind. Bewahre bei der Arbeit innerhalb eines IPv4-Oktetts stets alle acht Positionen.

:::single-choice{#subnet-cheats-binary-123} Welcher Acht-Bit-Wert entspricht Dezimal 123?

::option[`1111011`]{#subnet-cheats-123-seven-bit explanation="Der Zahlenwert ist ähnlich, doch die Oktettdarstellung muss acht Positionen bewahren."}
::option[`01111011`]{#subnet-cheats-123-correct .correct explanation="Die gesetzten Stellen ergeben 64 + 32 + 16 + 8 + 2 + 1."}
::option[`01111100`]{#subnet-cheats-124 explanation="Dieses Muster setzt die 4er-Stelle statt 2 und 1 und ergibt 124."}
:::

## Zusammenfassung

Du kannst häufige IPv4-Berechnungen nun mit kompakten Binärmustern prüfen.

1. Verwende die acht Oktettstellenwerte von 128 bis 1.
2. Merke dir die Folge zusammenhängender Teiloktettmasken.
3. Leite die Blockgröße ab, indem du die Teilmaske von 256 abziehst.
4. Bewahre bei der Umwandlung einzelner Oktette acht Bits.
