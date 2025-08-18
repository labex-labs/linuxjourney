---
lang: "de"
title: "Distance-Vector-Protokolle"
meta_title: "Distance-Vector-Protokolle - Routing"
meta_description: "Erfahren Sie mehr über Distance-Vector-Protokolle wie RIP, wie sie funktionieren und ihre Einschränkungen für das Netzwerk-Routing. Verstehen Sie Hop-Count und Netzwerkeffizienz."
meta_keywords: "Distance-Vector-Protokolle, RIP, Routing Information Protocol, Hop-Count, Netzwerk-Routing, Linux-Netzwerk, Anfängerleitfaden, Tutorial"
---

## Lesson Content

Distance-Vector-Protokolle bestimmen den Pfad zu anderen Netzwerken anhand der Hop-Anzahl, die ein Paket über das Netzwerk nimmt. Wenn beispielsweise Netzwerk A 3 Hops entfernt ist und Netzwerk B neben Netzwerk A liegt, dann gehen wir davon aus, dass Netzwerk B 4 Hops entfernt sein muss. Bei Distance-Vector-Protokollen wäre die nächste Route diejenige mit der geringsten Anzahl von Hops.

Distance-Vector-Protokolle eignen sich hervorragend für kleine Netzwerke. Wenn Netzwerke jedoch zu skalieren beginnen, dauert es länger, bis die Router konvergieren, da sie periodisch die gesamte Routing-Tabelle an jeden Router senden. Ein weiterer Nachteil von Distance-Vector-Protokollen ist die Effizienz; sie wählen Routen, die in Hops näher liegen, aber dies ist möglicherweise nicht immer die effizienteste Route.

Eines der gängigen Distance-Vector-Protokolle ist RIP (Routing Information Protocol). Es sendet die Routing-Tabelle alle 30 Sekunden an jeden Router im Netzwerk. Für ein großes Netzwerk kann dies erhebliche Ressourcen verbrauchen. Aus diesem Grund begrenzt RIP seine Hop-Anzahl auf 15.

## Exercise

No exercises for this lesson.

## Quiz Question

Wahr oder falsch: Distance-Vector-Protokolle verwenden die Route mit der geringsten Bandbreite?

## Quiz Answer

False
