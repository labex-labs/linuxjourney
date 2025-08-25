---
index: 4
lang: "de"
title: "/etc/shadow"
meta_title: "/etc/shadow - Benutzerverwaltung"
meta_description: "Erfahren Sie mehr über die Datei /etc/shadow in Linux, ihre Felder und wie sie Benutzerpasswörter sichert. Verstehen Sie die Linux-Authentifizierung für Anfänger."
meta_keywords: "/etc/shadow, Linux-Sicherheit, Benutzerauthentifizierung, Passwortverwaltung, Linux-Tutorial, Anfängerleitfaden"
---

## Lesson Content

Die Datei `/etc/shadow` wird verwendet, um Informationen zur Benutzerauthentifizierung zu speichern. Sie erfordert Superuser-Leseberechtigungen.

```bash
$ sudo cat /etc/shadow

root:MyEPTEa$6Nonsense:15000:0:99999:7:::
```

Sie werden feststellen, dass sie dem Inhalt von `/etc/passwd` sehr ähnlich sieht; im Passwortfeld sehen Sie jedoch ein verschlüsseltes Passwort. Die Felder sind durch Doppelpunkte getrennt, wie folgt:

1. Benutzername
2. Verschlüsseltes Passwort
3. Datum der letzten Passwortänderung – ausgedrückt als Anzahl der Tage seit dem 1. Januar 1970. Wenn eine 0 vorhanden ist, bedeutet dies, dass der Benutzer sein Passwort beim nächsten Login ändern sollte.
4. Mindestalter des Passworts – Tage, die ein Benutzer warten muss, bevor er sein Passwort erneut ändern kann.
5. Maximales Passwortalter – Maximale Anzahl von Tagen, bevor ein Benutzer sein Passwort ändern muss.
6. Passwort-Warnperiode – Anzahl der Tage, bevor ein Passwort abläuft.
7. Passwort-Inaktivitätsperiode – Anzahl der Tage nach Ablauf eines Passworts, um die Anmeldung mit diesem Passwort zu erlauben.
8. Ablaufdatum des Kontos – Datum, an dem sich ein Benutzer nicht mehr anmelden kann.
9. Reserviertes Feld für zukünftige Verwendung.

In den meisten Distributionen von heute basiert die Benutzerauthentifizierung nicht nur auf der Datei `/etc/shadow`; es gibt andere Mechanismen, wie z.B. PAM (Pluggable Authentication Modules), die die Authentifizierung ersetzen.

## Exercise

Übung macht den Meister! Hier sind einige praktische Übungen, um Ihr Verständnis der Benutzerauthentifizierung und Passwortverwaltung unter Linux zu vertiefen:

1. **[Linux-Benutzerkonten mit useradd, usermod und userdel verwalten](https://labex.io/de/labs/comptia-manage-linux-user-accounts-with-useradd-usermod-and-userdel-590837)** – Üben Sie den gesamten Lebenszyklus der Benutzerverwaltung, vom Erstellen und Sichern neuer Konten mit `useradd` und `passwd` bis zum Ändern und Löschen.
2. **[Benutzerkonten und Sudo-Berechtigungen in Linux konfigurieren](https://labex.io/de/labs/comptia-configure-user-accounts-and-sudo-privileges-in-linux-590856)** – Lernen Sie wesentliche Techniken zur Verwaltung von Benutzerkonten und Sudo-Berechtigungen, einschließlich der Durchsetzung von Passwortrichtlinien und der Sicherung von Konten.

Diese Übungen helfen Ihnen, die Konzepte der Benutzer- und Passwortverwaltung in realen Szenarien anzuwenden und Vertrauen in die Linux-Systemadministration aufzubauen.

## Quiz Question

Keine Fragen, weiter geht's!

## Quiz Answer
