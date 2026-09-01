---
lesson_id: "sysv-services"
course_id: "init"
lang: "de"
order_index: 2
title: "System-V-Dienst"
description: "Erfahre, wie du ältere SysV-Dienstskripte über den unterstützten Wrapper des aktiven Systems prüfst und bedienst."
meta_title: "System-V-Dienst – Init"
meta_description: "Lerne, traditionelle System-V-Dienste (SysV) unter Linux zu verwalten. Dieser Leitfaden behandelt die Verwendung des Befehls `service`, um Dienste auf einem System-V-init-System aufzulisten, zu starten, zu stoppen und neu zu starten."
meta_keywords: "System V, SysV init, Linux-Dienste, service-Befehl, Linux-Dienste verwalten, Dienst starten, Dienst stoppen, Dienst neu starten, Linux System V"
---

SysV-Dienste werden gewöhnlich durch ausführbare Skripte unter `/etc/init.d/` dargestellt. Ein Skript akzeptiert gemäß seiner Implementierung und den Distributionskonventionen Aktionen wie `start`, `stop`, `restart` oder `status`. Der Befehl `service` stellt einen Wrapper bereit, der ein benanntes Skript in einer stärker kontrollierten Umgebung ausführt.

## Dienste und Aktionen ermitteln

Liste zuerst die Skriptnamen auf:

```bash
$ ls -1 /etc/init.d/
```

Einige Implementierungen stellen Folgendes bereit:

```bash
$ service --status-all
```

Seine Klammermarkierungen und Beendigungsstatus sind Wrapper-spezifisch, und ein Skript kann einen unbekannten Status melden. Prüfe für einen einzelnen Dienst die Nutzungsausgabe oder Dokumentation des Skripts, statt anzunehmen, dass jede Aktion vorhanden ist.

