---
lesson_id: "packet-analysis"
course_id: "troubleshooting"
lang: "de"
order_index: 5
title: "Paketanalyse"
description: "Lerne, eine begrenzte, gefilterte Paketaufzeichnung zu erstellen und mit tcpdump sicher zu analysieren."
meta_title: "Paketanalyse – Fehlersuche"
meta_description: "Lerne die Grundlagen der Netzwerkpaketanalyse unter Linux. Diese Anleitung führt in tcpdump ein, um Netzwerkverkehr aufzuzeichnen und zu interpretieren."
meta_keywords: "tcpdump, Paketanalyse, Netzwerkpaketanalyse, Netzwerkpaketanalysator, Netzwerkanalyse, Werkzeuge zur Netzwerkpaketanalyse, Linux-Vernetzung, Wireshark, Linux-Befehle, Netzwerkverkehr"
---

Eine Paketaufzeichnung erfasst Datenverkehr, der an einem ausgewählten Beobachtungspunkt sichtbar ist. Sie kann Protokollaustausch und Zeitverlauf offenlegen, aber auch Anmeldedaten, personenbezogene Daten und Datenverkehr unabhängiger Benutzer sammeln. Hole eine Genehmigung ein, begrenze den Umfang, schütze Dateien und befolge die Aufbewahrungsrichtlinie.

## Den Beobachtungspunkt auswählen

Zeichne auf der Schnittstelle und im Netzwerknamensraum auf, die der betroffene Datenstrom tatsächlich durchquert. Bridges, Container, VPNs, Bonds, VLANs und Offloading können verändern, was eine Schnittstelle zeigt. Ermittle vor der Aufzeichnung mit `ip route get` und `ip link` mögliche Kandidaten.

