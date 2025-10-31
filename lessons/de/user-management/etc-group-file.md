---
index: 5
lang: "de"
title: "/etc/group"
meta_title: "/etc/group - Benutzerverwaltung"
meta_description: "Erkunden Sie die Datei /etc/group unter Linux, um die Gruppenverwaltung zu verstehen. Erfahren Sie, wie Sie Gruppendaten mit cat /etc/group anzeigen, und verstehen Sie die Struktur einschließlich GID und Benutzerlisten. Dieser Leitfaden behandelt die Grundlagen der etc group linux Datei."
meta_keywords: "/etc/group, /etc/group linux, /etc/group datei in linux, cat /etc/group, etc group linux, Gruppenverwaltung, GID, Linux Berechtigungen, Linux Gruppen"
---

## Lesson Content

Unter Linux wird die Verwaltung von Berechtigungen für mehrere Benutzer durch die Verwendung von Gruppen vereinfacht. Die zentrale Datei hierfür ist `/etc/group`, die die Gruppen auf dem System und deren Mitglieder definiert.

### Was ist die /etc/group Datei?

Die Datei `/etc/group` unter Linux ist eine einfache Textdatei, die die Liste aller Benutzergruppen enthält. Jeder Gruppe können spezifische Berechtigungen für Dateien und Verzeichnisse zugewiesen werden, sodass Administratoren die Zugriffsrechte für mehrere Benutzer gleichzeitig effizient verwalten können. Das Verständnis dieser Datei ist entscheidend für die korrekte Benutzer- und Berechtigungsverwaltung in jeder `etc group linux`-Umgebung.

### Anzeigen von Gruppeninformationen

Um den Inhalt dieser Datei zu überprüfen, können Sie einen einfachen Befehl verwenden. Die Ausführung von `cat /etc/group` in Ihrem Terminal zeigt alle Gruppendefinitionen auf Ihrem System an.

```bash
$ cat /etc/group

root:*:0:pete
```

### Struktur der /etc/group Datei

Ähnlich wie bei der Datei `/etc/passwd` repräsentiert jede Zeile in der Datei `/etc/group` eine einzelne Gruppe und enthält vier durch Doppelpunkte (`:`) getrennte Felder.

1.  **Gruppenname**: Der eindeutige Name der Gruppe.
2.  **Gruppenpasswort**: Dieses Feld ist ein veraltetes Merkmal und wird selten verwendet. Moderne Systeme verwenden Tools wie `sudo` für erweiterte Berechtigungen anstelle von Gruppenpasswörtern. Sie sehen typischerweise einen Platzhalter wie ein Sternchen (`*`) oder ein 'x'.
3.  **Gruppen-ID (GID)**: Eine eindeutige numerische Kennung für die Gruppe. Das System verwendet intern oft die GID anstelle des Gruppennamens.
4.  **Liste der Benutzer**: Eine durch Kommas getrennte Liste von Benutzernamen, die Mitglieder dieser Gruppe sind.

Im Beispiel `root:*:0:pete` ist der Gruppenname `root`, es gibt kein Passwort, die GID ist `0` und der Benutzer `pete` ist Mitglied.

## Exercise

Übung macht den Meister! Hier sind einige praktische Übungen, um Ihr Verständnis der Linux Benutzer- und Gruppenverwaltung zu festigen:

1.  **[Linux-Benutzerkonten mit useradd, usermod und userdel verwalten](https://labex.io/de/labs/comptia-manage-linux-user-accounts-with-useradd-usermod-and-userdel-590837)** - Üben Sie den gesamten Lebenszyklus der Benutzeradministration, vom Erstellen und Sichern neuer Konten bis hin zum Ändern und Löschen dieser.
2.  **[Linux-Gruppen mit groupadd, usermod und groupdel verwalten](https://labex.io/de/labs/comptia-manage-linux-groups-with-groupadd-usermod-and-groupdel-590836)** - Sammeln Sie praktische Erfahrungen mit den zentralen Befehlszeilenprogrammen für die Gruppenadministration, einschließlich `groupadd`, `usermod` und `groupdel`.
3.  **[Neuen Benutzer und neue Gruppe hinzufügen](https://labex.io/de/labs/linux-add-new-user-and-group-17987)** - Simulieren Sie das Hinzufügen neuer Teammitglieder zu einer Serverumgebung, indem Sie neue Benutzerkonten erstellen, benutzerdefinierte Gruppen einrichten und Gruppenmitgliedschaften verwalten.

Diese Labs helfen Ihnen, die Konzepte in realen Szenarien anzuwenden und Vertrauen in die Linux Benutzer- und Gruppenverwaltung aufzubauen.

## Quiz Question

Was ist die GID von root?

## Quiz Answer

0
