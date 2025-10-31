---
index: 4
lang: "de"
title: "Routing-Protokolle"
meta_title: "Routing-Protokolle - Routing"
meta_description: "Erkunden Sie die Grundlagen von Routing-Protokollen im Linux-Netzwerk. Dieser Leitfaden behandelt Distanzvektor- und Link-State-Protokolle, Netzwerkkonvergenz und wie Router Routing-Tabellen erstellen und pflegen. Ein perfektes Tutorial für Anfänger."
meta_keywords: "Routing-Protokolle, Netzwerkkonvergenz, Distanzvektor, Link State, Linux-Netzwerk, Routing-Tabelle, Netzwerk-Tutorial, Anfänger-Leitfaden, Router-Kommunikation"
---

## Lesson Content

Die manuelle Konfiguration von Routen in einer Routing-Tabelle für jedes Gerät in einem großen Netzwerk wäre eine unglaublich mühsame Aufgabe. Um diesen Prozess zu automatisieren, verwenden wir dynamische **Routing-Protokolle**. Diese Protokolle ermöglichen es Routern, sich automatisch an Netzwerkänderungen anzupassen, indem sie verschiedene Routen erlernen, diese in die Routing-Tabelle aufnehmen und Pakete entsprechend weiterleiten. Es gibt zwei Haupttypen von Routing-Protokollen: Distanzvektor und Link-State.

### Distanzvektor-Protokolle

Distanzvektor-Protokolle arbeiten nach dem Prinzip des „Routings durch Gerüchte“. Jeder Router teilt seine gesamte Routing-Tabelle in regelmäßigen Abständen mit seinen direkt verbundenen Nachbarn. Wenn ein Router eine Routing-Tabelle von einem Nachbarn empfängt, aktualisiert er seine eigene Tabelle mit neuen oder besseren Routen. Die „Distanz“ wird typischerweise durch eine Metrik wie die Hop-Anzahl gemessen. Diese Methode ist einfach, kann aber langsam konvergieren und ist anfällig für Routing-Schleifen. Ein Beispiel für ein Distanzvektor-Protokoll ist das Routing Information Protocol (RIP).

### Link-State-Protokolle

Im Gegensatz dazu geben **Link-State-Protokolle** jedem Router eine vollständige Karte der Netzwerktopologie. Anstatt ihre gesamte Routing-Tabelle zu teilen, senden Router Informationen über den Zustand ihrer eigenen Links (z. B. verbundene Nachbarn und die Kosten der Verbindung) an alle anderen Router im Netzwerk. Anhand dieser Informationen kann jeder Router unabhängig eine identische Karte des Netzwerks erstellen und den besten Pfad zu jedem Ziel berechnen. Dieser Ansatz führt zu einer schnelleren **Netzwerkkonvergenz** und ist besser skalierbar als Distanzvektor-Protokolle. Ein Beispiel ist das Open Shortest Path First (OSPF) Protokoll.

### Netzwerkkonvergenz

Bevor wir uns weiter mit den Protokollen befassen, ist es wichtig, ein Schlüsselkonzept im Routing zu verstehen, die **Netzwerkkonvergenz**. Bei der Verwendung von Routing-Protokollen kommunizieren Router, um Informationen zu sammeln und auszutauschen. Konvergenz ist der Zustand, in dem alle Router eine konsistente und genaue Sicht auf die Netzwerktopologie haben. Wenn jede Routing-Tabelle das gesamte Netzwerk korrekt abbildet, gilt das Netzwerk als „konvergiert“. Wenn eine Änderung auftritt, beispielsweise wenn ein Link ausfällt, wird die Konvergenz vorübergehend unterbrochen, bis alle Router von der Änderung erfahren und ihre Routing-Tabellen aktualisiert haben.

## Exercise

Übung macht den Meister! Hier sind einige praktische Labs, um Ihr Verständnis von Netzwerk-Routing und IP-Adressierung zu festigen:

1.  **[IP-Adressierung in Linux verwalten](https://labex.io/de/labs/comptia-manage-ip-addressing-in-linux-592736)** – Üben Sie die Konfiguration statischer und dynamischer IP-Adressen, das Festlegen eines Standard-Gateways und die Überprüfung von Netzwerkkonfigurationen, was entscheidend für das Verständnis ist, wie Routing-Tabellen erstellt und genutzt werden.
2.  **[Interaktion der Netzwerkschicht mit ping und arp in Linux erkunden](https://labex.io/de/labs/comptia-explore-network-layer-interaction-with-ping-and-arp-in-linux-592746)** – Lernen Sie, wie Geräte auf der Netzwerkschicht interagieren, beobachten Sie ARP und wie das Standard-Gateway den Remote-Verkehr behandelt, was Einblicke in die Mechanismen gibt, die Routing-Protokolle verwalten.
3.  **[Konnektivität der Netzwerkschicht in Linux simulieren](https://labex.io/de/labs/comptia-simulate-network-layer-connectivity-in-linux-592752)** – Verwenden Sie Docker, um Netzwerkknoten zu simulieren, IP-Adressen zuzuweisen und die Konnektivität über Subnetze hinweg zu testen, wobei Konzepte im Zusammenhang mit Netzwerkänderungen und Routing-Entscheidungen direkt angewendet werden.

Diese Labs helfen Ihnen, die Konzepte der Netzwerkkonfiguration und -konnektivität in realen Szenarien anzuwenden und Vertrauen in die grundlegenden Elemente aufzubauen, die Routing-Protokolle automatisieren.

## Quiz Question

Wie wird der Zustand genannt, in dem alle Routing-Tabellen in einem Netzwerk über die Netzwerktopologie übereinstimmen? (Bitte antworten Sie auf Englisch und achten Sie auf die Groß-/Kleinschreibung.)

## Quiz Answer

Convergence
