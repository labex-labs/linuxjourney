---
lesson_id: "etc-passwd-file"
course_id: "user-management"
lang: "de"
order_index: 3
title: "/etc/passwd"
description: "Erfahre, wie du lokale passwd-Einträge liest und sie von der vollständigen NSS-Kontoansicht unterscheidest."
meta_title: "/etc/passwd – Benutzerverwaltung"
meta_description: "Ein umfassender Leitfaden zur Datei /etc/passwd unter Linux. Lerne, Benutzer-Datenfelder zu interpretieren und UIDs zu verstehen, und sieh dir Beispiele wie root:x:0:0:root:/root:/bin/bash an."
meta_keywords: "/etc/passwd, /etc/passwd unter Linux, root:x:0:0:root:/root:/bin/bash, Benutzer-ID, UID, Benutzerverwaltung, Linux-Tutorial"
---

`/etc/passwd` speichert lokale Kontoeinträge in einem durch Doppelpunkte getrennten Textformat. Die Datei ordnet Anmeldenamen numerischen UIDs zu und erfasst eine primäre GID, ein Beschreibungsfeld, den Home-Pfad und das Anmeldeprogramm.

## Lokale Einträge und aufgelöste Konten

Zeige die lokale Datei mit einem schreibgeschützten Befehl an:

```bash
$ cat /etc/passwd
```

Dies sind nicht unbedingt alle dem System bekannten Konten. Der Name Service Switch (NSS) kann Konten aus Dateien, Verzeichnisdiensten, Systemdatenbanken oder anderen konfigurierten Quellen auflösen. Verwende `getent`, um die aufgelöste passwd-Datenbank abzufragen:

```bash
$ getent passwd
$ getent passwd root
```

Der erste Befehl kann Kontonamen und Metadaten offenlegen. Prüfe die Ausgabe daher, bevor du sie öffentlich teilst.

