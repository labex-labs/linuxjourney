---
index: 6
lang: "de"
title: "Benutzerverwaltungstools"
meta_title: "Benutzerverwaltungstools - Benutzerverwaltung"
meta_description: "Lernen Sie die Linux-Benutzerverwaltung: Hinzufügen, Entfernen und Ändern von Passwörtern mit den Befehlen useradd, userdel und passwd. Starten Sie mit diesem anfängerfreundlichen Leitfaden!"
meta_keywords: "Linux-Benutzerverwaltung, adduser, userdel, passwd, Linux-Tutorial, Linux für Anfänger, Benutzerkonten, Linux-Befehle"
---

## Lesson Content

Die meisten Unternehmensumgebungen verwenden Managementsysteme zur Verwaltung von Benutzern, Konten und Passwörtern. Auf einem Einzelplatzcomputer gibt es jedoch nützliche Befehle zur Benutzerverwaltung.

### Benutzer hinzufügen

Sie können den Befehl `adduser` oder `useradd` verwenden. Der Befehl `adduser` enthält nützlichere Funktionen, wie das Erstellen eines Home-Verzeichnisses und mehr. Es gibt Konfigurationsdateien zum Hinzufügen neuer Benutzer, die je nachdem, was Sie einem Standardbenutzer zuweisen möchten, angepasst werden können.

```bash
sudo useradd bob
```

Sie werden sehen, dass der obige Befehl einen Eintrag in `/etc/passwd` für bob erstellt, Standardgruppen einrichtet und einen Eintrag in der Datei `/etc/shadow` hinzufügt.

### Benutzer entfernen

Um einen Benutzer zu entfernen, können Sie den Befehl `userdel` verwenden.

```bash
sudo userdel bob
```

Dies versucht im Wesentlichen, die durch `useradd` vorgenommenen Dateiänderungen rückgängig zu machen.

### Passwörter ändern

```bash
passwd bob
```

Dies ermöglicht es Ihnen, das Passwort von sich selbst oder einem anderen Benutzer zu ändern (wenn Sie root sind).

## Exercise

Übung macht den Meister! Hier sind einige praktische Übungen, um Ihr Verständnis der Benutzer- und Kontoverwaltung in Linux zu vertiefen:

1. **[Linux-Benutzerkonten mit useradd, usermod und userdel verwalten](https://labex.io/de/labs/comptia-manage-linux-user-accounts-with-useradd-usermod-and-userdel-590837)** – Üben Sie den gesamten Lebenszyklus der Benutzerverwaltung, vom Erstellen und Sichern neuer Konten bis zum Ändern und Löschen.
2. **[Linux-Gruppen mit groupadd, usermod und groupdel verwalten](https://labex.io/de/labs/comptia-manage-linux-groups-with-groupadd-usermod-and-groupdel-590836)** – Sammeln Sie praktische Erfahrungen mit den wichtigsten Befehlszeilenprogrammen für die Gruppenverwaltung, einschließlich des Hinzufügens, Änderns und Löschens von Gruppen.
3. **[Benutzerkonten und Sudo-Berechtigungen in Linux konfigurieren](https://labex.io/de/labs/comptia-configure-user-accounts-and-sudo-privileges-in-linux-590856)** – Lernen Sie wesentliche Techniken zur Verwaltung von Benutzerkonten und Sudo-Berechtigungen, um die Sicherheit eines Linux-Systems zu verbessern.

Diese Übungen helfen Ihnen, die Konzepte in realen Szenarien anzuwenden und Vertrauen in die Linux-Benutzer- und Gruppenverwaltung aufzubauen.

## Quiz Question

Welcher Befehl wird verwendet, um ein Passwort zu ändern?

## Quiz Answer

passwd
