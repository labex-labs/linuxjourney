---
lang: "de"
title: "Subnetting-Tricks"
description: "Lernen Sie die Grundlagen des Subnetting und der Binärumwandlung für die Netzwerktechnik. Verstehen Sie IP-Adressen und Subnetzmasken mit diesem anfängerfreundlichen Leitfaden. Beginnen Sie jetzt mit dem Lernen!"
keywords: "Subnetting, Binärumwandlung, IP-Adresse, Netzwerk, Linux-Netzwerk, Anfänger, Tutorial, Leitfaden"
---

## Lesson Content

Ich hasse es, diesen Abschnitt hinzufügen zu müssen. In der realen Welt müssten Sie höchstwahrscheinlich niemals Subnetz-Mathematik von Hand durchführen. Wenn Sie jedoch dazu interviewt würden, müssten Sie wissen, wie man für das Subnetting in und aus der Binärform umrechnet. Glücklicherweise gibt es einige arithmetische Tricks, die Sie sich merken können.

Merken Sie sich zuerst Ihre Basis-2-Berechnungen; tun Sie es einfach:

- 2^1 = 2
- 2^2 = 4
- 2^3 = 8
- 2^4 = 16
- 2^5 = 32
- 2^6 = 64
- 2^7 = 128
- 2^8 = 256
- 2^9 = 512
- 2^10 = 1024
- 2^11 = 2048
- 2^12 = 4096

### Decimal to Binary Chart

```plaintext
1   1  1  1  1 1 1 1
128 64 32 16 8 4 2 1
```

Es gibt viele Gründe, warum die folgende Tabelle so aussieht, wie sie aussieht. Wenn Sie neugierig sind, wie sie funktioniert, gibt es viele Online-Ressourcen.

Okay, haben Sie sich diese gemerkt? Machen wir eine schnelle Dezimal-zu-Binär-Umwandlung:

### Convert 192.168.23.43 to Binary

Denken Sie daran: 128 / 64 / 32 / 16 / 8 / 4 / 2 / 1

Gehen wir die Umwandlung des ersten Oktetts in Binärform durch, und Sie werden verstehen, wie der Rest funktioniert.

1. Können Sie 192 - 128 subtrahieren? Ja, also ist das erste Bit 1.
2. 192 - 128 = 64. Die nächste Zahl in der Tabelle ist 64. Können Sie 64 - 64 subtrahieren? Ja, also ist das zweite Bit 1.
3. Uns sind die Zahlen zum Subtrahieren ausgegangen, daher ist unsere Binärform von 192 11000000.

### Convert Binary 11000000 to Decimal

Für die Binär-zu-Dezimal-Umwandlung addieren Sie die Zahlen, die eine 1 haben, also:

128 + 64 + 0 + 0 + 0 + 0 + 0 + 0 = 192!

## Exercise

Schauen Sie sich Ihre IP-Adresse und Subnetzmaske an und sehen Sie, wie viele Hosts Sie in Ihrem Subnetz haben können.

## Quiz Question

Was ist die binäre Umwandlung von 123?

## Quiz Answer

1111011
