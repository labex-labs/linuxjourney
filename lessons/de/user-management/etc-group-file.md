---
lesson_id: "etc-group-file"
course_id: "user-management"
lang: "de"
order_index: 5
title: "/etc/group"
description: "Erfahre, wie lokale Gruppeneinträge Namen GIDs zuordnen und ergänzende Mitglieder auflisten."
meta_title: "/etc/group – Benutzerverwaltung"
meta_description: "Erkunde die Datei /etc/group unter Linux, um die Gruppenverwaltung zu verstehen. Erfahre, wie du Gruppendaten mit cat /etc/group anzeigst und die Struktur mit GID und Benutzerlisten interpretierst. Dieser Leitfaden behandelt die Grundlagen der Linux-Datei etc group."
meta_keywords: "/etc/group, /etc/group Linux, Datei /etc/group unter Linux, cat /etc/group, etc group Linux, Gruppenverwaltung, GID, Linux-Berechtigungen, Linux-Gruppen"
---

`/etc/group` speichert lokale Gruppeneinträge. Die Datei ordnet Gruppennamen numerischen GIDs zu und listet ausdrückliche Mitglieder auf. Dadurch unterstützt sie eine Zugriffskontrolle, die sich mehrere Konten teilen.

## Lokale und aufgelöste Gruppen

Die Datei ist nur eine mögliche Gruppenquelle. NSS kann Gruppen aus lokalen Dateien, Verzeichnisdiensten oder anderen konfigurierten Datenbanken auflösen. Zeige die lokalen Einträge an mit:

```bash
$ cat /etc/group
```

Frage die aufgelöste Gruppendatenbank mit `getent` ab:

```bash
$ getent group
$ getent group developers
```

Gruppenlisten können interne Konto- und Rollennamen offenlegen. Prüfe die Ausgabe daher, bevor du sie teilst.

