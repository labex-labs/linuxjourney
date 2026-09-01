---
lesson_id: "user-management-tools"
course_id: "user-management"
lang: "de"
order_index: 6
title: "Werkzeuge zur Benutzerverwaltung"
description: "Erfahre, wie du lokale Konten mit ausdrücklichen Optionen erstellst, änderst, absicherst, überprüfst und entfernst."
meta_title: "Werkzeuge zur Benutzerverwaltung – Benutzerverwaltung"
meta_description: "Beherrsche die Linux-Benutzerverwaltung mit grundlegenden Befehlszeilenwerkzeugen. Dieser Leitfaden behandelt useradd, userdel und passwd zur Verwaltung von Konten unter Linux und eignet sich hervorragend für Einsteiger."
meta_keywords: "Linux-Benutzerverwaltung, Befehlszeilenwerkzeug zur Kontoverwaltung unter Linux, useradd, userdel, passwd, Linux-Konten, Linux-Benutzer verwalten"
---

Linux-Distributionen stellen gewöhnlich Kontowerkzeuge aus der Shadow-Utilities-Sammlung bereit, doch Voreinstellungen und übergeordnete Hilfsprogramme unterscheiden sich. Bevor du ein lokales Konto änderst, musst du bestätigen, dass es nicht zentral verwaltet wird, die lokale Handbuchseite des Befehls prüfen und einen Wiederherstellungsweg bereithalten.

Die Befehle in dieser Lektion verändern Authentifizierungs- und Eigentumszustände. Übe ausschließlich in einer autorisierten, entbehrlichen Umgebung und nicht auf einem Produktivsystem.

## Voreinstellungen für die Kontoerstellung prüfen

`useradd` erstellt ein lokales Konto anhand der Befehlsoptionen und der standortspezifischen Voreinstellungen. Zeige kompilierte und konfigurierte Voreinstellungen an mit:

```bash
$ useradd -D
```

Dateien wie `/etc/default/useradd`, `/etc/login.defs` und Vorlageninhalte können das Verhalten beeinflussen, doch ihre Rollen unterscheiden sich je nach Distribution. Ein übergeordneter Befehl `adduser` kann vorhanden sein, seine Oberfläche ist jedoch nicht auf allen Linux-Systemen standardisiert.

## Ein lokales Konto ausdrücklich erstellen

Gib in einer kontrollierten Umgebung wichtige Eigenschaften an, statt dich auf unbekannte Voreinstellungen zu verlassen:

```bash
$ sudo useradd -m -s /bin/bash -c "Bob Example" bob
```

- `-m` fordert die Erstellung des Home-Verzeichnisses an.
- `-s /bin/bash` wählt die Anmelde-Shell aus, nachdem du bestätigt hast, dass dieser Pfad erlaubt und installiert ist.
- `-c` gibt das GECOS-/Kommentarfeld an.

Das neue Konto kann sich gewöhnlich erst dann mit einem verwendbaren lokalen Passwort authentifizieren, wenn eines festgelegt wurde. Der genaue anfängliche Passwort- und Sperrzustand hängt jedoch von den lokalen Werkzeugen und Richtlinien ab. Überprüfe die Einträge, statt Annahmen zu treffen:

```bash
$ getent passwd bob
$ sudo passwd -S bob
$ id bob
```

