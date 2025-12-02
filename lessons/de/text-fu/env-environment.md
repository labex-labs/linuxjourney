---
index: 5
lang: "de"
title: "env (Umgebung)"
meta_title: "env (Umgebung) - Text-Fu"
meta_description: "Erfahren Sie, was der env-Befehl in Linux bewirkt. Diese Anleitung erklärt, wie Sie Linux-Umgebungsvariablen wie PATH, HOME und USER mit dem env-Linux-Befehl anzeigen und verwenden."
meta_keywords: "env, linux env, env linux, env befehl linux, linux env befehl, was macht env in linux, umgebungsvariablen, PATH variable, shell variablen"
---

## Lesson Content

Ihr Linux-System verwendet Umgebungsvariablen, um Informationen zu speichern, auf die die Shell und andere Prozesse zugreifen können. Diese Variablen enthalten nützliche Daten zu Ihrer Benutzersitzung und Systemkonfiguration.

### Grundlegende Umgebungsvariablen untersuchen

Sie können den Wert einer bestimmten Variablen anzeigen, indem Sie deren Namen ein `$`-Symbol voranstellen. Führen Sie zum Beispiel den folgenden Befehl aus:

```bash
echo $HOME
```

Dieser Befehl zeigt den Pfad zu Ihrem Home-Verzeichnis an, der etwa so aussehen könnte: `/home/pete`.

Versuchen Sie nun Folgendes:

```bash
echo $USER
```

Dies gibt Ihren aktuellen Benutzernamen aus. Aber woher stammen diese Informationen? Sie sind in der Umgebung Ihrer Shell gespeichert.

### Was macht env unter Linux

Um alle Umgebungsvariablen anzuzeigen, die derzeit für Ihre Sitzung festgelegt sind, können Sie den Befehl `env` verwenden. Der `linux env command` ist ein grundlegendes Werkzeug zur Überprüfung der Konfiguration Ihrer Shell.

```bash
env
```

Wenn Sie den Befehl `env` ausführen, wird eine Liste von Schlüssel-Wert-Paaren ausgegeben. Hier ist ein kurzes Beispiel dafür, was Sie sehen könnten:

```plaintext
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/bin
PWD=/home/user
USER=pete
```

Das Verständnis von `linux env` ist entscheidend für die effektive Verwaltung Ihres Systems.

### Die Bedeutung der PATH-Variable

Eine der wichtigsten Variablen in Ihrer `env linux`-Ausgabe ist `PATH`. Sie können deren Inhalt gezielt mit folgendem Befehl anzeigen:

```bash
echo $PATH
```

Dieser Befehl gibt eine durch Doppelpunkte getrennte Liste von Verzeichnissen zurück. Wenn Sie einen Befehl eingeben, durchsucht Ihr System diese Verzeichnisse, um die entsprechende ausführbare Datei zu finden.

Stellen Sie sich vor, Sie installieren manuell ein Programm in einem nicht standardmäßigen Verzeichnis wie `/opt/coolapp/bin`. Wenn Sie versuchen, es auszuführen, indem Sie `coolcommand` eingeben, erhalten Sie möglicherweise eine Fehlermeldung „command not found“. Dies geschieht, weil das Verzeichnis, das Ihr Programm enthält, nicht in der `PATH`-Variable aufgeführt ist, sodass die Shell nicht weiß, wo sie danach suchen soll.

Um dies zu beheben, können Sie die `PATH`-Variable ändern, um das neue Verzeichnis einzuschließen. Indem Sie Ihr benutzerdefiniertes Verzeichnis zu `PATH` hinzufügen, ermöglichen Sie der Shell, Ihre Programme von überall im Terminal aus zu finden und auszuführen.

### Festlegen einer Umgebungsvariable für die aktuelle Sitzung

Der folgende Befehl im Terminal legt die Umgebungsvariable `TEST` nur für die aktuelle Sitzung fest:

```bash
export TEST=test
```

Danach, wenn Sie ausführen:

```bash
echo $TEST
```

wird die Ausgabe sein:

```
test
```

Diese Variable ist verfügbar, solange die Terminalsitzung geöffnet bleibt. Sobald Sie das Terminal schließen und erneut öffnen, existiert die Variable nicht mehr.

### Die Umgebungsvariable sitzungsübergreifend persistent machen

Wenn die Umgebungsvariable in jeder Terminalsitzung verfügbar sein soll (auch nach dem Schließen und erneuten Öffnen des Terminals), müssen Sie sie zur Startdatei Ihrer Shell hinzufügen. Im Falle von Bash (der Standard-Shell für viele Linux-Distributionen und macOS) ist diese Datei normalerweise `.bashrc` in Ihrem Home-Verzeichnis.

Hier erfahren Sie, wie Sie dies tun:

1. Öffnen Sie `.bashrc` in Ihrem bevorzugten Texteditor. Zum Beispiel:

```bash
nano ~/.bashrc
```

2. Fügen Sie die `export`-Zeile am Ende der Datei hinzu:

```bash
export TEST=test
```

3. Speichern und beenden Sie den Editor (in Nano wäre dies `Strg+X`, dann `J` zur Bestätigung und `Enter`).

4. Um die Änderungen sofort anzuwenden, ohne das Terminal erneut öffnen zu müssen, führen Sie Folgendes aus:

```bash
source ~/.bashrc
```

Danach ist die Variable `TEST` in allen zukünftigen Terminalsitzungen verfügbar, und die Ausführung von `echo $TEST` gibt `test` aus, auch nachdem Sie das Terminal geschlossen und erneut geöffnet haben.

### Ein Hinweis zu Shell-Konfigurationsdateien

- Für **Bash** (Standard auf vielen Systemen) ist die relevante Datei `~/.bashrc` für nicht-anmeldende interaktive Shells.
- Für **Zsh** ist die entsprechende Datei normalerweise `~/.zshrc`.
- Für **Fish** würden Sie typischerweise `~/.config/fish/config.fish` verwenden.

## Exercise

Übung macht den Meister! Hier sind einige praktische Übungen, um Ihr Verständnis von Linux-Umgebungsvariablen zu festigen:

1. **[Shell-Umgebung und Konfiguration in Linux verwalten](https://labex.io/de/labs/comptia-manage-shell-environment-and-configuration-in-linux-590838)** - Üben Sie das Erstellen und Verwalten lokaler Variablen und Umgebungsvariablen, das Verständnis der Vererbung und das dauerhaftes Speichern von Konfigurationen durch Bearbeiten der Datei `.bashrc`.
2. **[Umgebungsvariablen in Linux](https://labex.io/de/labs/linux-environment-variables-in-linux-385274)** - Lernen Sie das Konzept und die Verwendung von Umgebungsvariablen kennen, wie man sie erstellt, ändert und verwaltet und welche Rolle sie bei der Systemkonfiguration spielen.
3. **[Linux-Umgebungsvariablen konfigurieren](https://labex.io/de/labs/linux-configure-linux-environment-variables-437861)** - Sammeln Sie praktische Erfahrungen beim Erstellen, Festlegen und Verwalten von Umgebungsvariablen in einem Linux-System.

Diese Labs helfen Ihnen, die Konzepte in realen Szenarien anzuwenden und Vertrauen im Umgang mit Ihrer Linux-Shell-Umgebung aufzubauen.

## Quiz Question

Welcher Befehl zeigt alle Ihre aktuellen Umgebungsvariablen an? (Bitte antworten Sie auf Englisch, verwenden Sie nur den Befehlsnamen in Kleinbuchstaben).

## Quiz Answer

env
