---
lesson_id: "general-logging"
course_id: "logging"
lang: "de"
order_index: 3
title: "Allgemeine Protokollierung"
description: "Lerne, allgemeine Linux-Systemprotokolle zu ermitteln, zu filtern, zu verfolgen und miteinander zu verknüpfen."
meta_title: "Allgemeine Protokollierung – Protokollierung"
meta_description: "Eine Einführung in allgemeine Linux-Protokolle. Lerne /var/log/messages und syslog für wirksame Systemüberwachung, Protokollanalyse und Linux-Fehlersuche kennen."
meta_keywords: "Linux-Protokolle, syslog, var/log/messages, Linux-Fehlersuche, Systemprotokolle, Protokollanalyse, Systemüberwachung, Linux-Anleitung, Linux-Einsteiger, /var/log"
---

Allgemeine Systemprotokolle verbinden routinemäßige Hinweise, Warnungen und Fehler aus mehreren Quellen. Sie sind nützliche Ausgangspunkte, doch ihre Dateinamen und Inhalte sind Entscheidungen der Weiterleitungsrichtlinie und keine allgemeingültigen Linux-Garantien.

## Die relevante Quelle finden

Abhängig von Distribution und Konfiguration können allgemeine Nachrichten in `/var/log/syslog`, `/var/log/messages`, im systemd-Journal oder an mehreren Zielen erscheinen. Ermittle zuerst Host und Zeitraum des Vorfalls und untersuche anschließend die verfügbaren Quellen:

```bash
$ ls -lh /var/log
$ journalctl --since '2026-08-31 09:00' --until '2026-08-31 09:15'
```

Anwendungsprotokolle können in eigenen Unterverzeichnissen oder einem externen Dienst liegen. Datensätze zu Authentifizierung, Audit, Paketen, Datenbanken und Webservern können absichtlich vom allgemeinen Strom getrennt sein.

