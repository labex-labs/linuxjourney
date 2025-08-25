---
index: 1
lang: "de"
title: "Was ist ein Router?"
meta_title: "Was ist ein Router? - Routing"
meta_description: "Erfahren Sie, was ein Router ist, wie er funktioniert und welche Rolle er in Netzwerken spielt. Verstehen Sie Routing, Hops und Paketlieferung für Anfänger."
meta_keywords: "Router, Netzwerk, Routing, Hops, Paketvermittlung, Linux-Netzwerk, Anfänger-Tutorial, Netzwerk-Leitfaden"
---

## Lesson Content

Wir haben den Begriff Router schon einmal verwendet; hoffentlich wissen Sie, was das ist, da Sie wahrscheinlich einen zu Hause haben. Ein Router ermöglicht es Maschinen in einem Netzwerk, miteinander sowie mit anderen Netzwerken zu kommunizieren. Bei einem typischen Router haben Sie LAN-Ports, die es Ihren Maschinen ermöglichen, sich mit demselben lokalen Netzwerk zu verbinden, und Sie haben auch einen Internet-Uplink-Port, der Sie mit dem Internet verbindet. Manchmal sehen Sie diesen Port als WAN bezeichnet, da er Sie im Wesentlichen mit einem größeren Netzwerk verbindet. Wenn wir irgendeine Art von Netzwerkaktivität durchführen, muss diese über den Router laufen. Der Router entscheidet, wohin unsere Netzwerkpakete gehen und welche hereinkommen. Er leitet unsere Pakete zwischen mehreren Netzwerken weiter, um von ihrem Quellhost zu ihrem Zielhost zu gelangen.

### Wie funktioniert ein Router?

Stellen Sie sich das Routing wie die Postzustellung vor. Wir haben eine Adresse, an die wir einen Brief senden möchten. Wenn wir ihn zur Post schicken, erhalten sie den Brief und sehen: "Oh, das geht nach Kalifornien." Ich lege ihn auf den Lastwagen, der nach Kalifornien fährt (ich habe ehrlich gesagt keine Ahnung, wie das Postsystem funktioniert). Der Brief wird dann nach San Francisco geschickt. Innerhalb von San Francisco gibt es verschiedene Postleitzahlen, und in diesen Postleitzahlen gibt es kleinere Adresscodes, bis schließlich jemand Ihren Brief an die gewünschte Adresse zustellen kann. Wenn Sie hingegen bereits in San Francisco und in derselben Postleitzahl wohnen würden, wüsste der Postbote wahrscheinlich genau, wohin der Brief gehen muss, ohne ihn an jemand anderen weiterzugeben.

Wenn wir Pakete routen, verwenden sie ähnliche Adress-"Routen", wie z.B. "um zu Netzwerk A zu gelangen, senden Sie diese Pakete an Netzwerk B." Wenn wir keine Route dafür festgelegt haben, haben wir eine Standardroute, die unsere Pakete verwenden werden. Diese Routen sind in einer Routing-Tabelle festgelegt, die unser System verwendet, um uns durch Netzwerke zu navigieren.

### Hops

Wenn Pakete sich über Netzwerke bewegen, reisen sie in Hops. Ein Hop ist, wie wir grob die Entfernung messen, die das Paket zurücklegen muss, um von der Quelle zum Ziel zu gelangen. Nehmen wir an, ich habe zwei Router, die Host A mit Host B verbinden; daher sagen wir, dass es zwei Hops zwischen Host A und Host B gibt. Jeder Hop ist ein Zwischengerät, wie die Router, das wir passieren müssen.

### Den grundlegenden Unterschied zwischen Switching, Routing & Flooding verstehen?

- **Packet SWITCHING** ist im Grunde das Empfangen, Verarbeiten und Weiterleiten von Daten an das Zielgerät.
- **ROUTING** ist ein Prozess zur Erstellung der Routing-Tabelle, damit wir SWITCHING besser durchführen können.
- Vor dem Routing wurde **FLOODING** verwendet. Wenn ein Router nicht weiß, wohin ein Paket gesendet werden soll, wird jedes eingehende Paket über jeden ausgehenden Link gesendet, außer dem, über den es angekommen ist.

## Exercise

Übung macht den Meister! Hier sind einige praktische Übungen, um Ihr Verständnis der Netzwerkkonnektivität und des Routings zu vertiefen:

1. **[IP-Adresstypen und Erreichbarkeit in Linux erkunden](https://labex.io/de/labs/linux-explore-ip-address-types-and-reachability-in-linux-592780)** - Üben Sie das Testen des lokalen TCP/IP-Stacks, das Identifizieren privater und öffentlicher IPs und das Überprüfen der Netzwerkerreichbarkeit, die entscheidend sind, um zu verstehen, wie ein Router die Kommunikation erleichtert.
2. **[Netzwerkschicht-Interaktion mit ping und arp in Linux erkunden](https://labex.io/de/labs/linux-explore-network-layer-interaction-with-ping-and-arp-in-linux-592746)** - Erfahren Sie, wie die Befehle `ping` und `arp` Ihnen helfen, zu beobachten, wie die Netzwerk- und Datenverbindungsschichten interagieren und wie das Standard-Gateway (Router) den Remote-Verkehr handhabt.
3. **[Netzwerkschicht-Konnektivität in Linux simulieren](https://labex.io/de/labs/linux-simulate-network-layer-connectivity-in-linux-592752)** - Verwenden Sie Docker, um Netzwerkknoten zu simulieren und IP-Adressen zuzuweisen, und testen Sie dann die Konnektivität, um zu verstehen, wie IP-Subnetze und Routing die Netzwerkkommunikation steuern.

Diese Labs helfen Ihnen, die Konzepte der Netzwerkkommunikation, der IP-Adressierung und der Rolle des Routings in realen Szenarien anzuwenden und Vertrauen in die Netzwerk-Grundlagen aufzubauen.

## Quiz Question

Wie messen Pakete die Entfernung?

## Quiz Answer

Hops
