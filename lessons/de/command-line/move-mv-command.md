---
lesson_id: "move-mv-command"
course_id: "command-line"
lang: "de"
order_index: 11
title: "mv (Verschieben)"
description: "Lerne, Dateien und Verzeichnisse umzubenennen oder zu verschieben, ohne unbeabsichtigt Ziele zu überschreiben."
meta_title: "mv (Verschieben) - Kommandozeile"
meta_description: "Lernen Sie den Linux-Befehl mv mit Beispielen zum Verschieben von Dateien, Umbenennen von Dateien und Verzeichnissen, Verschieben mehrerer Dateien und Vermeidung von Überschreibungen."
meta_keywords: "linux mv befehl, mv befehl, dateien verschieben linux, datei umbenennen linux, verzeichnis umbenennen linux, mv -i, mv -n, mv -t"
---

Der Befehl `mv` benennt eine Datei oder ein Verzeichnis um oder verschiebt das Element an einen anderen Ort. Im Gegensatz zu `cp` lässt er den ursprünglichen Pfad nach einem erfolgreichen Verschieben nicht bestehen.

Die grundlegende Syntax lautet:

```bash
mv [OPTIONS] SOURCE DESTINATION
```

## Dateien und Verzeichnisse umbenennen

Zum Umbenennen setzt du zuerst den aktuellen und danach den neuen Pfad.

Eine Datei benennst du so um:

```bash
$ mv oldfile newfile
```

Mit derselben Operandenreihenfolge benennst du ein Verzeichnis um:

```bash
$ mv old_directory_name new_directory_name
```

