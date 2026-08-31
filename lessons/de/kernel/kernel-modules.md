---
lesson_id: "kernel-modules"
course_id: "kernel"
lang: "de"
order_index: 6
title: "Kernelmodule"
description: "Erfahre, wie du veröffentlichungsspezifische Linux-Kernelmodule prüfst, lädst, konfigurierst und sicher entfernst."
meta_title: "Kernelmodule – Kernel"
meta_description: "Entdecke, was Kernelmodule unter Linux sind und wie sie die Kernelfunktionalität erweitern. Diese Lektion behandelt die Verwendung von lsmod und modprobe, um Module bei Bedarf aufzulisten, zu laden und zu entladen."
meta_keywords: "was sind Kernelmodule, Linux-Kernelmodule, modprobe, lsmod, Kernelverwaltung, Linux-Tutorial, Linux für Einsteiger, Linux-Leitfaden"
---

Ein ladbares Kernelmodul ist privilegierter Code, der den laufenden Kernel um einen Treiber, ein Dateisystem, eine Netzwerkfunktion oder ein anderes Subsystem erweitern kann. Module vermeiden, dass jede optionale Funktion in ein einziges Kernelabbild eingebaut werden muss, doch das Laden eines Moduls erweitert die vertrauenswürdige Angriffsfläche des Kernels.

## Module auflisten und prüfen

Liste die derzeit geladenen Module auf:

```bash
$ lsmod
```

Die Ausgabe wird aus Kernelzuständen wie `/proc/modules` abgeleitet und enthält Modulname, Größe und einen Nutzungszähler oder Abhängigkeiten. Ein scheinbarer Zähler von null beweist nicht vollständig, dass eine Entfernung sicher ist; ein Treiber kann weiterhin aktive Geräte besitzen oder am Zustand eines Subsystems beteiligt sein.

Prüfe ein für den laufenden Kernel verfügbares Modul mit:

```bash
$ modinfo MODULE_NAME
```

`modinfo` kann Dateiname, Aliase, Parameter, Lizenz, Beschreibung und Signaturinformationen anzeigen. Behandle Metadaten als Beschreibung und nicht als Beweis, dass das Modul vertrauenswürdig oder mit der Arbeitslast kompatibel ist.

