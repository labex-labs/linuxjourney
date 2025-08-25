---
index: 3
lang: "de"
title: "Pfad eines Pakets"
meta_title: "Pfad eines Pakets - Routing"
meta_description: "Erfahren Sie, wie ein Paket innerhalb und außerhalb eines Netzwerks reist. Verstehen Sie IP, MAC, ARP und Routing-Tabellen für die Netzwerkkommunikation. Beginnen Sie Ihre Linux-Netzwerkreise!"
meta_keywords: "Paketreise, Netzwerkkommunikation, ARP, IP-Adresse, MAC-Adresse, Routing-Tabelle, Linux-Netzwerk, Anfängerleitfaden"
---

## Lesson Content

### Schauen wir uns an, wie ein Paket innerhalb seines lokalen Netzwerks reist

1. Zuerst vergleicht die lokale Maschine die Ziel-IP-Adresse, um festzustellen, ob sie sich im selben Subnetz befindet, indem sie ihre Subnetzmaske überprüft.
2. Wenn Pakete gesendet werden, benötigen sie eine Quell-MAC-Adresse, eine Ziel-MAC-Adresse, eine Quell-IP-Adresse und eine Ziel-IP-Adresse. Zu diesem Zeitpunkt kennen wir die Ziel-MAC-Adresse nicht.
3. Um den Zielhost zu erreichen, verwenden wir ARP, um eine Anfrage im lokalen Netzwerk zu senden, um die MAC-Adresse des Zielhosts zu finden.
4. Jetzt kann das Paket erfolgreich gesendet werden!

### Schauen wir uns an, wie ein Paket außerhalb seines Netzwerks reist

1. Zuerst vergleicht die lokale Maschine die Ziel-IP-Adresse. Da sie sich außerhalb unseres Netzwerks befindet, sieht sie die MAC-Adresse des Zielhosts nicht. Und wir können ARP nicht verwenden, da die ARP-Anfrage eine Broadcast-Nachricht an lokal verbundene Hosts ist.
2. Unser Paket schaut sich nun die Routing-Tabelle an. Es kennt die Adresse der Ziel-IP nicht, also sendet es sie an das Standard-Gateway (einen anderen Router). Unser Paket enthält nun unsere Quell-IP, Ziel-IP und Quell-MAC; wir haben jedoch keine Ziel-MAC. Denken Sie daran, MAC-Adressen werden nur innerhalb desselben Netzwerks erreicht. Was tut es also? Es sendet eine ARP-Anfrage, um die MAC-Adresse des Standard-Gateways zu erhalten.
3. Der Router schaut sich das Paket an und bestätigt die Ziel-MAC-Adresse, aber es ist nicht die endgültige Ziel-IP-Adresse, also schaut er weiterhin in der Routing-Tabelle nach, um das Paket an eine andere IP-Adresse weiterzuleiten, die dem Paket helfen kann, sein Ziel zu erreichen. Jedes Mal, wenn sich das Paket bewegt, entfernt es die alten Quell- und Ziel-MAC-Adressen und aktualisiert das Paket mit den neuen Quell- und Ziel-MAC-Adressen.
4. Sobald das Paket an dasselbe Netzwerk weitergeleitet wird, verwenden wir ARP, um die endgültige Ziel-MAC-Adresse zu finden.
5. Während dieses Prozesses ändert unser Paket weder die Quell- noch die Ziel-IP-Adresse.

## Exercise

Übung macht den Meister! Hier sind einige praktische Übungen, um Ihr Verständnis der grundlegenden Linux-Datei- und Verzeichnisverwaltung zu vertiefen:

1. **[Grundlegende Dateioperationen in Linux](https://labex.io/de/labs/linux-basic-file-operations-in-linux-18001)** - Üben Sie das Navigieren im Dateisystem, das Verwalten von Dateien und Verzeichnissen und die Verwendung von Befehlszeilen-Shortcuts in einer echten Linux-Umgebung.
2. **[Datei- und Verzeichnisoperationen](https://labex.io/de/labs/linux-file-and-directory-operations-17997)** - Lernen Sie, die Verzeichnisstruktur zu navigieren, Dateien und Ordner zu verwalten und leistungsstarke Befehlszeilentools wie `ls`, `cd`, `mkdir`, `cp`, `mv` und `rm` zu verwenden.
3. **[Dateien und Verzeichnisse organisieren](https://labex.io/de/labs/linux-organizing-files-and-directories-387877)** - Üben Sie grundlegende Linux-Dateiverwaltungsfähigkeiten, indem Sie die Befehle `cp`, `mv` und `rm` verwenden, um eine Projektstruktur zu organisieren, Dateien zu verschieben und unnötige Verzeichnisse zu bereinigen.

Diese Labs helfen Ihnen, die Konzepte in realen Szenarien anzuwenden und Vertrauen im Umgang mit Linux-Dateisystemen aufzubauen.

## Quiz Question

Wie finden wir die MAC-Adresse einer IP-Adresse heraus?

## Quiz Answer

ARP
