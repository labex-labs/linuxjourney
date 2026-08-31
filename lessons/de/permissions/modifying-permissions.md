---
lesson_id: "modifying-permissions"
course_id: "permissions"
lang: "de"
order_index: 2
title: "Berechtigungen ändern"
description: "Erfahre, wie du Linux-Berechtigungsbits mit symbolischen und oktalen `chmod`-Modi änderst."
meta_title: "Berechtigungen ändern – Berechtigungen"
meta_description: "Erfahre, wie du Berechtigungen unter Linux mit dem Befehl chmod änderst. Dieser Leitfaden behandelt symbolische und numerische Methoden, damit du den Zugriff auf Dateien und Verzeichnisse sicher verwalten kannst. Beherrsche das Ändern von Linux-Berechtigungen für eine bessere Systemadministration."
meta_keywords: "Linux-Berechtigungen ändern, Berechtigung unter Linux ändern, Berechtigungen unter Linux ändern, Dateiberechtigungen unter Linux ändern, chmod, Dateiberechtigungen, Linux-Sicherheit, symbolische Berechtigungen, numerische Berechtigungen"
---

Der Befehl `chmod` ändert die Modusbits von Dateien und Verzeichnissen. Gewöhnlich kann dies nur der Dateieigentümer oder ein Prozess mit den erforderlichen Rechten tun. Prüfe den aktuellen Modus vor und nach der Ausführung von `chmod` mit `ls -l`.

## Den symbolischen Modus verwenden

Ein symbolischer Modus gibt an, welche Berechtigungsklasse geändert werden soll, wie sie geändert wird und welche Berechtigungen betroffen sind.

- `u` wählt die Eigentümerklasse aus.
- `g` wählt die Gruppenklasse aus.
- `o` wählt die Klasse für andere aus.
- `a` wählt alle drei Klassen aus.
- `+` fügt Berechtigungen hinzu, `-` entfernt sie und `=` setzt die ausgewählte Klasse exakt.

Füge beispielsweise die Ausführungsberechtigung für den Eigentümer hinzu:

```bash
$ chmod u+x myfile
```

Entferne die Schreibberechtigung der Gruppe:

```bash
$ chmod g-w myfile
```

Füge die Schreibberechtigung für Eigentümer und Gruppe hinzu:

```bash
$ chmod ug+w myfile
```

Mehrere Klauseln können durch Kommas getrennt werden. Dieser Befehl setzt den Eigentümer auf Lesen und Schreiben, die Gruppe auf ausschließlich Lesen und andere auf keine Berechtigungen:

```bash
$ chmod u=rw,g=r,o= myfile
```

Wenn die Klasse wie in `chmod +x myfile` weggelassen wird, beeinflusst die umask des Prozesses, welche Klassen geändert werden. Die ausdrückliche Angabe der Klasse macht das beabsichtigte Ergebnis leichter überprüfbar.

