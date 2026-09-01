---
lesson_id: "file-permissions"
course_id: "permissions"
lang: "de"
order_index: 1
title: "Dateiberechtigungen"
description: "Erfahre, wie du Linux-Dateitypen und die Berechtigungsbits für Eigentümer, Gruppe und andere liest."
meta_title: "Dateiberechtigungen – Berechtigungen"
meta_description: "Ein wichtiger Teil unseres vollständigen Linux-Tutorials. Lerne Linux-Dateiberechtigungen kennen, darunter die rwx-Bits für Benutzer, Gruppe und andere. Beherrsche die Ausgabe von `ls -l` und verstehe Dateimodi."
meta_keywords: "Dateiberechtigungen, Linux-Dateiberechtigungen, bester Weg Linux zu lernen, vollständiges Linux-Tutorial, rwx-Berechtigungen, Befehl ls -l, Dateimodi, Linux-Leitfaden"
---

Linux stellt viele Ressourcen über dateiähnliche Schnittstellen dar, und jedes Dateisystemobjekt besitzt Metadaten, die den Zugriff steuern. Das Lesen dieser Metadaten ist eine Grundlage für den sicheren Umgang mit Dateien und Verzeichnissen.

## Eine ausführliche Auflistung lesen

Verwende `ls -l`, um eine ausführliche Auflistung anzuzeigen:

```bash
$ ls -ld Desktop/
drwxr-xr-x 2 pete penguins 4096 Dec 1 11:45 Desktop/
```

Das erste Feld, `drwxr-xr-x`, verbindet ein Zeichen für den Dateityp mit neun Berechtigungszeichen. Die Auflistung nennt außerdem `pete` als Eigentümer und `penguins` als die dem Verzeichnis zugeordnete Gruppe.

Das erste Zeichen beschreibt den Objekttyp. Häufige Werte sind:

- `-` für eine reguläre Datei
- `d` für ein Verzeichnis
- `l` für einen symbolischen Link

Es gibt weitere besondere Dateitypen. Die übrigen neun Zeichen sind die Zugriffsberechtigungen:

```text
d | rwx | r-x | r-x
```

