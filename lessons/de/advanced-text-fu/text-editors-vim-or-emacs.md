---
lesson_id: "text-editors-vim-or-emacs"
course_id: "advanced-text-fu"
lang: "de"
order_index: 2
title: "Texteditoren"
description: "Lerne, einen Terminal-Texteditor für Linux-Administration und Entwicklung auszuwählen und einzurichten."
meta_title: "Texteditoren - Fortgeschrittene Text-Fu"
meta_description: "Erfahren Sie mehr über Linux-Texteditoren wie Vim und Emacs. Entdecken Sie deren Verwendung und Bedeutung für die Systemnavigation. Beginnen Sie Ihre Reise mit Linux-Texteditoren!"
meta_keywords: "Linux-Texteditoren, Vim, Emacs, Linux-Befehle, Linux-Tutorial, Linux für Anfänger, Linux-Anleitung"
---

Linux-Konfigurationen, Skripte, Quellcode und Protokolle werden häufig als Klartext gespeichert. Mit einem Terminaleditor kannst du solche Dateien in einem lokalen Terminal, einer entfernten SSH-Sitzung oder einer Umgebung ohne grafischen Desktop bearbeiten.

## Einen Editor für die Umgebung auswählen

Kein einzelner Editor ist für jede Person und Aufgabe der beste. Grafische Editoren, Terminaleditoren und integrierte Entwicklungsumgebungen können gleichermaßen sinnvoll sein. Wähle für die Kommandozeilenarbeit einen installierten Editor, den du sicher beenden kannst und dessen grundlegendes Bedienmodell du verstehst.

Gehe nicht davon aus, dass Vim oder Emacs installiert ist. Prüfe die Befehlsauflösung der aktuellen Shell:

```bash
$ command -v vim
/usr/bin/vim
$ command -v emacs
/usr/bin/emacs
```

Eine leere Ausgabe mit einem von null verschiedenen Status bedeutet, dass der Name über die aktuelle Befehlssuche nicht gefunden wurde. Minimale Systeme stellen möglicherweise `vi`, andere Nano oder gar keinen interaktiven Editor bereit.

