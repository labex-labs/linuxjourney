---
lesson_id: "systemd-goals"
course_id: "init"
lang: "de"
order_index: 6
title: "Systemd-Ziele"
description: "Erfahre, wie du systemd-Dienst-Units untersuchst, überschreibst, validierst, startest, aktivierst und Fehler diagnostizierst."
meta_title: "Systemd-Ziele – Init"
meta_description: "Erkunde systemd-Ziele und lerne, Linux-Dienste mit wichtigen systemctl-Befehlen zu verwalten. Diese Anleitung behandelt Grundlagen von Unit-Dateien sowie Starten, Stoppen, Aktivieren und Statusprüfung von Diensten."
meta_keywords: "systemd, systemctl, Linux-Dienste, Unit-Dateien, systemd-Ziele, Dienstverwaltung, systemd-Units, Einsteiger, Tutorial, Anleitung, Linux-Befehle"
---

`systemctl` sendet Anforderungen an einen systemd-Manager. Diese Lektion konzentriert sich auf Systemdienst-Units. Bestätige den genauen Unit-Namen, den Managerbereich, die Abhängigkeiten und die betrieblichen Auswirkungen, bevor du den Zustand änderst.

## Eine Dienst-Unit lesen

Eine minimale beispielhafte Unit kann so aussehen:

