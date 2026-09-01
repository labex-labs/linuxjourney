---
lesson_id: "tracking-processes-lsof-fuser"
course_id: "process-utilization"
lang: "de"
order_index: 2
title: "lsof und fuser"
description: "Lerne, Prozesse zu ermitteln, die Dateien, Verzeichnisse, Einhängepunkte und Netzwerk-Sockets verwenden."
meta_title: "lsof und fuser – Prozessauslastung"
meta_description: "Erkunde die Linux-Befehle lsof und fuser, um Prozesse zu ermitteln, die bestimmte Dateien verwenden. Behebe Fehler wie „Gerät oder Ressource belegt“, vergleiche fuser mit lsof und verwalte offene Dateien umsichtig."
meta_keywords: "lsof, fuser, fuser-Befehl, Linux fuser, fuser versus lsof, lsof versus fuser, fuser -k Linux, offene Dateien, Prozessverwaltung, Gerät belegt, Linux-Befehle"
---

Ein Dateisystem kann belegt bleiben, weil ein Prozess eine Datei geöffnet hat, eine Datei in den Speicher abbildet oder ein Verzeichnis als aktuelles Arbeitsverzeichnis verwendet. `lsof` und `fuser` helfen, diese Beziehungen zu ermitteln. Untersuche sie zuerst; Prozesse zu stoppen ist eine getrennte Entscheidung mit betrieblichen Folgen.

## Offene Dateien mit lsof auflisten

`lsof` bedeutet „list open files“. Frage einen Pfad ab, um passende Datensätze offener Dateien zu sehen:

```bash
$ sudo lsof -- /mnt/usb
```

Für einen vollständigen Verzeichnisbaum auf demselben Dateisystem unterstützen Implementierungen üblicherweise `+D`; rekursive Scans können jedoch aufwendig sein:

```bash
$ sudo lsof +D /mnt/usb
```

Nützliche Spalten sind `COMMAND`, `PID`, `USER`, der Dateideskriptor (`FD`), Typ, Gerät und `NAME`. Ein Datensatz mit `cwd` im Feld `FD` zeigt an, dass der Prozess das Verzeichnis als sein aktuelles Arbeitsverzeichnis verwendet. Die Ausgabe ohne erhöhte Rechte kann für Prozesse anderer Benutzer unvollständig sein.

