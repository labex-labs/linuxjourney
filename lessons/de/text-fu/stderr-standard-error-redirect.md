---
lesson_id: "stderr-standard-error-redirect"
course_id: "text-fu"
lang: "de"
order_index: 3
title: "stderr (Standardfehler)"
description: "Lerne, die Standardfehlerausgabe in Bash getrennt umzuleiten oder mit der Standardausgabe zusammenzuführen."
meta_title: "stderr (Standardfehler) - Text-Fu"
meta_description: "Erfahren Sie, wie Sie Standardfehler (stderr) unter Linux verwalten. Dieser Leitfaden behandelt stderr-Umleitung, den stderr-Dateideskriptor (2) und wie man stderr mithilfe von 2>, 2>&1 und &> in eine Datei oder nach /dev/null umleitet."
meta_keywords: "stderr, Standardfehler Linux, stderr Dateideskriptor, stderr Datei, Linux Standardfehler, stderr umleiten, 2>, 2>&1, &>, /dev/null, Bash Fehlerbehandlung"
---

Programme schreiben reguläre Ergebnisse normalerweise in die Standardausgabe und Diagnosen in einen getrennten Strom namens Standardfehlerausgabe oder **stderr**. Durch die Trennung kannst du nützliche Daten speichern, ohne Fehlermeldungen mit ihnen zu vermischen.

## Reguläre Ausgabe und Fehler trennen

Betrachte einen Befehl mit einem nicht vorhandenen Pfad:

```bash
$ ls /fake/directory > peanuts.txt
ls: cannot access '/fake/directory': No such file or directory
```

Der Operator `>` leitet nur stdout um. Die Diagnose wird nach stderr geschrieben, das weiterhin mit dem Terminal verbunden ist. Gleichzeitig erstellt oder leert die Shell `peanuts.txt` für stdout, obwohl `ls` kein reguläres Ergebnis erzeugt.

Die Standardströme verwenden konventionsgemäß diese Dateideskriptoren:

- `0`: stdin (Standardeingabe)
- `1`: stdout (Standardausgabe)
- `2`: stderr (Standardfehlerausgabe)

