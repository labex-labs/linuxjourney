---
lesson_id: "fedora"
course_id: "getting-started"
lang: "de"
order_index: 6
title: "Fedora"
description: "Erfahre, wie Fedora als mit Red Hat verbundenes Gemeinschaftsprojekt aktuelle Linux-Technologie bereitstellt."
meta_title: "Fedora-Linux-Distribution"
meta_description: "Erfahre, was die Fedora-Linux-Distribution ist, wie Fedora mit Red Hat zusammenhängt, wie die Paketverwaltung mit DNF funktioniert und warum Fedora bei Entwicklern und Desktop-Nutzern beliebt ist."
meta_keywords: "Fedora Linux, Fedora-Linux-Distribution, was ist Fedora, Fedora Red Hat, Fedora-Veröffentlichungen, DNF-Paketverwaltung, Linux-Distribution"
---

## Was ist Fedora?

Fedora ist eine gemeinschaftlich entwickelte Linux-Distribution, die von Red Hat gefördert wird. Sie ist dafür bekannt, moderne Technologien, eine ausgefeilte Desktop-Erfahrung und gute Unterstützung für Entwickler und technisch versierte Nutzer bereitzustellen.

Fedora hat den Ruf, sich schneller weiterzuentwickeln als konservativere Distributionen und zugleich auf Qualität und Benutzerfreundlichkeit zu achten. Dieses Gleichgewicht macht es für Nutzer attraktiv, die ein modernes Linux-System möchten, ohne alles von Grund auf selbst aufzubauen.

