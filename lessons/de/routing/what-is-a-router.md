---
lang: "de"
title: "Was ist ein Router?"
meta_title: "Was ist ein Router? - Routing"
meta_description: "Erfahren Sie, was ein Router ist, wie er funktioniert und welche Rolle er in der Netzwerktechnik spielt. Verstehen Sie Routing, Hops und Paketlieferung für Anfänger."
meta_keywords: "Router, Netzwerk, Routing, Hops, Paketvermittlung, Linux-Netzwerk, Anfänger-Tutorial, Netzwerk-Leitfaden"
---

## Lesson Content

Wir haben den Begriff Router schon einmal verwendet; hoffentlich wissen Sie, was das ist, da Sie wahrscheinlich einen zu Hause haben. Ein Router ermöglicht es Maschinen in einem Netzwerk, miteinander sowie mit anderen Netzwerken zu kommunizieren. Bei einem typischen Router gibt es LAN-Ports, die es Ihren Maschinen ermöglichen, sich mit demselben lokalen Netzwerk zu verbinden, und es gibt auch einen Internet-Uplink-Port, der Sie mit dem Internet verbindet. Manchmal wird dieser Port als WAN bezeichnet, da er Sie im Wesentlichen mit einem größeren Netzwerk verbindet. Wenn wir irgendeine Art von Netzwerkaktivität durchführen, muss diese über den Router laufen. Der Router entscheidet, wohin unsere Netzwerkpakete gehen und welche hereinkommen. Er leitet unsere Pakete zwischen mehreren Netzwerken weiter, um von ihrem Quell-Host zu ihrem Ziel-Host zu gelangen.

### Wie funktioniert ein Router?

Stellen Sie sich das Routing genauso vor wie die Postzustellung. Wir haben eine Adresse, an die wir einen Brief senden möchten. Wenn wir ihn zur Post schicken, erhalten sie den Brief und sehen: "Oh, das geht nach Kalifornien." Ich lege ihn auf den Lastwagen, der nach Kalifornien fährt (ich habe ehrlich gesagt keine Ahnung, wie das Postsystem funktioniert). Der Brief wird dann nach San Francisco geschickt. Innerhalb von San Francisco gibt es verschiedene Postleitzahlen, und in diesen Postleitzahlen gibt es kleinere Adresscodes, bis schließlich jemand Ihren Brief an die gewünschte Adresse liefern kann. Wenn Sie hingegen bereits in San Francisco und in derselben Postleitzahl wohnen würden, wüsste der Postbote wahrscheinlich genau, wohin der Brief gehen muss, ohne ihn an jemand anderen weiterzugeben.

Wenn wir Pakete routen, verwenden sie ähnliche Adress-"Routen", wie z.B. "um zu Netzwerk A zu gelangen, senden Sie diese Pakete an Netzwerk B." Wenn wir keine Route dafür festgelegt haben, haben wir eine Standardroute, die unsere Pakete verwenden werden. Diese Routen sind in einer Routing-Tabelle festgelegt, die unser System verwendet, um uns durch Netzwerke zu navigieren.

### Hops

Wenn Pakete sich über Netzwerke bewegen, reisen sie in Hops. Ein Hop ist, wie wir grob die Entfernung messen, die das Paket zurücklegen muss, um von der Quelle zum Ziel zu gelangen. Nehmen wir an, ich habe zwei Router, die Host A mit Host B verbinden; daher sagen wir, dass es zwei Hops zwischen Host A und Host B gibt. Jeder Hop ist ein Zwischengerät, wie die Router, das wir passieren müssen.

### Understanding the basic difference between Switching, Routing & Flooding?

- **Packet SWITCHING** is basically receiving, processing, and forwarding data to the destination device.
- **ROUTING** is a process of creating the routing table so that we can do SWITCHING better.
- Before routing, **FLOODING** was used. If a router doesn't know which way to send a packet, then every incoming packet is sent through every outgoing link except the one it arrived on.

## Exercise

No exercises for this lesson.

## Quiz Question

Wie messen Pakete die Entfernung?

## Quiz Answer

Hops
