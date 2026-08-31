---
lesson_id: "compile-source-code"
course_id: "packages"
lang: "de"
order_index: 7
title: "Quellcode kompilieren"
description: "Erfahre, wie du aus Quellcode kompilierte Software überprüfst, konfigurierst, baust, testest, bereitstellst und nachverfolgst."
meta_title: "Quellcode kompilieren – Pakete"
meta_description: "Erfahre, wie du unter Linux aus Quellcode kompilierst. Dieser Leitfaden behandelt die wesentlichen Schritte zum Bauen von Quellcode mit configure, make und dem empfohlenen Befehl checkinstall für eine saubere Paketverwaltung."
meta_keywords: "aus Quellcode kompilieren, Quellcode bauen, Quellcode kompilieren, make install, checkinstall, Linux kompilieren, build-essential, configure-Skript, Makefile, Linux-Tutorial"
---

Das Bauen aus Quellcode kann eine Version oder Funktion bereitstellen, die in den konfigurierten Paketquellen nicht verfügbar ist, verlagert jedoch Integrations-, Aktualisierungs- und Vertrauensarbeit von der Distribution auf dich. Bevorzuge ein unterstütztes Distributionspaket, wenn es die Anforderung erfüllt.

## Vor dem Bauen überprüfen und lesen

Beziehe Quellcode über einen authentifizierten Veröffentlichungskanal des Upstream-Projekts. Überprüfe seine Signatur oder Prüfsumme über einen vertrauenswürdigen Weg und prüfe anschließend das Archiv, bevor du es in ein unprivilegiertes Staging-Verzeichnis extrahierst. Lies Dateien wie `README`, `INSTALL`, `SECURITY` und die Build-Dokumentation des Projekts.

Build-Anweisungen sind ausführbarer Code. Ein `configure`-Skript, eine Build-Definition, ein Test oder ein Compiler-Plug-in kann beliebige Befehle als dein Benutzer ausführen. Baue keinen nicht vertrauenswürdigen Quellcode und führe den Build selbst nicht mit `sudo` aus.

