---
index: 4
lang: "de"
title: "Routing-Protokolle"
meta_title: "Routing-Protokolle - Routing"
meta_description: "Erfahren Sie mehr über Routing-Protokolle wie Distanzvektor und Link-State. Verstehen Sie Netzwerkkonvergenz und wie Router sich an Änderungen anpassen. Beginnen Sie Ihre Linux-Netzwerkreise!"
meta_keywords: "Routing-Protokolle, Netzwerkkonvergenz, Distanzvektor, Link-State, Linux-Netzwerk, Anfängerleitfaden, Netzwerk-Tutorial"
---

## Lesson Content

Es wäre mühsam, Routen auf einer Routing-Tabelle für jedes Gerät in Ihrem Netzwerk manuell konfigurieren zu müssen. Stattdessen verwenden wir sogenannte Routing-Protokolle. Routing-Protokolle helfen unserem System, sich an Netzwerkänderungen anzupassen; sie lernen verschiedene Routen, bauen sie in die Routing-Tabelle ein und leiten unsere Pakete dann auf diese Weise weiter. Es gibt zwei primäre Arten von Routing-Protokollen: Distanzvektor-Protokolle und Link-State-Protokolle.

### Konvergenz

Bevor wir über die Protokolle sprechen, sollten wir einen Begriff besprechen, der im Routing verwendet wird: Konvergenz. Bei der Verwendung von Routing-Protokollen kommunizieren Router mit anderen Routern, um Informationen über das Netzwerk zu sammeln und auszutauschen. Wenn sie sich darüber einig sind, wie ein Netzwerk aussehen soll, bildet jede Routing-Tabelle die vollständige Topologie des Netzwerks ab und "konvergiert" somit. Wenn etwas in der Netzwerktopologie auftritt, wird die Konvergenz vorübergehend unterbrochen, bis alle Router über diese Änderung informiert sind.

## Exercise

Übung macht den Meister! Hier sind einige praktische Übungen, um Ihr Verständnis von Netzwerk-Routing und IP-Adressierung zu vertiefen:

1. **[IP-Adressierung in Linux verwalten](https://labex.io/de/labs/comptia-manage-ip-addressing-in-linux-592736)** – Üben Sie die Konfiguration statischer und dynamischer IP-Adressen, das Festlegen eines Standard-Gateways und die Überprüfung von Netzwerkkonfigurationen, die entscheidend sind, um zu verstehen, wie Routing-Tabellen erstellt und verwendet werden.
2. **[Netzwerkschicht-Interaktion mit ping und arp in Linux erkunden](https://labex.io/de/labs/comptia-explore-network-layer-interaction-with-ping-and-arp-in-linux-592746)** – Erfahren Sie, wie Geräte auf der Netzwerkschicht interagieren, beobachten Sie ARP und wie das Standard-Gateway den Remote-Verkehr handhabt, was Einblicke in die Mechanismen gibt, die Routing-Protokolle verwalten.
3. **[Netzwerkschicht-Konnektivität in Linux simulieren](https://labex.io/de/labs/comptia-simulate-network-layer-connectivity-in-linux-592752)** – Verwenden Sie Docker, um Netzwerkknoten zu simulieren, IP-Adressen zuzuweisen und die Konnektivität über Subnetze hinweg zu testen, wobei Konzepte im Zusammenhang mit Netzwerkänderungen und Routing-Entscheidungen direkt angewendet werden.

Diese Labs helfen Ihnen, die Konzepte der Netzwerkkonfiguration und -konnektivität in realen Szenarien anzuwenden und Vertrauen in die grundlegenden Elemente aufzubauen, die Routing-Protokolle automatisieren.

## Quiz Question

Wie nennt man den Zustand, wenn alle Routing-Tabellen die Netzwerktopologie kennen?

## Quiz Answer

Convergence
