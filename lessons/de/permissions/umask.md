---
lesson_id: "umask"
course_id: "permissions"
lang: "de"
order_index: 4
title: "Umask"
description: "Erfahre, wie die umask eines Prozesses die für neu erstellte Dateien und Verzeichnisse angeforderten Berechtigungsbits begrenzt."
meta_title: "Umask – Berechtigungen"
meta_description: "Erfahre, wie du mit dem Befehl `umask` die Standard-Dateiberechtigungen unter Linux steuerst. Verstehe numerische Berechtigungen und verwalte den Zugriff auf neue Dateien mühelos."
meta_keywords: "umask, Linux-Berechtigungen, Dateiberechtigungen, Linux-Befehle, Linux für Einsteiger, Linux-Tutorial, Standardberechtigungen"
---

Die Dateierstellungsmaske oder umask eines Prozesses verhindert, dass ausgewählte Berechtigungsbits gesetzt werden, wenn dieser Prozess ein Dateisystemobjekt erstellt. Sie ist eine Maske und kein vollständiger Standardmodus: Die Anwendung fordert zuerst einen Modus an, und der Kernel entfernt die von der umask untersagten Bits.

Konzeptionell gilt:

```text
resultierender Modus = angeforderter Modus AND NOT umask
```

Zugriffssteuerungslisten und das Verhalten der Anwendung können weitere Einzelheiten hinzufügen. Prüfe daher das Ergebnis, wenn genaue Berechtigungen wichtig sind.

## Die Umask anzeigen und festlegen

Führe `umask` ohne Operanden aus, um die Maske der aktuellen Shell anzuzeigen, häufig in oktaler Form:

```bash
$ umask
0022
```

Lege sie für die aktuelle Shell und die anschließend von dieser Shell gestarteten Prozesse fest:

```bash
$ umask 027
```

Jede oktale Position steht für Eigentümer, Gruppe und andere. Ein Maskenbit entfernt die entsprechende angeforderte Berechtigung: `2` maskiert Schreiben, `4` maskiert Lesen und `1` maskiert Ausführen.

