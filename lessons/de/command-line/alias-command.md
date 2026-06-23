---
index: 18
lang: "de"
title: "alias"
meta_title: "alias - Kommandozeile"
meta_description: "Lerne den Linux alias-Befehl mit Beispielen zum Erstellen temporärer Aliase, Speichern von Aliase in .bashrc, Auflisten von Aliase und Entfernen mit unalias."
meta_keywords: "linux alias befehl, alias befehl, bash alias, .bashrc alias, unalias befehl, befehl abkürzung linux, shell alias"
---

## Lesson Content

Das Eintippen langer oder sich wiederholender Befehle kann mühsam sein. Ein Alias ist eine Shell-Abkürzung, mit der du einen eigenen Namen für einen Befehl oder eine Befehlsfolge definieren kannst.

### Erstellen eines temporären Alias

Um einen temporären Alias zu erstellen, der nur für deine aktuelle Terminal-Sitzung gilt, gibst du einfach einen Namen an und setzt ihn gleich dem Befehlsstring.

Beispielsweise erstelle einen Alias namens `ll` für `ls -la`:

```bash
$ alias ll='ls -la'
```

Statt `ls -la` zu tippen, kannst du nun einfach `ll` eingeben, und es wird derselbe Befehl ausgeführt. Das ist eine einfache, aber wirkungsvolle Möglichkeit, deine Shell anzupassen.

### Einen Alias dauerhaft machen

Ein temporärer Alias verschwindet, sobald du dein Terminal schließt oder dein System neu startest. Um einen `command alias in linux` dauerhaft zu machen, musst du ihn in die Konfigurationsdatei deiner Shell eintragen. Für die Bash-Shell ist das üblicherweise die Datei `~/.bashrc`.

1. Öffne die Datei in einem Texteditor: `nano ~/.bashrc`
2. Füge deine Alias-Definition in die Datei ein, genau so, wie du sie in der Kommandozeile eingegeben hast:

```bash
alias ll='ls -la'
alias update='sudo apt update && sudo apt upgrade'
```

3. Speichere die Datei und verlasse den Editor.

Damit die Änderungen wirksam werden, musst du entweder dein Terminal schließen und neu öffnen oder der Shell mitteilen, die Konfigurationsdatei neu zu laden, indem du den Befehl `source` verwendest:

```bash
$ source ~/.bashrc
```

Dein Alias steht nun bei jedem Start einer neuen Bash-Sitzung zur Verfügung.

### Entfernen eines Alias

Wenn du einen Alias nicht mehr benötigst, kannst du ihn mit dem Befehl `unalias` entfernen. Dadurch wird er aus deiner aktuellen Sitzung gelöscht.

```bash
$ unalias ll
```

Um einen permanenten Alias zu entfernen, musst du außerdem die Definition aus deiner `~/.bashrc`-Datei löschen.

### Auflisten vorhandener Aliase

Führe `alias` ohne Argumente aus, um die Aliase in deiner aktuellen Shell aufzulisten.

```bash
$ alias
alias ll='ls -la'
alias grep='grep --color=auto'
```

Verwende `type`, um zu sehen, was ausgeführt wird, wenn du einen Befehl eingibst:

```bash
$ type ll
ll is aliased to 'ls -la'
```

### Nützliche Alias-Beispiele

```bash
$ alias la='ls -la'
$ alias ..='cd ..'
$ alias grep='grep --color=auto'
```

Halte Aliase kurz und vorhersehbar. Vermeide es, destruktive Befehle durch überraschendes Verhalten zu ersetzen, es sei denn, du bist dir sehr sicher.

### Häufige Fragen

**Funktionieren Aliase in Skripten?** Meistens nein, nicht standardmäßig. Skripte sollten vollständige Befehle oder Funktionen verwenden.

**Wo sollten Bash-Aliase abgelegt werden?** Lege sie in `~/.bashrc` für interaktive Bash-Sitzungen.

**Was, wenn ein Alias mit einem echten Befehl kollidiert?** Der Alias hat in der interaktiven Shell normalerweise Vorrang. Verwende `command name` oder `\name`, um einen Alias zu umgehen.

## Exercise

Obwohl es keine spezifischen Labs zu diesem Thema gibt, empfehlen wir, den umfassenden [Linux Learning Path](https://labex.io/de/learn/linux) zu erkunden, um verwandte Linux-Fähigkeiten und Konzepte zu üben.

## Quiz Question

Welcher Befehl wird verwendet, um einen Alias zu erstellen? Bitte antworte in kleingeschriebenem Englisch.

## Quiz Answer

alias
