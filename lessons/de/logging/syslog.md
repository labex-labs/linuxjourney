---
lesson_id: "syslog"
course_id: "logging"
lang: "de"
order_index: 2
title: "syslog"
description: "Lerne, wie Syslog-Facilities, Schweregrade, Weiterleitungsregeln und der Befehl logger funktionieren."
meta_title: "syslog – Protokollierung"
meta_description: "Lerne syslog und rsyslog unter Linux kennen, verwalte Systemprotokolle und verwende den Befehl logger. Eine verständliche Einführung für Einsteiger."
meta_keywords: "syslog, rsyslog, Linux-Protokolle, logger-Befehl, /var/log/syslog, Linux-Tutorial, Linux für Einsteiger, Systemprotokollierung"
---

Syslog definiert ein Nachrichtenmodell und Transportkonventionen, die von vielen Unix-artigen Systemen verwendet werden. Rsyslog ist eine Implementierung, die Nachrichten empfangen, filtern, umwandeln, speichern und weiterleiten kann. Es kann neben `systemd-journald` bestehen; keiner der Namen bedeutet, dass jede Anwendung diesen Weg verwendet.

## Facilities und Schweregrade

Eine Syslog-Nachricht enthält eine Facility, die ihre grobe Quellkategorie beschreibt, und einen Schweregrad von Notfall bis Debug. Zu den häufigen Facilities gehören `auth`, `cron`, `daemon`, `kern`, `mail`, `user` sowie `local0` bis `local7`.

Schweregrade sind geordnet. In der klassischen Selektorsyntax entspricht `daemon.warning` normalerweise Daemon-Nachrichten mit dem Schweregrad Warnung und allen schwerwiegenderen Stufen, nicht nur Warnungen. Eine genaue Übereinstimmung verwendet bei Implementierungen, die die klassische Syntax unterstützen, einen Gleichheitsmodifikator wie `daemon.=warning`.