:::single-choice{#umask-command-purpose}
Was ändert `umask 027` in der aktuellen Shell?

::option[Die Berechtigungen aller bereits vorhandenen Dateien.]{#umask-existing-files explanation="Eine umask beeinflusst Erstellungsanfragen; sie führt nicht nachträglich `chmod` auf bestehenden Objekten aus."}
::option[Die Maske, die später aus dieser Shell gestartete Befehle erben.]{#umask-current-shell-mask .correct explanation="Die Shell setzt die umask ihres Prozesses, und Kindprozesse erben diesen Wert gewöhnlich."}
::option[Die auf neuen Dateien gespeicherten Eigentümer- und Gruppennamen.]{#umask-owner-group explanation="Die Maske filtert Berechtigungsbits und wählt keine Eigentumsidentitäten aus."}
:::

## Modi neuer Dateien und Verzeichnisse berechnen

Viele gewöhnliche Programme fordern für neue reguläre Dateien `0666` an, da es unsicher wäre, neu erstellte Dateien standardmäßig ausführbar zu machen. Für neue Verzeichnisse fordern sie häufig `0777` an, weil dort die Ausführungsberechtigung zum Durchqueren erforderlich ist.

Mit der umask `0022`:

```text
reguläre Datei: 0666 maskiert durch 0022 -> 0644 (rw-r--r--)
Verzeichnis:     0777 maskiert durch 0022 -> 0755 (rwxr-xr-x)
```

Die umask entfernt ausschließlich angeforderte Bits. Sie kann keine Ausführungsberechtigung hinzufügen, wenn eine Anwendung sie nicht angefordert hat. Eine Anwendung kann außerdem einen stärker eingeschränkten Ausgangsmodus anfordern, wodurch ein restriktiveres Ergebnis entsteht.

:::single-choice{#umask-file-mode-022}
Welcher Modus entsteht, wenn ein Programm für eine reguläre Datei den Modus `0666` anfordert und die umask `0022` lautet?

::option[`0666`]{#umask-file-0666 explanation="Die von `0666` angeforderten Schreibbits für Gruppe und andere werden von der Maske `0022` entfernt."}
::option[`0755`]{#umask-file-0755 explanation="Für die reguläre Datei wurden keine Ausführungsbits angefordert, daher kann die umask sie nicht hinzufügen."}
::option[`0644`]{#umask-file-0644 .correct explanation="Nach dem Entfernen der Schreibberechtigung für Gruppe und andere aus `0666` bleiben Lesen/Schreiben für den Eigentümer und reiner Lesezugriff für Gruppe und andere."}
:::

:::single-choice{#umask-directory-mode-027}
Welcher Modus entsteht, wenn ein Programm für ein Verzeichnis `0777` anfordert und die umask `0027` lautet?

::option[`0777`]{#umask-directory-0777 explanation="Die angeforderte Gruppenschreibberechtigung und die Berechtigungen für andere werden von der von null verschiedenen Maske gefiltert."}
::option[`0640`]{#umask-directory-0640 explanation="Dieses Ergebnis entfernt zusätzlich Ausführungsbits, die die Maske `0027` weder beim Eigentümer noch bei der Gruppe entfernt."}
::option[`0750`]{#umask-directory-0750 .correct explanation="Die Maske entfernt die Gruppenschreibberechtigung und alle Berechtigungen für andere. Übrig bleibt `rwxr-x---`."}
:::

## Gültigkeitsbereich und Dauerhaftigkeit

Die Änderung der umask in einer Shell verändert weder deren Elternprozess noch unabhängige Sitzungen. Der Wert gilt für zukünftige Erstellungen durch diese Shell und ihre Nachkommen; bestehende Dateien behalten ihre Modi.

Um einen bevorzugten Wert dauerhaft festzulegen, konfiguriere ihn an der für deine Umgebung geeigneten Stelle für Anmeldung, Shell, PAM, Dienstmanager oder Anwendung. Der richtige Ort variiert, und Dienste können ihre eigene umask festlegen. Gehe nicht davon aus, dass die Bearbeitung einer einzelnen Datei für eine interaktive Shell jeden Prozess auf dem System steuert.

:::single-choice{#umask-existing-file-effect}
Was geschieht mit einer bestehenden Datei, wenn du eine neue umask festlegst?

::option[Ihr aktueller Modus bleibt unverändert.]{#umask-existing-unchanged .correct explanation="Eine neue umask filtert spätere Erstellungsanfragen und ändert keine bereits auf Dateisystemobjekten gespeicherten Modi."}
::option[Ihr Modus wird aus `0666` neu berechnet.]{#umask-existing-recalculated explanation="Bestehende Objekte werden weder neu erstellt noch automatisch durch die neue Maske verarbeitet."}
::option[Ihr Eigentümer verliert die maskierten Berechtigungen sofort.]{#umask-existing-owner-loss explanation="Die Änderung der umask eines Prozesses ist kein Vorgang auf bestehenden Dateimetadaten."}
:::

Erstelle für praktische Übungen Dateien und Verzeichnisse unter verschiedenen Masken in einer isolierten Umgebung und vergleiche anschließend ihre Modi mit `ls -ld`. Das Lab [Linux-Benutzer, -Gruppen und Dateiberechtigungen](https://labex.io/labs/linux-linux-user-group-and-file-permissions-18002) bietet eine passende Übungsumgebung.

## Zusammenfassung

Du kannst nun vorhersagen, wie eine umask neu angeforderte Berechtigungen begrenzt.

1. Zeige die Maske der aktuellen Shell mit `umask` an oder lege sie damit fest.
2. Entferne maskierte Bits aus dem von einer Anwendung angeforderten Modus.
3. Unterscheide die häufige Dateianforderung `0666` von der Verzeichnisanforderung `0777`.
4. Behandle Gültigkeitsbereich und Dauerhaftigkeit der umask als prozess- und umgebungsspezifisch.