:::single-choice{#passwd-query-resolved-database}
Welcher Befehl fragt die durch NSS aufgelöste passwd-Datenbank ab, statt nur die lokale Datei zu lesen?

::option[`cat /etc/passwd`]{#passwd-cat-local explanation="Dies zeigt nur die lokale Datei an und enthält keine Konten, die ausschließlich von anderen NSS-Quellen bereitgestellt werden."}
::option[`cat /etc/shadow`]{#passwd-cat-shadow explanation="Die shadow-Datei enthält geschützte lokale Daten zur Passwortalterung und sollte zu diesem Zweck nicht angezeigt werden."}
::option[`getent passwd`]{#passwd-getent-all .correct explanation="`getent` fragt die konfigurierten Quellen der passwd-Datenbank über NSS ab."}
:::

## Die sieben Felder lesen

Ein lokaler Eintrag sieht häufig so aus:

```text
root:x:0:0:root:/root:/bin/bash
```

Die sieben durch Doppelpunkte getrennten Felder sind:

1. **Anmeldename**: Der menschenlesbare Kontoname, beispielsweise `root`.
2. **Passwortfeld**: Auf einem System mit Shadow-Passwörtern gewöhnlich `x`; dies weist darauf hin, dass geschützte Passwortdaten getrennt gespeichert sind.
3. **UID**: Die numerische Benutzeridentität. Die UID 0 wird traditionell als Superuser behandelt.
4. **Primäre GID**: Die numerische Kennung der primären Gruppe des Kontos.
5. **GECOS/Kommentar**: Beschreibende Kontoinformationen, die intern häufig durch Kommas getrennt sind.
6. **Home-Verzeichnis**: Der als Home-Einstellung des Kontos verwendete Pfad; er muss auf dem Datenträger nicht vorhanden sein.
7. **Anmelde-Shell/-Programm**: Das für geeignete Anmeldesitzungen angeforderte Programm, beispielsweise `/bin/bash` oder ein Programm, das Anmeldungen verhindert.

Der Kernel verlangt bei fehlerhaften oder absichtlich doppelten Einträgen keine eindeutigen UID-Werte. Konten mit derselben UID sind jedoch bei vielen Eigentums- und Berechtigungsentscheidungen nicht voneinander zu unterscheiden. Administratoren sollten Konto-UIDs gewöhnlich eindeutig halten.

:::single-choice{#passwd-uid-field}
Welches Feld enthält in `root:x:0:0:root:/root:/bin/bash` die UID?

::option[Das zweite Feld, `x`]{#passwd-second-password explanation="Das zweite Feld ist der Passwortplatzhalter und nicht die numerische Benutzeridentität."}
::option[Das vierte Feld, die zweite `0`]{#passwd-fourth-gid explanation="Feld 4 ist die primäre GID und nicht die UID."}
::option[Das dritte Feld, die erste `0`]{#passwd-third-uid .correct explanation="Feld 3 ist die UID, daher kennzeichnet die erste Null diesen Eintrag als UID 0."}
:::

:::single-choice{#passwd-primary-gid-field}
Welches Feld eines passwd-Eintrags speichert die primäre GID des Kontos?

::option[Feld 5]{#passwd-gecos-five explanation="Das fünfte Feld ist das GECOS- oder Kommentarfeld."}
::option[Feld 4]{#passwd-gid-four .correct explanation="Das vierte durch Doppelpunkte getrennte Feld identifiziert die primäre Gruppe numerisch."}
::option[Feld 7]{#passwd-shell-seven explanation="Das siebte Feld legt die Anmelde-Shell oder das Anmeldeprogramm fest."}
:::

## Den Passwortplatzhalter interpretieren

Auf typischen Systemen mit Shadow-Passwörtern verweist `x` in Feld 2 passwortbewusste Werkzeuge auf geschützte Daten in `/etc/shadow`. Werte wie `*` oder `!` sind keine gültigen Passwort-Hashes und verhindern im Allgemeinen die Authentifizierung mit einem Unix-Passwort über diesen Eintrag.

Das beweist nicht, dass sich das Konto mit überhaupt keiner Methode authentifizieren kann. SSH-Schlüssel, Zertifikate, Token oder dienstspezifische Mechanismen können davon unabhängig sein. Ebenso besitzt ein leeres Passwortfeld sicherheitsrelevantes Verhalten, das vom Authentifizierungsstapel abhängt. Erstelle oder „repariere“ es nicht manuell.

:::single-choice{#passwd-x-placeholder}
Was bedeutet `x` gewöhnlich in Feld 2 eines lokalen `/etc/passwd`-Eintrags?

::option[Das Konto hat garantiert keine Authentifizierungsmethode.]{#passwd-no-auth-guarantee explanation="Der Platzhalter beschreibt nicht jede mögliche Authentifizierungsmethode und bedeutet für sich genommen nicht, dass das Konto unbrauchbar ist."}
::option[Das Home-Verzeichnis des Kontos wurde gelöscht.]{#passwd-home-deleted explanation="Informationen zum Home-Verzeichnis stehen in Feld 6 und haben nichts mit dem Platzhalter `x` zu tun."}
::option[Geschützte Passwortdaten werden in der shadow-Datenbank gespeichert.]{#passwd-shadow-placeholder .correct explanation="Der öffentliche passwd-Eintrag enthält einen Platzhalter, während Passwort-Hash und Alterungsfelder in geschützten shadow-Daten liegen."}
:::

## Dienstkonten erkennen

Viele Einträge repräsentieren Dienste und keine Menschen. Getrennte Dienstidentitäten helfen dabei, Dateien und Prozesse auf die für einen bestimmten Daemon erforderlichen Befugnisse zu beschränken. Ihre Home-Pfade können ungewöhnlich oder nicht vorhanden sein, und ihr Anmeldeprogramm kann `/usr/sbin/nologin`, `/bin/false` oder ein anderes einschränkendes Programm sein.

Leite den Zweck eines Kontos nicht allein aus seinem UID-Bereich ab, ohne die Richtlinien der Distribution zu prüfen. Die Zuweisungsbereiche unterscheiden sich, und zentral verwaltete Konten können anderen Konventionen folgen.

:::single-choice{#passwd-nologin-shell}
Was ist ein häufiger Zweck eines Anmeldeprogramms wie `/usr/sbin/nologin` in Feld 7?

::option[Die Dateien des Kontos bei jedem Beenden eines Dienstes zu löschen.]{#passwd-nologin-delete explanation="Das Anmeldeprogramm entfernt nicht automatisch Dateien im Besitz des Kontos und verwaltet keine Dateien beim Herunterfahren von Diensten."}
::option[Eine gewöhnliche interaktive Shell über Anmeldewege zu verhindern, die dieses Feld berücksichtigen.]{#passwd-nologin-purpose .correct explanation="Ein Programm zur Verhinderung von Anmeldungen wird häufig für Dienstkonten verwendet, die über die normale Anmeldung keine interaktive Shell erhalten sollen."}
::option[Dem Konto dieselben Rechte wie der UID 0 zu gewähren.]{#passwd-nologin-root explanation="Die Einschränkung einer interaktiven Anmeldung erhöht weder die Rechte des Kontos noch ändert sie seine numerische UID."}
:::

## Kontoeinträge sicher ändern

Bevorzuge Werkzeuge zur Kontoverwaltung wie `useradd`, `usermod` und `userdel`, da sie zusammengehörige Einträge koordinieren und Systemvoreinstellungen anwenden. Ihr genaues Verhalten kann von der Distribution konfiguriert werden. Prüfe daher die Optionen, bevor du ein Konto änderst.

Wenn eine lokale passwd-Datenbank tatsächlich manuell repariert werden muss, verwende `vipw` statt eines gewöhnlichen Editors. Es sperrt die Datei, um gleichzeitige Bearbeitungen zu vermeiden. Validiere Datenbanken mit Werkzeugen wie `pwck` und halte eine Wiederherstellungssitzung aufrecht, bevor du Authentifizierungsdateien aus der Ferne änderst.

Probiere diese praktischen Labs aus, um Benutzer- und Gruppeneinträge in einer kontrollierten Umgebung zu üben:

1. **[Linux-Benutzerkonten mit useradd, usermod und userdel verwalten](https://labex.io/labs/comptia-manage-linux-user-accounts-with-useradd-usermod-and-userdel-590837)** - Übe den vollständigen Lebenszyklus der Benutzerverwaltung, vom Erstellen und Absichern neuer Konten bis zu deren Änderung und Löschung.
2. **[Linux-Gruppen mit groupadd, usermod und groupdel verwalten](https://labex.io/labs/comptia-manage-linux-groups-with-groupadd-usermod-and-groupdel-590836)** - Sammle praktische Erfahrung mit den zentralen Befehlszeilenwerkzeugen zur Gruppenverwaltung, darunter das Erstellen neuer Gruppen und das Ändern von Benutzermitgliedschaften.
## Zusammenfassung

Du kannst nun lokale passwd-Einträge interpretieren, ohne sie mit der vollständigen Identitätsdatenbank zu verwechseln.

1. Frage durch NSS aufgelöste Konten mit `getent passwd` ab.
2. Lies die sieben durch Doppelpunkte getrennten passwd-Felder.
3. Bestimme die Felder für UID und primäre GID.
4. Interpretiere Passwortplatzhalter, ohne zu weitreichende Aussagen über den Anmeldestatus zu treffen.
5. Verwende Kontowerkzeuge oder `vipw` statt eines gewöhnlichen Editors.
