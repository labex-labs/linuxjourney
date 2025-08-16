---
lang: "de"
title: "NAT"
description: "Erfahren Sie mehr über NAT (Network Address Translation) in Linux, wie es funktioniert und welche Rolle es bei der Netzwerksicherheit spielt. Verstehen Sie private vs. öffentliche IPs. Linux-Netzwerkanleitung."
keywords: "NAT, Network Address Translation, Linux-Netzwerk, private IP, öffentliche IP, Linux-Tutorial, Anfängerleitfaden"
---

## Lesson Content

Wir haben NAT (Network Address Translation) schon einmal erwähnt, sind aber nicht darauf eingegangen. Wenn wir in unserem Netzwerk arbeiten, bedeutet das, dass das Internet unsere IP-Adresse sehen kann? Nicht ganz.

NAT lässt ein Gerät wie unseren Router als Vermittler zwischen dem Internet und einem privaten Netzwerk agieren. So ist nur eine einzige, eindeutige IP-Adresse erforderlich, um eine ganze Gruppe von Computern darzustellen.

Stellen Sie sich NAT wie eine Empfangsdame in einem großen Büro vor. Wenn jemand Sie kontaktieren möchte, kennt er nur die Nummer des gesamten Büros. Die Empfangsdame müsste dann Ihre Durchwahlnummer suchen und den Anruf an Sie weiterleiten.

### How does it work?

Ein einfacher Fall würde so aussehen:

1. Patty möchte sich mit <www.google.com> verbinden, also sendet ihr Gerät diese Anfrage über den Router.
2. Der Router nimmt diese Anfrage entgegen und öffnet seine eigene Verbindung zu google.com, dann sendet er Pattys Anfrage, sobald eine Verbindung hergestellt ist.
3. Der Router ist der Vermittler zwischen Patty und <www.google.com>. Google weiß nichts über Patty; stattdessen kann es nur den Router sehen.

NAT und Paket-Routing im Allgemeinen können ziemlich kompliziert werden, aber wir werden nicht auf die Besonderheiten eingehen.

## Exercise

Keine Übungen für diese Lektion.

## Quiz Question

Was wird verwendet, um eine einzelne private Adresse dem Internet gegenüber darzustellen?

## Quiz Answer

NAT
