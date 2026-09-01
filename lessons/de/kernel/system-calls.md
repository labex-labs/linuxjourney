---
lesson_id: "system-calls"
course_id: "kernel"
lang: "de"
order_index: 3
title: "Systemaufrufe"
description: "Erfahre, wie User-Space-Code Linux-Kerneldienste aufruft und wie du Aufrufe sicher mit `strace` untersuchst."
meta_title: "Systemaufrufe – Kernel"
meta_description: "Erkunde die Grundlagen eines Systemaufrufs unter Linux. Erfahre, wie User-Space-Prozesse mit Systemaufrufen (Syscalls) Dienste vom Kernel anfordern, den Modus wechseln und wie die Syscall-Tabelle funktioniert. Verwende `strace`, um Systemaufrufe in Aktion zu sehen."
meta_keywords: "Systemaufruf Linux, Systemaufrufe, Syscall-Tabelle, Kernelmodus, Benutzermodus, strace, Linux-Kernel, Syscall-API"
---

Ein Systemaufruf ist ein festgelegter Einstieg in den Kernel, über den User-Space-Code einen Vorgang anfordert, etwa eine Datei zu öffnen, Speicher abzubilden, einen Prozess zu erzeugen oder Netzwerkdaten zu senden. Der Kernel prüft Argumente, Zugangsdaten, Objektzustand und Sicherheitsrichtlinie, bevor er die Anfrage ausführt.

## Bibliotheken und die Systemaufruf-ABI

Anwendungen rufen gewöhnlich Funktionen der C-Bibliothek auf, statt architekturspezifische Einstiegsanweisungen selbst zu schreiben. Eine Bibliothekskapselung bereitet Register und Speicher gemäß der Systemaufruf-ABI vor, tritt in den Kernel ein und übersetzt das Ergebnis in die Konvention der jeweiligen Sprache.

Die Beziehung ist nicht immer eine Funktion zu einem Systemaufruf:

- Eine Bibliotheksfunktion kann mehrere Systemaufrufe verbinden.
- Manche Funktionen arbeiten vollständig im User-Space.
- Eine optimierte vDSO-Funktion kann bestimmte vom Kernel gepflegte Daten ohne vollständigen Modusübergang beziehen.
- Ein Systemaufruf kann viele übergeordnete APIs unterstützen.