:::single-choice{#group-query-resolved-database} Welcher Befehl fragt die durch NSS aufgelöste Gruppendatenbank ab?

::option[`getent group`]{#group-getent-all .correct explanation="`getent` fragt die konfigurierten NSS-Quellen nach Gruppeneinträgen ab."}
::option[`cat /etc/group`]{#group-cat-local explanation="Dies liest nur die lokale Gruppendatei und kann Gruppen aus anderen Quellen auslassen."}
::option[`groups /etc/group`]{#group-groups-file explanation="`groups` erwartet Benutzernamen und gibt Mitgliedschaften aus; es behandelt den Pfad der lokalen Datenbank nicht als NSS-Abfrage."}
:::

## Die vier Felder lesen

Ein lokaler Eintrag besitzt vier durch Doppelpunkte getrennte Felder:

```text
developers:x:1500:alice,bob
```

1. **Gruppenname**: `developers`.
2. **Passwortfeld**: Gewöhnlich `x`, `*` oder ein anderer Platzhalter; geschützte Gruppenpasswortdaten können in `/etc/gshadow` gespeichert werden.
3. **GID**: Die numerische Gruppenidentität, hier `1500`.
4. **Mitgliederliste**: Durch Kommas getrennte ausdrückliche Mitgliedsnamen, hier `alice` und `bob`.

Gruppenpasswörter sind eine Altlast, die in einigen Konfigurationen von Werkzeugen wie `newgrp` verwendet wird. Sie sind nicht der übliche Mechanismus, um sudo-Autorisierungen zu gewähren, und sollten nicht durch manuelle Änderungen an Feldern eingeführt werden.

:::single-choice{#group-gid-field} Welches Feld enthält in `developers:x:1500:alice,bob` die GID?

::option[Das zweite Feld, `x`]{#group-second-password explanation="Feld 2 ist der Platzhalter für das Gruppenpasswort und nicht die numerische Identität."}
::option[Das vierte Feld, `alice,bob`]{#group-fourth-members explanation="Feld 4 listet ausdrückliche Mitgliedsnamen auf und nicht die GID."}
::option[Das dritte Feld, `1500`]{#group-third-gid .correct explanation="Das dritte durch Doppelpunkte getrennte Feld ist die numerische Gruppen-ID."}
:::

:::single-choice{#group-explicit-member-field} Wie werden ausdrückliche Mitgliedsnamen in einem lokalen Gruppeneintrag dargestellt?

::option[Als durch Kommas getrennte Liste in Feld 4.]{#group-members-field-four .correct explanation="Das letzte Feld enthält ausdrückliche ergänzende Mitgliedsnamen, die durch Kommas getrennt sind."}
::option[Als durch Leerzeichen getrennte Liste in Feld 2.]{#group-members-field-two explanation="Feld 2 ist für passwortbezogene Daten oder einen Platzhalter vorgesehen und nicht für die Mitgliederliste."}
::option[Als numerische UIDs, die in den Gruppennamen eingebettet sind.]{#group-members-in-name explanation="Gruppenname und Mitgliedsnamen sind getrennte Felder; gewöhnliche Mitgliedseinträge sind Anmeldenamen und keine eingebetteten UID-Ziffern."}
:::

## Primäre Gruppenmitgliedschaften berücksichtigen

Die Mitgliederliste in `/etc/group` wiederholt gewöhnlich keine Benutzer, deren passwd-Eintrag diese GID als primäre Gruppe nennt. Ein Benutzer kann der Gruppe daher auch dann angehören, wenn sein Name in Feld 4 fehlt.

Wenn beispielsweise Alices passwd-Eintrag die primäre GID 1500 besitzt, gehört sie zu `developers`, selbst wenn der lokale Gruppeneintrag mit einem leeren Mitgliederfeld endet:

```text
developers:x:1500:
```

Deshalb ergibt die alleinige Auswertung von Feld 4 eine unvollständige Ansicht der Mitgliedschaften.

:::single-choice{#group-primary-membership-visibility} Alices passwd-Eintrag verwendet die GID 1500 als primäre GID, aber ihr Name fehlt in Feld 4 der Gruppe 1500. Ist sie Mitglied dieser Gruppe?

::option[Nein, jede Mitgliedschaft muss in Feld 4 von `/etc/group` stehen.]{#group-field-four-only explanation="Dies ignoriert die Mitgliedschaft über die primäre GID und würde zu wenige Gruppenmitglieder zählen."}
::option[Ja, die primäre Mitgliedschaft stammt aus dem GID-Feld des passwd-Eintrags.]{#group-primary-from-passwd .correct explanation="Die ausdrückliche Liste der Gruppendatei dient hauptsächlich ergänzenden Mitgliedschaften; die primäre Mitgliedschaft wird beim Konto erfasst."}
::option[Nur wenn das Gruppenpasswortfeld ihren Benutzernamen enthält.]{#group-password-member explanation="Das Passwortfeld hat nichts mit der Festlegung einer primären Mitgliedschaft zu tun."}
:::

## Die Gruppen eines Benutzers prüfen

Verwende `id USER` oder `groups USER` für eine aufgelöste Kontoansicht:

```bash
$ id alice
$ groups alice
```

Für den aktuellen Prozess gibt ein einfaches `id` die Gruppen aus, die tatsächlich in seinen Zugangsdaten vorhanden sind. Eine neu konfigurierte ergänzende Mitgliedschaft erscheint gewöhnlich nicht in einer bereits laufenden Anmeldesitzung. Starte eine neue authentifizierte Sitzung oder verwende gegebenenfalls einen bewusst konfigurierten Mechanismus wie `newgrp`.

:::single-choice{#group-current-process-credentials} Welcher Befehl gibt die UID, die primäre GID und die ergänzenden Gruppen des aktuellen Prozesses aus?

::option[`id`]{#group-current-id .correct explanation="Ohne Benutzeroperand gibt `id` die Identitätszugangsdaten des aktuellen Prozesses aus."}
::option[`cat /etc/group`]{#group-current-cat explanation="Die lokale Datei listet Einträge auf, zeigt aber nicht, welche aufgelösten Gruppen im aktuellen Prozess aktiv sind."}
::option[`getent passwd`]{#group-current-passwd explanation="Dies fragt Kontoeinträge ab und gibt nicht gezielt die ergänzende Gruppenliste des aktuellen Prozesses aus."}
:::

## Lokale Gruppen sicher ändern

Verwende Werkzeuge wie `groupadd`, `groupmod`, `groupdel`, `gpasswd` und `usermod`, statt Einträge mit einem allgemeinen Editor zu bearbeiten. Sei besonders vorsichtig mit:

- `usermod -aG GROUP USER`, das eine ergänzende Mitgliedschaft hinzufügt.
- `usermod -G ...`, das ohne `-a` die Liste der ergänzenden Gruppen ersetzt.

Wenn eine manuelle Reparatur der lokalen Datenbank unvermeidbar ist, verwende `vigr` zur Sperrung und `grpck` zur Validierung. Halte einen Wiederherstellungsweg bereit, bevor du entfernte Identitätsänderungen vornimmst.

Probiere diese praktischen Labs aus, um die lokale Gruppenverwaltung in einer kontrollierten Umgebung zu üben:

1. **[Linux-Benutzerkonten mit useradd, usermod und userdel verwalten](https://labex.io/labs/comptia-manage-linux-user-accounts-with-useradd-usermod-and-userdel-590837)** - Übe den vollständigen Lebenszyklus der Benutzerverwaltung, vom Erstellen und Absichern neuer Konten bis zu deren Änderung und Löschung.
2. **[Linux-Gruppen mit groupadd, usermod und groupdel verwalten](https://labex.io/labs/comptia-manage-linux-groups-with-groupadd-usermod-and-groupdel-590836)** - Sammle praktische Erfahrung mit zentralen Befehlszeilenwerkzeugen zur Gruppenverwaltung, darunter `groupadd`, `usermod` und `groupdel`.
3. **[Neuen Benutzer und neue Gruppe hinzufügen](https://labex.io/labs/linux-add-new-user-and-group-17987)** - Simuliere das Hinzufügen neuer Teammitglieder zu einer Serverumgebung, indem du neue Benutzerkonten erstellst, eigene Gruppen einrichtest und Gruppenmitgliedschaften verwaltest.

## Zusammenfassung

Du kannst nun lokale Gruppeneinträge interpretieren und vollständige Mitgliedschaften genauer auflösen.

1. Frage konfigurierte Gruppenquellen mit `getent group` ab.
2. Lies die vier durch Doppelpunkte getrennten Gruppenfelder.
3. Bestimme die numerische GID und die ausdrückliche Mitgliederliste.
4. Beziehe primäre Mitgliedschaften aus passwd-Einträgen ein.
5. Prüfe aktive Zugangsdaten, bevor du dich auf eine geänderte Mitgliedschaft verlässt.
