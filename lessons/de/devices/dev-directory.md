---
lesson_id: "dev-directory"
course_id: "devices"
lang: "de"
order_index: 1
title: "Das Verzeichnis /dev"
description: "Lerne, wie Linux Geräteschnittstellen und Pseudogeräte über Knoten unter `/dev` bereitstellt."
meta_title: "Das Verzeichnis /dev – Geräte"
meta_description: "Entdecke den Zweck des Verzeichnisses /dev unter Linux, erkunde es mit ls und lerne die Rolle von Gerätedateien, Pseudogeräten und dauerhaften Links kennen."
meta_keywords: "dev Linux, /dev Verzeichnis Linux, dev Ordner Linux, ls /dev, Gerätedateien, Geräteknoten, Linux Geräte"
---

Linux stellt viele Geräteschnittstellen des Kernels über besondere Dateisystemobjekte bereit, die Geräteknoten heißen. Sie befinden sich normalerweise unter `/dev`, zusammen mit nützlichen symbolischen Links und Kommunikationsendpunkten. Öffnet eine Anwendung einen Geräteknoten, verbindet sie sich mit einem Kernel-Treiber und nicht mit Bytes, die in einer gewöhnlichen Datei gespeichert sind.

## `/dev` erkunden

Liste das Verzeichnis auf, ohne Geräte zu dereferenzieren oder auszulesen:

```bash
$ ls -l /dev
```

Einträge können physischen Speicher, Terminals, Eingabeschnittstellen, logische Geräte oder vom Kernel bereitgestellte Pseudogeräte darstellen. Nicht jede Hardwarekomponente benötigt einen eigenen sichtbaren Knoten, und ein Gerät kann durch mehrere Links oder Schnittstellen repräsentiert werden.

Das erste Zeichen einer langen Auflistung bezeichnet den Typ des Dateisystemobjekts. Zeichen- und Blockgeräteknoten erscheinen als `c` beziehungsweise `b`; spätere Lektionen behandeln diese Typen und ihre Major- und Minor-Nummern.

