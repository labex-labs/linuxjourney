---
index: 4
lang: "de"
title: "Subnetz-Spickzettel"
meta_title: "Subnetz-Spickzettel - Subnetting"
meta_description: "Meistern Sie Subnetting mit unserem Leitfaden zu binären Konvertierungs-Spickzetteln. Lernen Sie, die 128+64+32+16+8+4+2+1-Tabelle zu verwenden, um IP-Adressen schnell von Dezimal in Binär und zurück umzuwandeln. Unerlässlich für Netzwerk-Interviews und Zertifizierungen."
meta_keywords: "subnetting, binäre Umwandlung, IP-Adresse, Netzwerk, Linux-Netzwerk, 128+64+32+16+8+4+2+1, 128 64 32 16 8 4 2 1, dezimal zu binär, Subnetz-Mathematik, Tutorial, Leitfaden"
---

## Lesson Content

In der modernen Netzwerktechnik werden Sie selten Subnetz-Mathematik von Hand durchführen, da Tools und Rechner diesen Prozess automatisieren. Das Verständnis der manuellen Umwandlung zwischen Dezimal und Binär ist jedoch entscheidend für Netzwerkinterviews, Zertifizierungsprüfungen und um ein tieferes Verständnis dafür zu entwickeln, wie die IP-Adressierung funktioniert. Diese Lektion bietet einige einfache "Spickzettel" (Cheats), die Ihnen helfen, dies zu meistern.

Zuerst ist es sehr vorteilhaft, sich die Basis-2-Berechnungen einzuprägen, da sie die Grundlage der Binärmathematik bilden.

- 2^1 = 2
- 2^2 = 4
- 2^3 = 8
- 2^4 = 16
- 2^5 = 32
- 2^6 = 64
- 2^7 = 128
- 2^8 = 256

### Die Binärkonvertierungstabelle

Um Zahlen einfach umzuwandeln, verwenden wir eine Tabelle, die den Wert jedes Bits in einem 8-Bit-Oktett einer IP-Adresse darstellt.

```plaintext
1   1  1  1  1 1 1 1
128 64 32 16 8 4 2 1
```

Diese Tabelle ist Ihr primäres Werkzeug. Jede Zahl entspricht der Position eines Bits. Die volle Summe, `128+64+32+16+8+4+2+1`, ergibt 255, was der höchstmögliche Wert in einem Oktett ist.

### Dezimal-zu-Binär-Umwandlung

Lassen Sie uns die IP-Adresse `192.168.23.43` in Binär umwandeln. Wir gehen das erste Oktett, `192`, durch, um den Prozess zu demonstrieren. Wir verwenden die Werte aus unserer Tabelle: `128 64 32 16 8 4 2 1`.

1. Beginnen Sie mit der Zahl `192`. Können Sie 128 davon subtrahieren? Ja (192 - 128 = 64). Das erste Bit ist also **1**.
2. Unsere neue Zahl ist `64`. Können Sie den nächsten Wert, 64, davon subtrahieren? Ja (64 - 64 = 0). Das zweite Bit ist **1**.
3. Unser Restbetrag ist nun `0`. Wir können 32, 16, 8, 4, 2 oder 1 nicht subtrahieren. Daher sind die restlichen Bits alle **0**.

Die Binärform von 192 ist `11000000`. Sie können diese gleiche Subtraktionsmethode auf die anderen Oktette anwenden.

### Binär-zu-Dezimal-Umwandlung

Um von Binär zurück zu Dezimal zu konvertieren, addieren Sie einfach die Werte aus der Tabelle, bei denen eine `1` in der Binärzahl erscheint. Wandeln wir `11000000` zurück in Dezimal um.

Wenn wir die Tabelle `128 64 32 16 8 4 2 1` betrachten, sind die ersten beiden Bits `1`. Das bedeutet, wir addieren die ersten beiden Werte:

`128 + 64 = 192`

Da alle anderen Bits `0` sind, addieren wir keine weiteren Werte. Die Formel `128 + 64 + 0 + 0 + 0 + 0 + 0 + 0` ergibt 192. So einfach ist das!

## Exercise

Übung macht den Meister! Obwohl Subnetz-Mathematik in der realen Welt oft automatisiert wird, ist das Verständnis der zugrunde liegenden Binärkonvertierungen für Interviews und ein tieferes Verständnis von Netzwerken entscheidend. Hier ist ein praktisches Labor, um Ihr Verständnis zu festigen:

1. **[IP-Subnetting und Binärkonvertierung im Linux-Terminal durchführen](https://labex.io/de/labs/comptia-perform-ip-subnetting-and-binary-conversion-in-the-linux-terminal-592782)** - Meistern Sie IP-Subnetting und Binärkonvertierung, indem Sie Python in einem Linux-Terminal verwenden, um IP-Adressen umzuwandeln, CIDR-Masken zu übersetzen und Netzwerkdetails zu berechnen.

Dieses Labor hilft Ihnen, die Konzepte der Binärkonvertierung und des Subnetting in einem praktischen Szenario anzuwenden und Vertrauen in die Grundlagen der Netzwerkadressierung aufzubauen.

## Quiz Question

Was ist die Binärkonvertierung von 123? Bitte geben Sie die Antwort in englischen Zeichen (Zahlen) an.

## Quiz Answer

01111011
