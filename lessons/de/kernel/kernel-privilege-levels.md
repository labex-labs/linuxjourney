---
lesson_id: "kernel-privilege-levels"
course_id: "kernel"
lang: "de"
order_index: 2
title: "Privilegienstufen"
description: "Erfahre, wie Prozessorprivilegien die Benutzerausführung von vertrauenswürdiger Kernelausführung trennen."
meta_title: "Privilegienstufen – Kernel"
meta_description: "Erkunde die Kernkonzepte der Linux-Privilegienstufen. Diese Lektion erklärt den Unterschied zwischen Kernel- und Benutzermodus, die Rolle von Schutzringen und wie Systemaufrufe privilegierten Hardwarezugriff ermöglichen. Verstehe, wie der Kernel Sicherheit und Kernelprivilegien verwaltet."
meta_keywords: "Linux-Privilegienstufen, Kernelmodus, Benutzermodus, Schutzringe, Systemaufrufe, privilegierter Zugriff, Kernelprivilegien, Unterschied zwischen Kernelmodus und Benutzermodus, Linux-Sicherheit"
---

Prozessoren stellen Privilegienmodi bereit, die vertrauliche Anweisungen und Speicherzugriffe einschränken. Linux verwendet diese Hardwaregrenze, damit gewöhnliche Anwendungsfehler weder direkt Kernelspeicher überschreiben noch Geräte neu konfigurieren können. Der Kernel steuert die Übergänge in die privilegierte Ausführung.

## Benutzermodus

Ein gewöhnlicher Prozess läuft im Benutzermodus innerhalb seines virtuellen Adressraums. Er kann frei rechnen und auf vom Kernel gewährte Speicherabbildungen zugreifen, die sehr groß sein können; Benutzermodus bedeutet nicht „nur wenig Speicher“. Er kann weder unmittelbar auf beliebigen physischen Speicher oder private Abbildungen eines anderen Prozesses noch auf privilegierte Prozessorsteuerungen zugreifen.

Seitentabellen und Schutzbits setzen den Speicherzugriff durch. Wenn ein Thread auf eine ungültige oder unzulässige Adresse verweist, löst der Prozessor eine Trap in den Kernel aus. Dieser kann einen gültigen Seitenfehler beheben oder ein Signal wie `SIGSEGV` zustellen.

