---
index: 3
lang: "de"
title: "/etc/passwd"
meta_title: "/etc/passwd - Benutzerverwaltung"
meta_description: "Ein umfassender Leitfaden zur /etc/passwd-Datei unter Linux. Erfahren Sie, wie Sie Benutzerdatenfelder interpretieren, UIDs verstehen und Beispiele wie root:x:0:0:root:/root:/bin/bash sehen."
meta_keywords: "/etc/passwd, /etc/passwd in linux, root:x:0:0:root:/root:/bin/bash, Benutzer-ID, UID, Benutzerverwaltung, Linux Tutorial"
---

## Lesson Content

Unter Linux sind Benutzernamen menschenlesbare Bezeichnungen, aber das System identifiziert Benutzer anhand einer eindeutigen Benutzer-ID (UID). Die Zuordnung zwischen Benutzernamen und UIDs wird in der Datei `/etc/passwd` gespeichert, einer kritischen Komponente für die Benutzerverwaltung.

Um ihren Inhalt anzuzeigen, können Sie einen einfachen Befehl verwenden:

```bash
cat /etc/passwd
```

Diese Datei zeigt eine Liste aller Systembenutzer und detaillierte Informationen über sie an. Jede Zeile repräsentiert ein einzelnes Benutzerkonto.

### Die Felder von /etc/passwd aufschlüsseln

A-typische Zeile in dieser Datei, oft die allererste, sieht wie folgt aus:

```plaintext
root:x:0:0:root:/root:/bin/bash
```

Dieser Eintrag für den Benutzer `root` enthält sieben durch Doppelpunkte (`:`) getrennte Felder. Das Verständnis der Struktur von `/etc/passwd` unter Linux ist der Schlüssel zur Verwaltung von Benutzern. Lassen Sie uns jedes Feld aufschlüsseln:

1. **Benutzername**: Der Anmeldename des Benutzers (z. B. `root`).
2. **Passwort**: Ein Platzhalter für das verschlüsselte Passwort des Benutzers. Das tatsächliche Passwort wird aus Sicherheitsgründen hier nicht gespeichert.
    - Ein `x` zeigt an, dass das verschlüsselte Passwort in der Datei `/etc/shadow` gespeichert ist.
    - Ein `*` (Sternchen) bedeutet, dass das Konto gesperrt ist und nicht für die Anmeldung verwendet werden kann.
    - Ein leeres Feld bedeutet, dass der Benutzer kein Passwort hat.
3. **Benutzer-ID (UID)**: Die eindeutige numerische Kennung für den Benutzer. Der Benutzer `root` hat immer eine UID von `0`.
4. **Gruppen-ID (GID)**: Die numerische Kennung für die primäre Gruppe des Benutzers.
5. **GECOS-Feld**: Ein Kommentarfeld, das traditionell zusätzliche Informationen wie den vollständigen Namen des Benutzers, die Telefonnummer oder den Bürositz enthält. Es ist durch Kommas getrennt.
6. **Home-Verzeichnis**: Der absolute Pfad zum Home-Verzeichnis des Benutzers (z. B. `/root`).
7. **Standard-Shell**: Der Standard-Kommandozeileninterpreter des Benutzers, der bei der Anmeldung ausgeführt wird (z. B. `/bin/bash`).

### Systembenutzer und spezielle Konten

Wenn Sie die Datei `/etc/passwd` überprüfen, werden Ihnen viele Konten auffallen, die nicht zu menschlichen Benutzern gehören. Dies sind Systemkonten, die verwendet werden, um bestimmte Dienste oder Prozesse mit eingeschränkten Berechtigungen auszuführen, was die Systemsicherheit erhöht. Zum Beispiel wird der Benutzer `daemon` zur Ausführung von Hintergrundprozessen (Daemons) verwendet.

### Bearbeiten der Datei /etc/passwd

Obwohl Sie die Datei `/etc/passwd` technisch gesehen direkt mit einem Texteditor oder dem Befehl `vipw` bearbeiten können, wird dies dringend abgeraten. Manuelle Bearbeitungen können leicht Syntaxfehler verursachen, was Sie potenziell vom System aussperren oder zu Instabilität führen kann.

Es ist immer sicherer und zuverlässiger, dedizierte Befehlszeilen-Dienstprogramme wie `useradd`, `usermod` und `userdel` zur Verwaltung von Benutzerkonten zu verwenden. Diese Tools sind dafür konzipiert, die Datei korrekt zu ändern und alle zugehörigen Konfigurationen zu verwalten.

## Exercise

Um Ihr Wissen zu festigen, probieren Sie diese praktischen Übungen aus. Sie helfen Ihnen, die Konzepte von Benutzer-IDs und Kontoverwaltung in realen Szenarien anzuwenden und Vertrauen in die Linux-Benutzeradministration aufzubauen.

1. **[Linux-Benutzerkonten mit useradd, usermod und userdel verwalten](https://labex.io/de/labs/comptia-manage-linux-user-accounts-with-useradd-usermod-and-userdel-590837)** - Üben Sie den gesamten Lebenszyklus der Benutzeradministration, vom Erstellen und Sichern neuer Konten bis hin zum Ändern und Löschen dieser.
2. **[Linux-Gruppen mit groupadd, usermod und groupdel verwalten](https://labex.io/de/labs/comptia-manage-linux-groups-with-groupadd-usermod-and-groupdel-590836)** - Sammeln Sie praktische Erfahrungen mit grundlegenden Befehlszeilen-Dienstprogrammen für die Gruppenadministration, einschließlich der Erstellung neuer Gruppen und der Änderung von Benutzerzuordnungen.
3. **[Benutzerkonten und Sudo-Berechtigungen in Linux konfigurieren](https://labex.io/de/labs/comptia-configure-user-accounts-and-sudo-privileges-in-linux-590856)** - Lernen Sie wesentliche Techniken zur Verwaltung von Benutzerkonten und Sudo-Berechtigungen kennen, um die Sicherheit eines Linux-Systems zu erhöhen.

## Quiz Question

Wenn ein Benutzerkonto gesperrt ist und nicht zur Anmeldung verwendet werden kann, wie wird dies im Passwortfeld der Datei `/etc/passwd` gekennzeichnet? Antworten Sie nur mit dem erforderlichen Zeichen.

## Quiz Answer

`*`