:::single-choice{#modifying-permissions-remove-group-write}
Welcher symbolische Modus entfernt die Schreibberechtigung der Gruppe, ohne deren andere Bits zu ändern?

::option[`chmod u-w myfile`]{#modifying-permissions-user-minus-write explanation="Dies entfernt die Schreibberechtigung der Eigentümerklasse und nicht der Gruppenklasse."}
::option[`chmod g-w myfile`]{#modifying-permissions-group-minus-write .correct explanation="Das `g` wählt die Gruppenklasse aus, `-` entfernt ein Bit und `w` bezeichnet die Schreibberechtigung."}
::option[`chmod g=w myfile`]{#modifying-permissions-group-equals-write explanation="Der Operator `=` ersetzt die ausgewählte Klasse durch eine reine Schreibberechtigung, statt die Schreibberechtigung zu entfernen."}
:::

## Den oktalen Modus verwenden

Ein oktaler Modus legt jedes grundlegende Berechtigungstripel mit einer Ziffer fest. Addiere innerhalb jeder Klasse diese Werte:

- `4` für Lesen
- `2` für Schreiben
- `1` für Ausführen
- `0` für keine Berechtigungen

Die drei Ziffern ganz rechts stehen in dieser Reihenfolge für Eigentümer, Gruppe und andere. Zum Beispiel:

```bash
$ chmod 755 myfile
```

Der Modus `755` wird wie folgt aufgeschlüsselt:

- Eigentümer `7` ist `4 + 2 + 1` oder `rwx`.
- Gruppe `5` ist `4 + 1` oder `r-x`.
- Andere `5` ist `4 + 1` oder `r-x`.

Anders als symbolische Operationen mit `+` oder `-` gibt ein oktaler Modus den vollständigen gewöhnlichen Berechtigungssatz an. Eine spätere Lektion behandelt die optionale führende Ziffer für besondere Modusbits.

:::single-choice{#modifying-permissions-octal-read-value}
Welcher oktale Wert steht für die Leseberechtigung?

::option[`1`]{#modifying-permissions-value-one explanation="Der Wert `1` steht für die Ausführungsberechtigung."}
::option[`2`]{#modifying-permissions-value-two explanation="Der Wert `2` steht für die Schreibberechtigung."}
::option[`4`]{#modifying-permissions-value-four .correct explanation="Die Leseberechtigung trägt den oktalen Wert `4` zur Ziffer einer Klasse bei."}
:::

:::single-choice{#modifying-permissions-mode-640}
Welche gewöhnlichen Berechtigungen setzt `chmod 640 report`?

::option[Eigentümer lesen, Gruppe schreiben, andere ausführen.]{#modifying-permissions-640-separated explanation="Oktale Ziffern sind Summen für jede Klasse und keine getrennten Spalten für Lesen, Schreiben und Ausführen."}
::option[Eigentümer lesen/ausführen, Gruppe schreiben, andere keine.]{#modifying-permissions-640-wrong-sums explanation="Der Eigentümerwert `6` bedeutet Lesen plus Schreiben, während der Gruppenwert `4` Lesen bedeutet."}
::option[Eigentümer lesen/schreiben, Gruppe lesen, andere keine.]{#modifying-permissions-640-correct .correct explanation="Die Ziffern ergeben Eigentümer `6` (`rw-`), Gruppe `4` (`r--`) und andere `0` (`---`)."}
:::

## Änderungen sicher anwenden

Gewähre nur den Zugriff, den Benutzer und Dienste benötigen. Vermeide `chmod 777` als schnelle Abhilfe bei Zugriffsproblemen, da es jeder Klasse Lese-, Schreib- und Ausführungsberechtigungen gewährt. Das schafft häufig zusätzliche Risiken, ohne Probleme mit Eigentum, Verzeichnisdurchquerung, ACLs oder Dienstrichtlinien zu lösen.

Rekursive Änderungen erfordern besondere Vorsicht. Zeige den Zielbaum vorab an, berücksichtige symbolische Links und eingehängte Dateisysteme und teste in einem kleinen Umfang, bevor du `chmod -R` verwendest. Überprüfe nach einer Änderung den resultierenden Modus, statt anzunehmen, der Befehl habe die beabsichtigten Objekte beeinflusst.

:::single-choice{#modifying-permissions-least-privilege}
Warum ist `chmod 777` gewöhnlich eine schlechte allgemeine Lösung für ein Zugriffsproblem?

::option[Es entfernt alle Berechtigungen des Eigentümers.]{#modifying-permissions-777-removes explanation="Jede `7` gewährt Lesen, Schreiben und Ausführen; sie entfernt keine Eigentümerberechtigungen."}
::option[Es gewährt Eigentümer, Gruppe und anderen jede grundlegende Berechtigung.]{#modifying-permissions-777-grants-all .correct explanation="Alle drei Klassen erhalten `rwx`, was den tatsächlich erforderlichen Zugriff häufig übersteigt."}
::option[Es ändert ausschließlich den Gruppeneigentümer der Datei.]{#modifying-permissions-777-group explanation="`chmod` ändert Modusbits; Gruppeneigentum wird mit einem Werkzeug wie `chgrp` oder `chown` geändert."}
:::

Nutze für praktische Übungen in einer isolierten Umgebung das Lab [Linux-Benutzer, -Gruppen und Dateiberechtigungen](https://labex.io/labs/linux-linux-user-group-and-file-permissions-18002) und prüfe jeden Modus vor und nach seiner Änderung.

## Zusammenfassung

Du kannst nun gewöhnliche Linux-Modusbits mit gezielten `chmod`-Ausdrücken ändern.

1. Verwende den symbolischen Modus für gezielte Ergänzungen, Entfernungen oder Zuweisungen.
2. Bilde oktale Ziffern aus Lesen `4`, Schreiben `2` und Ausführen `1`.
3. Lies oktale Klassen in der Reihenfolge Eigentümer, Gruppe und andere.
4. Überprüfe Änderungen und gewähre nur die mindestens erforderlichen Rechte.