:::single-choice{#packet-analysis-interface-choice} Warum ist die Auswahl der Aufzeichnungsschnittstelle wichtig?

::option[Jede Schnittstelle spiegelt automatisch das gesamte Internet.]{#packet-analysis-mirrors-internet explanation="Ein Host sieht normalerweise nur Datenverkehr, der über seine Schnittstellen zugestellt oder zu ihnen gespiegelt wird."}
::option[Nur an diesem Beobachtungspunkt sichtbarer Datenverkehr kann aufgezeichnet werden.]{#packet-analysis-visible-point .correct explanation="Namensräume, Tunnel, Bridges und Routing können den relevanten Datenstrom andernorts platzieren."}
::option[Der Schnittstellenname entschlüsselt TLS-Nutzlasten.]{#packet-analysis-name-decrypts explanation="Eine Benennung besitzt keine Entschlüsselungsfähigkeit."}
:::

## Einen begrenzten Datenstrom aufzeichnen

Zeichne ohne Namensauflösung höchstens 100 Pakete auf, beschränkt auf einen Host und TCP-Port:

```bash
$ sudo tcpdump -i enp1s0 -n -c 100 -w incident.pcap \
    'host 192.0.2.25 and tcp port 443'
```

`-i` wählt die Schnittstelle, `-n` bewahrt numerische Namen, `-c` begrenzt die Paketanzahl, `-w` schreibt pcap-Daten, und der abschließende Ausdruck ist ein Aufzeichnungsfilter. Lege zusätzlich extern eine Zeitgrenze fest, falls kein Datenverkehr auftritt.

:::single-choice{#packet-analysis-count-bound} Was bewirkt `-c 100`?

::option[Es zeichnet nur TCP-Port 100 auf.]{#packet-analysis-port-hundred explanation="Die Portauswahl gehört in den Filterausdruck."}
::option[Es komprimiert die Datei auf 100 Byte.]{#packet-analysis-compress-hundred explanation="Die Option bezeichnet eine Paketanzahl und keine Dateigrößengrenze."}
::option[Es stoppt nach der Aufzeichnung von 100 Paketen.]{#packet-analysis-hundred .correct explanation="Die Anzahl verhindert, dass eine unbeaufsichtigte Aufzeichnung nach Paketmenge unbegrenzt wächst."}
:::

## Aufgezeichnete Pakete lesen

Analysiere die gespeicherte Datei, ohne sie zu verändern:

```bash
$ tcpdump -n -tttt -r incident.pcap
```

Lies je nach Protokoll Zeitstempel, Protokoll, Quelle, Ziel, Kennzeichen, Sequenz- oder Bestätigungsdaten und Länge. Ein Aufzeichnungszeitstempel kennzeichnet die Beobachtung auf diesem Host und nicht zwangsläufig die genaue Sendezeit andernorts. Uhrsynchronisierung ist wichtig, wenn Aufzeichnungen mehrerer Systeme miteinander verknüpft werden.

:::single-choice{#packet-analysis-read-file} Welche Option liest Pakete aus einer gespeicherten pcap-Datei?

::option[`-r`]{#packet-analysis-option-read .correct explanation="Die Leseoption verarbeitet eine bestehende Aufzeichnungsdatei."}
::option[`-i`]{#packet-analysis-option-interface explanation="Dies wählt eine Schnittstelle für eine Live-Aufzeichnung aus."}
::option[`-w`]{#packet-analysis-option-write explanation="Dies schreibt rohe Pakete in eine Datei."}
:::

## Abwesenheit und Verschlüsselung interpretieren

Keine aufgezeichneten Pakete können eine falsche Schnittstelle oder einen falschen Namensraum, Aufzeichnungsverlust, einen zu engen Filter, Offloading-Auswirkungen, anderes Routing oder ausbleibenden Datenverkehr bedeuten. Prüfe die Zähler von tcpdump für empfangene und verworfene Pakete und reproduziere ein bekanntes Ereignis.

TLS und andere Verschlüsselung verbergen normalerweise Anwendungsnutzlasten, lassen jedoch nützliche Metadaten wie Endpunkte, Zeitverlauf, Größen, TCP-Verhalten und Teile von Handshakes sichtbar. Versuche keine unautorisierte Entschlüsselung und sammle private Schlüssel nicht leichtfertig.

:::single-choice{#packet-analysis-no-packets} Was beweist eine leere gefilterte Aufzeichnung?

::option[Die entfernte Anwendung wurde dauerhaft gelöscht.]{#packet-analysis-empty-deleted explanation="Fehler bei Beobachtungspunkt und Filter können dasselbe Ergebnis erzeugen."}
::option[Das gesamte Netzwerk besitzt keinen Datenverkehr.]{#packet-analysis-empty-network explanation="Ein enger Filter kann unabhängigen Datenverkehr ausschließen."}
::option[Nur, dass an diesem Aufzeichnungspunkt keine passenden Pakete erfasst wurden.]{#packet-analysis-empty-limited .correct explanation="Validiere Schnittstelle, Namensraum, Filter, verworfene Aufzeichnungen und Testerzeugung, bevor du Schlussfolgerungen ziehst."}
:::

## Belege schützen und weitergeben

Speichere pcaps mit restriktiven Berechtigungen, erfasse Befehl, Host, Schnittstelle, Zeitzone, Filter und Vorfallszeitraum und hashe Belege, wenn Integrität wichtig ist. Minimiere oder bereinige Daten vor der Weitergabe mit Werkzeugen und Verfahren, die benötigte Felder erhalten; Paketnutzlasten und sogar Metadaten können Benutzer und Systeme identifizieren.

:::single-choice{#packet-analysis-pcap-safety} Wie sollte eine pcap-Datei eines Vorfalls behandelt werden?

::option[Als vertraulicher Beleg mit beschränktem Zugriff und dokumentierter Herkunft.]{#packet-analysis-sensitive-evidence .correct explanation="Aufzeichnungen können vertrauliche Inhalte enthalten und benötigen sowohl Integritäts- als auch Vertraulichkeitskontrollen."}
::option[Als harmloser Text, der ohne Prüfung öffentlich hochgeladen werden kann.]{#packet-analysis-public explanation="Binäre Aufzeichnungen können Nutzlasten, Identitäten und Infrastruktur offenlegen."}
::option[Durch Bearbeiten von Bytes an Ort und Stelle, ohne das Original zu bewahren.]{#packet-analysis-edit-original explanation="Dies beschädigt die Herkunft und kann spätere Analysen ungültig machen."}
:::

## Zusammenfassung

Du kannst nun eine nützliche Paketaufzeichnung erstellen, ohne sie unnötig breit oder unsicher zu machen.

1. Wähle die richtige Schnittstelle und den richtigen Netzwerknamensraum.
2. Begrenze Aufzeichnungen durch Filter, Paketanzahl und Zeit.
3. Speichere rohe Pakete und analysiere die Datei schreibgeschützt.
4. Behandle Abwesenheit und verschlüsselte Nutzlasten mit angemessenen Grenzen.
5. Schütze Vertraulichkeit, Integrität und Herkunft der Aufzeichnung.
