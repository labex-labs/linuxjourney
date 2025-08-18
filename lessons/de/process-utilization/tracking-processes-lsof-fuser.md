---
index: 2
lang: "de"
title: "lsof und fuser"
meta_title: "lsof und fuser - Prozessauslastung"
meta_description: "Erfahren Sie, wie Sie die Befehle lsof und fuser in Linux verwenden, um Prozesse zu identifizieren, die Dateien nutzen. Verstehen Sie 'Device or Resource Busy'-Fehler und verwalten Sie offene Dateien effektiv."
meta_keywords: "lsof, fuser, Linux-Befehle, offene Dateien, Prozessverwaltung, Linux-Tutorial, Anfängerleitfaden, Gerät besetzt"
---

## Lesson Content

Nehmen wir an, Sie haben ein USB-Laufwerk angeschlossen und begonnen, an einigen Dateien zu arbeiten. Nachdem Sie fertig waren, versuchten Sie, das USB-Gerät auszuhängen, und erhielten einen Fehler: "Device or Resource Busy." Wie würden Sie herausfinden, welche Dateien auf dem USB-Laufwerk noch verwendet werden? Dafür gibt es zwei Tools, die Sie verwenden können:

### lsof

Denken Sie daran, Dateien sind nicht nur Textdateien, Bilder usw.; sie sind alles auf dem System: Festplatten, Pipes, Netzwerk-Sockets, Geräte usw. Um zu sehen, was von einem Prozess verwendet wird, können Sie den Befehl `lsof` (kurz für "list open files") verwenden. Dieser zeigt Ihnen eine Liste aller offenen Dateien und ihrer zugehörigen Prozesse.

```bash
pete@icebox:~$ lsof .
COMMAND    PID  USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
lxsession 1491 pete  cwd    DIR    8,6     4096  131 .
update-no 1796 pete  cwd    DIR    8,6     4096  131 .
nm-applet 1804 pete  cwd    DIR    8,6     4096  131 .
indicator 1809 pete  cwd    DIR    8,6     4096  131 .
xterm     2205 pete  cwd    DIR    8,6     4096  131 .
bash      2207 pete  cwd    DIR    8,6     4096  131 .
lsof      5914 pete  cwd    DIR    8,6     4096  131 .
lsof      5915 pete  cwd    DIR    8,6     4096  131 .
```

Jetzt kann ich sehen, welche Prozesse das Gerät/die Datei derzeit geöffnet halten. In unserem USB-Beispiel können Sie diese Prozesse auch beenden, damit Sie dieses lästige Laufwerk aushängen können.

### fuser

Eine weitere Möglichkeit, einen Prozess zu verfolgen, ist der Befehl `fuser` (kurz für "file user"). Dieser zeigt Ihnen Informationen über den Prozess, der die Datei oder den Dateibenutzer verwendet.

```bash
pete@icebox:~$ fuser -v .
                     USER        PID ACCESS COMMAND
/home/pete:         pete  1491 ..c.. lxsession
                     pete  1796 ..c.. update-notifier
                     pete  1804 ..c.. nm-applet
                     pete  1809 ..c.. indicator-power
                     pete  2205 ..c.. xterm
                     pete  2207 ..c.. bash
```

Wir können sehen, welche Prozesse derzeit unser `/home/pete`-Verzeichnis verwenden. Die Tools `lsof` und `fuser` sind sehr ähnlich. Machen Sie sich mit diesen Tools vertraut und versuchen Sie, sie das nächste Mal zu verwenden, wenn Sie eine Datei oder einen Prozess verfolgen müssen.

## Exercise

Lesen Sie die Manpages für `lsof` und `fuser`. Es gibt viele Informationen, die wir nicht behandelt haben, die Ihnen eine größere Flexibilität mit diesen Tools ermöglichen.

## Quiz Question

Welcher Befehl wird verwendet, um offene Dateien und ihre Prozessinformationen aufzulisten?

## Quiz Answer

lsof