:::single-choice{#stderr-not-in-stdout-file}
Warum bleibt der Fehler von `ls /missing > results.txt` normalerweise im Terminal sichtbar?

::option[`>` leitet stdout um, während die Diagnose nach stderr geschrieben wird.]{#stderr-separate-stream .correct explanation="Ein einfaches `>` verändert nur Dateideskriptor 1. Dateideskriptor 2 behält sein bisheriges Ziel, das Terminal."}
::option[`ls` wartet mit der Fehlerausgabe, bis die Datei geschlossen wurde.]{#stderr-waits-for-close explanation="Es geht nicht um den Zeitpunkt. Reguläre Ausgaben und Diagnosen verwenden unterschiedliche Ausgabeströme."}
::option[`results.txt` kann normalen Text, aber keine Diagnosen speichern.]{#stderr-file-capability explanation="Eine gewöhnliche Datei kann beide Ströme speichern. In der Befehlszeile wurde stderr lediglich nicht dorthin umgeleitet."}
:::

## stderr mit 2> umleiten

Setze den Dateideskriptor `2` vor `>`, um stderr umzuleiten:

```bash
$ ls /fake/directory 2> errors.txt
```

Die Shell erstellt oder leert `errors.txt` und verbindet die Datei mit Deskriptor 2. Stdout behält sein bisheriges Ziel. Verwende stattdessen `2>> errors.txt`, wenn Fehlerausgaben angehängt werden sollen.

:::single-choice{#stderr-to-error-file}
Welcher Befehl ersetzt `errors.log` durch Diagnosen von `find /restricted`, während stdout mit seinem bisherigen Ziel verbunden bleibt?

::option[`find /restricted > errors.log`]{#stdout-errors-log explanation="Ein einfaches `>` leitet Deskriptor 1 um und erfasst damit reguläre Ergebnisse statt gezielt Diagnosen."}
::option[`find /restricted < errors.log`]{#stdin-errors-log explanation="Das Kleiner-als-Zeichen stellt die Datei als stdin bereit. Keiner der Ausgabeströme wird damit erfasst."}
::option[`find /restricted 2> errors.log`]{#stderr-errors-log .correct explanation="Die vorangestellte `2` wählt stderr aus; `>` erstellt oder leert das Ziel für diesen Strom."}
:::

## stdout und stderr zusammenführen

Um beide Ausgabeströme in eine Datei zu schreiben, leitest du zuerst stdout um und duplizierst danach stderr auf das aktuelle Ziel von stdout:

```bash
$ ls /fake/directory /etc/passwd > combined.txt 2>&1
```

Umleitungen werden von links nach rechts verarbeitet:

1. `> combined.txt` verbindet stdout mit der Datei.
2. `2>&1` verbindet stderr mit dem Ziel, auf das stdout in diesem Moment zeigt.

Eine umgekehrte Reihenfolge ändert das Ergebnis:

```bash
$ ls /fake/directory /etc/passwd 2>&1 > regular.txt
```

Hier dupliziert stderr zuerst das ursprüngliche Terminalziel von stdout. Danach wird nur stdout nach `regular.txt` verschoben; die Ströme enden an unterschiedlichen Orten.

:::single-choice{#stderr-combine-order}
Welche Bash-Umleitung sendet stdout und stderr von `command` gemeinsam nach `all.log`?

::option[`command 2>&1 > all.log`]{#stderr-before-stdout explanation="Damit wird stderr zuerst mit dem alten stdout-Ziel verbunden und anschließend nur stdout in die Datei umgeleitet. Die Ströme bleiben getrennt."}
::option[`command 2> all.log > /dev/null`]{#stderr-file-stdout-null explanation="Dieser Befehl sendet stderr nach `all.log`, verwirft aber stdout. Beide Ströme werden nicht in der Datei zusammengeführt."}
::option[`command > all.log 2>&1`]{#stdout-then-stderr .correct explanation="Zuerst wird stdout mit der Datei verbunden; anschließend dupliziert stderr dieses aktuelle stdout-Ziel."}
:::

Bash bietet mit `&>` außerdem eine kürzere Syntax, um eine Datei durch beide Ströme zu ersetzen:

```bash
$ ls /fake/directory /etc/passwd &> combined.txt
```

Mit `&>>` hängst du beide Ströme in Bash an. Die ausdrückliche Form `> file 2>&1` solltest du ebenfalls erkennen, da sie häufig in Shell-Skripten und Dokumentationen vorkommt.

:::single-choice{#stderr-bash-short-form}
Welcher Bash-Befehl hängt stdout und stderr von `build` gemeinsam an `build.log` an?

::option[`build &> build.log`]{#replace-both-build explanation="Bash `&>` leitet beide Ströme um, ersetzt aber eine vorhandene Datei, statt an sie anzuhängen."}
::option[`build 2>> build.log`]{#append-errors-build explanation="Damit wird nur stderr angehängt. Stdout behält sein bisheriges Ziel."}
::option[`build &>> build.log`]{#append-both-build .correct explanation="In Bash hängt `&>>` die Dateideskriptoren 1 und 2 an dasselbe Ziel an."}
:::

## Einen Strom bewusst verwerfen

`/dev/null` ist ein besonderes Gerät, das alle hineingeschriebenen Daten verwirft. Leite stderr nur dann dorthin um, wenn du festgestellt hast, dass die Diagnosen erwartet und entbehrlich sind:

```bash
$ ls /fake/directory 2> /dev/null
```

Dadurch wird der Befehl weder erfolgreich noch sein Beendigungsstatus verändert; lediglich der Diagnosestrom bleibt unsichtbar. Bei der Fehlersuche solltest du stderr bewahren oder anzeigen, statt benötigte Informationen zu verwerfen.

:::single-choice{#stderr-dev-null-effect}
Was verändert `check-data 2> /dev/null`?

::option[Der Befehl verwirft stdout und macht aus jedem Fehler einen Erfolg.]{#discard-stdout-success explanation="Deskriptor 2 ist stderr, nicht stdout, und eine Umleitung verändert den Beendigungsstatus des Programms nicht."}
::option[Der Befehl verwirft stderr, erzwingt aber keinen erfolgreichen Beendigungsstatus.]{#discard-stderr-only .correct explanation="Die Umleitung verändert das Ziel der Diagnosen. Erfolg oder Misserfolg bestimmt weiterhin das Programm selbst."}
::option[Der Befehl speichert stderr in einer versteckten Datei namens `/dev/null`.]{#save-dev-null explanation="`/dev/null` verwirft geschriebene Daten; es ist keine Speicherdatei, aus der sie später wiederhergestellt werden können."}
:::

Mit dieser Übung kannst du die Verwaltung aller drei Standardströme praktisch trainieren:

1. **[Umleitung von Eingabe und Ausgabe in Linux](https://labex.io/de/labs/comptia-redirecting-input-and-output-in-linux-590840)** – Steuere den Datenfluss von Befehlen, indem du Standardausgabe, Standardfehler und Standardeingabe mit Operatoren wie >, >> und 2> sowie dem Befehl tee umleitest.

## Zusammenfassung

Du kannst nun Diagnosen getrennt halten oder mit regulären Befehlsausgaben zusammenführen.

1. Erkenne stderr als Dateideskriptor 2.
2. Ersetze oder ergänze ein Fehlerprotokoll mit `2>` oder `2>>`.
3. Verarbeite mehrere Umleitungen von links nach rechts.
4. Führe beide Ausgabeströme mit bewusst gewählter Syntax zusammen.
5. Verwirf Diagnosen nur, wenn ihr Verlust vertretbar ist.
