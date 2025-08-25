---
index: 7
lang: "de"
title: "Netzwerkschicht"
meta_title: "Netzwerkschicht - Netzwerk-Grundlagen"
meta_description: "Erfahren Sie mehr über die Netzwerkschicht in Linux, wie IP-Adressen Pakete über Subnetze routen und ihre Rolle bei der Datenübertragung. Beginnen Sie Ihre Linux-Netzwerkreise!"
meta_keywords: "Netzwerkschicht, IP-Adressen, Subnetze, Linux-Netzwerk, Paket-Routing, Anfänger, Tutorial, Anleitung"
---

## Lesson Content

Die Netzwerkschicht bestimmt das Routing unserer Pakete von unserem Quellhost zu einem Zielhost. Glücklicherweise reist unser Paket in unserem Beispiel nur innerhalb desselben Netzwerks, aber das Internet besteht aus vielen Netzwerken. Diese kleineren Netzwerke, aus denen das Internet besteht, werden als Subnetze bezeichnet. Alle Subnetze sind auf irgendeine Weise miteinander verbunden, weshalb wir `https://www.google.com` erreichen können, obwohl es sich in einem eigenen Netzwerk befindet. Ich werde nicht ins Detail gehen, da wir einen ganzen Kurs über Subnetze haben, aber vorerst, in Bezug auf unsere Netzwerkschicht, wissen Sie, dass die IP-Adressen die Regeln definieren, um zu verschiedenen Subnetzen zu gelangen.

In der Netzwerkschicht empfängt sie das von der Transportschicht kommende Segment und kapselt dieses Segment in ein IP-Paket, dann hängt sie die IP-Adresse des Quellhosts und die IP-Adresse des Zielhosts an den Paket-Header an. Zu diesem Zeitpunkt enthält unser Paket Informationen darüber, wohin es geht und woher es kam. Nun sendet es unser Paket an die physische Hardwareschicht.

## Exercise

Übung macht den Meister! Hier sind einige praktische Übungen, um Ihr Verständnis der Netzwerkschicht, der IP-Adressierung und der Subnetze zu vertiefen:

1. **[Netzwerkschicht-Konnektivität in Linux simulieren](https://labex.io/de/labs/linux-simulate-network-layer-connectivity-in-linux-592752)** – Üben Sie das Zuweisen statischer IP-Adressen und das Testen der Konnektivität innerhalb und zwischen verschiedenen Subnetzen mithilfe von Docker-Containern.
2. **[IP-Subnetting und Binärkonvertierung im Linux-Terminal durchführen](https://labex.io/de/labs/linux-perform-ip-subnetting-and-binary-conversion-in-the-linux-terminal-592782)** – Meistern Sie IP-Subnetting und Binärkonvertierung, einschließlich der Berechnung nutzbarer Hosts und Subnetze, direkt im Linux-Terminal.
3. **[IP-Adresstypen und Erreichbarkeit in Linux erkunden](https://labex.io/de/labs/linux-explore-ip-address-types-and-reachability-in-linux-592780)** – Erkunden Sie verschiedene IP-Adresstypen (privat, öffentlich, Multicast) und testen Sie die Netzwerk-Erreichbarkeit mit `ping` und `ip a`.

Diese Labs helfen Ihnen, die Konzepte der IP-Adressierung und des Subnettings in realen Szenarien anzuwenden und Vertrauen in die Grundlagen der Netzwerkschicht aufzubauen.

## Quiz Question

Wie werden kleinere Netzwerke genannt, aus denen das Internet besteht?

## Quiz Answer

subnets
