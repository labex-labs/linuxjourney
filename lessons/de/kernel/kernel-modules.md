---
title: "Kernelmodule"
description: "Erfahren Sie mehr über Linux-Kernelmodule: wie man sie lädt, entlädt und verwaltet. Verstehen Sie die Befehle `modprobe` und `lsmod` zur Erweiterung der Kernel-Funktionalität. Beginnen Sie Ihre Linux-Reise!"
keywords: "Linux-Kernelmodule, modprobe, lsmod, Kernel-Verwaltung, Linux-Tutorial, Linux für Anfänger, Linux-Anleitung"
---

## Lesson Content

Nehmen wir an, ich habe ein tolles Auto; ich investiere viel Zeit und Geld hinein. Ich füge einen Spoiler, eine Anhängerkupplung, einen Fahrradträger und andere zufällige Dinge hinzu. Diese Komponenten ändern die Kernfunktionalität des Autos nicht wirklich, und ich kann sie sehr einfach entfernen und hinzufügen. Der Kernel verwendet dasselbe Konzept mit Kernelmodulen.

Der Kernel selbst ist ein monolithisches Softwarestück. Wenn wir Unterstützung für einen neuen Tastaturtyp hinzufügen möchten, schreiben wir diesen Code nicht direkt in den Kernelcode. So wie wir keinen Fahrradträger an unser Auto schweißen würden (nun, vielleicht würden das manche Leute tun). Kernelmodule sind Codestücke, die bei Bedarf in den Kernel geladen und entladen werden können. Sie ermöglichen es uns, die Funktionalität des Kernels zu erweitern, ohne tatsächlich den Kern-Kernelcode zu erweitern. Wir können auch Module hinzufügen und müssen das System nicht neu starten (in den meisten Fällen).

### Eine Liste der aktuell geladenen Module anzeigen

```bash
lsmod
```

### Ein Modul laden

```bash
sudo modprobe bluetooth
```

`modprobe` lädt das Modul aus `/lib/modules/(kernel version)/kernel/drivers`. Kernelmodule können auch Abhängigkeiten haben; `modprobe` lädt unsere Modulabhängigkeiten, falls sie noch nicht geladen sind.

### Ein Modul entfernen

```bash
sudo modprobe -r bluetooth
```

### Beim Booten laden

Sie können Module auch während des Systemstarts laden, anstatt sie temporär mit `modprobe` zu laden (was beim Neustart entladen wird). Ändern Sie einfach das Verzeichnis `/etc/modprobe.d` und fügen Sie dort eine Konfigurationsdatei wie folgt hinzu:

```plaintext
pete@icebox:~$ /etc/modprobe.d/peanutbutter.conf

options peanut_butter type=almond
```

Ein etwas ausgefallenes Beispiel, aber wenn Sie ein Modul namens `peanut_butter` hätten und einen Kernelparameter für `type=almond` hinzufügen wollten, können Sie es mit dieser Konfigurationsdatei beim Start laden lassen. Beachten Sie auch, dass Kernelmodule ihre eigenen Kernelparameter haben, daher sollten Sie sich speziell über das Modul informieren, um mehr zu erfahren.

### Nicht beim Booten laden

Sie können auch sicherstellen, dass ein Modul beim Booten nicht geladen wird, indem Sie eine Konfigurationsdatei wie folgt hinzufügen:

```plaintext
pete@icebox:~$ /etc/modprobe.d/peanutbutter.conf

blacklist peanut_butter
```

## Exercise

Entladen Sie Ihr Bluetooth-Modul mit `modprobe` und sehen Sie, was passiert. Wie werden Sie das beheben?

## Quiz Question

Welcher Befehl wird verwendet, um ein Modul zu entladen?

## Quiz Answer

modprobe -r
