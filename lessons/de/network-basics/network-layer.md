---
index: 7
lang: "de"
title: "Netzwerkschicht"
meta_title: "Netzwerkschicht - Netzwerk Grundlagen"
meta_description: "Erkunden Sie die Netzwerkschicht im Linux-Networking. Dieser Leitfaden erklärt, wie IP-Adressen und Subnetze das Paket-Routing für die Datenübertragung zwischen Netzwerken ermöglichen."
meta_keywords: "Netzwerkschicht, IP-Adressen, Subnetze, Linux-Networking, Paket-Routing, Datenübertragung, OSI-Modell, IP-Paket"
---

## Lesson Content

Die Vermittlungsschicht (Network Layer) ist für die logische Adressierung und das Routing von Datenpaketen von einem Quellhost zu einem Zielhost verantwortlich. Obwohl ein Paket manchmal innerhalb eines einzigen lokalen Netzwerks reist, ist das Internet eine riesige Sammlung miteinander verbundener Netzwerke.

### Die Rolle des Paketroutings

Die Hauptfunktion der Vermittlungsschicht besteht darin, den optimalen Pfad für die Datenübertragung zu bestimmen. Dieser Prozess, bekannt als **Paketrouting**, stellt sicher, dass Informationen effizient ihr beabsichtigtes Ziel erreichen, selbst wenn sie mehrere Netzwerk-Grenzen überschreiten müssen. Im Bereich **Linux-Netzwerke** ist diese Schicht für die gesamte Internetkommunikation von grundlegender Bedeutung.

### Verstehen von Subnetzen und IP-Adressen

Die kleineren Netzwerke, aus denen das Internet besteht, werden als **Subnetze** bezeichnet. Alle Subnetze sind miteinander verbunden, was es einem Gerät in einem Netzwerk ermöglicht, mit einem Gerät in einem anderen zu kommunizieren, beispielsweise beim Zugriff auf eine Website wie `google.com`. Die Regeln für die Übertragung zwischen diesen verschiedenen Subnetzen werden durch **IP-Adressen** definiert. Eine IP-Adresse bietet eine eindeutige Kennung für ein Gerät in einem Netzwerk, ähnlich einer Straßenadresse für ein Haus.

### Kapselung auf der Vermittlungsschicht

Auf der Vermittlungsschicht wird das von der Transportschicht empfangene Datensegment in eine neue Einheit, das IP-Paket, gekapselt. Während dieses Prozesses wird dem Paket ein Header hinzugefügt, der die Quell-IP-Adresse (woher das Paket stammt) und die Ziel-IP-Adresse (wohin es geht) enthält. Mit diesen entscheidenden Adressinformationen ist das Paket nun für seine Reise gerüstet und wird zur Datenbankschicht (Data Link Layer) weitergegeben, um für die physische Übertragung vorbereitet zu werden.

## Exercise

Übung macht den Meister! Hier sind einige praktische Labs, um Ihr Verständnis der Vermittlungsschicht, der IP-Adressierung und der Subnetze zu festigen:

1.  **[Simulieren der Konnektivität der Vermittlungsschicht in Linux](https://labex.io/de/labs/comptia-simulate-network-layer-connectivity-in-linux-592752)** – Üben Sie die Zuweisung statischer IP-Adressen und testen Sie die Konnektivität innerhalb und über verschiedene Subnetze hinweg mithilfe von Docker-Containern.
2.  **[Durchführen von IP-Subnetting und binärer Konvertierung im Linux-Terminal](https://labex.io/de/labs/comptia-perform-ip-subnetting-and-binary-conversion-in-the-linux-terminal-592782)** – Meistern Sie IP-Subnetting und binäre Konvertierung, einschließlich der Berechnung nutzbarer Hosts und Subnetze, direkt im Linux-Terminal.
3.  **[Erkunden von IP-Adress-Typen und Erreichbarkeit in Linux](https://labex.io/de/labs/comptia-explore-ip-address-types-and-reachability-in-linux-592780)** – Erkunden Sie verschiedene IP-Adress-Typen (privat, öffentlich, Multicast) und testen Sie die Netzwerkerreichbarkeit mithilfe von `ping` und `ip a`.

Diese Labs helfen Ihnen, die Konzepte der IP-Adressierung und des Subnetting in realen Szenarien anzuwenden und Vertrauen in die Grundlagen der Vermittlungsschicht aufzubauen.

## Quiz Question

Wie werden die kleineren Netzwerke genannt, aus denen das Internet besteht? Bitte antworten Sie mit einem einzigen, kleingeschriebenen englischen Wort.

## Quiz Answer

subnets