:::single-choice{#dev-directory-device-node-purpose}
Was geschieht, wenn ein Programm einen Geräteknoten unter `/dev` öffnet?

::option[Es liest immer eine gewöhnliche Datei auf dem Datenträger, die eine Kopie der Hardware enthält.]{#dev-directory-ordinary-copy explanation="Ein Geräteknoten ist ein besonderes Objekt und speichert keine Kopie der Gerätedaten als gewöhnliche Datei."}
::option[Es greift auf eine von einem Kernel-Treiber implementierte Schnittstelle zu.]{#dev-directory-kernel-interface .correct explanation="Operationen am Geräteknoten werden über dessen Geräteidentität an das Verhalten des Kernel-Treibers weitergeleitet."}
::option[Es kompiliert den Treiberquellcode für dieses Gerät neu.]{#dev-directory-recompile-driver explanation="Das Öffnen einer Schnittstelle ruft keinen Compiler auf und baut keine Kernelmodule neu."}
:::

## Pseudogeräte

Einige Knoten stellen Kernel-Dienste bereit, ohne physischer Hardware zu entsprechen. `/dev/null` nimmt geschriebene Daten an und verwirft sie:

```bash
$ command > /dev/null
```

Weitere bekannte Beispiele sind `/dev/zero`, das Nullbytes erzeugt, und `/dev/urandom`, das Zufallsbytes über das Zufallssubsystem des Kernels bereitstellt. Jedes besitzt eine genau festgelegte Semantik; leite sein Verhalten nicht allein vom Dateinamen ab.

:::single-choice{#dev-directory-null-behavior}
Was macht `/dev/null` mit hineingeschriebenen Daten?

::option[Es speichert die Daten bis zum nächsten Neustart.]{#dev-directory-null-temporary-storage explanation="Das Nullgerät ist eine Senke und kein temporärer Speicher."}
::option[Es sendet die Daten an alle angemeldeten Terminals.]{#dev-directory-null-broadcast explanation="Das Senden an Terminals steht in keinem Zusammenhang mit dem Null-Pseudogerät."}
::option[Es verwirft die Daten.]{#dev-directory-null-discards .correct explanation="Das Nullgerät nimmt Schreibvorgänge an, ohne deren Inhalt aufzubewahren."}
:::

## Dynamische Geräteverwaltung

Auf modernen Linux-Systemen kann das vom Kernel gestützte `devtmpfs` grundlegende Geräteknoten anlegen, sobald Geräte erscheinen. Ein Userspace-Gerätemanager wie `udev` verarbeitet Ereignisse, wendet Berechtigungen und Eigentümerschaft an und erzeugt nützliche symbolische Links oder richtliniengesteuerte Namen. Die genaue Aufgabenverteilung hängt vom System ab.

Dauerhafte Links wie Einträge unter `/dev/disk/by-id/` oder `/dev/disk/by-uuid/` können in Konfigurationen sicherer sein als von der Erkennungsreihenfolge abhängige Namen wie `/dev/sda`. Letztere können sich ändern, wenn sich Hardwaretopologie oder Erkennungsreihenfolge ändern.

:::single-choice{#dev-directory-persistent-link}
Warum kann ein Administrator in einer Konfiguration `/dev/disk/by-id/...` gegenüber `/dev/sda` bevorzugen?

::option[Der kennungsbasierte Link hängt weniger von der Erkennungsreihenfolge der Geräte ab.]{#dev-directory-stable-identifier .correct explanation="Dauerhafte Links werden aus Geräteeigenschaften abgeleitet und nicht aus einem bei der Aufzählung vergebenen Buchstaben."}
::option[Der Link sichert automatisch jeden Block des Geräts.]{#dev-directory-link-backup explanation="Ein symbolischer Link benennt dasselbe Gerät und erzeugt keine Sicherungsdaten."}
::option[Der Link umgeht sämtliche Berechtigungen des Zielgeräts.]{#dev-directory-link-permissions explanation="Auch das Öffnen über einen symbolischen Link erreicht das Zielgerät und seine Zugriffskontrollen."}
:::

## Sicher interagieren

Standardwerkzeuge können Geräteknoten öffnen, doch beliebige Lese- und Schreibvorgänge werden dadurch nicht sicher. Lesen kann sensible Eingaben oder Speicherdaten offenlegen; Schreiben auf einen Datenträger, ein Terminal oder eine Firmware-Schnittstelle kann Daten beschädigen oder Benutzer stören. Deshalb begrenzen Berechtigungen, Gruppen, ACLs, Capabilities und vermittelnde Dienste den Zugriff auf Geräteknoten.

Verwende zuerst schreibgeschützte Erkundungswerkzeuge, bestätige den genauen Knoten und die Geräteidentität und folge der gerätespezifischen Dokumentation. Experimentiere auf einem wichtigen System niemals, indem du Daten in einen unbekannten Eintrag unter `/dev` umleitest.

:::single-choice{#dev-directory-direct-write-risk}
Warum solltest du keine beliebigen Daten in einen unbekannten Geräteknoten schreiben?

::option[Jeder Geräteknoten ist garantiert eine harmlose Textdatei.]{#dev-directory-harmless-text explanation="Geräteknoten sind gerade keine gewöhnlichen Textdateien."}
::option[Der Vorgang kann sich direkt auf Hardware, Speicher oder eine andere Kernel-Schnittstelle auswirken.]{#dev-directory-write-impact .correct explanation="Schreibvorgänge auf Geräten rufen vom Treiber festgelegte Operationen auf und können zerstörerische oder störende Folgen haben."}
::option[Linux wandelt jeden Schreibvorgang auf einem Gerät in eine schreibgeschützte Auflistung um.]{#dev-directory-write-listing explanation="Der Treiber legt die Schreibsemantik fest; der Kernel wandelt Schreibvorgänge nicht allgemein in Auflistungen um."}
:::

Nutze das Lab [Hardwaregeräte unter Linux erkunden](https://labex.io/labs/comptia-explore-hardware-devices-in-linux-590861) für schreibgeschützte Untersuchungen in einer kontrollierten Umgebung.

## Zusammenfassung

Du kannst `/dev` nun als Sammlung aktiver, dem Kernel zugewandter Schnittstellen beschreiben.

1. Unterscheide Geräteknoten von gewöhnlichen Dateien.
2. Erkenne Pseudogeräte wie `/dev/null`.
3. Ordne dynamische Knoten und dauerhafte Links der Geräteverwaltung zu.
4. Behandle direkten Gerätezugriff als schnittstellenspezifisch und potenziell zerstörerisch.
