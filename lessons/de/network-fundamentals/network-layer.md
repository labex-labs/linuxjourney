---
lang: "de"
title: "Netzwerkschicht"
meta_description: "Erfahren Sie mehr über die Netzwerkschicht in Linux, wie IP-Adressen Pakete über Subnetze routen und ihre Rolle bei der Datenübertragung. Beginnen Sie Ihre Reise ins Linux-Netzwerk!"
meta_keywords: "Netzwerkschicht, IP-Adressen, Subnetze, Linux-Netzwerk, Paket-Routing, Anfänger, Tutorial, Leitfaden"
---

## Lesson Content

Die Netzwerkschicht bestimmt das Routing unserer Pakete von unserem Quell-Host zu einem Ziel-Host. Glücklicherweise reist unser Paket in unserem Beispiel nur innerhalb desselben Netzwerks, aber das Internet besteht aus vielen Netzwerken. Diese kleineren Netzwerke, aus denen das Internet besteht, werden als subnets bezeichnet. Alle subnets sind auf irgendeine Weise miteinander verbunden, weshalb wir <https://www.google.com> erreichen können, obwohl es sich in einem eigenen Netzwerk befindet. Ich werde nicht ins Detail gehen, da wir einen ganzen Kurs über subnets haben, aber für den Moment, in Bezug auf unsere Netzwerkschicht, wissen Sie, dass die IP addresses die Regeln für die Reise zu verschiedenen subnets definieren.

In der Netzwerkschicht empfängt sie das Segment, das von der Transport layer kommt, und kapselt dieses Segment in ein IP packet ein, fügt dann die IP address des Quell-Hosts und die IP address des Ziel-Hosts dem packet header hinzu. Zu diesem Zeitpunkt enthält unser Paket Informationen darüber, wohin es geht und woher es kam. Nun sendet es unser Paket an die physical hardware layer.

## Exercise

No exercises for this lesson.

## Quiz Question

Wie werden kleinere Netzwerke genannt, aus denen das Internet besteht?

## Quiz Answer

subnets
