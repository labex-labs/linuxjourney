---
index: 5
lang: "de"
title: "/etc/group"
meta_title: "/etc/group - Benutzerverwaltung"
meta_description: "Erfahren Sie mehr über die Datei /etc/group in Linux, verstehen Sie Gruppenverwaltung, GID und Benutzerberechtigungen. Ein essentielles Linux-Gruppendatei-Tutorial für Anfänger."
meta_keywords: "/etc/group, Linux-Gruppen, Gruppenverwaltung, GID, Linux-Berechtigungen, Linux-Tutorial, Linux für Anfänger, Linux-Anleitung"
---

## Lesson Content

Eine weitere Datei, die in der Benutzerverwaltung verwendet wird, ist die Datei `/etc/group`. Diese Datei ermöglicht verschiedene Gruppen mit unterschiedlichen Berechtigungen.

```bash
$ cat /etc/group

root:*:0:pete
```

Ähnlich wie bei der Datei `/etc/passwd` sind die Felder der Datei `/etc/group` wie folgt:

1. Gruppenname
2. Gruppenpasswort – es ist nicht notwendig, ein Gruppenpasswort festzulegen; die Verwendung eines erhöhten Privilegs wie `sudo` ist Standard. Ein Sternchen (`*`) wird als Standardwert eingesetzt.
3. Gruppen-ID (GID)
4. Liste der Benutzer – Sie können manuell Benutzer angeben, die Sie in einer bestimmten Gruppe haben möchten

## Exercise

Übung macht den Meister! Hier sind einige praktische Labs, um Ihr Verständnis der Linux-Benutzer- und Gruppenverwaltung zu vertiefen:

1. **[Linux-Benutzerkonten mit useradd, usermod und userdel verwalten](https://labex.io/de/labs/comptia-manage-linux-user-accounts-with-useradd-usermod-and-userdel-590837)** – Üben Sie den gesamten Lebenszyklus der Benutzerverwaltung, vom Erstellen und Sichern neuer Konten bis zum Ändern und Löschen.
2. **[Linux-Gruppen mit groupadd, usermod und groupdel verwalten](https://labex.io/de/labs/comptia-manage-linux-groups-with-groupadd-usermod-and-groupdel-590836)** – Sammeln Sie praktische Erfahrungen mit den wichtigsten Befehlszeilendienstprogrammen für die Gruppenverwaltung, einschließlich `groupadd`, `usermod` und `groupdel`.
3. **[Neuen Benutzer und neue Gruppe hinzufügen](https://labex.io/de/labs/linux-add-new-user-and-group-17987)** – Simulieren Sie das Hinzufügen neuer Teammitglieder zu einer Serverumgebung, indem Sie neue Benutzerkonten erstellen, benutzerdefinierte Gruppen einrichten und Gruppenmitgliedschaften verwalten.

Diese Labs helfen Ihnen, die Konzepte in realen Szenarien anzuwenden und Vertrauen in die Linux-Benutzer- und Gruppenverwaltung aufzubauen.

## Quiz Question

Was ist die GID von root?

## Quiz Answer

0