:::single-choice{#lsof-cwd-record} Was zeigt `cwd` in der Spalte `FD` an?

::option[Der Prozess verwendet dieses Verzeichnis als aktuelles Arbeitsverzeichnis.]{#lsof-current-directory .correct explanation="Das aktuelle Verzeichnis eines Prozesses kann ein eingehängtes Dateisystem belegt halten."}
::option[Die Datei wurde geschlossen, während in sie geschrieben wurde.]{#lsof-closed-write explanation="Die Kennzeichnung beschreibt eine Verzeichnisbeziehung und kein Schließereignis."}
::option[Der Prozess ist Eigentümer des Dateisystemgeräts.]{#lsof-device-owner explanation="Dateisystemeigentum wird nicht durch die Deskriptorkennzeichnung `cwd` dargestellt."}
:::

## Benutzer mit fuser ermitteln

`fuser` meldet Prozess-IDs, die eine angegebene Datei oder ein Dateisystem verwenden. Die ausführliche Ausgabe ergänzt Benutzer, Zugriffsarten und Befehlsnamen:

```bash
$ sudo fuser -v /mnt/usb
```

Verwende die von `fuser` aus procps unterstützte Mount-Option, um das Argument als eingehängtes Dateisystem zu behandeln und Prozesse zu finden, die darin enthaltene Dateien verwenden:

```bash
$ sudo fuser -vm /mnt/usb
```

Überprüfe mit Werkzeugen wie `findmnt --target /mnt/usb`, dass der Pfad der beabsichtigte Einhängepunkt ist. Bind-Mounts, Namensräume, Berechtigungen und Wettlaufsituationen können beeinflussen, was eine einzelne Abfrage zeigt.

:::single-choice{#fuser-verbose-purpose} Warum solltest du während der Untersuchung `fuser -v` statt einfachem `fuser` verwenden?

::option[Der Befehl hängt das ausgewählte Dateisystem automatisch aus.]{#fuser-verbose-unmount explanation="Der ausführliche Modus meldet Details und fordert kein Aushängen an."}
::option[Er ergänzt Kontext wie Benutzer, Zugriffsart und Befehl.]{#fuser-verbose-details .correct explanation="Die zusätzlichen Spalten helfen zu beurteilen, welche Prozesse sicher koordiniert oder gestoppt werden können."}
::option[Er verhindert dauerhaft, dass die Prozesse Dateien erneut öffnen.]{#fuser-verbose-prevent explanation="Eine Ausgabe erzeugt keine Zugriffskontrollregel."}
:::

## Mit einem belegten Dateisystem umgehen

Arbeite in einer überlegten Reihenfolge, statt sofort jede passende PID zu beenden:

1. Bestätige Host, Pfad, Mount-Quelle und beabsichtigte Wartung.
2. Ermittle Prozesse, wenn möglich, mit beiden Werkzeugen.
3. Stelle fest, ob jeder Prozess gestoppt, aus dem Verzeichnis verschoben oder bis zum Abschluss weiterlaufen kann.
4. Stoppe ihn nach Möglichkeit über seinen Dienstmanager oder seine Anwendungsschnittstelle.
5. Frage erneut ab, hänge dann aus und überprüfe das Ergebnis.

`fuser -k` sendet ein Signal an passende Prozesse. Bei üblichen procps-Implementierungen ist das Standardsignal `SIGKILL`, sodass kein geordnetes Herunterfahren stattfindet. Falls eine ausdrücklich genehmigte Beendigung nötig ist, wähle ein geeignetes Signal, überprüfe PID und Eigentümer und berücksichtige, dass sich die Prozessmenge zwischen Untersuchung und Eingriff ändern kann.

:::single-choice{#fuser-k-risk} Warum ist `fuser -k /mnt/usb` ein schlechter erster Schritt bei der Fehlersuche?

::option[Der Befehl gibt nur den freien Speicherplatz des Dateisystems aus.]{#fuser-k-space explanation="Die Option zielt auf Prozesse, statt Kapazität zu melden."}
::option[Er kann mehrere passende Prozesse ohne geordnetes Aufräumen beenden.]{#fuser-k-kills .correct explanation="Die weitreichende Signalaktion kann Schreibvorgänge oder Dienste unterbrechen; Untersuchung und Koordination sollten daher zuerst erfolgen."}
::option[Er ändert das Arbeitsverzeichnis jedes passenden Prozesses.]{#fuser-k-chdir explanation="Der Befehl sendet ein Signal und verschiebt keine Prozessverzeichnisse."}
:::

## Das Werkzeug auswählen

Verwende `lsof`, wenn du detaillierte Datensätze offener Dateien, Deskriptoren oder Socketinformationen benötigst. Verwende `fuser` für eine pfadorientierte Ansicht passender PIDs und Zugriffsarten. Keines der Ergebnisse sagt für sich allein, ob ein Prozess sicher beendet werden kann.

Verwende für Netzwerk-Sockets mit `fuser` einen ausdrücklichen Protokollnamensraum oder ein auf Sockets spezialisiertes Werkzeug wie `ss`:

```bash
$ sudo fuser -v 22/tcp
$ sudo ss -lntp
```

:::single-choice{#lsof-fuser-tool-choice} Welches Werkzeug eignet sich für eine detaillierte Liste offener Dateideskriptoren und der zugehörigen Prozesse?

::option[`lsof`]{#lsof-detailed-records .correct explanation="Seine Ausgabe ist nach Datensätzen offener Dateien und deren Prozessmetadaten organisiert."}
::option[`uptime`]{#lsof-uptime explanation="Uptime meldet Betriebsdauer und Lastmittelwerte, keine offenen Deskriptoren."}
::option[`free`]{#lsof-free explanation="Free fasst den Speicher zusammen und nicht die Dateinutzung."}
:::

## Zusammenfassung

Du kannst Datei- und Dateisystemnutzung nun untersuchen, ohne das Beenden als Standardreaktion zu behandeln.

1. Verwende `lsof` für detaillierte Datensätze offener Dateien.
2. Verwende `fuser` für pfadorientierte PID- und Zugriffsinformationen.
3. Bestätige den Einhängepunkt und berücksichtige Berechtigungen sowie Wettlaufsituationen.
4. Koordiniere ein geordnetes Stoppen, bevor du ein Signal erwägst.
5. Frage erneut ab und überprüfe das Aushängen oder das Ergebnis des Dienstes.
