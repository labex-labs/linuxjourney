---
index: 7
lang: "de"
title: "Quellcode kompilieren"
meta_title: "Quellcode kompilieren - Pakete"
meta_description: "Erfahren Sie, wie Sie Quellcode in Linux mit make, configure und checkinstall kompilieren. Verstehen Sie den Build-Prozess für Anfänger und fortgeschrittene Benutzer."
meta_keywords: "Quellcode kompilieren, make install, checkinstall, Linux kompilieren, build-essential, Linux Tutorial, Anfängerleitfaden"
---

## Lesson Content

Oft stößt man auf ein obskures Paket, das nur in Form von reinem Quellcode vorliegt. Sie müssen ein paar Befehle verwenden, um dieses Quellcodepaket zu kompilieren und auf Ihrem System zu installieren.

Zunächst benötigen Sie Software, um die Tools zu installieren, mit denen Sie Quellcode kompilieren können.

```bash
sudo apt install build-essential
```

Danach extrahieren Sie den Inhalt der Paketdatei, höchstwahrscheinlich eine `.tar.gz`-Datei.

```bash
tar -xzvf package.tar.gz
```

Bevor Sie etwas tun, werfen Sie einen Blick auf die Datei `README` oder `INSTALL` innerhalb des Pakets. Manchmal gibt es spezifische Installationsanweisungen.

Je nachdem, welche Kompilierungsmethode der Entwickler verwendet hat, müssen Sie verschiedene Befehle verwenden, wie z.B. `cmake` oder etwas anderes.

Am häufigsten sehen Sie jedoch die grundlegende `make`-Kompilierung, daher werden wir diese besprechen:

Innerhalb des Paketinhaltes befindet sich ein `configure`-Skript. Dieses Skript überprüft die Abhängigkeiten auf Ihrem System, und wenn Ihnen etwas fehlt, wird eine Fehlermeldung angezeigt und Sie müssen diese Abhängigkeiten beheben.

```bash
./configure
```

Das `./` ermöglicht es Ihnen, ein Skript im aktuellen Verzeichnis auszuführen.

```bash
make
```

Innerhalb des Paketinhaltes befindet sich eine Datei namens `Makefile`, die Regeln zum Erstellen der Software enthält. Wenn Sie den Befehl `make` ausführen, schaut er in diese Datei, um die Software zu erstellen.

```bash
sudo make install
```

Dieser Befehl installiert das Paket tatsächlich; er kopiert die richtigen Dateien an die richtigen Stellen auf Ihrem Computer.

Wenn Sie das Paket deinstallieren möchten, verwenden Sie:

```bash
sudo make uninstall
```

Seien Sie vorsichtig bei der Verwendung von `make install`; Sie merken vielleicht nicht, wie viel tatsächlich im Hintergrund passiert. Wenn Sie sich entscheiden, dieses Paket zu entfernen, entfernen Sie möglicherweise nicht alles, weil Sie nicht wussten, was Ihrem System hinzugefügt wurde. Vergessen Sie stattdessen alles über `make install`, was ich Ihnen gerade erklärt habe, und verwenden Sie den Befehl **checkinstall**. Dieser Befehl erstellt eine `.deb`-Datei für Sie, die Sie einfach installieren und deinstallieren können.

```bash
sudo checkinstall
```

Dieser Befehl wird im Wesentlichen "make install" ausführen und ein `.deb`-Paket erstellen und installieren. Dies erleichtert das spätere Entfernen des Pakets.

## Exercise

Übung macht den Meister! Hier ist ein praktisches Labor, um Ihr Verständnis des Erstellens von Software aus dem Quellcode zu vertiefen:

1. **[Software aus Quellcode in Linux erstellen](https://labex.io/de/labs/comptia-build-software-from-source-code-in-linux-590853)** - Üben Sie den grundlegenden Prozess des Erstellens und Installierens von Software aus ihrem Quellcode, einschließlich der Verwendung von `configure`, `make` und `make install`.

Dieses Labor wird Ihnen helfen, die Konzepte in einem realen Szenario anzuwenden und Vertrauen beim Kompilieren von Software aufzubauen.

## Quiz Question

Was sollten Sie IMMER anstelle von `make install` verwenden?

## Quiz Answer

checkinstall
