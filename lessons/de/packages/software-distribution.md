---
lesson_id: "software-distribution"
course_id: "packages"
lang: "de"
order_index: 1
title: "Softwareverteilung"
description: "Erfahre, wie Upstream-Projekte, Distributionsbetreuer, Pakete und Paketformate eine Linux-Softwarelieferkette bilden."
meta_title: "Softwareverteilung – Pakete"
meta_description: "Erkunde den besten Weg, Linux zu lernen, indem du Softwareverteilung, Paketverwaltungen und Paketformate wie .deb und .rpm verstehst. Ein wichtiger Teil unseres kostenlosen Linux-Zertifizierungskurses."
meta_keywords: "Linux-Softwareverteilung, Paketverwaltung, .deb, .rpm, bester Weg Linux zu lernen, kostenloser Linux-Zertifizierungskurs, beste Ressourcen zum Linux-Lernen, bester Weg die Linux-Befehlszeile zu lernen, Softwareinstallation"
---

Linux-Software wird gewöhnlich als Pakete ausgeliefert, die von distributionsspezifischen Werkzeugen verwaltet werden. Ein Paket fasst installierbare Dateien mit Metadaten zusammen, damit das System Versionen, Abhängigkeiten, Eigentum, Prüfsummen und Aktionen im Lebenszyklus nachverfolgen kann.

## Was ein Paket enthält

Ein Binärpaket kann ausführbare Dateien, Bibliotheken, Dokumentation, Standardkonfiguration, Dienstdefinitionen und weitere Ressourcen enthalten. Außerdem führt es Metadaten mit wie:

- Paketname und Version
- Zielarchitektur und Distributionskontext
- deklarierte Abhängigkeiten und Konflikte
- Dateilisten und Integritätsinformationen
- optionale Skripte oder Trigger, die bei Lebenszyklusvorgängen verwendet werden

Nicht jedes Paket ist eine interaktive Anwendung. Ein Paket kann eine Bibliothek, eine Kernelkomponente, Sprachdaten, Schriftarten, Debug-Symbole oder Metadaten bereitstellen, die von einer Sammlung anderer Pakete abhängen.

