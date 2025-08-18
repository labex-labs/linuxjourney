---
lang: "de"
title: "Subnetz-Mathematik"
meta_title: "Subnetz-Mathematik - Subnetting"
meta_description: "Lernen Sie die Grundlagen der Subnetz-Mathematik und wie Sie verfügbare Hosts in einem Netzwerk berechnen. Verstehen Sie IP-Adressierung und Subnetzmasken für Anfänger. Beginnen Sie Ihre Linux-Reise!"
meta_keywords: "Subnetz-Mathematik, IP-Adresse, Subnetzmaske, Netzwerk-Hosts, Binär, Linux-Netzwerk, Anfänger-Tutorial, Leitfaden"
---

## Lesson Content

Okay, wir wissen, dass Subnetzmasken wichtig sind, um herauszufinden, wie viele Hosts wir in unserem Subnetz haben können. Wie viele Hosts wären das also?

Nehmen wir an, ich habe eine IP-Adresse von **192.168.1.0** und eine Subnetzmaske von **255.255.255.0**. Nun, lassen Sie uns diese Zahlen in binärer Form anordnen. Verwenden Sie vorerst einen Online-Rechner, um diese Werte von dezimal in binär umzuwandeln.

```
192.168.1.165  = 11000000.10101000.00000001.10100101
255.255.255.0  = 11111111.11111111.11111111.00000000
```

Die IP-Adresse wird durch unsere Subnetzmaske maskiert. Wenn Sie eine 1 sehen, ist sie maskiert, und wir tun so, als würden wir sie nicht sehen. Die einzigen möglichen Hosts, die wir haben können, stammen also aus dem Bereich `00000000`. Denken Sie daran, `11111111` in binärer Form entspricht 255. Wir berücksichtigen auch 0 als Host-Nummer, so dass es 256 mögliche Optionen gibt. Es mag jedoch so aussehen, als hätten wir 256 mögliche Optionen, aber wir ziehen tatsächlich 2 Hosts ab, da wir die Broadcast-Adresse und die Subnetz-Adresse berücksichtigen müssen, was uns 254 mögliche Hosts in unserem Subnetz lässt. Wir wissen also, dass wir Hosts mit IP-Adressen im Bereich von 192.168.1.1 - 192.168.1.254 haben können.

## Exercise

No exercises for this lesson.

## Quiz Question

Was ist das binäre Äquivalent von 255?

## Quiz Answer

11111111