:::single-choice{#sysv-services-wrapper-purpose} Was kapselt der Befehl `service` gewöhnlich?

::option[Einen Partitionseditor, der auf jeder Dienstdatei läuft.]{#sysv-services-partition-editor explanation="Die Dienststeuerung hat nichts mit der Speicherpartitionierung zu tun."}
::option[Einen Kernel-Systemaufruf, der vom Skript dynamisch hinzugefügt wird.]{#sysv-services-new-syscall explanation="Init-Skripte sind Programme zur Prozesssteuerung im User-Space."}
::option[Ein benanntes init-Skript und eine seiner unterstützten Aktionen.]{#sysv-services-script-action .correct explanation="Der Wrapper findet ein älteres Dienstskript und ruft es mit einer normalisierten Umgebung auf."}
:::

## Starten und stoppen

Auf einem tatsächlich durch SysV verwalteten Host sind diese Formen üblich:

```bash
$ sudo service SERVICE_NAME start
$ sudo service SERVICE_NAME stop
```

Ersetze den Platzhalter erst, nachdem du den Dienst, seine Abhängigen, seinen aktuellen Zustand und die betrieblichen Auswirkungen bestimmt hast. Das Stoppen von Netzwerk, Fernzugriff, Speicher oder Authentifizierung aus einer entfernten Sitzung kann dich aussperren oder aktive Arbeit beschädigen.

Die direkte Form `/etc/init.d/SERVICE_NAME ACTION` kann vorhanden sein. Verwende auf einem Host, dessen aktiver Manager Kompatibilität bereitstellt, jedoch den an den Manager gerichteten Befehl, damit dieser Zustand und Abhängigkeiten verfolgen kann.

:::single-choice{#sysv-services-stop-peanut} Welcher Befehl fordert an, den SysV-Dienst `peanut` zu stoppen?

::option[`sudo service stop peanut`]{#sysv-services-stop-first explanation="Die konventionelle Operandenreihenfolge setzt den Dienstnamen vor die Aktion."}
::option[`sudo stop --partition peanut`]{#sysv-services-partition-stop explanation="Dies ist nicht die Syntax des SysV-Dienst-Wrappers."}
::option[`sudo service peanut stop`]{#sysv-services-peanut-stop .correct explanation="Der Wrapper erhält den Dienstnamen gefolgt von der angeforderten Stoppaktion."}
:::

## Neuladen, Neustarten und Status

`restart` stoppt und startet einen Dienst gewöhnlich und verursacht damit eine Unterbrechung. `reload` kann einen Dienst auffordern, die Konfiguration ohne vollständigen Neustart neu einzulesen, jedoch nur, wenn Skript und Daemon dies unterstützen. Einige Skripte bieten `force-reload` mit von der Distribution festgelegtem Fallbackverhalten an.

Validiere die Konfiguration vor jedem Neuladen oder Neustart, halte bei Änderungen am Fernzugriff eine zweite administrative Verbindung offen und überprüfe den Dienst anschließend über seinen tatsächlichen Endpunkt und seine Protokolle – nicht nur anhand eines Status „running“.

```bash
$ sudo service SERVICE_NAME status
$ sudo service SERVICE_NAME reload
```

:::single-choice{#sysv-services-reload-versus-restart} Warum solltest du nicht annehmen, dass `reload` und `restart` gleichwertig sind?

::option[Reload fährt immer das gesamte Betriebssystem herunter.]{#sysv-services-reload-shutdown explanation="Das ist nicht die gewöhnliche Bedeutung einer Neuladeaktion für einen Dienst."}
::option[Restart gibt nur Konfiguration aus und ändert niemals den Prozesszustand.]{#sysv-services-restart-readonly explanation="Restart stoppt und startet den Dienst gewöhnlich."}
::option[Reload ist dienstspezifisch und kann Konfiguration ohne Stoppen des Prozesses neu einlesen.]{#sysv-services-reload-specific .correct explanation="Unterstützung und Semantik gehören zum init-Skript und Daemon, während ein Neustart gewöhnlich eine Unterbrechung des Lebenszyklus verursacht."}
:::

## Laufzeitsteuerung und Aktivierung beim Systemstart

Das sofortige Starten eines Dienstes aktiviert ihn nicht zwangsläufig für zukünftige Runlevel. Die Aktivierung beim Systemstart wird durch Runlevel-Links dargestellt und mit distributionsspezifischen Werkzeugen wie `update-rc.d`, `chkconfig` oder Kompatibilitätsgeneratoren des Dienstmanagers verwaltet.

Erstelle `S`- und `K`-Links nicht manuell, bevor du die Abhängigkeitsmetadaten und das Verwaltungswerkzeug der Distribution verstehst; manuelle Links können überschrieben oder falsch angeordnet werden.

:::single-choice{#sysv-services-start-versus-enable} Aktiviert `service SERVICE start` den Dienst zwangsläufig für zukünftige Systemstarts?

::option[Ja; jede Startaktion erzeugt automatisch alle Runlevel-Links.]{#sysv-services-start-links explanation="Der Wrapper ändert die dauerhafte Aktivierung nicht grundsätzlich."}
::option[Nein; Laufzeitzustand und Runlevel-Aktivierung sind getrennt.]{#sysv-services-runtime-separate .correct explanation="Bootlinks oder Managerrichtlinien bestimmen die zukünftige Aktivierung unabhängig vom jetzigen Prozessstart."}
::option[Ja; eine laufende PID wird dauerhaft im Bootsektor gespeichert.]{#sysv-services-pid-boot-sector explanation="PIDs sind Laufzeitkennungen und keine Metadaten zur Aktivierung beim Systemstart."}
:::

## Zusammenfassung

Du kannst einen älteren Dienst nun bedienen, ohne Laufzeitsteuerung und Startrichtlinie zu verwechseln.

1. Ermittle das tatsächliche Skript und die unterstützten Aktionen.
2. Setze in der Wrapper-Syntax den Dienstnamen vor die Aktion.
3. Validiere und überprüfe das Verhalten beim Neuladen oder Neustarten.
4. Verwalte die Aktivierung für zukünftige Runlevel mit Distributionswerkzeugen.