:::single-choice{#software-distribution-package-metadata} Welche Information ist gewöhnlich Paketmetadaten und keine ausführbare Anwendungsdatei?

::option[Die CPU-Anweisungen, die die Anwendung implementieren.]{#software-distribution-executable-code explanation="Kompilierte Anweisungen sind Nutzinhalt des Pakets und keine Abhängigkeitsmetadaten."}
::option[Deklarierte Abhängigkeitsbeziehungen.]{#software-distribution-dependencies .correct explanation="Pakete beschreiben erforderliche oder in Konflikt stehende Pakete, damit Verwaltungswerkzeuge über die Installation entscheiden können."}
::option[Das ungespeicherte Dokument des Benutzers, das derzeit im Speicher geöffnet ist.]{#software-distribution-user-document explanation="Laufzeitdaten des Benutzers gehören nicht zu den Metadaten des verteilten Pakets."}
:::

## Rollen von Upstream und Distribution

Ein Upstream-Projekt entwickelt und veröffentlicht den ursprünglichen Quellcode. Die Betreuer einer Linux-Distribution passen anschließend ausgewählte Veröffentlichungen an die Distribution an. Ihre Arbeit kann die Prüfung von Lizenzen, das Anwenden von Integrations- oder Sicherheitspatches, das Festlegen von Build-Anweisungen, das Aufteilen der Ausgabe in Pakete, das Deklarieren von Abhängigkeiten, das Ausführen von Tests und die Pflege von Aktualisierungen umfassen.

Die Build-Infrastruktur der Distribution erzeugt Pakete für unterstützte Veröffentlichungen und Architekturen. Werkzeuge für Paketquellen veröffentlichen Metadaten und Signaturen, die Clients überprüfen können. Die genauen Zuständigkeiten unterscheiden sich: Einige Upstream-Projekte veröffentlichen eigene Pakete, während Distributionen unabhängig aus dem Quellcode bauen können.

:::single-choice{#software-distribution-maintainer-role} Welche Aufgabe gehört gewöhnlich zu den Tätigkeiten eines Distributionspaketbetreuers?

::option[Upstream-Quellcode an Build- und Abhängigkeitsregeln der Distribution anzupassen.]{#software-distribution-maintainer-integrates .correct explanation="Betreuer passen Software an Distributionsrichtlinien, Builds, Abhängigkeiten und unterstützte Umgebungen an."}
::option[Das lokale Kontopasswort jedes Benutzers auszuwählen.]{#software-distribution-maintainer-passwords explanation="Lokale Authentifizierungsdaten haben nichts mit der Paketpflege zu tun."}
::option[Jeden installierten Prozess auf einer CPU einzuplanen.]{#software-distribution-maintainer-scheduler explanation="Der laufende Kernel-Scheduler kümmert sich nach der Installation um die CPU-Ausführung."}
:::

## Verbreitete native Paketformate

Zwei weitverbreitete native Formate sind:

- `.deb`, verwendet von Debian und davon abgeleiteten Distributionen wie Ubuntu und Linux Mint
- `.rpm`, verwendet von Fedora, Red Hat Enterprise Linux und vielen verwandten Distributionen

Es gibt weitere native und distributionsübergreifende Formate. Eine passende Dateinamenerweiterung allein garantiert keine Kompatibilität: Paketarchitektur, Distributionsveröffentlichung, Bibliotheksversionen, Richtlinien, Signaturen und Abhängigkeiten spielen ebenfalls eine Rolle.

:::single-choice{#software-distribution-debian-format} Welches native Paketformat verwenden Debian und Ubuntu?

::option[`.deb`]{#software-distribution-format-deb .correct explanation="Paketwerkzeuge der Debian-Familie verwenden das Archivformat `.deb`."}
::option[`.rpm`]{#software-distribution-format-rpm explanation="RPM ist das native Format von Fedora, RHEL und verwandten Distributionsfamilien."}
::option[`.tar`]{#software-distribution-format-tar explanation="Ein tar-Archiv ist ein allgemeiner Container und stellt für sich allein keine Debian-Paketmetadaten und Lebenszyklussemantik bereit."}
:::

## Warum eine verwaltete Verteilung wichtig ist

Eine Paketverwaltung erfasst den installierten Zustand und koordiniert Änderungen über mehrere Pakete hinweg. Die Installation aus vertrauenswürdigen Paketquellen der Distribution bietet gewöhnlich konsistente Abhängigkeitsauflösung, Signaturprüfung, Sicherheitsaktualisierungen und saubere Entfernung. Eine manuell kopierte Binärdatei oder Quellinstallation kann angemessen sein, wird aber nicht automatisch Teil dieses verwalteten Lebenszyklus.

Das Vertrauen hängt weiterhin von der Konfiguration der Paketquellen und den Signaturschlüsseln ab. Ein kryptografisch gültiges Paket beweist die Verbindung mit einem vertrauenswürdigen Schlüssel, nicht aber, dass beliebige Drittanbietersoftware sicher oder geeignet ist. Bevorzuge nach Möglichkeit die Paketquellen der Distribution und bewerte jede externe Quelle, bevor du ihr Installationsrechte gewährst.

:::single-choice{#software-distribution-package-manager-benefit} Was ist ein Vorteil der Installation über eine vertrauenswürdige Paketquelle?

::option[Die Verwaltung kann Versionen verfolgen und deklarierte Abhängigkeiten auflösen.]{#software-distribution-managed-lifecycle .correct explanation="Metadaten der Paketquelle und Aufzeichnungen des installierten Zustands unterstützen koordinierte Installation, Aktualisierung und Entfernung."}
::option[Jedes installierte Programm wird gegen Sicherheitslücken immun.]{#software-distribution-no-vulnerabilities explanation="Die Paketverwaltung unterstützt Aktualisierungen, kann aber keine fehlerfreie Software garantieren."}
::option[Alle Pakete sämtlicher Distributionen werden austauschbar.]{#software-distribution-universal-compatibility explanation="Native Pakete bleiben an Formate, Veröffentlichungen, Architekturen und Abhängigkeitsumgebungen gebunden."}
:::

Nutze das Lab [Pakete mit RPM verwalten](https://labex.io/labs/rhel-managing-packages-with-rpm-in-linux-590868), um Paketmetadaten und Integrität zu prüfen, oder das Lab [Software aus Quellcode erstellen](https://labex.io/labs/comptia-build-software-from-source-code-in-linux-590853), um einen Quellcode-Arbeitsablauf mit verwalteten Paketen zu vergleichen.

## Zusammenfassung

Du kannst nun die wesentlichen Bestandteile der Linux-Softwareverteilung bestimmen.

1. Trenne Paketnutzdateien von Paketmetadaten.
2. Unterscheide Upstream-Entwicklung von Distributionsintegration.
3. Ordne `.deb` und `.rpm` ihren Distributionsfamilien zu.
4. Bewerte Kompatibilität und Vertrauen über die Dateinamenerweiterung hinaus.