:::single-choice{#editors-check-availability} Welcher Befehl prüft, ob die aktuelle Shell eine ausführbare Datei namens `vim` auflösen kann?

::option[`vim --install`]{#editors-vim-install explanation="Vim verwendet diesen Befehl nicht als portierbare Installationsprüfung; außerdem ist die Paketinstallation distributionsabhängig."}
::option[`file ~/.vimrc`]{#editors-file-vimrc explanation="Dieser Befehl klassifiziert einen Konfigurationspfad, sofern er existiert, bestimmt aber nicht, ob `vim` aufgelöst werden kann."}
::option[`command -v vim`]{#editors-command-v-vim .correct explanation="Das Shell-Builtin prüft die Befehlsauflösung und gibt bei Verfügbarkeit die aufgelöste Form aus."}
:::

## Das Bedienmodell von Vim verstehen

Vim ist ein modaler Editor. Dieselbe Taste kann je nach aktivem Modus verschiedene Bedeutungen haben:

- Der Normalmodus interpretiert Tasten als Navigations- und Bearbeitungsbefehle.
- Der Einfügemodus fügt eingegebenen Text ein.
- Der Befehlszeilenmodus akzeptiert Befehle zum Speichern oder Beenden.

Nach einiger Übung ermöglicht dieses Modell effiziente wiederholte Tastaturbearbeitung. Neue Benutzer müssen jedoch auf den aktiven Modus achten. Die nächsten Lektionen führen Vim schrittweise ein.

:::single-choice{#editors-vim-modal-meaning} Was bedeutet es, dass Vim modal ist?

::option[Jede Datei wird in einem eigenen grafischen Fenster geöffnet.]{#editors-vim-windows explanation="Fenster und Puffer sind eigene Konzepte. „Modal“ beschreibt, wie sich die Tastenbelegung mit dem Editorzustand ändert."}
::option[Vim kann jeweils nur eine Art von Textdatei bearbeiten.]{#editors-vim-file-type explanation="Vim unterstützt viele Dateitypen. „Modal“ beschreibt das Bedienmodell und keine Dateibeschränkung."}
::option[Tasten führen je nach aktivem Modus unterschiedliche Aktionen aus.]{#editors-vim-modes .correct explanation="Eine Taste kann beispielsweise im Normalmodus einen Befehl auslösen, im Einfügemodus aber Text einfügen."}
:::

## Das Bedienmodell von Emacs verstehen

Emacs verwendet häufig Tastenkombinationen und benannte Befehle in einer erweiterbaren Umgebung. Dateien werden in Puffern besucht; Haupt- und Nebenmodi passen das Verhalten an unterschiedliche Inhalte und Aufgaben an. Emacs kann im Terminal oder in einem grafischen Frame laufen.

Vim und Emacs unterstützen über Konfiguration und Erweiterungen weit mehr als einfache Textbearbeitung. Beginne mit dem Öffnen, Ändern, Speichern und Schließen einer Klartextdatei, bevor du Anpassungen hinzufügst.

:::single-choice{#editors-emacs-buffer} Wo wird der bearbeitbare Text einer besuchten Datei in der Emacs-Terminologie normalerweise gehalten?

::option[In einem Puffer.]{#editors-emacs-buffer-answer .correct explanation="Emacs besucht eine Datei in einem Puffer, der den angezeigten oder bearbeiteten Text enthält."}
::option[In der Aliastabelle der Shell.]{#editors-emacs-alias-table explanation="Aliase gehören zur Befehlsauflösung der Shell und speichern keinen Editortext."}
::option[Ausschließlich im Scrollback des Terminals.]{#editors-emacs-scrollback explanation="Der Terminal-Scrollback zeichnet angezeigte Ausgaben auf; Emacs verwaltet bearbeitbaren Text in Puffern."}
:::

## Einen bevorzugten Editor festlegen

Viele Kommandozeilenprogramme berücksichtigen `VISUAL` oder `EDITOR`, wenn sie einen Editor starten müssen. So wählst du Vim für Befehle der aktuellen Bash-Sitzung und ihrer Kindprozesse:

```bash
$ export VISUAL=vim
$ export EDITOR="$VISUAL"
```

Diese Variablen drücken eine Präferenz aus; das Programm wird dadurch nicht installiert. Verwende einen tatsächlich vorhandenen Befehl und trage die Exporte erst nach einem Test in die passende Shell-Startdatei ein.

:::single-choice{#editors-editor-variable} Was bewirkt `export EDITOR=vim`?

::option[Der Befehl teilt künftigen Kindprozessen mit, dass `vim` der bevorzugte Editorwert ist.]{#editors-export-preference .correct explanation="Durch den Export wird die Präferenz Teil der Umgebung, die von der aktuellen Shell gestartete Befehle erben."}
::option[Der Befehl installiert Vim für alle Benutzer des Systems.]{#editors-install-vim explanation="Eine Umgebungsvariablenzuweisung installiert keine Pakete und verändert nicht die Systeme anderer Benutzer."}
::option[Der Befehl zwingt jedes Programm, die Tastenkürzel von Vim zu verwenden.]{#editors-global-bindings explanation="Programme können die Variable zum Starten eines Editors auswerten; ihr eigenes Bedienmodell wird dadurch nicht ersetzt."}
:::

## Ohne Risiko für wichtige Dateien üben

Lerne mit einer entbehrlichen Datei in einem Verzeichnis, das dir gehört:

```bash
$ printf 'first line\nsecond line\n' > editor-practice.txt
$ vim editor-practice.txt
```

Beginne nicht mit einer Systemkonfiguration oder Daten anderer Benutzer. Lege vor dem Ändern einer wichtigen Datei eine Sicherung an, verstehe das Speichern und Beenden und prüfe das Ergebnis mit einem schreibgeschützten Befehl wie `cat` oder `diff`.

:::single-choice{#editors-first-practice-file} Welche Datei ist zum ersten Üben mit einem unbekannten Editor am sichersten?

::option[Eine kritische Startkonfiguration, die als root geöffnet wurde.]{#editors-boot-file explanation="Eine versehentliche Änderung kann den normalen Systemstart verhindern; erhöhte Rechte vergrößern die Folgen eines Fehlers."}
::option[Eine entbehrliche Textdatei in einem eigenen Verzeichnis.]{#editors-disposable-file .correct explanation="Eine Übungsdatei begrenzt die Folgen versehentlicher Änderungen beim Erlernen von Navigation, Speichern und Beenden."}
::option[Eine gemeinsam genutzte Produktionsdatei ohne Sicherung.]{#editors-production-file explanation="Ungeprüftes Üben an gemeinsamen Daten kann andere stören und bietet keinen einfachen Wiederherstellungsweg."}
:::

Mit dieser Übung kannst du die Arbeit mit Terminal-Texteditoren praktisch trainieren:

1. **[Textdateien in Linux mit Vim und Nano bearbeiten](https://labex.io/de/labs/comptia-edit-text-files-in-linux-with-vim-and-nano-591076)** – Erstelle Dateien, bearbeite und speichere Text und navigiere sowohl mit vi/Vim als auch mit Nano.

## Zusammenfassung

Du kannst nun einen Terminaleditor auswählen und einen sicheren Übungsablauf vorbereiten.

1. Prüfe, ob ein Editorbefehl verfügbar ist.
2. Erkenne das modale Bedienmodell von Vim.
3. Erkenne Emacs-Puffer und erweiterbare Modi.
4. Setze eine Editorpräferenz, ohne sie mit einer Installation zu verwechseln.
5. Übe an entbehrlichem Text, bevor du wichtige Dateien bearbeitest.