:::single-choice{#identify-fedora-project-model}
Welche Aussage beschreibt das Fedora-Projekt richtig?

::option[Es ist eine eingestellte Version von Red Hat Enterprise Linux]{#discontinued-rhel explanation="Fedora ist eine aktive Distribution mit eigenen Veröffentlichungen. Es ist RHEL vorgelagert und keine veraltete RHEL-Version."}
::option[Es ist eine von einem einzigen Hardwarehersteller gepflegte Distribution]{#hardware-maintained explanation="Fedora arbeitet mit Hardwareanbietern zusammen, wird aber von der Gemeinschaft entwickelt und von Red Hat gefördert."}
::option[Es ist ein von Red Hat gefördertes Gemeinschaftsprojekt]{#community-sponsored .correct explanation="Fedora wird von einer Gemeinschaft mit Förderung und Unterstützung durch Red Hat entwickelt. Es bleibt eine eigenständige Gemeinschaftsdistribution."}
:::

## Was Fedora auszeichnet

Fedora zeichnet sich dadurch aus, dass es neue Linux-Funktionen häufig früher übernimmt als unternehmensorientierte Distributionen. Das macht es für Entwickler, Open-Source-Mitwirkende und Desktop-Nutzer attraktiv, die ein aktuelles System mit engen Verbindungen zu vorgelagerten Projekten wünschen.

Außerdem ist Fedora für eine aufgeräumte Standardumgebung bekannt. Fedora Workstation ist besonders bei Entwicklern beliebt, die einen modernen Desktop, aktuelle Werkzeuge und gute Unterstützung für Container, Virtualisierung und andere Entwicklungsabläufe möchten.

:::single-choice{#match-fedora-user}
Welches Nutzerziel passt am besten zu Fedora Workstation?

::option[Eine Unternehmensversion viele Jahre unverändert behalten]{#long-enterprise-lifecycle explanation="Ein langer, konservativer Unternehmenslebenszyklus entspricht eher der Rolle von RHEL. Fedora folgt einem schnelleren Zeitplan für Veröffentlichungen und Upgrades."}
::option[Aktuelle Entwicklerwerkzeuge in einem ausgefeilten Desktop-System verwenden]{#current-developer-desktop .correct explanation="Fedora Workstation verbindet einen sorgfältig zusammengestellten Desktop mit aktuellen Werkzeugen für Entwicklung, Container und Virtualisierung. Das entspricht diesem Ziel unmittelbar."}
::option[Jede Systemkomponente manuell aus dem Quellcode erstellen]{#fedora-manual-source explanation="Fedora stellt ein vollständiges paketiertes System bereit und verlangt nicht, dass Nutzer jede Komponente selbst erstellen. Dieses Ziel beschreibt eher einen spezielleren Arbeitsablauf."}
:::

## Fedora und Red Hat

Fedora spielt im Red-Hat-Ökosystem eine wichtige Rolle. Neue Technologien und Änderungen erscheinen häufig zuerst in Fedora, und ein Teil dieser Arbeit beeinflusst später Red Hat Enterprise Linux. Diese Beziehung erklärt, warum Fedora aktueller wirkt, während RHEL konservativer und stärker auf Unternehmen ausgerichtet ist.

Wenn du Fedora mit unternehmensorientierten Optionen vergleichen möchtest, sieh dir [Red Hat Enterprise Linux](https://labex.io/lesson/red-hat-enterprise-linux) an. Wenn du noch Distributionsfamilien vergleichst, bietet [Eine Linux-Distribution auswählen](https://labex.io/lesson/choosing-a-linux-distribution) einen breiteren Überblick.

:::single-choice{#explain-fedora-upstream-role}
Was bedeutet Fedoras vorgelagerte Beziehung zu RHEL?

::option[RHEL-Veröffentlichungen werden anschließend unverändert nach Fedora kopiert]{#rhel-copied-to-fedora explanation="Das kehrt die Beziehung um. Fedora entwickelt sich schneller und dient als vorgelagerte Quelle, statt eine spätere Kopie von RHEL zu sein."}
::option[Fedora und RHEL liefern immer identische Softwareversionen aus]{#identical-software-versions explanation="Die Distributionen verfolgen unterschiedliche Veröffentlichungsziele und Zeitpläne. RHEL wählt Technologien aus und stabilisiert sie, statt jede Fedora-Version zu übernehmen."}
::option[In Fedora entwickelte Arbeit kann später RHEL beeinflussen]{#fedora-influences-rhel .correct explanation="Fedora ist ein Ort, an dem neuere Technologien frühzeitig integriert werden. Ein Teil dieser Arbeit trägt später zu Red Hats Unternehmensplattform bei."}
:::

## Fedora-Veröffentlichungen

Fedora folgt einem regelmäßigen Veröffentlichungszyklus mit zwei Hauptversionen in den meisten Jahren und etwa dreizehn Monaten Support für jede Veröffentlichung. Im Vergleich zu konservativeren Distributionen stellt Fedora neuere Kernel, Desktop-Umgebungen und Entwicklerwerkzeuge tendenziell schneller bereit.

Damit eignet sich Fedora gut für Nutzer, die aktuelle Software möchten, aber eine strukturierte, verbreitete Linux-Distribution einem stärker manuellen Rolling-Release-System vorziehen.

:::single-choice{#plan-fedora-upgrades}
Welche Wartung sollte ein Fedora-Nutzer aufgrund dieses Veröffentlichungsmodells einplanen?

::option[Keine Versionsupgrades während der gesamten Lebensdauer des Computers]{#no-version-upgrades explanation="Fedora-Versionen besitzen einen begrenzten Supportzeitraum. Um weiterhin eine unterstützte Version zu verwenden, musst du im Laufe der Zeit auf neuere Veröffentlichungen wechseln."}
::option[Regelmäßige Upgrades, um eine unterstützte Veröffentlichung zu verwenden]{#regular-release-upgrades .correct explanation="Fedora-Veröffentlichungen folgen einem vergleichsweise schnellen Zeitplan und erhalten ungefähr dreizehn Monate lang Aktualisierungen. Nutzer sollten regelmäßige Versionsupgrades einplanen."}
::option[Fortlaufende Paketänderungen ohne eigenständige Systemveröffentlichungen]{#no-distinct-releases explanation="Fedora veröffentlicht eigenständige Hauptversionen und arbeitet nicht wie eine herkömmliche Rolling-Release-Distribution. Seine Pakete sind aktuell, aber die Veröffentlichungen bleiben wichtig."}
:::

## Paketverwaltung

Fedora verwendet das RPM-Paketformat und die Paketverwaltung DNF, um Software zu installieren, zu aktualisieren und zu entfernen. DNF ist ein zentraler Bestandteil der Fedora-Erfahrung und eines der wichtigsten Werkzeuge, mit denen Nutzer ihr System aktuell halten.

Die Paketverwaltung unter Fedora ist unkompliziert und fügt sich natürlich in die breitere Red-Hat-Systemfamilie ein.

:::single-choice{#identify-fedora-package-tool}
Welches Werkzeug verwendet Fedora für die übergeordnete Paketverwaltung?

::option[APT]{#fedora-apt-tool explanation="APT gehört zu Debian-basierten Distributionen. Fedora gehört zur RPM-Paketfamilie und verwendet DNF."}
::option[DNF]{#fedora-dnf-tool .correct explanation="DNF installiert, aktualisiert und entfernt Pakete aus den Fedora-Paketquellen. Darunter verwenden Fedora-Pakete das RPM-Format."}
::option[Pacman]{#fedora-pacman-tool explanation="Pacman ist die Paketverwaltung von Arch Linux. Fedoras übergeordnetes Paketwerkzeug ist DNF."}
:::

## Häufige Einsatzgebiete

Fedora wird häufig auf Entwickler-Arbeitsstationen, technischen Desktops und Laptops eingesetzt. Es ist besonders für Nutzer attraktiv, die eine moderne Linux-Umgebung zum Programmieren, für Container, virtuelle Maschinen und allgemeine Desktop-Arbeit wünschen.

Fedora kann zwar auch auf Servern eingesetzt werden, wird jedoch vor allem als aktuelle, entwicklerfreundliche Linux-Distribution wahrgenommen.

## Ist Fedora einsteigerfreundlich?

Fedora kann einsteigerfreundlich sein, passt gewöhnlich aber besser zu Nutzern, die sich mit einem etwas schneller verändernden System wohlfühlen. Es ist zugänglicher als sehr manuelle Distributionen, kann jedoch weniger konservativ als Debian und weniger auf Einsteiger ausgerichtet als Ubuntu oder Linux Mint wirken.

Für Nutzer, die eine moderne Linux-Distribution möchten und bereit sind, unterwegs etwas dazuzulernen, ist Fedora eine gute Option.

## Weiterführende Literatur

- [Fedora Workstation](https://fedoraproject.org/workstation/)
- [Fedora-Dokumentation](https://docs.fedoraproject.org/)
- [Lebenszyklus von Fedora-Veröffentlichungen](https://docs.fedoraproject.org/en-US/releases/lifecycle/)
- [Arbeitsgruppe Fedora Workstation](https://docs.fedoraproject.org/en-US/workstation-working-group/)

Um nach dieser Einführung in Fedora praktische Linux-Kenntnisse aufzubauen, empfehlen wir diese LabEx-Kurse:

1. **[Schnellstart mit Linux](https://labex.io/courses/quick-start-with-linux)** - Behandle die Linux-Grundlagen, die für viele Distributionen gelten.
2. **[Linux-Befehle online üben](https://labex.io/courses/linux-basic-commands-practice-online)** - Festige die Gewohnheiten auf der Befehlszeile, die bei der täglichen Arbeit mit Linux wichtig sind.
3. **[Paketverwaltung mit RPM und DNF](https://labex.io/courses/rpm-and-dnf-package-management)** - Übe Konzepte der Paketverwaltung mit RPM und DNF.

## Zusammenfassung

Du kannst nun Fedoras Rolle als aktuelle, gemeinschaftlich entwickelte Distribution im Red-Hat-Ökosystem erklären.

1. Beschreibe Fedoras Gemeinschafts- und Fördermodell.
2. Erkenne die Nutzer und Arbeitsabläufe, die Fedora Workstation unterstützt.
3. Erkläre Fedoras vorgelagerte Beziehung zu RHEL.
4. Plane regelmäßige Upgrades auf neue Fedora-Versionen ein.
5. Bestimme DNF als Fedoras Paketverwaltungswerkzeug.
