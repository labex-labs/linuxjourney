---
index: 1
lang: "de"
title: "Was ist DNS?"
meta_title: "Was ist DNS? - DNS"
meta_description: "Wenn Sie Linux-Netzwerke lernen möchten, ist das Verständnis von DNS entscheidend. Dieser Leitfaden erklärt, was das Domain Name System (DNS) ist, wie es Domainnamen in IP-Adressen übersetzt und warum es das unverzichtbare Adressbuch des Internets ist. Ein perfekter Startpunkt für alle, die Linux lernen möchten."
meta_keywords: "DNS, Domain Name System, IP-Adresse, Linux lernen, Linux-Grundlagen, Hostname, Linux-Netzwerke, Anfänger, Tutorial, Anleitung, Labex Linux"
---

## Lesson Content

### Das Telefonbuch des Internets

Stellen Sie sich vor, Sie müssten jedes Mal, wenn Sie Google besuchen möchten, `http://192.78.12.4` eingeben, anstatt `www.google.com`. Ohne das Domain Name System (DNS) wäre das Internet genau so. Protokolle auf niedriger Ebene verstehen zur Identifizierung eines Hosts nur numerische IP-Adressen. DNS ist das System, das es uns Menschen ermöglicht, einprägsame Namen für Websites und Server anstelle langer Zahlenreihen zu verwenden. Betrachten Sie es als ein Adressbuch für das Internet: Sie suchen einen Namen, um die entsprechende Nummer zu finden.

### Wie DNS funktioniert

Im Kern übersetzt DNS menschenlesbare Hostnamen (wie `www.google.com`) in maschinenlesbare IP-Adressen (wie `192.78.12.4`). Dieser Vorgang wird als Auflösung bezeichnet. Wenn Sie einen Domainnamen in Ihren Browser eingeben, sendet Ihr Computer eine Abfrage an einen DNS-Server, der dann die korrekte IP-Adresse nachschlägt und zurücksendet, wodurch Ihr Browser eine Verbindung zum Server der Website herstellen kann.

### Ein verteiltes globales System

DNS ist keine einzelne, zentrale Datenbank. Stattdessen ist es ein riesiges, verteiltes System. Website-Besitzer verwalten ihre eigenen DNS-Einträge, um der Welt mitzuteilen, wie sie ihre Domain finden können. Diese einzelnen Domains kommunizieren miteinander und bilden ein riesiges, miteinander verbundenes Verzeichnis für das gesamte Internet. Diese dezentrale Struktur macht das System unglaublich widerstandsfähig und skalierbar.

### Warum Sie Linux DNS lernen sollten

Wenn Sie **Linux lernen** möchten für Systemadministration oder Webentwicklung, ist das Verständnis von DNS unerlässlich. Die Fähigkeit, DNS zu konfigurieren, zu verwalten und Fehler darin zu beheben, ist eine grundlegende Fertigkeit. Dieser Kurs behandelt die Grundlagen, aber seien Sie sich bewusst, dass DNS ein tiefes und komplexes Thema ist. Um es wirklich zu meistern, müssen Sie zusätzliche Recherchen und Übungen durchführen. Dies ist ein großartiger erster Schritt auf Ihrem Weg zu **linux learn**.

## Exercise

Übung macht den Meister! Hier sind einige praktische Labs, um Ihr Verständnis von DNS und Hostnamenauflösung zu festigen. Die Verwendung eines **labex linux Terminals** für diese Übungen ist eine großartige Möglichkeit, praktische Erfahrungen zu sammeln.

1. **[DNS-Einträge in Linux mit dig und nslookup abfragen](https://labex.io/de/labs/comptia-query-dns-records-in-linux-with-dig-and-nslookup-592796)** - Lernen Sie, wie man wichtige Linux-Tools wie `dig` und `nslookup` verwendet, um verschiedene DNS-Eintragstypen abzufragen, was Ihnen hilft zu verstehen, wie Hostnamen in IP-Adressen aufgelöst werden.
2. **[Lokale Hostnamenauflösung in Linux verwalten](https://labex.io/de/labs/comptia-manage-local-hostname-resolution-in-linux-592792)** - Üben Sie die Bearbeitung der Datei `/etc/hosts`, um die lokale Hostnamenauflösung zu verwalten, eine grundlegende Fähigkeit, um zu steuern, wie Ihr Linux-System Namen auflöst, ohne sich auf externe DNS-Server verlassen zu müssen.
3. **[Einen lokalen autoritativen DNS-Server unter Linux einrichten](https://labex.io/de/labs/comptia-set-up-a-local-authoritative-dns-server-on-linux-592803)** - Sammeln Sie praktische Erfahrungen, indem Sie Ihren eigenen lokalen autoritativen DNS-Server mit `bind9` einrichten und konfigurieren, sodass Sie tiefer in die Verwaltung von DNS-Zonen und -Einträgen eintauchen können.

Diese Labs helfen Ihnen, die Konzepte in realen Szenarien anzuwenden und Vertrauen in DNS und Hostnamenauflösung in einer Linux-Umgebung aufzubauen.

## Quiz Question

Richtig oder falsch: DNS hilft uns, MAC-Adressen für Hostnamen zu finden?

## Quiz Answer

False