```ini
[Unit]
Description=Example worker
Wants=network-online.target
After=network-online.target

[Service]
Type=exec
ExecStart=/usr/local/bin/example-worker
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

- `[Unit]` enthält die Beschreibung und Abhängigkeitsbeziehungen.
- `[Service]` definiert den Prozesslebenszyklus und dienstspezifisches Verhalten.
- `[Install]` teilt Aktivierungsbefehlen mit, welche Aliase oder Abhängigkeitsverknüpfungen sie erstellen sollen; der Abschnitt ist nicht automatisch eine aktive Laufzeitabhängigkeit.

`ExecStart=` wird standardmäßig nicht durch eine Shell geleitet. Shell-Pipelines, Umleitungen, Variablen und Anführungszeichen verhalten sich nicht wie in einer interaktiven Befehlszeile, sofern nicht absichtlich eine ausdrückliche Shell aufgerufen wird.

:::single-choice{#systemd-goals-install-section}
Was ist der Hauptzweck von `[Install]`-Direktiven wie `WantedBy=`?

::option[Sie garantieren, dass der Dienstprozess bereits läuft.]{#systemd-goals-install-running explanation="Die Laufzeitaktivierung erfordert start oder eine andere auslösende Abhängigkeit."}
::option[Sie beschreiben Verknüpfungen oder Beziehungen, die beim Aktivieren der Unit erstellt werden.]{#systemd-goals-enable-links .correct explanation="Installationsmetadaten werden von Aktivierungsoperationen ausgewertet und sind vom aktuellen Prozesszustand getrennt."}
::option[Sie führen jeden Befehl durch die interaktive Shell des Benutzers aus.]{#systemd-goals-install-shell explanation="Die Befehlsauswertung von Units verwendet standardmäßig keine interaktive Shell."}
:::

## Die wirksame Konfiguration untersuchen

Liste geladene Units auf mit:

```bash
$ systemctl list-units --type=service
```

Liste installierte Unit-Dateien und Aktivierungszustände auf mit:

```bash
$ systemctl list-unit-files --type=service
```

Dies sind unterschiedliche Ansichten: Eine Unit-Datei kann aktiviert, aber inaktiv, aktiv, aber deaktiviert, statisch, erzeugt, transient, maskiert oder in einer der Auflistungen nicht vorhanden sein. Untersuche zusammengeführte Anbieter- und Drop-in-Inhalte mit:

```bash
$ systemctl cat UNIT.service
$ systemctl show UNIT.service
```

:::single-choice{#systemd-goals-list-units-versus-files}
Was zeigt `list-unit-files`, das `list-units` nicht in erster Linie zeigt?

::option[Nur die Prozesse mit dem höchsten CPU-Verbrauch.]{#systemd-goals-cpu-processes explanation="Die Rangfolge des Ressourcenverbrauchs von Prozessen gehört nicht zu diesen Unit-Inventarbefehlen."}
::option[Die Aktivierungszustände installierter Unit-Dateien.]{#systemd-goals-unit-file-state .correct explanation="Der Befehl meldet, ob Unit-Dateien aktiviert, deaktiviert, statisch, maskiert oder in verwandten Installationszuständen sind."}
::option[Jede jemals in das Journal geschriebene Zeile.]{#systemd-goals-all-journal explanation="Journalabfragen verwenden `journalctl`."}
:::

## Eine lokale Überschreibung erstellen

Verwende ein Drop-in, statt eine mit einem Paket gelieferte Unit zu bearbeiten:

```bash
$ sudo systemctl edit UNIT.service
```

Nach dem Speichern weist systemctl den Manager bei aktuellen Implementierungen im Rahmen dieses Bearbeitungsablaufs normalerweise an, neu zu laden. Wenn Dateien auf andere Weise geändert werden, führe dagegen Folgendes aus:

```bash
$ sudo systemctl daemon-reload
```

`daemon-reload` liest Unit-Definitionen neu ein und erstellt Abhängigkeiten erneut. Der Befehl lädt weder Anwendungskonfiguration neu noch startet er laufende Dienste neu. Validiere gegebenenfalls Unit-Syntax und Abhängigkeiten mit `systemd-analyze verify` und prüfe danach die wirksame zusammengeführte Unit.

:::single-choice{#systemd-goals-daemon-reload}
Was bewirkt `systemctl daemon-reload`?

::option[Es zwingt jeden Daemon, seine Anwendungskonfiguration neu einzulesen.]{#systemd-goals-reload-all-apps explanation="Das Neuladen einer Anwendung ist dienstspezifisch und von der Managerkonfiguration getrennt."}
::option[Es startet den Kernel mit einer neuen Version neu.]{#systemd-goals-reload-kernel explanation="Die Aktivierung eines Kernels erfordert einen Bootvorgang und kein Neuladen von Unit-Definitionen."}
::option[Es lädt systemd-Unit-Definitionen und Abhängigkeitsinformationen neu.]{#systemd-goals-reload-manager .correct explanation="Es aktualisiert die Konfigurationssicht des Managers, ohne zwangsläufig Dienste neu zu starten."}
:::

## Laufzeitzustand von Diensten

Nachdem du die Dienstkonfiguration validiert und einen Wiederherstellungszugang bewahrt hast:

```bash
$ sudo systemctl start peanut.service
$ sudo systemctl stop peanut.service
$ sudo systemctl restart peanut.service
$ sudo systemctl reload peanut.service
```

`reload` ist nur erfolgreich, wenn die Unit eine Neuladeaktion definiert oder unterstützt. `restart` unterbricht den Prozess und kann den Dienst möglicherweise nicht wiederherstellen. Halte für Fernzugriff, Netzwerk, Speicher oder Authentifizierung einen separaten Konsolenzugang bereit und prüfe die Konfiguration, bevor du handelst.

Prüfe Zustand und Protokolle mit:

```bash
$ systemctl status peanut.service
$ systemctl is-active peanut.service
$ journalctl -u peanut.service -b
```

„Active“ ist ein Managerzustand und kein Beweis dafür, dass jeder Anwendungsendpunkt fehlerfrei ist.

:::single-choice{#systemd-goals-start-peanut}
Welcher Befehl startet `peanut.service` jetzt, ohne für sich allein die künftige Aktivierung zu ändern?

::option[`sudo systemctl enable peanut.service`]{#systemd-goals-enable-only explanation="Enable ändert Aktivierungsverknüpfungen, startet den Dienst jedoch nur in Verbindung mit `--now`."}
::option[`sudo systemctl start peanut.service`]{#systemd-goals-start-command .correct explanation="Start fordert die aktuelle Laufzeitaktivierung an und ist von der dauerhaften Aktivierung getrennt."}
::option[`sudo systemctl daemon-reload peanut.service`]{#systemd-goals-daemon-reload-unit explanation="Daemon-reload akzeptiert keinen Operanden zur Unit-Aktivierung und startet diesen Dienst nicht."}
:::

## Aktivieren, Deaktivieren und Maskieren

Verwalte Verknüpfungen für künftige Abhängigkeiten mit:

```bash
$ sudo systemctl enable peanut.service
$ sudo systemctl disable peanut.service
```

Enable startet die Unit nur, wenn `--now` hinzugefügt wird. Disable stoppt eine laufende Unit nur, wenn `--now` hinzugefügt wird. Einer statischen Unit können Installationsmetadaten fehlen, obwohl sie weiterhin als Abhängigkeit einer anderen Unit aktiviert werden kann.

Beim Maskieren wird die Unit mit `/dev/null` verknüpft. Dadurch wird die gewöhnliche Aktivierung einschließlich der Aktivierung als Abhängigkeit blockiert, bis die Maskierung aufgehoben wird. Dies ist stärker als Deaktivieren und kann abhängige Units beeinträchtigen; prüfe vor der Verwendung die umgekehrten Abhängigkeiten.

:::single-choice{#systemd-goals-disable-runtime}
Was geschieht mit einem bereits laufenden Dienst nach `systemctl disable UNIT` ohne `--now`?

::option[Er wird sofort mit `SIGKILL` beendet.]{#systemd-goals-disable-kills explanation="Disable allein fordert keinen aktuellen Stopp an."}
::option[Seine ausführbare Datei wird aus dem Dateisystem gelöscht.]{#systemd-goals-disable-deletes explanation="Aktivierungsoperationen verwalten Verknüpfungen und keine Programmdateien aus Paketen."}
::option[Er läuft normalerweise weiter, während Verknüpfungen für künftige Aktivierungen entfernt werden.]{#systemd-goals-disable-keeps-running .correct explanation="Laufzeitzustand und Installationszustand sind getrennte Dimensionen."}
:::

## Das Ergebnis des Dienstes überprüfen

Prüfe nach einer Änderung den Prozesszustand, aktuelle Protokolle, lauschende Endpunkte, abhängige Units, den Zustand der Anwendung und – falls sich die Bootaktivierung geändert hat – das Verhalten nach einem kontrollierten Neustart. Verwende je nach Bedarf `systemctl is-failed`, `systemctl list-dependencies` und anwendungseigene Prüfungen.

## Zusammenfassung

Du kannst einen systemd-Dienst nun verwalten, ohne Konfiguration, Laufzeit und Aktivierung miteinander zu verwechseln.

1. Lies `[Unit]`, `[Service]` und `[Install]` entsprechend ihren unterschiedlichen Aufgaben.
2. Vergleiche den Zustand geladener Units mit dem Zustand installierter Unit-Dateien.
3. Verwende Drop-ins und lade den Manager nach externen Dateiänderungen neu.
4. Starte, stoppe, lade neu oder starte erst nach Prüfung der Auswirkungen neu.
5. Behandle Aktivieren, Deaktivieren und Maskieren als getrennte Steuerungen der Dauerhaftigkeit.
