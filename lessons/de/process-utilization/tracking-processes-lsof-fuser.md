---
index: 2
lang: "de"
title: "lsof und fuser"
meta_title: "lsof und fuser - Prozessauslastung"
meta_description: "Erkunden Sie die Befehle lsof und fuser unter Linux, um herauszufinden, welche Prozesse bestimmte Dateien verwenden. Lernen Sie, Fehler wie 'Gerät oder Ressource belegt' zu beheben, vergleichen Sie fuser mit lsof und nutzen Sie Optionen wie fuser -k, um geöffnete Dateien effektiv zu verwalten."
meta_keywords: "lsof, fuser, fuser Befehl, linux fuser, fuser vs lsof, lsof vs fuser, fuser -k linux, geöffnete Dateien, Prozessverwaltung, Gerät belegt, Linux Befehle"
---

## Lesson Content

Haben Sie jemals versucht, ein USB-Laufwerk auszuhängen, und die Fehlermeldung „Gerät oder Ressource belegt“ erhalten? Dieses häufige Problem tritt auf, wenn ein Prozess noch eine Datei oder ein Verzeichnis auf dem Gerät verwendet. Um dies zu beheben, müssen Sie herausfinden, welcher Prozess die Ressource blockiert. Zwei leistungsstarke Dienstprogramme für diese Aufgabe sind `lsof` und `fuser`.

### Verwendung von lsof zum Auflisten geöffneter Dateien

In Linux wird fast alles als Datei behandelt, einschließlich Festplatten, Pipes, Netzwerk-Sockets und Geräten. Der Befehl `lsof` (Kurzform für „list open files“) zeigt Ihnen eine detaillierte Liste aller geöffneten Dateien und der Prozesse, die sie verwenden.

Um zu sehen, welche Prozesse das aktuelle Verzeichnis (`.`) verwenden, können Sie Folgendes ausführen:

```bash
pete@icebox:~$ lsof .
COMMAND    PID  USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
lxsession 1491 pete  cwd    DIR    8,6     4096  131 .
update-no 1796 pete  cwd    DIR    8,6     4096  131 .
nm-applet 1804 pete  cwd    DIR    8,6     4096  131 .
xterm     2205 pete  cwd    DIR    8,6     4096  131 .
bash      2207 pete  cwd    DIR    8,6     4096  131 .
lsof      5914 pete  cwd    DIR    8,6     4096  131 .
```

Die Ausgabe zeigt den Befehl (`COMMAND`), die Prozess-ID (`PID`) und den Benutzer (`USER`), die mit jeder geöffneten Datei verknüpft sind. Mit diesen Informationen können Sie die Prozesse identifizieren, die Sie daran hindern, ein Gerät auszuhängen.

### Der fuser-Befehl

Ein weiteres ausgezeichnetes Werkzeug ist der Befehl `fuser` (Kurzform für „file user“). Dieses Dienstprogramm identifiziert, welche Prozesse bestimmte Dateien, Sockets oder Dateisysteme verwenden. Der Befehl `linux fuser` ist eine schnelle Möglichkeit, die PIDs der Prozesse anzuzeigen, die auf eine bestimmte Ressource zugreifen.

Die Verwendung der Option `-v` (verbose/ausführlich) liefert eine detailliertere Ausgabe:

```bash
pete@icebox:~$ fuser -v .
                     USER        PID ACCESS COMMAND
/home/pete:         pete  1491 ..c.. lxsession
                     pete  1796 ..c.. update-notifier
                     pete  1804 ..c.. nm-applet
                     pete  2205 ..c.. xterm
                     pete  2207 ..c.. bash
```

Hier können wir deutlich sehen, welche Prozesse unser aktuelles Verzeichnis verwenden. Die Spalte `ACCESS` zeigt an, wie die Datei verwendet wird (z. B. `c` für aktuelles Verzeichnis).

### Prozesse mit fuser beenden

Ein Hauptmerkmal des Befehls `fuser` ist seine Fähigkeit, Prozesse zu beenden, die eine Ressource verwenden. Die Option `fuser -k` sendet ein `SIGKILL`-Signal an jeden Prozess, der auf die angegebene Datei oder das Dateisystem zugreift. Dies ist besonders nützlich, um ein belegtes Gerät auszuhängen.

Um beispielsweise alle Prozesse zu beenden, die den Einhängepunkt unter `/mnt/usb` verwenden, würden Sie Folgendes ausführen:

```bash
sudo fuser -k /mnt/usb
```

Die Verwendung von `fuser -k` unter Linux ist eine schnelle und effektive Methode, um eine Ressource freizugeben.

### fuser vs lsof

Wann sollten Sie also `fuser` vs `lsof` verwenden?

- **`lsof`** eignet sich hervorragend für detaillierte Untersuchungen. Es liefert umfangreiche Informationen zu allen geöffneten Dateien und ist somit ideal für komplexe Fehlerbehebungen.
- **`fuser`** ist direkter. Es eignet sich perfekt, um schnell Prozesse auf einer bestimmten Datei oder einem Einhängepunkt zu identifizieren und bei Bedarf zu beenden. Der `fuser command` ist oft die schnellere Wahl zur Behebung von Fehlern wie „Gerät oder Ressource belegt“.

Beide Tools sind für jeden Linux-Benutzer unerlässlich. Machen Sie sich mit ihnen vertraut, um Dateien und Prozesse effizient zu verwalten.

## Exercise

Übung macht den Meister! Hier sind einige praktische Übungen, um Ihr Verständnis für die Verwaltung von Prozessen und die Behebung von Ressourcenkonflikten zu festigen:

1.  **[Linux-Prozesse verwalten und überwachen](https://labex.io/de/labs/comptia-manage-and-monitor-linux-processes-590864)** – Üben Sie die Interaktion mit Vordergrund- und Hintergrundprozessen, deren Überprüfung mit `ps`, die Überwachung von Ressourcen mit `top` und deren Beendigung mit `kill`. Dieses Labor hilft Ihnen dabei, Prozesse zu identifizieren und zu verwalten, die möglicherweise Ressourcen wie Dateien auf einem USB-Laufwerk blockieren.

Dieses Labor hilft Ihnen, diese Konzepte in realen Szenarien anzuwenden und Vertrauen beim Identifizieren und Verwalten von Systemprozessen aufzubauen.

## Quiz Question

Welcher Befehl wird verwendet, um geöffnete Dateien und die zugehörigen Prozessinformationen aufzulisten?

## Quiz Answer

lsof
