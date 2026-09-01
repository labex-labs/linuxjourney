---
lesson_id: "rsync"
course_id: "network-sharing"
lang: "de"
order_index: 2
title: "rsync"
description: "Lerne, sichere lokale oder SSH-basierte Verzeichnissynchronisierung mit rsync vorab zu prüfen, auszuführen und zu verifizieren."
meta_title: "rsync – Netzwerkfreigaben"
meta_description: "Lerne den leistungsfähigen Linux-Befehl rsync für effiziente Dateisynchronisierung, entfernte Datenübertragung und verlässliche Sicherungen kennen."
meta_keywords: "rsync, Linux rsync, Dateisynchronisierung, Datensicherung, entfernte Synchronisierung, rsync-Befehl, Linux-Dateiübertragung, rsync-Tutorial"
---

`rsync` gleicht Dateien und Verzeichnisbäume ab und vermeidet dabei unnötige Übertragung unveränderter Daten. Seine Effizienz macht nicht jeden Aufruf sicher: Quellsyntax, abschließende Schrägstriche, Metadaten, Ausschlüsse und Löschrichtlinie bestimmen das Ergebnis.

## Quelle und Ziel lesen

Synchronisiere den Inhalt von `source/` lokal nach `destination/`:

```bash
$ rsync -a -- source/ destination/
```

Der abschließende Schrägstrich bei `source/` bedeutet „kopiere den Inhalt dieses Verzeichnisses“. Ohne ihn erstellt oder aktualisiert `rsync -a source destination/` den Pfad `destination/source`. Prüfe bei einer Änderung der Schrägstriche immer die entstehenden Pfade vorab.