:::single-choice{#user-tools-create-home} Welche Option von `useradd` fordert ausdrücklich die Erstellung des Home-Verzeichnisses für das neue Konto an?

::option[`-M`]{#user-tools-no-home-option explanation="Das großgeschriebene `-M` weist verbreitete `useradd`-Implementierungen ausdrücklich an, kein Home-Verzeichnis zu erstellen."}
::option[`-s`]{#user-tools-shell-option explanation="Die Option `-s` wählt eine Anmelde-Shell und erstellt nicht selbst ein Home-Verzeichnis."}
::option[`-m`]{#user-tools-home-option .correct explanation="Die kleingeschriebene Option `-m` fordert `useradd` auf, das Home-Verzeichnis gemäß den lokalen Voreinstellungen zu erstellen und zu befüllen."}
:::

## Ein Passwort festlegen oder ändern

Ein gewöhnlicher Benutzer ändert sein eigenes lokales Passwort interaktiv mit:

```bash
$ passwd
```

Ein autorisierter Administrator kann das Passwort eines anderen lokalen Kontos festlegen mit:

```bash
$ sudo passwd bob
```

Gib Passwörter ausschließlich an der geschützten Eingabeaufforderung ein und nicht in Befehlsargumenten, im Shell-Verlauf, in Lektionsnotizen oder in einem Chat. PAM-Richtlinien können schwache oder wiederverwendete Passwörter ablehnen. Für durch Verzeichnisdienste verwaltete Konten kann ein anderes Werkzeug erforderlich sein.

:::single-choice{#user-tools-change-own-password} Welcher Befehl ermöglicht dem aktuellen Benutzer gewöhnlich, sein eigenes Passwort über eine interaktive Eingabeaufforderung zu ändern?

::option[`useradd`]{#user-tools-add-not-password explanation="`useradd` erstellt einen Kontoeintrag und ist nicht der gewöhnliche interaktive Befehl zur Passwortänderung."}
::option[`userdel`]{#user-tools-delete-not-password explanation="`userdel` entfernt ein lokales Konto und hat nichts mit der Änderung des Passworts des Aufrufers zu tun."}
::option[`passwd`]{#user-tools-passwd-self .correct explanation="Ohne Benutzernamenoperand arbeitet `passwd` gemäß der PAM-Richtlinie mit dem lokalen Passwort des aufrufenden Benutzers."}
:::

## Kontoeigenschaften und Gruppen ändern

`usermod` ändert lokale Kontofelder. Beispiele sind:

```bash
$ sudo usermod -s /bin/zsh bob
$ sudo usermod -d /srv/home/bob -m bob
$ sudo usermod -aG developers bob
```

Prüfe vor dem Verschieben des Home-Verzeichnisses das Ziel, die Eigentumsverhältnisse, den verfügbaren Speicherplatz, laufende Prozesse, Einhängungen und Dienste. Bei ergänzenden Gruppen bedeutet `-aG`, dass die Gruppe der aktuellen Liste hinzugefügt wird. `-G` ohne `-a` ersetzt die gesamte Liste der ergänzenden Gruppen und kann unerwartet Zugriff entfernen.

Gruppenänderungen wirken gewöhnlich in neuen Anmeldesitzungen und nicht in Prozessen, die bereits mit den alten Zugangsdaten laufen.

:::single-choice{#user-tools-append-group} Welcher Befehl fügt `bob` der ergänzenden Gruppe `developers` hinzu, ohne seine anderen ergänzenden Mitgliedschaften zu ersetzen?

::option[`usermod -G developers bob`]{#user-tools-replace-groups explanation="Ohne `-a` ersetzt `-G` die Liste der ergänzenden Gruppen und kann bestehende Mitgliedschaften entfernen."}
::option[`usermod -aG developers bob`]{#user-tools-append-groups .correct explanation="Die Option `-a` fügt die mit `-G` benannte Gruppe hinzu und bewahrt andere ergänzende Mitgliedschaften."}
::option[`groupdel developers bob`]{#user-tools-delete-group explanation="`groupdel` entfernt eine Gruppendefinition und fügt keine Benutzermitgliedschaft hinzu."}
:::

## Ein lokales Passwort sperren

Ein Administrator kann den lokalen Passwort-Hash mit `passwd -l USER` sperren und den Status mit `passwd -S USER` prüfen. Die Entsperrung erfolgt mit `passwd -u USER`, aber erst nachdem geprüft wurde, warum die Sperre besteht und ob noch ein gültiger Hash vorhanden ist.

Eine Passwortsperre beendet nicht unbedingt den Zugriff über SSH-Schlüssel, Token, geplante Aufgaben, bereits laufende Prozesse oder dienstspezifische Authentifizierung. Um ein Konto umfassend zu deaktivieren, musst du die Bedrohung und die Zugriffswege bestimmen und anschließend eine abgestimmte Richtlinie anwenden. Diese kann Kontoablauf, Anmelde-Shell, Dienstzugriff, Schlüssel und Sitzungsbeendigung umfassen.

:::single-choice{#user-tools-password-lock-scope} Was sperrt `passwd -l bob` in erster Linie?

::option[Jeden möglichen Authentifizierungs- und Ausführungsweg für das Konto.]{#user-tools-lock-everything explanation="Schlüssel, Token, Aufgaben, Dienste und bestehende Sitzungen können getrennte Kontrollen erfordern."}
::option[Alle Dateien, die derzeit Bobs UID gehören.]{#user-tools-lock-files explanation="Der Passwortzustand ändert weder Dateisystemeigentum noch macht er Dateien im Besitz des Kontos automatisch unzugänglich."}
::option[Den lokalen Unix-Passwort-Hash, der für die Passwortauthentifizierung verwendet wird.]{#user-tools-lock-local-password .correct explanation="Der Befehl stellt dem lokalen Passwort-Hash ein Zeichen voran oder deaktiviert ihn auf andere Weise und verhindert so die normale Prüfung über diesen Weg."}
:::

## Ein lokales Konto bewusst entfernen

Ein einfaches `userdel bob` entfernt die lokalen Kontoeinträge, lässt das Home-Verzeichnis aber gewöhnlich bestehen. `userdel -r bob` versucht außerdem, das Home-Verzeichnis und den Mail-Spool zu entfernen, und ist damit ein destruktiver Vorgang.

Vor jeder Entfernung:

1. Bestätige das genaue Konto mit `getent passwd bob` und `id bob`.
2. Ermittle laufende Prozesse, geplante Aufgaben, Dienste, Schlüssel und delegierte Zugriffe.
3. Erfasse Dateien im Besitz der UID auf den vorgesehenen Dateisystemen.
4. Entscheide, ob Daten übertragen, archiviert, aufbewahrt oder sicher gelöscht werden müssen.
5. Stelle sicher, dass die UID nicht neu vergeben wird, solange verwaiste Dateien bestehen.

`userdel -r` garantiert nicht die Entfernung von Dateien außerhalb der konfigurierten Home- und Mail-Speicherorte. Das Löschen eines Kontos kann außerdem numerische Eigentumsangaben an Dateien, Datenbankberechtigungen, Anwendungsidentitäten und Einträge in entfernten Verzeichnisdiensten zurücklassen.

:::single-choice{#user-tools-userdel-r-scope} Welche zusätzliche Entfernung fordert ein übliches `userdel -r bob` im Vergleich zu einem einfachen `userdel bob` an?

::option[Jede Datei mit Bobs UID auf jedem eingehängten Dateisystem.]{#user-tools-delete-all-owned explanation="Das Werkzeug findet und löscht nicht grundsätzlich alle Dateien mit dieser UID auf sämtlichen Speichern."}
::option[Jedes entfernte Konto, dessen Benutzername ebenfalls `bob` lautet.]{#user-tools-delete-remote explanation="`userdel` arbeitet mit den betreffenden lokalen Kontodatenbanken und löscht keine unabhängigen Identitäten aus Verzeichnisdiensten."}
::option[Bobs Home-Verzeichnis und lokalen Mail-Spool zusätzlich zu den Kontoeinträgen.]{#user-tools-delete-home-mail .correct explanation="Die rekursive Option zur Kontoentfernung zielt auf das konfigurierte Home-Verzeichnis und den Mail-Spool, jedoch nicht auf jedes Objekt, das Bob andernorts gehören kann."}
:::

Probiere diese praktischen Labs aus, um den Lebenszyklus eines Kontos in einer isolierten Umgebung zu üben:

1. **[Linux-Benutzerkonten mit useradd, usermod und userdel verwalten](https://labex.io/labs/comptia-manage-linux-user-accounts-with-useradd-usermod-and-userdel-590837)** - Übe den vollständigen Lebenszyklus der Benutzerverwaltung, vom Erstellen und Absichern neuer Konten bis zu deren Änderung und Löschung.
2. **[Linux-Gruppen mit groupadd, usermod und groupdel verwalten](https://labex.io/labs/comptia-manage-linux-groups-with-groupadd-usermod-and-groupdel-590836)** - Sammle praktische Erfahrung mit zentralen Befehlszeilenwerkzeugen zur Gruppenverwaltung, einschließlich des Hinzufügens, Änderns und Löschens von Gruppen.
3. **[Benutzerkonten und sudo-Berechtigungen unter Linux konfigurieren](https://labex.io/labs/comptia-configure-user-accounts-and-sudo-privileges-in-linux-590856)** - Lerne grundlegende Techniken zur Verwaltung von Benutzerkonten und sudo-Berechtigungen, um die Sicherheit eines Linux-Systems zu erhöhen.

## Zusammenfassung

Du kannst nun lokale Konten mit ausdrücklich festgelegtem Umfang und anschließender Überprüfung verwalten.

1. Prüfe die Voreinstellungen von `useradd` vor der Kontoerstellung.
2. Fordere Home-Verzeichnis, Shell und Metadateneinstellungen ausdrücklich an.
3. Ändere Passwörter ausschließlich über geschützte Eingabeaufforderungen.
4. Füge ergänzende Gruppen hinzu, ohne die bestehende Liste zu ersetzen.
5. Erfasse Identitätsabhängigkeiten vor einer destruktiven Entfernung.