:::single-choice{#general-logs-universal-file} Warum solltest du nicht annehmen, dass `/var/log/messages` auf jedem Linux-Host vorhanden ist?

::option[Allgemeine Protokollziele hängen von lokalen Datensammlern und der Weiterleitungsrichtlinie ab.]{#general-logs-local-routing .correct explanation="Ein reines Journal-System oder eine andere Syslog-Konfiguration kann andere Ziele verwenden."}
::option[Linux erlaubt nur eine Protokolldatei auf jedem Datenträger.]{#general-logs-one-file explanation="Systeme verwalten gewöhnlich viele Protokolldateien und Journalspeicher."}
::option[Der Pfad ist ausschließlich für Benutzerdokumente reserviert.]{#general-logs-user-documents explanation="Die Hierarchie `/var/log` wird üblicherweise für Protokolle verwendet."}
:::

## Textprotokolle untersuchen

Verwende `less` zur kontrollierten Navigation und `tail` für die neuesten Datensätze:

```bash
$ sudo less /var/log/syslog
$ sudo tail -n 100 /var/log/messages
```

Verfolge während einer begrenzten Reproduktion neu angehängte Zeilen mit `tail -F FILE`. `-F` versucht den Zugriff erneut, wenn eine Datei bei der Rotation ersetzt wird, anders als eine einfache Momentaufnahme. Beende die Verfolgung mit `Ctrl-C` und lasse keine weitreichenden privilegierten Sitzungen offen.

:::single-choice{#general-logs-tail-f-capability} Wofür ist `tail -F` während einer kontrollierten Reproduktion nützlich?

::option[Zum Verfolgen einer benannten Datei über einen üblichen Rotationsaustausch hinweg.]{#general-logs-tail-follow .correct explanation="Das erneute Öffnen nach Namen hilft weiterzuarbeiten, nachdem die aktive Datei umbenannt und neu erstellt wurde."}
::option[Zum Ändern jedes Protokollschweregrads auf Debug.]{#general-logs-tail-debug explanation="Tail liest Dateiinhalte und konfiguriert keine Quellen neu."}
::option[Zum Entschlüsseln komprimierter Archive ohne ein weiteres Programm.]{#general-logs-tail-decrypt explanation="Es bietet keine allgemeine Archivdekomprimierung oder Entschlüsselung."}
:::

## Filtern, ohne den Zusammenhang zu verlieren

Durchsuche eine begrenzte Datei oder ein Journalintervall, statt sofort einen unbegrenzten Live-Strom durch eine Pipeline zu leiten:

```bash
$ grep -n -C 3 'connection refused' /var/log/example.log
$ journalctl -u example.service --since '10 minutes ago' --grep='connection refused'
```

Groß-/Kleinschreibung, Formulierung, Ratenbegrenzungen und Lokalisierung können eine wörtliche Suche unvollständig machen. Erfasse sowohl erfolgreiche als auch fehlgeschlagene Ereignisse und bewahre umgebende Zeilen, weil die Ursache dem sichtbaren Fehler vorausgehen kann.

:::single-choice{#general-logs-context-lines} Warum solltest du Zeilen um einen passenden Fehler herum einbeziehen?

::option[Das vorherige Ereignis kann den späteren Fehler erklären.]{#general-logs-preceding-context .correct explanation="Zeitlicher Zusammenhang hilft, eine Abfolge zu rekonstruieren, statt eine Zeichenfolge als gesamten Vorfall zu behandeln."}
::option[Der Zusammenhang garantiert, dass der erste Treffer die Ursache ist.]{#general-logs-guaranteed-cause explanation="Weitere Belege müssen weiterhin verknüpft werden; Zusammenhang beweist keine Kausalität."}
::option[Er ändert automatisch die Dienstkonfiguration.]{#general-logs-context-config explanation="Die Suchausgabe ist schreibgeschützt und aktualisiert keine Diensteinstellungen."}
:::

## Rotierte und archivierte Protokolle einbeziehen

Ein Vorfall kann eine Rotationsgrenze überschreiten. Aktive Dateien, nummerierte Archive und komprimierte Dateien können unterschiedliche Teile derselben Abfolge enthalten. Werkzeuge wie `zgrep` und `zless` lesen gzip-komprimierte Archive:

```bash
$ sudo zgrep -n 'connection refused' /var/log/example.log*.gz
```

Ordne Ergebnisse nach den tatsächlichen Zeitstempeln und nicht nur nach der Endung. Bewahre vor dem Kopieren von Belegen Metadaten und beschränke den Zugriff, weil Protokolle personenbezogene Daten oder Anmeldedaten enthalten können.

:::single-choice{#general-logs-rotation-boundary} Was solltest du prüfen, wenn ein Vorfall eine Protokollrotation überschreitet?

::option[Nur die neu erstellte leere aktive Datei.]{#general-logs-active-only explanation="Frühere Datensätze können in rotierte Archive verschoben worden sein."}
::option[Aktive und archivierte Protokolle, geordnet nach Ereigniszeit.]{#general-logs-all-intervals .correct explanation="Die relevante Abfolge kann auf aktuelle und rotierte Dateien verteilt sein."}
::option[Nur Dateinamen, unabhängig von den Zeitstempeln der Datensätze.]{#general-logs-filenames-only explanation="Endungsreihenfolge und Ereigniszeit sind nicht immer gleichbedeutend."}
:::

## Zusammenfassung

Du kannst allgemeine Protokolle nun über Dateien, Journale und Rotationsgrenzen hinweg untersuchen.

1. Ermittle Ziele, statt einen allgemeingültigen Dateinamen anzunehmen.
2. Lies ein begrenztes Intervall und verfolge nur während der Reproduktion.
3. Bewahre den zeitlichen Zusammenhang um passende Datensätze.
4. Beziehe rotierte Archive ein und schütze vertrauliche Belege.
