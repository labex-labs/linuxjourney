---
index: 6
lang: "de"
title: "Kernelmodule"
meta_title: "Kernelmodule - Kernel"
meta_description: "Erfahren Sie, was Kernelmodule unter Linux sind und wie sie die Kernel-Funktionalität erweitern. Diese Lektion behandelt die Verwendung von lsmod und modprobe zum Auflisten, Laden und Entladen von Modulen bei Bedarf."
meta_keywords: "was sind kernelmodule, Linux kernelmodule, modprobe, lsmod, kernelverwaltung, Linux Tutorial, Anfänger Linux, Linux Anleitung"
---

## Lesson Content

Stellen Sie sich den Linux-Kernel als den Kernmotor eines Autos vor. Sie können Zubehör wie einen Dachgepäckträger oder ein neues Soundsystem hinzufügen, ohne den Motor selbst zu verändern. Dieses Zubehör kann bei Bedarf hinzugefügt oder entfernt werden. Der Linux-Kernel verwendet ein ähnliches Konzept mit Kernel-Modulen.

### Was sind Kernel-Module

Also, **was sind Kernel-Module**? Es sind Codeabschnitte, die bei Bedarf in den Kernel geladen und aus ihm entladen werden können. Sie erweitern die Funktionalität des Kernels, ohne dass Sie den Kern-Kernel neu kompilieren oder das System neu starten müssen. Dieser modulare Ansatz ermöglicht es, Unterstützung für neue Hardware (wie eine neue WLAN-Karte) oder neue Softwarefunktionen (wie ein neues Dateisystem) dynamisch hinzuzufügen. Dies hält den Kern-Kernel schlank und ermöglicht gleichzeitig immense Flexibilität.

### Geladene Module auflisten

Um eine Liste aller aktuell in den Speicher geladenen Kernel-Module anzuzeigen, können Sie den Befehl `lsmod` verwenden. Dieser gibt Ihnen eine Momentaufnahme der aktiven Module und ihrer Abhängigkeiten.

```bash
lsmod
```

### Ein Kernel-Modul laden

Um ein Kernel-Modul zu laden, verwenden wir den Befehl `modprobe`. Um beispielsweise das Modul `bluetooth` zu laden, würden Sie Folgendes ausführen:

```bash
sudo modprobe bluetooth
```

Der Befehl `modprobe` ist intelligent; er sucht das Modul im Standardverzeichnis (`/lib/modules/$(uname -r)/`) und lädt auch alle anderen Module, von denen das Zielmodul abhängt.

### Ein Kernel-Modul entladen

Wenn ein Modul nicht mehr benötigt wird, können Sie es entladen, um Systemressourcen freizugeben. Verwenden Sie das Flag `-r` mit `modprobe`, um ein Modul zu entfernen:

```bash
sudo modprobe -r bluetooth
```

### Module beim Booten verwalten

Mit `modprobe` geladene Module sind temporär und verschwinden nach einem Neustart. Um Modulkonfigurationen dauerhaft zu speichern, können Sie Konfigurationsdateien im Verzeichnis `/etc/modprobe.d/` erstellen.

Um ein Modul beim Booten mit bestimmten Optionen automatisch zu laden, erstellen Sie eine `.conf`-Datei. Wenn Sie beispielsweise ein hypothetisches Modul namens `peanut_butter` hätten und dessen Parameter `type` auf `almond` setzen wollten, würde Ihre Datei wie folgt aussehen:

```plaintext
# /etc/modprobe.d/peanutbutter.conf

options peanut_butter type=almond
```

Umgekehrt können Sie, um das Laden eines Moduls beim Booten zu verhindern (ein als Blacklisting bezeichneter Vorgang), das Schlüsselwort `blacklist` in einer Konfigurationsdatei verwenden:

```plaintext
# /etc/modprobe.d/peanutbutter.conf

blacklist peanut_butter
```

Diese Konfigurationsdateien ermöglichen eine detaillierte Steuerung darüber, welche Module beim Start Ihres Systems verfügbar sind.

## Exercise

Übung macht den Meister! Hier ist ein praktisches Labor, um Ihr Verständnis von Linux-Kernel-Modulen zu festigen:

1. **[Kernel-Module unter Linux verwalten](https://labex.io/de/labs/comptia-manage-kernel-modules-in-linux-590865)** - Üben Sie das Auflisten, Inspizieren, Laden und Entladen von Kernel-Modulen sowie deren Konfiguration, damit sie beim Booten automatisch geladen werden. Dieses Labor hilft Ihnen, die Konzepte in einem realen Szenario anzuwenden und Vertrauen in die Verwaltung von Kernel-Modulen aufzubauen.

## Quiz Question

Welcher Befehl wird zum Entladen eines Moduls verwendet?

## Quiz Answer

modprobe -r
