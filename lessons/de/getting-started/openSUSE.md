---
lesson_id: "openSUSE"
course_id: "getting-started"
lang: "de"
order_index: 10
title: "openSUSE"
description: "Erfahre, wie openSUSE reguläre und fortlaufende Veröffentlichungen mit den Verwaltungswerkzeugen Zypper und YaST verbindet."
meta_title: "openSUSE Linux-Distribution"
meta_description: "Erfahre, was die Linux-Distribution openSUSE ist, wie sich Leap und Tumbleweed unterscheiden, wie die RPM-Paketverwaltung funktioniert und warum YaST openSUSE auszeichnet."
meta_keywords: "openSUSE Distribution, openSUSE Linux-Distribution, was ist openSUSE, openSUSE Leap, openSUSE Tumbleweed, YaST, RPM-Paketverwaltung"
---

## Was ist openSUSE?

openSUSE ist eine traditionsreiche Linux-Distribution, die für ihre Flexibilität, leistungsfähige Verwaltungswerkzeuge und mehrere Veröffentlichungsmodelle bekannt ist. Das Community-Projekt gilt sowohl auf Desktops als auch auf technischen Systemen als ausgereift und leistungsfähig.

openSUSE zeichnet sich unter anderem dadurch aus, dass es unterschiedlichen Benutzern verschiedene Wege anbietet. Manche wünschen sich eine stabile Grundlage, andere bevorzugen eine schnelllebigere Rolling-Release-Distribution.

## Leap und Tumbleweed

openSUSE ist für zwei wesentliche Veröffentlichungsmodelle bekannt: Leap und Tumbleweed. Leap ist die konservativere Variante und richtet sich an Benutzer, die Stabilität und ein traditionelles Veröffentlichungsmodell wünschen. Tumbleweed ist ein Rolling Release für alle, die kontinuierlich neuere Software erhalten möchten.

Diese Aufteilung verleiht openSUSE eine ungewöhnliche Flexibilität. Du kannst das passende Modell wählen, ohne dafür zu einer völlig anderen Distributionsfamilie wechseln zu müssen.

