---
lesson_id: "package-dependencies"
course_id: "packages"
lang: "de"
order_index: 4
title: "Paketabhängigkeiten"
description: "Erfahre, wie Paketmetadaten erforderliche Fähigkeiten, Versionen, Konflikte und Beziehungen zu gemeinsam genutzten Bibliotheken ausdrücken."
meta_title: "Paketabhängigkeiten – Pakete"
meta_description: "Lerne Linux-Paketabhängigkeiten kennen und erfahre, warum sie für die Softwareinstallation entscheidend sind. Dieser Leitfaden erklärt gemeinsam genutzte Bibliotheken und wie die Paketverwaltung Abhängigkeiten behandelt, um defekte Software zu vermeiden."
meta_keywords: "Linux-Paketabhängigkeiten, gemeinsam genutzte Bibliotheken, Linux-Pakete, Paketverwaltung, Linux-Softwareinstallation, Linux-Tutorial, Linux für Einsteiger, Linux-Leitfaden"
---

Eine Paketabhängigkeit besagt, dass ein Paket für seine Installation oder seinen Betrieb ein anderes Paket, eine Fähigkeit oder eine kompatible Version benötigt. Paketverwaltungen mit Paketquellenkenntnis berechnen anhand dieser Metadaten eine konsistente Menge von Änderungen, statt jedes Archiv isoliert zu behandeln.

## Abhängigkeitsbeziehungen

Paketmetadaten können mehr als einen einfachen erforderlichen Namen ausdrücken. Je nach Distributionsformat können Beziehungen Folgendes umfassen:

- erforderliche Abhängigkeiten
- Mindest-, Höchst- oder genaue Versionsbeschränkungen
- Alternativen, bei denen einer von mehreren Anbietern eine Anforderung erfüllt
- Empfehlungen oder Vorschläge mit schwächerer Semantik
- Konflikte, Brüche oder Ersetzungen
- virtuelle Fähigkeiten, die von mehr als einem Paket bereitgestellt werden

Mit diesen Regeln kann ein Solver eine Gruppe von Paketversionen auswählen, die mit den konfigurierten Paketquellen, der Architektur und dem installierten Zustand kompatibel ist. Eine Lösung kann Upgrades, Entfernungen oder die Wahl zwischen Anbietern erfordern. Prüfe daher die vorgeschlagene Transaktion, bevor du sie genehmigst.