:::single-choice{#syslog-warning-selector}
Was erfasst ein klassischer Selektor wie `daemon.warning` normalerweise?

::option[Nur Nachrichten, deren Text das Wort daemon enthält.]{#syslog-text-daemon explanation="Facility-Metadaten und keine Suche im Nachrichtentext steuern diesen Selektor."}
::option[Jede Debug-Nachricht jeder Facility.]{#syslog-all-debug explanation="Der Selektor ist auf die Facility daemon und einen Schweregradschwellenwert beschränkt."}
::option[Warnungen und schwerwiegendere Daemon-Nachrichten.]{#syslog-warning-or-higher .correct explanation="Der Prioritätsselektor umfasst den benannten Schweregrad und Stufen höherer Dringlichkeit."}
:::

## Rsyslog-Regeln lesen

Rsyslog lädt gewöhnlich eine Hauptdatei und Ausschnitte unter `/etc/rsyslog.d/`. Eine herkömmliche Regel besteht aus einem Selektor, gefolgt von einer Aktion:

```text
auth,authpriv.*          /var/log/auth.log
*.*;auth,authpriv.none  -/var/log/syslog
kern.*                  /var/log/kern.log
```

Die erste Zeile leitet alle Prioritäten zweier Authentifizierungs-Facilities weiter. Die zweite wählt Nachrichten breit aus und schließt diese Facilities aus. Die dritte leitet Nachrichten der Kernel-Facility weiter. Ein vorangestelltes `-` bei einer Dateiaktion fordert gewöhnlich asynchrone Schreibvorgänge an; es bedeutet keinen Ausschluss.

Untersuche alle eingebundenen Dateien und validiere die genaue Syntax der installierten Version, bevor du die Weiterleitung in einer Produktionsumgebung änderst.

:::single-choice{#syslog-selector-action}
Was ist in einer herkömmlichen Rsyslog-Regel die Aktion?

::option[Der Facility- und Schweregradausdruck auf der linken Seite.]{#syslog-left-selector explanation="Dieser Teil wählt Nachrichten aus."}
::option[Das Ziel oder der Vorgang auf der rechten Seite.]{#syslog-right-action .correct explanation="Die Aktion bestimmt, ob ausgewählte Datensätze an eine Datei, ein entferntes Ziel oder eine andere Ausgabe gehen."}
::option[Der Kommentar, der die Paketversion beschreibt.]{#syslog-comment-version explanation="Kommentare führen keine Nachrichtenweiterleitung aus."}
:::

## Eine Testnachricht senden

Verwende `logger`, um einen kontrollierten Test mit eindeutigem Tag und einer Priorität einzureichen:

```bash
$ logger -p user.notice -t lesson-test 'routing check 2026-08-31T10:00'
```

Frage anschließend das erwartete Ziel ab, zum Beispiel:

```bash
$ journalctl -t lesson-test --since '5 minutes ago'
```

Dasselbe Ereignis kann abhängig von Weiterleitung und Routing im Journal und in einer Textdatei erscheinen. `logger -s` kopiert die Nachricht zusätzlich in die Standardfehlerausgabe; dies beweist keine dauerhafte Speicherung.

:::single-choice{#syslog-logger-tag}
Was fügt `logger -t lesson-test` der eingereichten Nachricht hinzu?

::option[Eine Anforderung, ältere Testdatensätze zu löschen.]{#syslog-tag-delete explanation="Die Option setzt ein identifizierendes Tag und verwaltet keine Aufbewahrung."}
::option[Die Kennung `lesson-test` als Nachrichtentag.]{#syslog-tag-identifier .correct explanation="Ein eindeutiges Tag erleichtert das Auffinden des kontrollierten Ereignisses an den konfigurierten Zielen."}
::option[Eine Zustellverzögerung von fünf Minuten.]{#syslog-tag-delay explanation="Die Tag-Option codiert kein Zustellintervall."}
:::

## Weiterleitung ändern und überprüfen

Sichere vor einer Änderung die aktuelle Konfiguration und ermittle nachgelagerte Verbraucher. Validiere die Syntax mit dem Konfigurationsprüfmodus der Implementierung, gewöhnlich:

```bash
$ sudo rsyslogd -N1
```

Erst nach der Validierung solltest du den Dienst über seinen Manager neu laden. Sende eine neue markierte Nachricht, überprüfe jedes erforderliche Ziel und prüfe Dienstzustand sowie interne Fehlerprotokolle. Eine syntaktisch gültige Regel kann dennoch zu breit weiterleiten, Datensätze duplizieren oder vertrauliche Daten offenlegen.

Bei der Weiterleitung über nicht vertrauenswürdige Netzwerke sollte authentifizierter, verschlüsselter Transport verwendet werden. UDP-Zustellung besitzt keine Ende-zu-Ende-Bestätigung. Kritische Audit-Anforderungen benötigen daher einen Entwurf, der Warteschlangen, Verluste, Integrität, Zugriffskontrolle und Ausfälle des Empfängers berücksichtigt.

:::single-choice{#syslog-change-verification}
Welche Belege reichen aus, dass eine neue Weiterleitungsregel funktioniert?

::option[Die Konfigurationsdatei besitzt einen aktuellen Änderungszeitpunkt.]{#syslog-mtime explanation="Ein Zeitstempel beweist weder gültige Syntax noch Zustellung."}
::option[Der Sender kann den Empfänger mit einem Ping erreichen.]{#syslog-ping explanation="Netzwerkerreichbarkeit allein überprüft weder das Protokollierungsprotokoll noch den Speicherpfad."}
::option[Die Validierung ist erfolgreich, und ein markierter Test erreicht jedes beabsichtigte Ziel.]{#syslog-validate-and-test .correct explanation="Sowohl statische Validierung als auch ein beobachtetes Ende-zu-Ende-Ereignis sind erforderlich."}
:::

## Zusammenfassung

Du kannst die Syslog-Weiterleitung nun von den Nachrichtenmetadaten bis zum konfigurierten Ziel testen.

1. Unterscheide Facilities von geordneten Schweregraden.
2. Lies Selektoren getrennt von ihren Aktionen.
3. Sende mit `logger` ein markiertes Ereignis mit Priorität.
4. Validiere die Konfiguration und überprüfe die Zustellung von Ende zu Ende.
