---
lesson_id: "etc-fstab-file-system-table"
course_id: "filesystem"
lang: "de"
order_index: 7
title: "/etc/fstab"
description: "Lerne, dauerhafte Dateisystem- und Swap-Verbindungen in `/etc/fstab` zu definieren und sicher zu validieren."
meta_title: "/etc/fstab – Das Dateisystem"
meta_description: "Lerne Aufbau und sichere Bearbeitung von /etc/fstab kennen, um Dateisysteme und Swap dauerhaft zu konfigurieren und vor dem Neustart zu validieren."
meta_keywords: "fstab, fstab Linux, /etc/fstab, Dateisysteme einhängen, Linux Boot, fstab Syntax, mount -a, findmnt verify"
---

`/etc/fstab`, die Dateisystemtabelle, deklariert Dateisysteme, Swap-Bereiche, Bind-Mounts, Netzwerkquellen und andere Verbindungen, die Systemwerkzeuge einhängen oder aktivieren können. Einträge können am Systemstart teilnehmen. Optionen wie `noauto`, die Einbindung von Automount und Richtlinien des Dienstmanagers beeinflussen jedoch, wann oder ob dies geschieht.

## Die sechs Felder

Ein gewöhnlicher Eintrag besitzt sechs durch Leerraum getrennte Felder:

```text
UUID=130b882f-7d79-436d-a096-1e594c92bb76 /data ext4 defaults,nosuid,nodev 0 2
```

1. **Quelle**: ein Gerätepfad, `UUID=`, `LABEL=`, eine Netzwerkquelle oder eine andere unterstützte Angabe.
2. **Ziel**: Einhängepunkt oder, wo passend, `none` für Verwendungen wie Swap.
3. **Typ**: Dateisystemtyp, `swap`, `none` oder ein akzeptierter automatischer Typ.
4. **Optionen**: eine kommagetrennte Liste, die von Mount-Hilfsprogrammen und Integrationsschichten ausgewertet wird.
5. **Dump-Feld**: steuert historisch das Sicherungsprogramm `dump`; `0` deaktiviert die Teilnahme üblicherweise.
6. **Pass-Feld**: steuert, soweit anwendbar, die Reihenfolge von `fsck` beim Systemstart; `0` deaktiviert die automatische Prüfung über diesen Mechanismus.

Leerraum innerhalb eines Felds muss mit der fstab-Syntax maskiert werden, beispielsweise als `\040` für ein Leerzeichen. Ein `#` beginnt außerhalb eines Felds einen Kommentar.