:::single-choice{#file-permissions-type-character} Was zeigt das erste `d` in `drwxr-xr-x` an?

::option[Das Objekt ist ein symbolischer Link.]{#file-permissions-type-link explanation="Ein symbolischer Link wird an der Position für den Dateityp gewöhnlich mit `l` dargestellt."}
::option[Das Objekt ist ein Verzeichnis.]{#file-permissions-type-directory .correct explanation="Das erste Zeichen gibt den Dateityp an, und `d` kennzeichnet ein Verzeichnis."}
::option[Der Eigentümer besitzt eine Löschberechtigung.]{#file-permissions-type-delete explanation="Linux-Moduszeichenfolgen verwenden `d` nicht als Löschberechtigung; die erste Position beschreibt den Objekttyp."}
:::

## `r`, `w` und `x` verstehen

Jedes Berechtigungstripel verwendet diese Zeichen:

- `r` gewährt Leseberechtigung.
- `w` gewährt Schreibberechtigung.
- `x` gewährt Ausführungsberechtigung.
- `-` bedeutet, dass die betreffende Berechtigung fehlt.

Bei einer regulären Datei erlaubt Lesen den Zugriff auf ihren Inhalt, Schreiben die Änderung ihres Inhalts und Ausführen dem Kernel den Versuch, sie als Programm zu starten. Die Ausführung kann dennoch scheitern, wenn das Dateiformat, die Interpreterzeile, Einhängeoptionen oder eine andere Sicherheitskontrolle sie nicht zulassen.

Bei einem Verzeichnis beziehen sich die Bedeutungen auf Verzeichniseinträge:

- Lesen erlaubt das Auflisten der Namen im Verzeichnis.
- Schreiben erlaubt das Erstellen oder Entfernen von Einträgen, gewöhnlich in Verbindung mit der Ausführungsberechtigung.
- Ausführen, auch Suchberechtigung genannt, erlaubt das Durchqueren des Verzeichnisses und den Zugriff auf Einträge anhand ihres Namens.

Das Löschen einer Datei wird in erster Linie durch die Berechtigungen ihres übergeordneten Verzeichnisses gesteuert und nicht durch das Schreibbit der Datei selbst.

:::single-choice{#file-permissions-directory-execute} Was erlaubt die Ausführungsberechtigung auf einem Verzeichnis in erster Linie?

::option[Jede im Verzeichnis gespeicherte reguläre Datei auszuführen.]{#file-permissions-directory-run-files explanation="Das Ausführungsbit eines Verzeichnisses gewährt nicht jeder darin enthaltenen Datei eine Ausführungsberechtigung."}
::option[Den Inhalt jeder Datei im Verzeichnis zu ändern.]{#file-permissions-directory-edit-files explanation="Das Schreiben von Dateiinhalten hängt von den Berechtigungen der Dateien und anderen Zugriffskontrollen ab."}
::option[Das Verzeichnis zu durchqueren und anhand ihrer Namen auf Einträge zuzugreifen.]{#file-permissions-directory-search .correct explanation="Die Ausführungs- oder Suchberechtigung eines Verzeichnisses ermöglicht die Pfaddurchquerung durch dieses Verzeichnis."}
:::

## Klassen für Eigentümer, Gruppe und andere

Die neun Moduszeichen bilden drei Tripel in einer festen Reihenfolge:

1. **Eigentümer**: Berechtigungen, die verwendet werden, wenn die effektive Benutzer-ID des Prozesses mit dem Eigentümer der Datei übereinstimmt.
2. **Gruppe**: Berechtigungen, die verwendet werden, wenn eine zutreffende Gruppen-ID des Prozesses mit der Gruppe der Datei übereinstimmt.
3. **Andere**: Berechtigungen, die verwendet werden, wenn keine der vorherigen Klassen zutrifft.

Der Kernel wählt eine zutreffende Klasse aus; er kombiniert die drei Tripel nicht, um das großzügigste Ergebnis zu erhalten. Zusätzliche Mechanismen wie Zugriffssteuerungslisten, Einhängeoptionen, Capabilities oder verbindliche Zugriffskontrollen können die endgültige Entscheidung weiter beeinflussen.

Im Beispiel lautet das Tripel des Eigentümers `rwx`, während Gruppe und andere jeweils `r-x` besitzen. Der Eigentümer kann das Verzeichnis lesen, darin schreiben und es durchsuchen. Die Klassen Gruppe und andere können es lesen und durchsuchen, aber über die gewöhnlichen Modusbits des Verzeichnisses keine Einträge erstellen oder entfernen.

:::single-choice{#file-permissions-triplet-order} In welcher Reihenfolge stehen die drei Berechtigungstripel nach dem Dateitypzeichen?

::option[Gruppe, Eigentümer, dann andere.]{#file-permissions-order-group-first explanation="Das Gruppentripel steht an zweiter und nicht an erster Stelle."}
::option[Andere, Gruppe, dann Eigentümer.]{#file-permissions-order-other-first explanation="Das Tripel für andere steht zuletzt und das Eigentümertripel zuerst."}
::option[Eigentümer, Gruppe, dann andere.]{#file-permissions-order-owner-first .correct explanation="Die neun Berechtigungszeichen stellen die Tripel immer in der Reihenfolge Eigentümer, Gruppe und andere dar."}
:::

:::single-choice{#file-permissions-example-group} Welche gewöhnlichen Berechtigungen besitzt die Gruppenklasse in `drwxr-xr-x`?

::option[Lesen und Schreiben.]{#file-permissions-group-read-write explanation="Das Gruppentripel lautet `r-x`, daher enthält seine Schreibposition `-`."}
::option[Schreiben und Ausführen.]{#file-permissions-group-write-execute explanation="Das Gruppentripel enthält an seiner ersten Position `r` und nicht `w`."}
::option[Lesen und Ausführen.]{#file-permissions-group-read-execute .correct explanation="Das mittlere Tripel lautet `r-x` und gewährt damit Lesen und Ausführen, aber kein Schreiben."}
:::

Probiere zur Festigung dieser Konzepte das Lab [Linux-Benutzer, -Gruppen und Dateiberechtigungen](https://labex.io/labs/linux-linux-user-group-and-file-permissions-18002) in einer isolierten Umgebung aus. Darin übst du das Lesen von Modi sowie das Ändern von Eigentum und Berechtigungen.

## Zusammenfassung

Du kannst nun das grundlegende Berechtigungsfeld in einer ausführlichen Linux-Auflistung interpretieren.

1. Trenne das Dateitypzeichen von den neun Berechtigungsbits.
2. Lies `r`, `w` und `x` abhängig davon, ob das Objekt eine Datei oder ein Verzeichnis ist.
3. Unterteile den Modus in Tripel für Eigentümer, Gruppe und andere.
4. Setze die Tripel mit dem von `ls -l` angezeigten Eigentümer und der Gruppe in Beziehung.