:::single-choice{#rename-file-with-mv} Welcher Befehl benennt `cat` im aktuellen Verzeichnis in `dog` um?

::option[`mv cat dog`]{#rename-cat .correct explanation="`mv` behandelt `cat` als Quellpfad und `dog` als seinen neuen Zielpfad."}
::option[`mv dog cat`]{#rename-dog explanation="Hier sind die Operanden vertauscht. Der Befehl würde versuchen, ein vorhandenes `dog` in `cat` umzubenennen."}
::option[`cp cat dog`]{#copy-cat explanation="`cp` würde eine Kopie namens `dog` erstellen und `cat` erhalten. Die verlangte Umbenennung fände nicht statt."}
:::

## Elemente in ein Verzeichnis verschieben

Ist der letzte Operand ein vorhandenes Verzeichnis, legt `mv` die Quelle darin ab:

```bash
$ mv file2 /home/pete/Documents
```

Für mehrere Quellen führst du diese zuerst auf und setzt das Zielverzeichnis ans Ende:

```bash
$ mv file_1 file_2 somedirectory/
```

GNU `mv` bietet außerdem `-t`, um das Zielverzeichnis vor den Quellen anzugeben:

```bash
$ mv -t somedirectory/ file_1 file_2
```

Anders als `cp` benötigt `mv` für ein Verzeichnis keine rekursive Option.

:::single-choice{#move-multiple-files} Welcher Befehl verschiebt `file_1` und `file_2` in das vorhandene Verzeichnis `archive/`?

::option[`mv archive/ file_1 file_2`]{#target-first-without-option explanation="Ohne GNU-Option `-t` erwartet ein Verschieben mehrerer Quellen das Zielverzeichnis am Ende. Diese Reihenfolge entspricht nicht der üblichen Form."}
::option[`mv -r file_1 file_2 archive/`]{#recursive-move explanation="`mv` verwendet zum Verschieben von Dateien oder Verzeichnissen kein `-r`. Die normale Form für mehrere Quellen erledigt den Vorgang bereits."}
::option[`mv file_1 file_2 archive/`]{#target-last .correct explanation="Bei mehreren Quellen steht das vorhandene Zielverzeichnis als letzter Operand und nimmt beide Dateien auf."}
:::

## Vorhandene Ziele behandeln

Standardmäßig kann `mv` ein vorhandenes Ziel ersetzen. Prüfe Quell- und Zielpfade vor dem Verschieben und wähle bei Bedarf eine Überschreibungsregel:

- `-i`: Fragt vor dem Ersetzen eines vorhandenen Ziels nach.

  ```bash
  $ mv -i source_file destination_directory
  ```

- `-n`: Überschreibt kein vorhandenes Ziel.

  ```bash
  $ mv -n source_file destination_directory
  ```

- `-b`: Erstellt unter GNU/Linux eine Sicherung des Ziels, das andernfalls ersetzt würde. Das Standardsuffix ist üblicherweise `~`.

  ```bash
  $ mv -b file1 directory_with_file1
  ```

- `-v`: Gibt jeden Verschiebevorgang aus.

```bash
$ mv -v file1 file2 somedirectory/
```

:::single-choice{#move-without-overwriting} Welcher Befehl verschiebt `draft.txt` nur dann nach `finished/`, wenn dabei kein vorhandenes Ziel überschrieben wird?

::option[`mv -i draft.txt finished/`]{#interactive-draft explanation="Die Option `-i` fragt bei einem vorhandenen Ziel nach. Bestätigt der Benutzer, kann es dennoch überschrieben werden."}
::option[`mv -b draft.txt finished/`]{#backup-draft explanation="Die Option `-b` erlaubt das Ersetzen und bewahrt das frühere Ziel als Sicherung. Sie verhindert die Überschreibung nicht."}
::option[`mv -n draft.txt finished/`]{#no-clobber-draft .correct explanation="Die Option `-n` überspringt einen Verschiebevorgang, der ein vorhandenes Ziel überschreiben würde."}
:::

## Verzeichnisse und Platzhaltertreffer verschieben

Ein Verzeichnis lässt sich ohne `-r` verschieben:

```bash
$ mv project /home/pete/Documents/
```

Shell-Platzhalter können mehrere Quellen auswählen:

```bash
$ ls *.txt
$ mv *.txt notes/
```

Wenn du die Treffer vorher mit `ls` prüfst, kannst du ein zu weit gefasstes Muster erkennen, bevor du mehrere Pfade veränderst.

:::single-choice{#move-directory-without-recursion} Welcher Befehl verschiebt das Verzeichnis `project/` nach `/srv/archive/`?

::option[`mv -r project/ /srv/archive/`]{#recursive-project explanation="`mv` benötigt und unterstützt für diesen Zweck kein `-r`. Verzeichnisse werden vom gewöhnlichen Verschiebevorgang erfasst."}
::option[`mv project/ /srv/archive/`]{#move-project .correct explanation="Die normale `mv`-Syntax verschiebt ein Verzeichnis ohne rekursives Flag in ein vorhandenes Zielverzeichnis."}
::option[`cp project/ /srv/archive/`]{#copy-project explanation="Ein einfaches `cp` verschiebt das Verzeichnis nicht und bräuchte zum Kopieren eine rekursive Option. Außerdem bliebe das Original erhalten."}
:::

:::single-choice{#preview-text-file-move} Du möchtest `mv *.txt notes/` ausführen. Welcher Befehl zeigt zuvor die vom selben Platzhalter ausgewählten Pfade an?

::option[`ls '*.txt'`]{#literal-text-pattern explanation="Die Anführungszeichen verhindern, dass die Shell `*` erweitert. So wird nach einem wörtlichen Namen mit Sternchen gesucht, statt die Verschiebemenge anzuzeigen."}
::option[`ls *.txt`]{#list-text-matches .correct explanation="Die Shell erweitert `*.txt` für `ls` genauso wie für `mv`, sodass du die ausgewählten nicht versteckten Namen zuerst prüfen kannst."}
::option[`mv -v *.txt notes/`]{#verbose-text-move explanation="Der ausführliche Modus meldet Verschiebungen während ihrer Ausführung. Er führt den Vorgang aus, statt nur eine Vorschau zu zeigen."}
:::

Mit diesen Übungen kannst du das Verschieben und Umbenennen praktisch trainieren:

1. **[Linux mv Command: File Moving and Renaming](https://labex.io/de/labs/linux-linux-mv-command-file-moving-and-renaming-209743)** – Verschiebe und benenne Dateien sowie Verzeichnisse mit `mv` um und lerne seine Optionen und Verhaltensweisen kennen.
2. **[Organizing Files and Directories](https://labex.io/de/labs/linux-organizing-files-and-directories-387877)** – Organisiere mit `mv`, `cp` und `rm` eine Projektstruktur, verschiebe Dateien und räume Verzeichnisse auf.

## Zusammenfassung

Du kannst nun Dateien und Verzeichnisse umbenennen oder verschieben und vorhandene Ziele schützen.

1. Setze die Quelle vor ihren neuen Pfad.
2. Stelle bei mehreren Quellen das Zielverzeichnis ans Ende.
3. Frage nach, überspringe oder sichere, bevor ein Ziel ersetzt wird.
4. Verschiebe Verzeichnisse ohne rekursive Option.
5. Prüfe Platzhaltertreffer vor einer umfangreichen Verschiebung.
