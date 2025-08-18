---
index: 6
lang: "de"
title: "Link-State-Protokolle"
meta_title: "Link-State-Protokolle - Routing"
meta_description: "Erfahren Sie mehr über Link-State-Protokolle wie OSPF für große Netzwerke. Verstehen Sie ihre schnelle Konvergenz und wie sie Routing-Tabellen aktualisieren. Beginnen Sie Ihre Reise in die Linux-Netzwerktechnik!"
meta_keywords: "Link-State-Protokolle, OSPF, Linux-Netzwerktechnik, Routing-Protokolle, Netzwerktopologie, Anfänger"
---

## Lesson Content

Link-State-Protokolle eignen sich hervorragend für große Netzwerke. Sie sind komplexer als Distance-Vector-Protokolle; ein großer Vorteil ist jedoch ihre Fähigkeit, schnell zu konvergieren. Dies liegt daran, dass sie, anstatt periodisch die gesamte Routing-Tabelle zu senden, nur Updates an benachbarte Routen senden. Sie verwenden einen anderen Algorithmus, um den kürzesten Pfad zuerst zu berechnen und ihre Netzwerktopologie in Form eines Graphen zu konstruieren, um zu zeigen, welche Router mit anderen Routern verbunden sind.

Eines der gängigen Link-State-Protokolle ist OSPF (Open Shortest Path First). Es aktualisiert die Routing-Tabellen nur, wenn eine Netzwerkänderung vorliegt. Es hat keine Hop-Begrenzung.

## Exercise

No exercises for this lesson.

## Quiz Question

Was ist eines der gängigsten Link-State-Protokolle?

## Quiz Answer

OSPF