:::single-choice{#kernel-modules-lsmod-purpose}
Was zeigt `lsmod` an?

::option[Jedes in entfernten Paketquellen verfügbare Modulpaket.]{#kernel-modules-repository-list explanation="Für den Bestand von Paketquellen sind Abfragen der Paketverwaltung erforderlich."}
::option[Ausschließlich direkt in das Kernelabbild kompilierte Treiber.]{#kernel-modules-builtins explanation="Fest eingebaute Funktionen sind keine ladbaren Module und erscheinen gewöhnlich nicht in lsmod."}
::option[Derzeit in den laufenden Kernel geladene Module.]{#kernel-modules-loaded-list .correct explanation="Die Auflistung bildet den aktiven Modulzustand und Abhängigkeits-/Nutzungsinformationen ab."}
:::

## Mit `modprobe` laden

Lade ein Modul anhand seines Namens:

```bash
$ sudo modprobe MODULE_NAME
```

`modprobe` fragt Abhängigkeitsindizes, Aliase und Konfiguration für den laufenden Kernel unter `/lib/modules/$(uname -r)/` ab. Es lädt erforderliche Abhängigkeiten und übergibt konfigurierte Parameter. `insmod` fügt dagegen eine angegebene Moduldatei unmittelbar ein und stellt nicht denselben Arbeitsablauf zur Abhängigkeitsauflösung bereit.

Bestätige vor dem Laden Herkunft, Signaturrichtlinie, Kompatibilität mit der Kernelveröffentlichung, Parameter, erwartete Hardwarebindung und Rücksetzweg des Moduls. Secure Boot oder Kernel-Lockdown können nicht signierte Module ablehnen; das Erzwingen inkompatiblen Codes birgt Absturz- und Kompromittierungsrisiken.

:::single-choice{#kernel-modules-modprobe-dependencies}
Warum wird `modprobe` gewöhnlich gegenüber einem direkten `insmod` bevorzugt?

::option[Es führt das Modul vollständig im unprivilegierten User-Space aus.]{#kernel-modules-modprobe-userspace explanation="Das eingefügte Modul läuft als privilegierter Kernelcode."}
::option[Es garantiert, dass jedes Drittanbietermodul signiert und sicher ist.]{#kernel-modules-modprobe-guarantee explanation="Die Durchsetzung hängt von der Richtlinie ab, und eine gültige Signatur beweist nicht, dass keine Fehler vorhanden sind."}
::option[Es löst Modulaliase, Abhängigkeiten und Konfiguration auf.]{#kernel-modules-modprobe-resolves .correct explanation="Modprobe verwendet den indizierten Modulbaum für die genaue laufende Veröffentlichung."}
:::

## Modulparameter und Laden beim Systemstart

Dauerhafte Parameter- und Aliasrichtlinien gehören in eine `.conf`-Datei unter `/etc/modprobe.d/`:

```text
options example_module mode=careful
```

Diese Zeile beeinflusst, wie modprobe das Modul lädt; sie fordert nicht von selbst das Laden des Moduls beim Systemstart an. Eine einfache Liste zum Laden beim Systemstart befindet sich gewöhnlich unter `/etc/modules-load.d/`:

```text
example_module
```

Hardwarealiase lösen häufig ein automatisches Laden ohne ausdrückliche Liste aus. Aktualisiere für Module, die während der frühen Startphase benötigt werden, nach Konfigurationsänderungen das initramfs gemäß dem dokumentierten Verfahren der Distribution.

:::single-choice{#kernel-modules-options-versus-load}
Was bewirkt eine `options`-Zeile in `/etc/modprobe.d/`?

::option[Sie garantiert allein durch diese Zeile, dass das Modul bei jedem Start geladen wird.]{#kernel-modules-options-autoload explanation="Anforderungen zum Laden beim Systemstart verwenden einen anderen Mechanismus wie die modules-load-Konfiguration oder Gerätealiase."}
::option[Sie legt Parameter fest, die beim Laden des benannten Moduls verwendet werden.]{#kernel-modules-options-parameters .correct explanation="Modprobe wendet konfigurierte Schlüssel-Wert-Argumente beim Einfügen an."}
::option[Sie kompiliert das Modul für jede installierte Kernelveröffentlichung.]{#kernel-modules-options-compiles explanation="Konfiguration baut keine Binärmodule."}
:::

## Blacklisting und seine Grenzen

Eine modprobe-Konfiguration kann Folgendes enthalten:

```text
blacklist example_module
```

Blacklisting unterdrückt gewöhnlich das automatische Laden über die Aliase des Moduls. Es entlädt weder ein bereits geladenes Modul noch entfernt es das Modul aus einem initramfs. Auch verhindert es nicht zwangsläufig ein ausdrückliches Laden anhand des genauen Namens oder als Abhängigkeit. Sicherheitshärtung erfordert eine bedrohungsspezifische Kombination aus Modulverfügbarkeit, Signaturdurchsetzung, initramfs-Inhalt, Startparametern und Richtlinien.

:::single-choice{#kernel-modules-blacklist-effect}
Was unterdrückt eine einfache modprobe-`blacklist`-Zeile in erster Linie?

::option[Das automatische Laden über die Aliase des Moduls.]{#kernel-modules-blacklist-aliases .correct explanation="Die Direktive ist kein allgemeines Verbot sämtlicher Wege, über die Code bereits geladen sein oder geladen werden kann."}
::option[Die Ausführung jedes User-Space-Programms mit einem ähnlichen Namen.]{#kernel-modules-blacklist-user-programs explanation="Die modprobe-Konfiguration gilt für die Auflösung von Kernelmodulen."}
::option[Jeden fest in das Abbild kompilierten Kernelcode.]{#kernel-modules-blacklist-builtins explanation="Fest eingebaute Funktionalität kann nicht als Modul entladen oder blockiert werden."}
:::

## Ein Modul sicher entfernen

Fordere die Entfernung an mit:

```bash
$ sudo modprobe -r MODULE_NAME
```

Modprobe kann gegebenenfalls nun ungenutzte Abhängigkeiten entfernen. Der Kernel lehnt eine Entfernung ab, wenn die gewöhnliche Referenzverfolgung das Modul als belegt anzeigt. Verlasse dich aber nicht auf diese Prüfung allein. Stoppe Dienste, hänge Dateisysteme aus, trenne Geräte, versetze Netzwerke in einen ruhenden Zustand und bestätige einen anderen Treiber oder Wiederherstellungsweg, bevor du Code entfernst, der aktive Hardware unterstützt.

Erzwinge niemals das Entladen eines Moduls auf einem System, das du erhalten musst. Fehler beim Entfernen oder ausstehende Aktivität können den Kernel zum Absturz bringen oder Daten beschädigen.

:::single-choice{#kernel-modules-remove-command}
Welcher Befehl fordert die abhängigkeitsbewusste Entfernung eines Moduls anhand seines Namens an?

::option[`lsmod -r MODULE_NAME`]{#kernel-modules-lsmod-remove explanation="Lsmod ist ein schreibgeschütztes Auflistungswerkzeug und dient nicht zur Entfernung."}
::option[`uname -r MODULE_NAME`]{#kernel-modules-uname-remove explanation="Uname meldet Kernelinformationen und verwaltet keine Module."}
::option[`modprobe -r MODULE_NAME`]{#kernel-modules-modprobe-remove .correct explanation="Der Entfernungsmodus berücksichtigt die indizierten Abhängigkeitsbeziehungen rund um das angeforderte Modul."}
:::

Nutze [Kernelmodule unter Linux verwalten](https://labex.io/labs/comptia-manage-kernel-modules-in-linux-590865), um mit Modulen zu üben, die das Lab als sicher vorgesehen hat.

## Zusammenfassung

Du kannst Module nun unter Berücksichtigung ihres Risikos auf Kernelebene verwalten.

1. Verwende `lsmod` für den aktiven Zustand und `modinfo` für verfügbare Metadaten.
2. Verwende `modprobe` zum alias- und abhängigkeitsbewussten Laden.
3. Trenne modprobe-Parameter von Anforderungen zum Laden beim Systemstart.
4. Behandle Blacklisting als begrenzte Richtlinie und nicht als absolute Sperre.
5. Versetze jeden Verbraucher vor `modprobe -r` in einen ruhenden Zustand.
