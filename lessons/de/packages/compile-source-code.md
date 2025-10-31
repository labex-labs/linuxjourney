---
index: 7
lang: "de"
title: "Quellcode kompilieren"
meta_title: "Quellcode kompilieren - Pakete"
meta_description: "Erfahren Sie, wie Sie Quellcode unter Linux kompilieren. Diese Anleitung behandelt die wesentlichen Schritte zum Erstellen von Quellcode mit configure, make und dem empfohlenen checkinstall-Befehl für eine saubere Paketverwaltung."
meta_keywords: "Quellcode kompilieren, Quellcode erstellen, Quellcode kompilieren, make install, checkinstall, Linux kompilieren, build-essential, configure Skript, makefile, Linux Tutorial"
---

## Lesson Content

Gelegentlich finden Sie möglicherweise ein Paket, das nur als Quellcode verfügbar ist. Um es nutzen zu können, müssen Sie es auf Ihrem System kompilieren und installieren. Diese Lektion führt Sie durch den üblichen Prozess, wie man aus Quellcode kompiliert.

### Vorbereitung Ihres Systems

Bevor Sie etwas kompilieren können, benötigen Sie die notwendigen Werkzeuge. Auf Debian-basierten Systemen wie Ubuntu können Sie diese mit einem einzigen Befehl installieren.

```bash
sudo apt install build-essential
```

Das Paket `build-essential` installiert eine Reihe von Softwareentwicklungswerkzeugen, einschließlich des GCC-Compilers und des `make`-Dienstprogramms, die für die Kompilierung unerlässlich sind.

Nach der Installation der Werkzeuge entpacken Sie den Inhalt des Quellcode-Pakets, was typischerweise eine `.tar.gz`-Datei ist.

```bash
tar -xzvf package.tar.gz
```

Bevor Sie fortfahren, überprüfen Sie immer, ob sich im entpackten Verzeichnis eine `README`- oder `INSTALL`-Datei befindet. Diese Dateien enthalten oft spezifische Anweisungen oder Abhängigkeiten, die für dieses spezielle Paket erforderlich sind.

### Der Standard-Build-Prozess

Obwohl verschiedene Entwickler unterschiedliche Build-Systeme wie `cmake` verwenden mögen, beinhaltet die traditionellste Methode einen dreistufigen Prozess. Das Verständnis davon ist grundlegend, um zu lernen, wie man Quellcode erstellt.

Führen Sie zuerst das `configure`-Skript aus. Dieses Skript prüft Ihr System auf alle notwendigen Abhängigkeiten und Bibliotheken, die die Software benötigt, um korrekt zu bauen und ausgeführt zu werden.

```bash
./configure
```

Das Präfix `./` weist die Shell an, das Skript aus dem aktuellen Verzeichnis auszuführen. Wenn das Skript fehlende Abhängigkeiten meldet, müssen Sie diese installieren, bevor Sie fortfahren.

Als Nächstes führen Sie den Befehl `make` aus. Dieser Befehl liest eine Datei namens `Makefile` im Verzeichnis, die eine Reihe von Regeln enthält, wie der Quellcode in ausführbare Programme kompiliert wird.

```bash
make
```

Schließlich, um die Software auf Ihrem System zu installieren, würden Sie typischerweise ausführen:

```bash
sudo make install
```

Dieser Befehl kopiert die kompilierten Dateien in die entsprechenden Systemverzeichnisse und macht die Software zur Nutzung verfügbar.

### Ein besserer Weg zur Installation

Obwohl `sudo make install` funktioniert, hat es einen erheblichen Nachteil: Es registriert die Software nicht beim Paketmanager Ihres Systems. Dies erschwert das Nachverfolgen, Aktualisieren oder saubere Deinstallieren des Pakets zu einem späteren Zeitpunkt.

Ablösung ist die Verwendung von `checkinstall`. Dieses Werkzeug führt den Installationsprozess aus, aber anstatt Dateien direkt zu kopieren, erstellt es ein natives Systempaket (wie eine `.deb`-Datei unter Debian/Ubuntu) und installiert dieses.

```bash
sudo checkinstall
```

Die Verwendung von `checkinstall` integriert die kompilierte Software in Ihr Paketverwaltungssystem. Das bedeutet, Sie können sie später einfach mit `apt` oder `dpkg` entfernen, genau wie jedes andere Paket, das Sie aus den offiziellen Repositories installiert haben. Aus diesem Grund sollten Sie `checkinstall` immer `make install` vorziehen.

Um ein mit `make install` installiertes Paket zu deinstallieren, müssten Sie zurück in das Quellverzeichnis navigieren und `sudo make uninstall` ausführen, aber dies ist nicht immer zuverlässig.

## Exercise

Übung macht den Meister! Hier ist ein praktisches Labor, um Ihr Verständnis für das Erstellen von Software aus dem Quellcode zu festigen:

1. **[Software aus Quellcode in Linux erstellen](https://labex.io/de/labs/comptia-build-software-from-source-code-in-linux-590853)** - Üben Sie den grundlegenden Prozess des Erstellens und Installierens von Software aus ihrem Quellcode, einschließlich der Verwendung von `configure`, `make` und `make install`.

Dieses Labor hilft Ihnen, die Konzepte in einem realen Szenario anzuwenden und Vertrauen beim Kompilieren von Software aufzubauen.

## Quiz Question

Was sollten Sie IMMER anstelle von `make install` verwenden? (Bitte antworten Sie auf Englisch, achten Sie auf die Groß-/Kleinschreibung).

## Quiz Answer

checkinstall