:::single-choice{#kernel-privilege-user-mode-memory} Auf welchen Speicher kann ein Prozess im Benutzermodus gewöhnlich unmittelbar zugreifen?

::option[Auf jede physische RAM-Adresse und den gesamten Kernelspeicher.]{#kernel-privilege-all-physical explanation="Privilegien und der Schutz des virtuellen Speichers verhindern diese Zugriffe."}
::option[Ausschließlich auf ein festes Byte, das beim Prozessstart ausgewählt wird.]{#kernel-privilege-one-byte explanation="Ein Prozess kann viele abgebildete Bereiche besitzen und dennoch unprivilegiert bleiben."}
::option[Auf erlaubte Abbildungen in seinem eigenen virtuellen Adressraum.]{#kernel-privilege-own-mappings .correct explanation="Hardwareseitiger Seitenschutz beschränkt den Prozess auf Abbildungen, die mit entsprechendem Zugriff eingerichtet wurden."}
:::

## Kernelmodus

Der Kernelmodus erlaubt die Ausführung privilegierter Anweisungen und den Zugriff auf geschützte Kernelabbildungen, die für Speicherverwaltung, Scheduling, Interruptbehandlung und Treiber erforderlich sind. Auf x86 wird diese Linux-Aufteilung gewöhnlich als Ring 0 für den Kernel und Ring 3 für Benutzerprozesse beschrieben. Linux verwendet die Ringe 1 und 2 gewöhnlich nicht für die normale Prozessisolation.

Andere Architekturen verwenden andere Bezeichnungen und Mechanismen, beispielsweise Exception Levels. Virtualisierung fügt Beziehungen zwischen Hypervisor und Gast hinzu, die nicht in eine einfache Zeichnung mit zwei Ringen passen. Entscheidend ist das kontrollierte Privileg und nicht die x86-Ringnummer selbst.

:::single-choice{#kernel-privilege-x86-kernel-ring} In welchem x86-Schutzring läuft der Linux-Kernel gewöhnlich?

::option[Ring 3.]{#kernel-privilege-ring-three explanation="Ring 3 ist die herkömmliche Privilegienstufe des Benutzermodus."}
::option[Ring 0.]{#kernel-privilege-ring-zero .correct explanation="Der Kernel verwendet den privilegiertesten herkömmlichen x86-Ring."}
::option[Ring 7.]{#kernel-privilege-ring-seven explanation="Herkömmliche x86-Schutzringe sind von 0 bis 3 nummeriert."}
:::

## Kontrollierte Übergänge

Mehrere Ereignisse übertragen die Kontrolle an einen Kernel-Einstiegspunkt:

- Eine Systemaufrufanweisung fordert einen Kerneldienst an.
- Eine Ausnahme meldet einen Zustand wie einen Seitenfehler oder eine ungültige Anweisung.
- Ein Hardware-Interrupt meldet ein externes Ereignis.

Der Prozessor speichert den Ausführungskontext, ändert das Privileg entsprechend den konfigurierten Einstiegsmechanismen und beginnt mit der Ausführung vertrauenswürdigen Kernelcodes. Der Kernel validiert Anfrage und Zustand, führt die Arbeit aus oder lehnt sie ab und kehrt gegebenenfalls in den Benutzermodus zurück.

Die Anwendung wird nicht vorübergehend zu Kernelcode. Die CPU führt im Namen des Threads einen Kernelhandler mit vom Kernel gesteuerten Stacks und Abbildungen aus.

:::single-choice{#kernel-privilege-system-call-transition} Was geschieht während eines Systemaufrufübergangs?

::option[Der Benutzercode der Anwendung erhält uneingeschränkte Ausführung in Ring 0.]{#kernel-privilege-user-ring-zero explanation="Nach dem kontrollierten Einstieg wird ausschließlich vertrauenswürdiger Kernelcode ausgeführt."}
::option[Der Prozess ändert seine UID dauerhaft auf null.]{#kernel-privilege-uid-zero explanation="Ein Übergang des Prozessormodus schreibt keine Benutzerzugangsdaten um."}
::option[Die Kontrolle gelangt zu einem festgelegten Kernelhandler, der die Anfrage validiert.]{#kernel-privilege-kernel-handler .correct explanation="Der Prozessor ändert den Modus über einen konfigurierten Einstiegspfad und bewahrt den Benutzerkontext für die Rückkehr auf."}
:::

## CPU-Privilegien sind keine Benutzeridentität

Eine Anwendung, die als Linux-Benutzer `root` läuft, führt ihre Anweisungen gewöhnlich weiterhin im Benutzermodus aus. UID 0 beeinflusst Autorisierungsprüfungen des Kernels, erlaubt ihren Anweisungen aber keinen direkten Zugriff auf Kernelspeicher. Umgekehrt läuft Kernelcode unabhängig davon im privilegierten Modus, welcher Benutzer durch seinen Systemaufruf die Ausführung veranlasst hat.

Capabilities, Namensräume, seccomp, Sicherheitsmodule und cgroups schränken weiter ein, was ein Prozess anfordern darf. Diese geschichtete Richtlinie ist von der Hardwaregrenze zwischen Benutzer- und Kernelmodus getrennt.

:::single-choice{#kernel-privilege-root-distinction} Welche Aussage vergleicht die root-Identität und den Kernelmodus richtig?

::option[root ist eine User-Space-Zugangsangabe; der Kernelmodus ist ein Ausführungsprivileg des Prozessors.]{#kernel-privilege-credential-versus-mode .correct explanation="Ein root-Prozess stellt autorisierte Anfragen aus dem Benutzermodus, während vertrauenswürdiger Kernelcode die privilegierte Ausführung übernimmt."}
::option[Jede Anweisung im Besitz von root wird als ladbarer Kernelcode ausgeführt.]{#kernel-privilege-root-kernel-code explanation="Das UID-Eigentum verwandelt eine ausführbare Datei nicht in ein Kernelmodul."}
::option[Der Kernelmodus ist ein weiterer in `/etc/passwd` gespeicherter Benutzername.]{#kernel-privilege-kernel-username explanation="Prozessormodi sind Hardwarezustände und keine Anmeldekonten."}
:::

## Warum die Grenze wichtig ist

Die Grenze begrenzt Schäden durch gewöhnliche Fehler und stellt einen Ort für Zugriffsprüfungen bereit. Kernel-Schwachstellen und bösartige Module können sie jedoch überwinden. Halte Kernel und Firmware über vertrauenswürdige Kanäle aktuell, minimiere privilegierten Code und lade keine nicht vertrauenswürdigen Module.

Probleme mit spekulativer Ausführung und Seitenkanäle zeigen außerdem, dass Hardwareisolation fortlaufende Gegenmaßnahmen benötigt. Ein „anderer Ring“ ist eine Grundlage und kein vollständiger Sicherheitsbeweis.

:::single-choice{#kernel-privilege-boundary-limit} Garantiert die Trennung von Benutzer- und Kernelmodus vollständige Systemsicherheit?

::option[Ja; Kernel-Schwachstellen können Benutzerprozesse nicht beeinflussen.]{#kernel-privilege-no-kernel-vulns explanation="Eine Kernel-Schwachstelle kann das gesamte System gefährden."}
::option[Nein; Fehler in privilegiertem Code und Seitenkanäle können beabsichtigte Grenzen weiterhin überschreiten.]{#kernel-privilege-not-complete .correct explanation="Die Modusaufteilung verringert die Angriffsfläche, muss aber mit korrektem Kernelcode und zusätzlichen Gegenmaßnahmen kombiniert werden."}
::option[Ja; Hardwaremodi beseitigen die Notwendigkeit von Zugriffskontrollrichtlinien.]{#kernel-privilege-no-policy explanation="Zugangsdaten und Sicherheitsrichtlinien bleiben für die autorisierte gemeinsame Ressourcennutzung unerlässlich."}
:::

## Zusammenfassung

Du kannst nun Hardware-Ausführungsprivilegien von Linux-Kontobefugnissen unterscheiden.

1. Setze den Benutzermodus mit geschützten virtuellen Adressräumen in Beziehung.
2. Setze den Kernelmodus mit privilegierten Anweisungen und Abbildungen in Beziehung.
3. Behandle Systemaufrufe, Ausnahmen und Interrupts als kontrollierte Einstiegspunkte.
4. Trenne die Autorisierung der UID 0 von der Ausführung in Ring 0.
5. Betrachte Privilegienmodi als eine Schicht eines umfassenderen Sicherheitsentwurfs.