:::single-choice{#fstab-field-count} Wie viele Felder enthält ein normaler Eintrag in `/etc/fstab`?

::option[Vier.]{#fstab-four-fields explanation="Auf Quelle, Ziel, Typ und Optionen folgen die Felder Dump und Pass."}
::option[Acht.]{#fstab-eight-fields explanation="Acht ist nicht die Standardanzahl der Felder eines fstab-Eintrags."}
::option[Sechs.]{#fstab-six-fields .correct explanation="Das traditionelle Format enthält Quelle, Ziel, Typ, Optionen, Dump und Pass."}
:::

## Stabile Quellenkennungen

Für lokale Dateisysteme ist eine Dateisystem-UUID häufig stabiler als die Aufzählung `/dev/sdX`:

```bash
$ lsblk -f
$ sudo blkid
```

Verwende `UUID=...` erst, nachdem du bestätigt hast, dass die Kennung zum beabsichtigten Dateisystem gehört. Eine Neuformatierung erzeugt eine neue UUID, während Klone auf Blockebene dieselbe UUID besitzen können. `PARTUUID=` bezeichnet stattdessen einen Partitionstabelleneintrag und besitzt eine andere Semantik.

:::single-choice{#fstab-uuid-source} Was bezeichnet `UUID=...` im Quellenfeld normalerweise?

::option[Das Benutzerkonto, dem der Einhängepunkt gehört.]{#fstab-user-uuid explanation="Die Kontoidentität wird nicht über die Quellsyntax der Dateisystem-UUID ausgewählt."}
::option[Dateisystemmetadaten mit dieser UUID.]{#fstab-filesystem-uuid .correct explanation="Mount löst die Dateisystemkennung zu einem verfügbaren Blockgerät auf, statt sich auf dessen Aufzählungsnamen zu verlassen."}
::option[Den Prozess, der das Dateisystem zuletzt ausgehängt hat.]{#fstab-process-uuid explanation="Der Prozessverlauf ist in diesem Quellenfeld nicht codiert."}
:::

## Einhängeoptionen und Prüffelder

`defaults` wird zu einer implementierungsabhängigen herkömmlichen Optionsgruppe erweitert und ist nicht zwangsläufig die sicherste Richtlinie für jede Einhängung. Füge Optionen abhängig von Vertrauen und Arbeitslast hinzu, etwa schreibgeschützten Zugriff oder Einschränkungen für Geräteknoten und Setuid-Verhalten. Netzwerk- und Wechseldatenträgerdateisysteme können Richtlinien für Zeitüberschreitungen, Abhängigkeiten oder Fehlertoleranz benötigen, damit der Systemstart nicht unerwartet blockiert.

Bei von `fsck` unterstützten Dateisystemen verwendet das Root-Dateisystem herkömmlicherweise Pass `1`, andere geprüfte lokale Dateisysteme Pass `2`. Die Praxis hängt vom Dateisystem ab; manche Typen verwenden beispielsweise kein allgemeines fsck beim Start. Folge der Dokumentation des installierten Dateisystems und der Distribution, statt mechanisch `2` einzutragen.

:::single-choice{#fstab-pass-zero} Was fordert der Wert `0` im sechsten Feld an?

::option[Die automatische fsck-Reihenfolge über fstab für diesen Eintrag überspringen.]{#fstab-pass-zero-skip .correct explanation="Pass null schließt den Eintrag aus der durch dieses Feld gesteuerten Prüfsequenz beim Systemstart aus."}
::option[Das Dateisystem unter allen Umständen schreibgeschützt einhängen.]{#fstab-pass-zero-readonly explanation="Schreibgeschütztes Verhalten gehört in das Feld der Einhängeoptionen."}
::option[Das Dateisystem vor jedem Start löschen.]{#fstab-pass-zero-erase explanation="Das Pass-Feld formatiert oder löscht kein Dateisystem."}
:::

## Mit einem Wiederherstellungsweg bearbeiten

Ein ungültiger Eintrag für Root, Boot oder ein erforderliches Netzwerk kann den Systemstart unterbrechen. Vor der Bearbeitung:

1. Bestätige eine aktuelle Sicherung sowie Konsolen- oder Rettungszugang.
2. Kopiere die vorhandene Datei unter Erhaltung ihrer Berechtigungen.
3. Prüfe die Quellenidentität und erstelle den beabsichtigten Einhängepunkt.
4. Nimm eine einzelne, begrenzte Änderung vor.
5. Validiere und teste vor dem Neustart.

Schreibe keine Anmeldedaten direkt in einen für alle lesbaren fstab-Eintrag. Verwende den geschützten Anmeldedatenmechanismus des betreffenden Mount-Hilfsprogramms.

:::single-choice{#fstab-editing-recovery} Warum solltest du vor der Änderung eines wichtigen fstab-Eintrags den Rettungszugang bestätigen?

::option[Fstab-Änderungen löschen immer sofort die Partitionstabelle.]{#fstab-no-partition-erase explanation="Die Textänderung selbst schreibt keine Datenträgerpartitionen neu, auch wenn spätere Einhängungen Auswirkungen haben können."}
::option[Die Datei lässt sich ausschließlich aus einem anderen Betriebssystem bearbeiten.]{#fstab-other-os-only explanation="Sie kann unter Linux mit geeigneten Privilegien und Schutzmaßnahmen bearbeitet werden."}
::option[Ein fehlerhafter Eintrag kann verhindern, dass der normale Systemstart ein nutzbares System erreicht.]{#fstab-boot-failure .correct explanation="Fehler bei wichtigen Einhängungen können in den Notfallmodus führen oder abhängige Dienste blockieren."}
:::

## Validieren, ohne Erfolg vorauszusetzen

Beginne, soweit unterstützt, mit einer statischen Prüfung:

```bash
$ sudo findmnt --verify --verbose
```

Teste anschließend den konkreten neuen Eintrag unter kontrollierten Bedingungen, bestätige ihn mit `findmnt` und hänge ihn wieder aus, falls der Test vorübergehend war. `mount -a` versucht viele zulässige Einträge und kann Netzwerke kontaktieren oder unbeabsichtigte Quellen verbinden. Bereits eingehängte und mit `noauto` versehene Einträge werden übersprungen. Der Befehl ist daher weder ein harmloser Syntaxprüfer noch ein vollständiger Beleg.

Lade auf systemd-basierten Systemen nach der Bearbeitung von fstab die Manager-Konfiguration neu, damit erzeugte Mount-Units aktualisiert werden. Prüfe anschließend Abhängigkeiten und Startverhalten gemäß der lokalen Dokumentation.

:::single-choice{#fstab-mount-a-limit} Warum ist `mount -a` allein keine vollständige fstab-Validierung?

::option[Der Befehl formatiert vor dem Einhängen immer jedes aufgeführte Gerät neu.]{#fstab-mount-a-formats explanation="Mount erstellt normalerweise keine Dateisysteme."}
::option[Er kann Einträge überspringen und führt umfassende echte Einhängeoperationen statt nur einer Syntaxprüfung aus.]{#fstab-mount-a-incomplete .correct explanation="Bereits eingehängte oder mit `noauto` versehene Einträge werden möglicherweise nicht getestet, während zulässige Quellen aktive Auswirkungen haben können."}
::option[Er liest nur den Shell-Verlauf und ignoriert fstab.]{#fstab-mount-a-history explanation="Der Befehl berücksichtigt fstab für zulässige Einträge."}
:::

Übe im Lab [Linux-Partitionen und Dateisysteme verwalten](https://labex.io/labs/comptia-manage-linux-partitions-and-filesystems-590845) mit dem wiederherstellungssicheren zweiten Speicher des Labs.

## Zusammenfassung

Du kannst einen dauerhaften Eintrag der Dateisystemtabelle nun lesen und validieren.

1. Werte Quelle, Ziel, Typ, Optionen, Dump und Pass aus.
2. Wähle eine geprüfte Kennung mit der beabsichtigten Identitätssemantik.
3. Lege Einhänge- und Prüfrichtlinien passend zum tatsächlichen Dateisystem fest.
4. Bewahre Rettungszugang und nimm eine einzelne, begrenzte Änderung vor.
5. Verbinde statische Validierung, gezieltes Einhängen und Prüfungen der Startrichtlinie.
