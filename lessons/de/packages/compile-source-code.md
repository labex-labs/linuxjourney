---
title: "Quellcode kompilieren"
description: "Erfahren Sie, wie Sie Quellcode unter Linux mit make, configure und checkinstall kompilieren. Verstehen Sie den Build-Prozess für Anfänger und fortgeschrittene Benutzer."
keywords: "Quellcode kompilieren, make install, checkinstall, Linux kompilieren, build-essential, Linux Tutorial, Anfängerleitfaden"
---

## Lesson Content

Oft stößt man auf ein obskures Paket, das nur in Form von reinem Quellcode vorliegt. Sie müssen ein paar Befehle verwenden, um dieses Quellcodepaket zu kompilieren und auf Ihrem System zu installieren.

Zunächst benötigen Sie Software, um die Tools zu installieren, die Ihnen das Kompilieren von Quellcode ermöglichen.

```bash
sudo apt install build-essential
```

Danach entpacken Sie den Inhalt der Paketdatei, höchstwahrscheinlich eine `.tar.gz`-Datei.

```bash
tar -xzvf package.tar.gz
```

Bevor Sie etwas tun, werfen Sie einen Blick in die `README`- oder `INSTALL`-Datei innerhalb des Pakets. Manchmal gibt es spezifische Installationsanweisungen.

Je nachdem, welche Kompilierungsmethode der Entwickler verwendet hat, müssen Sie verschiedene Befehle verwenden, wie z.B. `cmake` oder etwas anderes.

Am häufigsten sehen Sie jedoch die grundlegende `make`-Kompilierung, daher werden wir diese besprechen:

Innerhalb des Paketinhalts befindet sich ein `configure`-Skript. Dieses Skript überprüft Abhängigkeiten auf Ihrem System, und wenn Ihnen etwas fehlt, wird ein Fehler angezeigt und Sie müssen diese Abhängigkeiten beheben.

```bash
./configure
```

Das `./` ermöglicht Ihnen die Ausführung eines Skripts im aktuellen Verzeichnis.

```bash
make
```

Innerhalb des Paketinhalts befindet sich eine Datei namens `Makefile`, die Regeln zum Erstellen der Software enthält. Wenn Sie den Befehl `make` ausführen, schaut er in diese Datei, um die Software zu erstellen.

```bash
sudo make install
```

Dieser Befehl installiert das Paket tatsächlich; er kopiert die richtigen Dateien an die richtigen Stellen auf Ihrem Computer.

Wenn Sie das Paket deinstallieren möchten, verwenden Sie:

```bash
sudo make uninstall
```

Seien Sie vorsichtig bei der Verwendung von `make install`; Sie merken vielleicht nicht, wie viel im Hintergrund tatsächlich passiert. Wenn Sie sich entscheiden, dieses Paket zu entfernen, entfernen Sie möglicherweise nicht alles, weil Sie nicht wussten, was Ihrem System hinzugefügt wurde. Vergessen Sie stattdessen alles über `make install`, was ich Ihnen gerade erklärt habe, und verwenden Sie den Befehl **checkinstall**. Dieser Befehl erstellt eine `.deb`-Datei für Sie, die Sie einfach installieren und deinstallieren können.

```bash
sudo checkinstall
```

Dieser Befehl wird im Wesentlichen "make install" ausführen und ein `.deb`-Paket erstellen und installieren. Dies erleichtert das spätere Entfernen des Pakets.

## Exercise

Suchen Sie ein Quellcode-Programm (von einer vertrauenswürdigen Seite) und installieren Sie es aus dem Quellcode.

## Quiz Question

Was sollten Sie IMMER anstelle von `make install` verwenden?

## Quiz Answer

checkinstall
