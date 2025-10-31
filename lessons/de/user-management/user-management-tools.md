---
index: 6
lang: "de"
title: "Benutzerverwaltungstools"
meta_title: "Benutzerverwaltungstools - Benutzerverwaltung"
meta_description: "Meistern Sie die Linux-Benutzerverwaltung mit essentiellen Kommandozeilen-Tools. Dieser Leitfaden behandelt die Verwendung von useradd, userdel und passwd zur Verwaltung von Konten unter Linux, ideal für Anfänger."
meta_keywords: "linux benutzerverwaltung, das kommandozeilen-tool zur verwaltung von kontos in linux, useradd, userdel, passwd, linux konten, benutzer verwalten linux"
---

## Lesson Content

Obwohl viele Unternehmensumgebungen auf dedizierte Systeme für das Identitätsmanagement angewiesen sind, ist das Verständnis der Grundlagen der **Linux-Benutzerverwaltung** direkt auf einer einzelnen Maschine eine entscheidende Fähigkeit. Verschiedene Dienstprogramme dienen als **das Befehlszeilentool für die Verwaltung von Konten unter Linux** und ermöglichen eine effiziente Administration über das Terminal.

### Benutzer hinzufügen

Um einen neuen Benutzer zu erstellen, können Sie den Befehl `useradd` verwenden. Es handelt sich um ein Low-Level-Dienstprogramm, das ein neues Benutzerkonto basierend auf Standardwerten in `/etc/default/useradd` erstellt. Obwohl einige Systeme auch `adduser` anbieten, ein interaktiveres und benutzerfreundlicheres Skript, ist `useradd` der universelle Standard.

```bash
sudo useradd bob
```

Die Ausführung dieses Befehls fügt einen Eintrag für den Benutzer "bob" in die Datei `/etc/passwd` ein, richtet Standardgruppenmitgliedschaften ein und erstellt einen entsprechenden Eintrag in der Datei `/etc/shadow`, um Kennwortinformationen sicher zu speichern.

### Benutzer entfernen

Um ein Benutzerkonto zu entfernen, können Sie den Befehl `userdel` verwenden. Dieser Befehl kehrt effektiv die durch `useradd` vorgenommenen Änderungen um, indem die Einträge des Benutzers aus den Systemkontodateien entfernt werden.

```bash
sudo userdel bob
```

Standardmäßig entfernt dieser Befehl möglicherweise nicht das Home-Verzeichnis des Benutzers. Sie können das Flag `-r` (`userdel -r bob`) verwenden, um sicherzustellen, dass auch das Home-Verzeichnis und der Mail-Spool gelöscht werden.

### Kennwörter ändern

Der Befehl `passwd` wird verwendet, um das Kennwort eines Benutzers festzulegen oder zu ändern. Ein regulärer Benutzer kann diesen Befehl ausführen, um sein eigenes Kennwort zu ändern. Der Root-Benutzer kann ihn ausführen, um das Kennwort eines beliebigen Benutzers zu ändern.

```bash
passwd bob
```

Wenn er von einem Administrator ausgeführt wird, fordert das System zur Eingabe eines neuen Kennworts für den angegebenen Benutzer auf, ohne nach dem alten zu fragen. Dies ist eine grundlegende Aufgabe in der **Linux-Benutzerverwaltung**.

## Exercise

Übung macht den Meister! Hier sind einige praktische Übungen, um Ihr Verständnis der Benutzer- und Kontoverwaltung unter Linux zu festigen:

1. **[Linux-Benutzerkonten mit useradd, usermod und userdel verwalten](https://labex.io/de/labs/comptia-manage-linux-user-accounts-with-useradd-usermod-and-userdel-590837)** - Üben Sie den vollständigen Lebenszyklus der Benutzeradministration, vom Erstellen und Sichern neuer Konten bis hin zum Ändern und Löschen dieser.
2. **[Linux-Gruppen mit groupadd, usermod und groupdel verwalten](https://labex.io/de/labs/comptia-manage-linux-groups-with-groupadd-usermod-and-groupdel-590836)** - Sammeln Sie praktische Erfahrungen mit zentralen Befehlszeilentools für die Gruppenadministration, einschließlich dem Hinzufügen, Ändern und Löschen von Gruppen.
3. **[Benutzerkonten und Sudo-Berechtigungen unter Linux konfigurieren](https://labex.io/de/labs/comptia-configure-user-accounts-and-sudo-privileges-in-linux-590856)** - Lernen Sie wesentliche Techniken zur Verwaltung von Benutzerkonten und Sudo-Berechtigungen kennen, um die Sicherheit eines Linux-Systems zu erhöhen.

Diese Labs helfen Ihnen, die Konzepte in realen Szenarien anzuwenden und Vertrauen in die Linux-Benutzer- und Gruppenverwaltung aufzubauen.

## Quiz Question

Welcher Befehl wird verwendet, um ein Kennwort zu ändern? Bitte antworten Sie nur mit dem Befehlsnamen in Kleinbuchstaben auf Englisch.

## Quiz Answer

passwd
