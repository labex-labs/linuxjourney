---
index: 4
lang: "de"
title: "/etc/shadow"
meta_title: "/etc/shadow - Benutzerverwaltung"
meta_description: "Erkunden Sie die Datei /etc/shadow unter Linux, eine kritische Komponente für die Benutzerauthentifizierung. Erfahren Sie, wie Sie sie mit 'cat /etc/shadow' anzeigen und die Struktur der etc shadow-Datei verstehen, die verschlüsselte Passwörter und Richtlinieninformationen speichert."
meta_keywords: "etc shadow, etc/shadow datei in linux, cat /etc/shadow, etc shadow in linux, /etc/shadow, benutzerauthentifizierung, passwortsicherheit, Linux-Systemadministration"
---

## Lesson Content

Die Datei `/etc/shadow` ist eine kritische Komponente in Linux-Systemen zur Speicherung sensibler Benutzerauthentifizierungsinformationen. Im Gegensatz zur für alle lesbaren Datei `/etc/passwd` erfordert sie Superuser-Rechte für den Zugriff und bietet somit einen sicheren Speicherort für Passwortdaten.

### Die Rolle der etc/shadow-Datei in Linux

Der Hauptzweck der **etc/shadow-Datei in Linux** besteht darin, verschlüsselte Benutzernamen und Passwortalterungsrichtlinien zu speichern. Durch die Trennung dieser sensiblen Daten von den allgemeinen Benutzerinformationen in `/etc/passwd` erhöht das System die Sicherheit. Könnte ein Benutzer ohne Berechtigung die Passwort-Hashes lesen, könnte er versuchen, diese offline zu knacken.

### Anzeigen der Datei mit cat /etc/shadow

Um den Inhalt dieser Datei zu überprüfen, müssen Sie einen Befehl mit Superuser-Rechten verwenden, wie z. B. `sudo`. Der Befehl `cat /etc/shadow` wird häufig zu diesem Zweck verwendet.

```bash
$ sudo cat /etc/shadow

root:MyEPTEa$6Nonsense:15000:0:99999:7:::
```

Das Ausgabeformat der **etc shadow**-Datei ist eine Reihe von durch Doppelpunkte getrennten Feldern, wobei jede Zeile einen einzelnen Benutzer darstellt.

### Verständnis der Dateistruktur

Jede Zeile in `/etc/shadow` enthält neun Felder, die durch Doppelpunkte getrennt sind:

1. **Benutzername**: Der Anmeldename des Benutzers.
2. **Verschlüsseltes Passwort**: Das gehashte Benutzerpasswort. Ein Sternchen (`*`) oder ein Ausrufezeichen (`!`) hier bedeutet, dass das Konto gesperrt ist.
3. **Datum der letzten Passwortänderung**: Die Anzahl der Tage seit dem 1. Januar 1970, an dem das Passwort zuletzt geändert wurde. Ein Wert von `0` erzwingt eine Passwortänderung beim nächsten Login.
4. **Mindestalter des Passworts**: Die Mindestanzahl von Tagen, die vergehen muss, bevor der Benutzer sein Passwort erneut ändern kann.
5. **Maximales Alter des Passworts**: Die maximale Gültigkeitsdauer des Passworts in Tagen. Nach Ablauf dieser Frist muss der Benutzer es ändern.
6. **Passwort-Warnperiode**: Die Anzahl der Tage vor Ablauf des Passworts, an denen der Benutzer eine Warnmeldung erhält.
7. **Inaktivitätsperiode des Passworts**: Die Anzahl der Tage nach Ablauf des Passworts, an denen das Konto deaktiviert wird.
8. **Ablaufdatum des Kontos**: Ein absolutes Datum, ausgedrückt in Tagen seit dem 1. Januar 1970, an dem das Benutzerkonto deaktiviert wird.
9. **Reserviertes Feld**: Dieses Feld ist für die zukünftige Verwendung reserviert.

Obwohl die Datei `/etc/shadow` grundlegend ist, ergänzen die meisten modernen Distributionen sie durch andere Authentifizierungsmechanismen wie Pluggable Authentication Modules (PAM), die flexiblere und fortschrittlichere Authentifizierungsschemata bieten.

## Exercise

Übung macht den Meister! Hier sind einige praktische Übungen, um Ihr Verständnis der Benutzerauthentifizierung und Passwortverwaltung in Linux zu festigen:

1. **[Linux-Benutzerkonten mit useradd, usermod und userdel verwalten](https://labex.io/de/labs/comptia-manage-linux-user-accounts-with-useradd-usermod-and-userdel-590837)** – Üben Sie den gesamten Lebenszyklus der Benutzeradministration, vom Erstellen und Sichern neuer Konten mit `useradd` und `passwd` bis hin zum Ändern und Löschen dieser.
2. **[Benutzerkonten und Sudo-Berechtigungen in Linux konfigurieren](https://labex.io/de/labs/comptia-configure-user-accounts-and-sudo-privileges-in-linux-590856)** – Lernen Sie wesentliche Techniken zur Verwaltung von Benutzerkonten und Sudo-Berechtigungen kennen, einschließlich der Durchsetzung von Passwortrichtlinien und der Sicherung von Konten.

Diese Labs helfen Ihnen, die Konzepte der Benutzer- und Passwortverwaltung in realen Szenarien anzuwenden und Vertrauen in die Linux-Systemadministration aufzubauen.

## Quiz Question

Keine Fragen, machen Sie weiter!