:::single-choice{#package-dependencies-solver-role} Was versucht ein Abhängigkeits-Solver mit Paketquellenkenntnis zu erzeugen?

::option[Eine konsistente Gruppe von Paketversionen und erforderlichen Änderungen.]{#package-dependencies-consistent-set .correct explanation="Der Solver bewertet deklarierte Beziehungen über installierte und verfügbare Pakete hinweg."}
::option[Ein neues Benutzerkonto für jede installierte Anwendung.]{#package-dependencies-user-account explanation="Das Erstellen eines Kontos kann eine Lebenszyklusaktion eines Pakets sein, ist aber nicht der Zweck der Abhängigkeitsauflösung."}
::option[Eine komprimierte Kopie jeder Datei in der Paketquelle.]{#package-dependencies-compressed-repository explanation="Der Solver wählt Metadaten und Pakete aus; er archiviert nicht die gesamte Paketquelle."}
:::

## Gemeinsam genutzte Bibliotheken als Abhängigkeiten

Eine gemeinsam genutzte Bibliothek enthält kompilierten Code, den mehrere Programme zur Laufzeit einbinden können. Die gemeinsame Nutzung verringert doppelte Implementierungen und erlaubt Distributionen, eine gemeinsame Bibliothek unabhängig zu aktualisieren. Programme sind jedoch von einer kompatiblen Binärschnittstelle der Anwendung oder ABI abhängig.

Auf ELF-basierten Linux-Systemen kann eine ausführbare Datei einen benötigten Bibliotheksnamen wie einen SONAME erfassen. Der dynamische Linker findet beim Programmstart eine passende installierte Bibliothek. Paketmetadaten stellen diese Anforderung gewöhnlich als Abhängigkeit von dem Paket oder der Fähigkeit dar, das beziehungsweise die die kompatible Bibliothek bereitstellt.

:::single-choice{#package-dependencies-shared-library} Was ist eine gemeinsam genutzte Bibliothek?

::option[Kompilierter Code, den mehrere Programme laden und verwenden können.]{#package-dependencies-library-code .correct explanation="Eine gemeinsam genutzte Bibliothek stellt wiederverwendbare Binärschnittstellen bereit, statt in jedes Programm eine getrennte Implementierung einzubetten."}
::option[Eine Liste von Paketquellen, die unabhängige Distributionen gemeinsam nutzen.]{#package-dependencies-shared-repository explanation="Die Konfiguration von Paketquellen und ausführbarer Bibliothekscode sind unterschiedliche Konzepte."}
::option[Eine Textdatei mit dem Shell-Verlauf jedes Benutzers.]{#package-dependencies-shared-history explanation="Der Shell-Verlauf sind Benutzerdaten und keine Programmbibliotheksabhängigkeit."}
:::

## Versions- und ABI-Kompatibilität

Eine Datei mit einem ähnlichen Bibliotheksnamen reicht nicht aus. Die erforderliche ABI, Architektur, Symbole und manchmal Mindestversion müssen übereinstimmen. Das manuelle Ersetzen einer Distributionsbibliothek kann jedes abhängige Programm beschädigen, selbst wenn der Dateiname richtig aussieht.

Paketbetreuer codieren Bibliotheksbeziehungen und koordinieren Übergänge, wenn sich eine ABI ändert. Belasse native Bibliotheken unter der Kontrolle der Paketverwaltung. Verwende unterstützte Mechanismen zur parallelen Installation, Container, Umgebungen oder Build-Mechanismen für Software, die eine in Konflikt stehende Version benötigt.

:::single-choice{#package-dependencies-filename-insufficient} Warum kann ein Programm trotz einer ähnlich benannten Bibliotheksdatei fehlschlagen?

::option[Linux erlaubt jeder Bibliothek nur die Nutzung durch eine einzige ausführbare Datei.]{#package-dependencies-one-consumer explanation="Ein wesentlicher Zweck gemeinsam genutzter Bibliotheken ist ihre Verwendung durch mehrere Prozesse und Programme."}
::option[Paketabhängigkeiten gelten nur vor dem ersten Systemstart.]{#package-dependencies-boot-only explanation="Abhängigkeiten bleiben während Installation, Upgrades und Laufzeit relevant."}
::option[Die ABI oder Architektur der Bibliothek erfüllt möglicherweise nicht die Anforderungen des Programms.]{#package-dependencies-abi-mismatch .correct explanation="Die Laufzeitverknüpfung hängt von kompatiblen Binärschnittstellen und der Maschinenarchitektur ab und nicht nur von einem Dateinamen."}
:::

## Defekte Abhängigkeitszustände

Ein Abhängigkeitsproblem kann durch gemischte Paketquellen, unterbrochene Vorgänge, manuell installierte Archive, zurückgehaltene Versionen, entfernte Dateien oder inkompatible Drittanbietersoftware entstehen. Reagiere darauf nicht, indem du Paketdatenbankdateien löschst oder eine Installation blind erzwingst.

Lies zuerst die Diagnose der Paketverwaltung, aktualisiere nur Metadaten vertrauenswürdiger Paketquellen, prüfe zurückgehaltene oder gepinnte Versionen und begutachte die vorgeschlagene Reparatur. Ein einfaches Paketinstallationswerkzeug kann ein Archiv entpacken, ohne alle Abhängigkeiten abzurufen. Ein übergeordnetes Werkzeug mit Paketquellenkenntnis ist für gewöhnliche Installationen meist sicherer, da es die vollständige Transaktion auflöst.

:::single-choice{#package-dependencies-low-level-limit} Was ist eine verbreitete Einschränkung bei der Installation eines lokalen Pakets mit einem einfachen Archivwerkzeug?

::option[Es ruft möglicherweise nicht alle fehlenden Abhängigkeiten aus Paketquellen ab und löst sie nicht vollständig auf.]{#package-dependencies-no-repository-resolution .correct explanation="Einfache Werkzeuge verwalten Paketarchive und Datenbanken, können das Abrufen von Abhängigkeiten aber einer übergeordneten Verwaltung überlassen."}
::option[Es kompiliert den Linux-Kernel immer aus dem Quellcode neu.]{#package-dependencies-recompile-kernel explanation="Die Installation eines Paketarchivs baut nicht zwangsläufig den Kernel neu."}
::option[Es verhindert, dass das Paket gemeinsam genutzte Bibliotheken enthält.]{#package-dependencies-no-libraries explanation="Ein Paketarchiv kann unabhängig vom verwendeten Installationswerkzeug Bibliotheken enthalten."}
:::

Nutze [Gemeinsam genutzte Bibliotheken unter Linux verwalten](https://labex.io/labs/comptia-manage-shared-libraries-in-linux-590867), um Laufzeitbeziehungen zu prüfen, und vergleiche sie anschließend mit Paketmetadaten in [Pakete mit RPM verwalten](https://labex.io/labs/rhel-managing-packages-with-rpm-in-linux-590868).

## Zusammenfassung

Du kannst nun erklären, wie die Auflösung von Paketabhängigkeiten funktioniert.

1. Erkenne erforderliche, alternative, versionierte und in Konflikt stehende Beziehungen.
2. Setze Pakete gemeinsam genutzter Bibliotheken mit ABI-Anforderungen zur Laufzeit in Beziehung.
3. Behandle Dateinamen als schwächeren Beleg als Architektur- und Schnittstellenkompatibilität.
4. Prüfe eine vollständige Paketverwaltungstransaktion, bevor du Reparaturen anwendest.
