---
lang: "de"
title: "Tools zur Benutzerverwaltung"
meta_description: "Lernen Sie die Linux-Benutzerverwaltung: Hinzufügen, Entfernen und Ändern von Passwörtern mit den Befehlen useradd, userdel und passwd. Starten Sie mit dieser anfängerfreundlichen Anleitung!"
meta_keywords: "Linux-Benutzerverwaltung, adduser, userdel, passwd, Linux-Tutorial, Linux für Anfänger, Benutzerkonten, Linux-Befehle"
---

## Lesson Content

Die meisten Unternehmensumgebungen verwenden Managementsysteme zur Verwaltung von Benutzern, Konten und Passwörtern. Auf einem Einzelplatzcomputer gibt es jedoch nützliche Befehle zur Benutzerverwaltung.

### Hinzufügen von Benutzern

Sie können den Befehl `adduser` oder `useradd` verwenden. Der Befehl `adduser` enthält hilfreichere Funktionen, wie z. B. das Erstellen eines Home-Verzeichnisses und mehr. Es gibt Konfigurationsdateien zum Hinzufügen neuer Benutzer, die je nachdem, was Sie einem Standardbenutzer zuweisen möchten, angepasst werden können.

```bash
sudo useradd bob
```

Sie werden sehen, dass der obige Befehl einen Eintrag in `/etc/passwd` für bob erstellt, Standardgruppen einrichtet und einen Eintrag in der Datei `/etc/shadow` hinzufügt.

### Entfernen von Benutzern

Um einen Benutzer zu entfernen, können Sie den Befehl `userdel` verwenden.

```bash
sudo userdel bob
```

Dies versucht im Wesentlichen, die durch `useradd` vorgenommenen Dateiänderungen rückgängig zu machen.

### Ändern von Passwörtern

```bash
passwd bob
```

Dies ermöglicht es Ihnen, das Passwort von sich selbst oder einem anderen Benutzer zu ändern (wenn Sie root sind).

## Exercise

Erstellen Sie einen neuen Benutzer, ändern Sie dann dessen Passwort und melden Sie sich als der neue Benutzer an.

## Quiz Question

Welcher Befehl wird verwendet, um ein Passwort zu ändern?

## Quiz Answer

passwd
