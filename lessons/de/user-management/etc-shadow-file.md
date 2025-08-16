---
lang: "de"
title: "/etc/shadow"
description: "Erfahren Sie mehr über die Datei /etc/shadow in Linux, ihre Felder und wie sie Benutzerpasswörter schützt. Verstehen Sie die Linux-Authentifizierung für Anfänger."
keywords: "/etc/shadow, Linux-Sicherheit, Benutzerauthentifizierung, Passwortverwaltung, Linux-Tutorial, Anfängerleitfaden"
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
8. Ablaufdatum des Kontos – Datum, ab dem sich ein Benutzer nicht mehr anmelden kann.
9. Reserviertes Feld für zukünftige Verwendung.

In den meisten heutigen Distributionen basiert die Benutzerauthentifizierung nicht nur auf der Datei `/etc/shadow`; es gibt andere Mechanismen, wie PAM (Pluggable Authentication Modules), die die Authentifizierung ersetzen.

## Exercise

Werfen Sie einen Blick auf die Datei `/etc/shadow`.

## Quiz Question

Keine Fragen, weiter geht's!

## Quiz Answer

No questions, move along!
