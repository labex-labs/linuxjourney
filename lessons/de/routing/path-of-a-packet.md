---
index: 3
lang: "de"
title: "Pfad eines Pakets"
meta_title: "Pfad eines Pakets - Routing"
meta_description: "Erkunden Sie den vollständigen Paketpfad für Daten, die sich innerhalb eines lokalen Netzwerks und über das Internet bewegen. Erfahren Sie, wie IP-Adressen, MAC-Adressen, ARP und Routing-Tabellen zusammenarbeiten, um eine erfolgreiche Netzwerkkommunikation unter Linux zu gewährleisten."
meta_keywords: "Paketpfad, Netzwerkkommunikation, ARP, IP-Adresse, MAC-Adresse, Routing-Tabelle, Standard-Gateway, Linux-Netzwerk, Paketverfolgung"
---

## Lesson Content

Das Verständnis, wie Daten durch ein Netzwerk reisen, ist grundlegend für die Netzwerktechnik. Diese Reise, oft als **Paketpfad** bezeichnet, erfordert eine koordinierte Anstrengung zwischen verschiedenen Protokollen und Hardware. Verfolgen wir den **Paketpfad** in zwei gängigen Szenarien: Kommunikation innerhalb eines lokalen Netzwerks und Kommunikation mit einem externen Netzwerk.

### Paketpfad innerhalb eines lokalen Netzwerks

Wenn ein Gerät ein Paket an ein anderes Gerät im selben lokalen Netzwerk sendet, ist der Prozess relativ unkompliziert.

1. Zuerst prüft der sendende Host, ob sich die Ziel-IP-Adresse im selben Subnetz befindet, indem er sie mit seiner eigenen IP-Adresse und Subnetzmaske vergleicht.
2. Um ein Paket zu senden, benötigt der Host vier Schlüsselinformationen: eine Quell-IP, eine Ziel-IP, eine Quell-MAC-Adresse und eine Ziel-MAC-Adresse. Anfangs kennt der Host die MAC-Adresse des Zielhosts nicht.
3. Der Host verwendet das Address Resolution Protocol (ARP), um die fehlenden Informationen zu finden. Er sendet eine ARP-Anfrage als Broadcast im lokalen Netzwerk und fragt, welches Gerät die Ziel-IP-Adresse besitzt. Das entsprechende Gerät antwortet mit seiner MAC-Adresse.
4. Da die Ziel-MAC-Adresse nun bekannt ist, ist das Paket vollständig adressiert und kann direkt an den Zielhost im lokalen Netzwerk gesendet werden.

### Paketpfad zu einem externen Netzwerk

Wenn ein Paket für ein Gerät außerhalb des lokalen Netzwerks bestimmt ist, beinhaltet der Prozess Router zur Weiterleitung des Pakets.

1. Der sendende Host stellt fest, dass sich die Ziel-IP-Adresse nicht in seinem lokalen Netzwerk befindet. Da ARP-Broadcasts auf das lokale Netzwerk beschränkt sind, kann der Host die MAC-Adresse des endgültigen Ziels nicht direkt ermitteln.
2. Der Host konsultiert seine Routing-Tabelle. Da es keine spezifische Route für die externe IP gibt, verwendet er die Standardroute, die auf das Standard-Gateway (einen Router) zeigt. Das Paket wird mit den ursprünglichen Quell- und Ziel-IP-Adressen vorbereitet. Die Ziel-MAC-Adresse wird jedoch auf die MAC-Adresse des Standard-Gateways gesetzt. Falls die MAC des Gateways unbekannt ist, verwendet der Host ARP, um sie zu finden.
3. Sobald das Paket den Router erreicht, untersucht der Router die Ziel-IP-Adresse und konsultiert seine eigene Routing-Tabelle, um den nächsten Hop auf dem **Paketpfad** zu bestimmen. Der Router schreibt dann die MAC-Adressen des Pakets neu: Die Quell-MAC wird zur MAC des Routers und die Ziel-MAC wird zur MAC des nächsten Hops. Dieser Vorgang wird bei jedem Router entlang des Pfades wiederholt.
4. Wenn das Paket schließlich beim Router ankommt, der mit dem lokalen Netzwerk des Ziels verbunden ist, verwendet dieser Router ARP, um die MAC-Adresse des endgültigen Hosts zu finden und das Paket zuzustellen.
5. Während dieser gesamten Reise bleiben die Quell- und Ziel-IP-Adressen im Paket-Header unverändert. Nur die MAC-Adressen werden bei jedem Hop aktualisiert.

## Exercise

Übung macht den Meister! Hier sind einige praktische Labs, um Ihr Verständnis der grundlegenden Linux-Datei- und Verzeichnisverwaltung zu festigen:

1. **[Grundlegende Dateioperationen unter Linux](https://labex.io/de/labs/linux-basic-file-operations-in-linux-18001)** - Üben Sie die Navigation im Dateisystem, die Verwaltung von Dateien und Verzeichnissen sowie die Verwendung von Tastenkombinationen in einer realen Linux-Umgebung.
2. **[Datei- und Verzeichnisoperationen](https://labex.io/de/labs/linux-file-and-directory-operations-17997)** - Lernen Sie, die Verzeichnisstruktur zu navigieren, Dateien und Ordner zu verwalten und leistungsstarke Befehlszeilentools wie `ls`, `cd`, `mkdir`, `cp`, `mv` und `rm` zu verwenden.
3. **[Organisieren von Dateien und Verzeichnissen](https://labex.io/de/labs/linux-organizing-files-and-directories-387877)** - Üben Sie wesentliche Linux-Dateiverwaltungsfähigkeiten, indem Sie die Befehle `cp`, `mv` und `rm` verwenden, um eine Projektstruktur zu organisieren, Dateien zu verschieben und unnötige Verzeichnisse zu bereinigen.

Diese Labs helfen Ihnen, die Konzepte in realen Szenarien anzuwenden und Vertrauen in die Interaktion mit dem Linux-Dateisystem aufzubauen.

## Quiz Question

Welches Protokoll wird verwendet, um die MAC-Adresse eines Hosts im lokalen Netzwerk zu finden, wenn dessen IP-Adresse bekannt ist? Bitte antworten Sie mit dem dreibuchstabigen Akronym in Großbuchstaben.

## Quiz Answer

ARP