:::single-choice{#choose-opensuse-leap} Welche openSUSE-Variante eignet sich am besten für einen Benutzer, der eine traditionelle, regelmäßige Veröffentlichung wünscht?

::option[Tumbleweed]{#tumbleweed-release explanation="Tumbleweed ist die kontinuierlich aktualisierte Rolling-Release-Variante von openSUSE. Sie eignet sich besser für Benutzer, denen neuere Pakete besonders wichtig sind."}
::option[YaST]{#yast-not-release explanation="YaST ist ein Installations- und Konfigurationswerkzeug und kein Veröffentlichungsmodell von openSUSE. Es dient zur Verwaltung des Systems."}
::option[Leap]{#leap-release .correct explanation="Leap folgt einem regelmäßigen Veröffentlichungsmodell und legt Wert auf eine konservativere Systemgrundlage. Das entspricht der genannten Anforderung."}
:::

:::single-choice{#recognize-tumbleweed-model} Wodurch unterscheidet sich Tumbleweed von Leap?

::option[Es stellt getestete Paketaktualisierungen kontinuierlich bereit]{#continuous-tested-updates .correct explanation="Tumbleweed ist ein Rolling Release, das fortlaufend getestete Snapshots veröffentlicht. Benutzer erhalten neue Software, ohne auf eine reguläre Hauptversion warten zu müssen."}
::option[Es erhält Software ausschließlich über feste Hauptversionen]{#fixed-major-releases explanation="Feste, regelmäßige Veröffentlichungen beschreiben eher den Ansatz von Leap. Tumbleweed wird kontinuierlich aktualisiert."}
::option[Es entfernt die Paketverwaltung aus dem Betriebssystem]{#no-package-management explanation="Auch Tumbleweed verwaltet Softwarepakete und Systemaktualisierungen. Rolling Release bezeichnet den Zeitpunkt der Aktualisierungen, nicht das Fehlen einer Paketverwaltung."}
:::

## Paketverwaltung

openSUSE verwendet das RPM-Paketformat und Werkzeuge wie `zypper`, um Software zu installieren, zu aktualisieren und zu entfernen. Damit gehört es zu einer anderen Paketfamilie als Debian und Ubuntu, die `.deb`-Pakete und APT verwenden.

Kenntnisse über Paketfamilien helfen dir beim Vergleich von Linux-Distributionen. Einen umfassenderen Vergleich findest du unter [Eine Linux-Distribution auswählen](https://labex.io/lesson/choosing-a-linux-distribution).

:::single-choice{#identify-zypper-role} Wofür wird `zypper` unter openSUSE verwendet?

::option[Zur Auswahl grafischer Hintergrunddesigns]{#zypper-wallpaper explanation="Das Erscheinungsbild des Desktops wird mit Desktop-Werkzeugen konfiguriert. `zypper` verwaltet stattdessen Softwarepakete."}
::option[Zum Installieren, Aktualisieren und Entfernen von Softwarepaketen]{#zypper-package-tool .correct explanation="`zypper` ist das Befehlszeilenwerkzeug von openSUSE zur Paketverwaltung. Es arbeitet mit Software aus RPM-Paketquellen."}
::option[Zum Umwandeln von Tumbleweed in eine feste Debian-Version]{#zypper-debian explanation="Eine Paketverwaltung verwandelt openSUSE nicht in eine andere Distributionsfamilie. Leap und Tumbleweed bleiben Veröffentlichungsvarianten von openSUSE."}
:::

## YaST

Eines der bekanntesten Merkmale von openSUSE ist **YaST**. YaST ist ein Verwaltungs- und Einrichtungswerkzeug, mit dem du Software, Dienste, Speicher, Netzwerke und andere Systemaufgaben über eine zentrale Oberfläche verwalten kannst.

Das ist ein wesentlicher Grund, weshalb openSUSE Benutzer anspricht, die leistungsfähige Werkzeuge zur Systemverwaltung wünschen, ohne alles manuell konfigurieren zu müssen.

:::single-choice{#identify-yast-purpose} Was soll YaST bereitstellen?

::option[Eine fortlaufende Paketquelle, die ausschließlich die neuesten Anwendungen enthält]{#yast-repository explanation="Tumbleweed stellt das Rolling-Release-Modell bereit. YaST ist ein Verwaltungs- und Konfigurationswerkzeug und kein Softwarezweig."}
::option[Ein mit Debian- und Ubuntu-Systemen gemeinsam genutztes Paketformat]{#yast-package-format explanation="openSUSE verwendet RPM-Pakete, während Debian-basierte Systeme `.deb` nutzen. YaST selbst ist kein Paketformat."}
::option[Eine zentrale Oberfläche für Installation und Systemkonfiguration]{#yast-administration .correct explanation="YaST verbindet die Installation mit Modulen zur Konfiguration vieler Bereiche eines openSUSE-Systems. Es ist über grafische Oberflächen und das Terminal verfügbar."}
:::

## Typische Einsatzgebiete

openSUSE eignet sich gut für Desktops, Entwicklungssysteme und technische Arbeitsplätze. Es ist außerdem für Benutzer attraktiv, die eine umfassende Kontrolle über die Systemkonfiguration und zugleich ausgereifte Werkzeuge wünschen.

Im Vergleich zu stärker auf Einsteiger ausgerichteten Distributionen spricht openSUSE häufig Benutzer an, die etwas mehr Struktur und Einblick in die Verwaltung wünschen.

## Wer sollte openSUSE verwenden?

openSUSE ist eine überzeugende Wahl für Benutzer, die beim Veröffentlichungsmodell flexibel sein möchten und leistungsfähige Verwaltungswerkzeuge schätzen. Es kann sich für Einsteiger eignen, insbesondere wenn sie grafische Verwaltungsoberflächen mögen, spricht jedoch häufig vor allem fortgeschrittene Benutzer und technisch orientierte Desktop-Benutzer an.

## Weiterführende Literatur

- [openSUSE-Desktop-Distributionen](https://get.opensuse.org/desktop/)
- [Tumbleweed](https://get.opensuse.org/tumbleweed/)
- [Leap](https://get.opensuse.org/leap/)
- [YaST](https://yast.opensuse.org/)

Nach dieser Einführung in openSUSE empfehlen wir dir folgende LabEx-Kurse:

1. **[Schnellstart mit Linux](https://labex.io/courses/quick-start-with-linux)** – Lerne die Linux-Grundlagen durch angeleitete praktische Übungen.
2. **[Linux-Befehle online üben](https://labex.io/courses/linux-basic-commands-practice-online)** – Werde sicherer im Umgang mit der Linux-Befehlszeile.
3. **[Junior-Systemadministrator werden](https://labex.io/courses/become-a-junior-system-administrator)** – Vertiefe anschließend umfassendere Themen der Linux-Systemverwaltung.

## Zusammenfassung

Du kannst nun die Veröffentlichungsvarianten von openSUSE vergleichen und seine wichtigsten Verwaltungswerkzeuge benennen.

1. Wähle je nach gewünschtem Veröffentlichungsmodell zwischen Leap und Tumbleweed.
2. Erkläre, wie Tumbleweed kontinuierliche Aktualisierungen bereitstellt.
3. Erkenne Zypper als Werkzeug zur Paketverwaltung.
4. Erkenne YaST als zentrale Konfigurationsoberfläche.