:::single-choice{#rsync-source-trailing-slash} Was bedeutet der abschließende Schrägstrich in `rsync -a source/ destination/`?

::option[Die Quelle nach einer erfolgreichen Übertragung löschen.]{#rsync-delete-source explanation="Das Entfernen der Quelle erfordert eine getrennte ausdrückliche Option und Richtlinie."}
::option[Den Inhalt von `source` in das Ziel kopieren.]{#rsync-copy-contents .correct explanation="Das Entfernen des Schrägstrichs an der Quelle verändert die oberste Zielstruktur."}
::option[Das Ziel als entfernte Windows-Freigabe interpretieren.]{#rsync-windows-share explanation="Der Schrägstrich steuert Verzeichnisinhalte und nicht den Transporttyp."}
:::

## Archivmodus verstehen

Der Archivmodus `-a` entspricht einer Sammlung rekursiver und metadatenerhaltender Optionen, die häufig als `-rlptgoD` zusammengefasst werden. Er bewahrt symbolische Links, Berechtigungen, Änderungszeiten, Gruppen, Eigentümer sowie Geräte- oder Spezialdateien, soweit Berechtigungen und Plattformunterstützung dies erlauben.

Der Archivmodus umfasst nicht die Erhaltung harter Links, ACLs oder erweiterter Attribute; dafür werden gewöhnlich `-H`, `-A` und `-X` benötigt. Er erstellt außerdem nicht von selbst historische Versionen.

:::single-choice{#rsync-archive-limit} Welche Metadaten sind in `-a` allein nicht enthalten?

::option[Beziehungen harter Links.]{#rsync-hard-links .correct explanation="Die Erhaltung harter Links erfordert die getrennte Option `-H`."}
::option[Rekursives Durchlaufen von Verzeichnissen.]{#rsync-archive-recursion explanation="Der Archivmodus umfasst rekursives Durchlaufen."}
::option[Änderungszeiten.]{#rsync-archive-times explanation="Der Archivmodus umfasst die Erhaltung von Zeiten."}
:::

## Eine Übertragung vorab prüfen

Verwende vor einer folgenreichen Synchronisierung einen Probelauf mit einzeln aufgeführten Änderungen:

```bash
$ rsync -a --dry-run --itemize-changes -- source/ destination/
```

Ein Probelauf sagt Aktionen anhand der aktuellen Erfassung voraus; er kann nicht garantieren, dass sich Dateien vor dem tatsächlichen Befehl nicht ändern. Speichere und prüfe den genauen Befehl und führe ihn erst nach Bestätigung beider Endpunkte ohne `--dry-run` aus.

:::single-choice{#rsync-dry-run-purpose} Was bietet `--dry-run --itemize-changes`?

::option[Eine dauerhafte Momentaufnahme auf einem anderen Gerät.]{#rsync-dry-backup explanation="Ein Probelauf erstellt weder eine Datenkopie noch unabhängige Aufbewahrung."}
::option[Eine Garantie, dass sich Quelldateien später nicht ändern können.]{#rsync-dry-lock explanation="Die Vorschau sperrt den Quellbaum nicht."}
::option[Eine Vorschau der aktuell von rsync geplanten Änderungen.]{#rsync-dry-preview .correct explanation="Die einzeln aufgeführte Probelaufausgabe zeigt Pfad- und Metadatenentscheidungen vor der Änderung."}
:::

## Über SSH synchronisieren

Übertrage zum entfernten Host oder rufe von ihm ab, indem du den bekannten entfernten Operanden verwendest:

```bash
$ rsync -a -- source/ alice@example.net:/srv/data/
$ rsync -a -- alice@example.net:/srv/data/ destination/
```

Modernes rsync verwendet für diese Form gewöhnlich SSH. Bestätige dennoch die konfigurierte entfernte Shell, den Hostschlüssel, Kontoberechtigungen und die Verfügbarkeit von rsync auf dem entfernten Host. Komprimierung mit `-z` kann bei komprimierbaren Daten über eine eingeschränkte Verbindung helfen, aber für bereits komprimierte Daten CPU verschwenden.

:::single-choice{#rsync-pull-direction} Welche Operandenreihenfolge ruft entfernte Daten in ein lokales Verzeichnis ab?

::option[`rsync -a local/ host:/data/`]{#rsync-local-first explanation="Diese Reihenfolge überträgt lokale Inhalte zum entfernten Ziel."}
::option[`rsync --delete host local`]{#rsync-missing-path explanation="Dies drückt nicht die gezeigte Syntax für entfernte Pfade aus und fügt eine unabhängige destruktive Option hinzu."}
::option[`rsync -a host:/data/ local/`]{#rsync-remote-first .correct explanation="Der entfernte Baum ist die Quelle und der lokale Baum das Ziel."}
:::

## Löschen als destruktiv behandeln

`--delete` entfernt Zieleinträge, die innerhalb des synchronisierten Bereichs an der Quelle fehlen. Vertauschte Endpunkte, ein falscher Schrägstrich oder ein fehlerhafter Ausschluss können deshalb gültige Daten löschen. Prüfe vorab gegen ein Testziel, stelle wiederherstellbare Sicherungen sicher, prüfe den Mountzustand und erwäge vor der Genehmigung eine Obergrenze für Löschungen.

Untersuche nach dem tatsächlichen Lauf Exit-Status und Protokolle, vergleiche erwartete Dateianzahlen und Metadaten und teste repräsentative Inhalte oder die Wiederherstellung. Rsync-Synchronisierung allein spiegelt unerwünschte Löschung oder Beschädigung und ist keine vollständige Sicherungsstrategie.

:::single-choice{#rsync-delete-effect} Was kann `--delete` während der Synchronisierung bewirken?

::option[Jede übertragene Datei mit dem SSH-Hostschlüssel verschlüsseln.]{#rsync-delete-encrypt explanation="Die Löschrichtlinie hat nichts mit Dateiverschlüsselung zu tun."}
::option[Alle Änderungen am Zieldateisystem verhindern.]{#rsync-delete-readonly explanation="Die Option erlaubt ausdrücklich zusätzliche Zieländerungen."}
::option[Zieleinträge entfernen, die im ausgewählten Quellbereich fehlen.]{#rsync-delete-destination .correct explanation="Die Option gleicht den Zielbestand an die Quelle an und erfordert eine geprüfte Vorschau sowie einen Wiederherstellungsplan."}
:::

## Zusammenfassung

Du kannst einen `rsync`-Vorgang nun vorab prüfen und verifizieren, ohne seine destruktiven Randfälle zu verbergen.

1. Verwende abschließende Schrägstriche, um die beabsichtigte Verzeichnisstruktur auszudrücken.
2. Ergänze bei Bedarf Metadatenoptionen, die der Archivmodus nicht umfasst.
3. Prüfe die einzeln aufgeführte Probelaufausgabe vor der tatsächlichen Synchronisierung.
4. Überprüfe SSH-Identität und Endpunktrichtung.
5. Behandle Löschung und Sicherungsaufbewahrung als ausdrückliche Richtlinien.