:::single-choice{#compile-source-code-build-privilege}
Warum sollte der Kompilierungsschritt gewöhnlich ohne `sudo` ausgeführt werden?

::option[Compiler weigern sich, Maschinencode für den root-Benutzer zu erzeugen.]{#compile-source-code-root-compiler explanation="Compiler können als root laufen, doch dies erhöht unnötig das Risiko."}
::option[`sudo` löscht automatisch jede erzeugte Objektdatei.]{#compile-source-code-sudo-delete explanation="Die Erhöhung von Rechten entfernt Build-Ausgaben nicht von sich aus."}
::option[Build-Logik kann beliebige Befehle ausführen und benötigt gewöhnlich keine Systemrechte.]{#compile-source-code-unprivileged-build .correct explanation="Ein unprivilegierter Build begrenzt Schäden durch Fehler oder bösartige Build-Anweisungen."}
:::

## Build-Anforderungen installieren

Auf einem Entwicklungssystem der Debian-Familie ist ein verbreiteter Ausgangspunkt:

```bash
$ sudo apt install build-essential
```

Dies installiert einen grundlegenden Compiler und Build-Werkzeuge, aber nicht jede für jedes Projekt erforderliche Abhängigkeit. Projekte können außerdem Sprachlaufzeiten, Generatoren, Build-Systemwerkzeuge, Entwicklungsheader oder genaue Bibliotheksversionen benötigen. Installiere Anforderungen aus vertrauenswürdigen Paketquellen und trenne Build-Abhängigkeiten von Laufzeitabhängigkeiten.

:::single-choice{#compile-source-code-build-essential-scope}
Was stellt `build-essential` auf einem System der Debian-Familie bereit?

::option[Eine Grundausstattung verbreiteter Kompilierungs- und Build-Werkzeuge.]{#compile-source-code-baseline-tools .correct explanation="Es stellt grundlegende Werkzeuge bereit, kann aber nicht alle projektspezifischen Bibliotheken oder Generatoren vorhersehen."}
::option[Jede Abhängigkeit für jedes Quellcodeprojekt.]{#compile-source-code-all-dependencies explanation="Einzelne Projekte deklarieren zusätzliche und manchmal versionsspezifische Anforderungen."}
::option[Eine Garantie, dass heruntergeladener Quellcode vertrauenswürdig ist.]{#compile-source-code-trust-guarantee explanation="Die Installation von Werkzeugen authentifiziert keine getrennte Quellcodeveröffentlichung."}
:::

## Konfigurieren und bauen

Ein traditionelles Projekt im Autoconf-Stil verwendet:

```bash
$ ./configure --prefix=/usr/local
$ make
```

`configure` prüft die Umgebung und erzeugt Build-Dateien gemäß den ausgewählten Optionen. `make` liest Abhängigkeits- und Befehlsregeln, gewöhnlich aus einem `Makefile`, und erstellt die angeforderten Ziele.

Diese Reihenfolge ist nicht universell. Projekte können CMake, Meson, Ninja, sprachspezifische Werkzeuge oder eigene Skripte verwenden. Folge der Dokumentation der genauen Veröffentlichung, statt `./configure` nur deshalb auszuführen, weil es vertraut ist. Ein Build-Verzeichnis außerhalb des Quellbaums kann erzeugte Dateien getrennt halten, sofern das Build-System dies unterstützt.

:::single-choice{#compile-source-code-make-role}
Was tut `make` im traditionellen Arbeitsablauf?

::option[Es registriert jede Ausgabe in der Paketdatenbank der Distribution.]{#compile-source-code-make-package-db explanation="Die Kompilierung allein erzeugt keine Eigentumseinträge nativer Pakete."}
::option[Es lädt automatisch eine authentifizierte Quellcodeveröffentlichung herunter.]{#compile-source-code-make-download explanation="Bezug und Überprüfung des Quellcodes erfolgen vor dem lokalen Build, sofern ein Projekt nicht ausdrücklich etwas anderes definiert."}
::option[Es führt zutreffende Regeln aus der Build-Beschreibung aus.]{#compile-source-code-make-rules .correct explanation="Make bewertet Abhängigkeiten und führt die Befehle aus, die erforderlich sind, um ausgewählte Ziele auf den aktuellen Stand zu bringen."}
:::

## Vor der Installation testen

Führe das dokumentierte Testziel des Projekts aus, zum Beispiel:

```bash
$ make check
```

Das tatsächliche Ziel kann `test`, `check` oder ein getrennter Befehl sein. Untersuche Fehlschläge, statt ungetestete Ausgaben zu installieren. Tests können Netzwerkzugriff, Dienste, besondere Hardware oder Isolation erfordern. Prüfe sie vor der Ausführung genauso wie anderen Build-Code.

:::single-choice{#compile-source-code-test-failure}
Was solltest du tun, wenn die dokumentierte Testsuite fehlschlägt?

::option[Dieselbe Installation sofort als root ausführen.]{#compile-source-code-install-after-failure explanation="Privilegien beheben keinen unbekannten Korrektheitsfehler und vergrößern die Folgen."}
::option[Die Paketverwaltungsdatenbank löschen, um Konflikte zu vermeiden.]{#compile-source-code-delete-database explanation="Die native Datenbank hat nichts mit der Behebung eines Quellcodetestfehlers zu tun und darf nicht verworfen werden."}
::option[Den Fehler vor der Installation des Builds untersuchen.]{#compile-source-code-investigate-tests .correct explanation="Ein fehlgeschlagener Test kann inkompatible Abhängigkeiten, Build-Fehler oder Annahmen über die Umgebung sichtbar machen."}
:::

## Installation bereitstellen und nachverfolgen

`sudo make install` kann Dateien direkt in Systempräfixe kopieren, ohne sie in der nativen Paketdatenbank zu erfassen. Ziele zur Deinstallation sind optional und können unvollständig sein, während spätere Upgrades Dateien überschreiben oder verwaisen lassen können.

Bevorzuge einen dieser kontrollierten Ansätze:

- ein offizielles natives Paket mit den Paketierungswerkzeugen der Distribution bauen
- unter einem klar getrennten Präfix wie `/usr/local` installieren, wenn die Richtlinie dies erlaubt
- Dateien mit einem unterstützten Mechanismus wie `DESTDIR` in einem temporären Paketierungsstamm bereitstellen
- gegebenenfalls ein unprivilegiertes Benutzerpräfix, eine isolierte Umgebung oder einen Container verwenden

`checkinstall` kann für einige `make install`-Arbeitsabläufe ein einfaches Paket erzeugen, ist aber weder universell noch ein Ersatz für ein geprüftes Paketierungsrezept in Distributionsqualität. Behandle es niemals als eine „immer gültige“ Regel. Prüfe vor jedem privilegierten Kopieren die bereitgestellte Dateiliste, Eigentumsverhältnisse, Berechtigungen, Pfade und den Plan zur Deinstallation oder Aktualisierung.

:::single-choice{#compile-source-code-destdir-purpose}
Welchen Zweck erfüllt eine unterstützte Staging-Installation mit `DESTDIR`?

::option[Beabsichtigte Installationsdateien zur Prüfung oder Paketierung unter einem temporären Stamm abzulegen.]{#compile-source-code-stage-root .correct explanation="Staging trennt die Dateisammlung von unmittelbaren Schreibvorgängen in das aktive Systempräfix."}
::option[Den Compiler in eine entfernte Paketquelle umzuwandeln.]{#compile-source-code-destdir-repository explanation="Die Variable leitet Installationspfade um und veröffentlicht keine Paketquellenmetadaten."}
::option[Die Kompilierung zu überspringen und stattdessen unbekannte Binärdateien herunterzuladen.]{#compile-source-code-destdir-download explanation="Staging wird nach einem Build angewendet und ersetzt keinen externen Binärdownload."}
:::

Nutze [Software unter Linux aus Quellcode bauen](https://labex.io/labs/comptia-build-software-from-source-code-in-linux-590853) in einer entbehrlichen Umgebung, um den Arbeitsablauf zu üben, ohne experimentelle Dateien in ein Produktivsystem zu mischen.

## Zusammenfassung

Du kannst Quellcode-Builds nun als kontrollierten Arbeitsablauf der Softwarelieferkette angehen.

1. Authentifiziere den Quellcode und prüfe seine Anweisungen als ausführbaren Code.
2. Installiere ausdrückliche Build-Anforderungen aus vertrauenswürdigen Paketquellen.
3. Konfiguriere, baue und teste ohne unnötige Privilegien.
4. Stelle Ausgaben bereit und prüfe sie vor der Systeminstallation.
5. Verfolge installierte Dateien mit nativer Paketierung oder einem bewusst gewählten isolierten Präfix.