:::single-choice{#system-calls-library-wrapper} Was tut eine typische Systemaufrufkapselung von libc?

::option[Sie bereitet ABI-Argumente vor, tritt in den Kernel ein und übersetzt das Ergebnis.]{#system-calls-wrapper-role .correct explanation="Die Kapselung verbirgt architekturspezifische Aufrufkonventionen hinter einer gewöhnlichen Bibliotheksschnittstelle."}
::option[Sie gewährt der Anwendung uneingeschränkten Zugriff auf Kernelspeicher.]{#system-calls-wrapper-unrestricted explanation="Der Kerneleintritt bleibt kontrolliert, und der Kernel validiert die Anfrage."}
::option[Sie kompiliert den Kernel bei jedem Funktionsaufruf neu.]{#system-calls-wrapper-compile explanation="Ein Laufzeitaufruf verwendet den bereits laufenden Kernel."}
:::

## In den Kernel eintreten und zurückkehren

Die Kapselung legt eine Systemaufrufnummer und Argumente an architekturseitig festgelegten Orten ab und führt anschließend eine Einstiegsanweisung wie `syscall` auf x86-64 oder `svc` auf AArch64 aus. Der Prozessor wechselt zu einem konfigurierten privilegierten Einstiegspunkt, und der Kernel leitet die Anfrage weiter.

Nach dem Abschluss gibt der Kernel einen Wert oder eine Fehleranzeige zurück. Kapselungen der C-Bibliothek geben bei Fehlern gewöhnlich `-1` zurück und setzen das Thread-lokale `errno`. Andere Sprachen und Laufzeiten stellen unterschiedliche Fehlertypen bereit.

Jeden Einstieg als „Software-Interrupt“ zu bezeichnen, ist auf aktuellen Architekturen ungenau. Traps, schnelle Systemaufrufanweisungen und Supervisor-Aufrufe implementieren verwandte kontrollierte Übergänge auf unterschiedliche Weise.

:::single-choice{#system-calls-entry-result} Wer validiert die Argumente und Autorisierung eines Systemaufrufs?

::option[Die Shell-Eingabeaufforderung, bevor der Prozess startet.]{#system-calls-shell-validates explanation="Ein Prozess kann unabhängig von einer Shell Systemaufrufe ausführen, und Kernelprüfungen bleiben erforderlich."}
::option[Die Kernelimplementierung des angeforderten Dienstes.]{#system-calls-kernel-validates .correct explanation="Der privilegierte Handler prüft Zeiger, Objektzustand, Zugangsdaten und Richtlinie, bevor er handelt."}
::option[Die Partitionstabelle des Datenträgers.]{#system-calls-partition-validates explanation="Metadaten der Speicheraufteilung autorisieren keine beliebigen Kerneldienste."}
:::

## Nummern und Kompatibilität

Systemaufrufnummern und Aufrufkonventionen sind architekturspezifisch. Derselbe symbolische Aufruf kann in einer anderen ABI eine andere Nummer oder Strukturaufteilung besitzen. Kernelveröffentlichungen können Systemaufrufe hinzufügen, während stabile User-Space-ABIs bestehendes Verhalten bewahren sollen.

Ein unprivilegierter Prozess kann keine beliebigen neuen Handler in die Syscall-Tabelle des laufenden Kernels einfügen. Eine Erweiterung der Schnittstelle erfordert Kernelcode und einen sorgfältigen ABI-Entwurf. Funktionen wie seccomp können filtern, welche Aufrufe ein Prozess ausführen darf, erzeugen aber keine neuen Kernelimplementierungen.

:::single-choice{#system-calls-number-portability} Warum sollte eine Anwendung keine Systemaufrufnummern einer anderen Architektur fest codieren?

::option[Nummern und Aufrufkonventionen sind ABI-spezifisch.]{#system-calls-abi-specific .correct explanation="Eine auf einer Architektur sinnvolle Nummer kann auf einer anderen einen anderen Vorgang bezeichnen oder fehlen."}
::option[Systemaufrufe werden nach dem aktuellen Arbeitsverzeichnis benannt.]{#system-calls-directory-names explanation="Pfade definieren nicht die Nummerierungs-ABI von Systemaufrufen."}
::option[Jeder Prozess erhält beim Start eine zufällige Syscall-Tabelle.]{#system-calls-random-table explanation="Die ABI des laufenden Kernels ist für eine Architektur stabil und wird nicht pro Prozess zufällig erzeugt."}
:::

## Mit `strace` verfolgen

Verfolge einen einfachen Befehl und speichere die Ausgabe getrennt:

```bash
$ strace -o trace.log -- ls
```

Folge autorisierten Kindprozessen mit `-f` oder begrenze die Ausgabe mit einem Ausdruck wie:

```bash
$ strace -f -e trace=%file -o trace.log -- command
```

`strace` kann Pfade, Argumente, aus der Umgebung stammende Daten, Netzwerkadressen, Fragmente von Dateiinhalten und fälschlich über Argumente übergebene Zugangsdaten offenlegen. Speichere Traces mit restriktiven Berechtigungen und entferne sie gemäß der Richtlinie für Vorfallsdaten.

:::single-choice{#system-calls-strace-purpose} Was beobachtet `strace` in erster Linie?

::option[Ausschließlich im Quellcode ausgeführte Zeilen der Anwendung.]{#system-calls-strace-source-lines explanation="Die Verfolgung auf Quellcodeebene benötigt Debugger oder Instrumentierung mit Symbolen."}
::option[Systemaufrufe und Signale an der Grenze zwischen Benutzer und Kernel.]{#system-calls-strace-boundary .correct explanation="Es meldet Anfragen, Argumente, Ergebnisse und Signalereignisse verfolgter Prozesse."}
::option[Die physische Spannung jedes CPU-Kerns.]{#system-calls-strace-voltage explanation="Hardwaretelemetrie liegt außerhalb der Systemaufrufverfolgung."}
:::

## Traces sorgfältig interpretieren

Tracing verändert Zeitabläufe und kann erheblichen Mehraufwand verursachen. Ein fehlgeschlagener Aufruf kann eine erwartete Prüfung sein, und der am Ende sichtbare Fehler kann aus einem früheren Vorgang oder einer Anwendungsrichtlinie entstehen. Löse Dateideskriptoren auf, verfolge Prozessbeziehungen und setze die Angaben mit Anwendungsprotokollen in Beziehung.

Berechtigungen und ptrace-Sicherheitsrichtlinien schränken ein, welche Prozesse verfolgt werden können. Hänge dich nicht ohne Autorisierung an den Prozess eines anderen Benutzers oder einen Produktivprozess; Unterbrechungen und Zeitveränderungen können das Dienstverhalten beeinflussen.

:::single-choice{#system-calls-strace-failure} Bedeutet ein einzelner fehlgeschlagener Systemaufruf in einem Trace zwangsläufig, dass die Anwendung defekt ist?

::option[Ja; jeder von null verschiedene Rückgabewert beendet Linux sofort.]{#system-calls-nonzero-terminates explanation="Anwendungen behandeln routinemäßig Systemaufruffehler, ohne dass das System ausfällt."}
::option[Nein; Programme prüfen häufig Alternativen und behandeln erwartete Fehler.]{#system-calls-expected-failure .correct explanation="Interpretiere den Rückgabewert im Kontrollfluss- und Anwendungskontext statt isoliert."}
::option[Ja; der Kernel gibt niemals erwartete Fehler zurück.]{#system-calls-no-expected-errors explanation="Fehler wie fehlende Pfade oder nicht unterstützte Vorgänge sind normale API-Ergebnisse."}
:::

## Zusammenfassung

Du kannst einen Systemaufruf nun von der Bibliotheks-API bis zur validierten Kernelarbeit verfolgen.

1. Trenne übergeordnete Funktionen von der Systemaufruf-ABI.
2. Setze architekturspezifische Einstiegsanweisungen mit kontrollierter Kernelweiterleitung in Beziehung.
3. Behandle Systemaufrufnummern und Strukturen als architekturspezifisch.
4. Verwende gefilterte `strace`-Ausgaben und schütze dabei vertrauliche Daten.
5. Interpretiere Fehler und Tracing-Mehraufwand im Anwendungskontext.
