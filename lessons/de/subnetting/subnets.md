---
lesson_id: "subnets"
course_id: "subnetting"
lang: "de"
order_index: 2
title: "Subnetze"
description: "Lerne, wie Präfixe IPv4-Subnetze definieren und direkte Zustellung, Routing sowie Richtlinien beeinflussen."
meta_title: "Subnetze – Subnetting"
meta_description: "Lerne die Grundlagen von Linux-Subnetzen und Subnetzmasken. Diese Anleitung erklärt Netzwerkpräfixe und die Verwaltung von Netzwerksegmentierung."
meta_keywords: "Subnetz Linux, Linux-Subnetz, Linux-Subnetzmaske, Subnetting, Subnetze, Subnetzmaske, Netzwerkpräfix, Linux-Vernetzung, IP-Adresse"
---

Ein Subnetz ist ein durch ein Netzwerkpräfix definierter IP-Adressbereich. Hosts in einem Subnetz befinden sich häufig auf derselben lokalen Verbindung, doch physische Nähe ist nicht die Definition: VLANs, Tunnel, Overlays und geroutete Verbindungen können die Topologie verändern.

## Präfixe und Masken

IPv4 kann ein 24-Bit-Präfix entweder als `/24` oder als Maske `255.255.255.0` ausdrücken. Binär besitzt eine gültige herkömmliche Subnetzmaske aufeinanderfolgende Einsen, gefolgt von Nullen:

```text
11111111.11111111.11111111.00000000
```

Für die Adresse `192.168.1.8/24` lautet das Netzwerkpräfix `192.168.1.0/24`. Die Schreibweise `192.168.1.0/255.255.255.0` wird in manchen Zusammenhängen verstanden, doch die CIDR-Präfixnotation ist die übliche kompakte Form.

:::single-choice{#subnets-mask-24} Welche punktgetrennte Dezimalmaske entspricht `/24`?

::option[`255.255.255.0`]{#subnets-mask-correct .correct explanation="Drei vollständige Oktette enthalten 24 führende Einsbits."}
::option[`255.255.0.255`]{#subnets-noncontiguous explanation="Diese Maske besitzt nicht zusammenhängende Netzwerkbits und ist keine herkömmliche `/24`-Maske."}
::option[`0.0.0.24`]{#subnets-prefix-as-octet explanation="Eine Präfixlänge wird nicht in das letzte Maskenoktett geschrieben."}
:::

## Entscheiden, ob ein Ziel direkt erreichbar ist

Linux installiert verbundene Routen anhand von Schnittstellenadressen und Präfixen. Es vergleicht ein Ziel mit geeigneten Routen, statt lediglich die ersten drei Dezimaloktette zu vergleichen. Bei Grenzen außerhalb von Oktetten wie `/20` erfolgt die Teilung innerhalb eines Oktetts.

Untersuche verbundene Routen und die Entscheidung für eine Adresse:

```bash
$ ip route show
$ ip route get 192.168.1.50
```

:::single-choice{#subnets-on-link-decision} Wie entscheidet ein Linux-Host, ob er direkt oder über einen Router sendet?

::option[Er nimmt immer an, dass Adressen mit `.1` lokal sind.]{#subnets-dot-one explanation="Konventionen für Hostnummern ersetzen keine konfigurierten Präfixe und Routen."}
::option[Er prüft Präfixe und die Routingrichtlinie.]{#subnets-route-policy .correct explanation="Die ausgewählte Route zeigt an, ob das Ziel direkt erreichbar ist und welche Schnittstelle oder welcher nächste Hop verwendet wird."}
::option[Er fragt die Zielanwendung nach dem Verbindungsaufbau nach einer Subnetzmaske.]{#subnets-ask-application explanation="Die Routenauswahl muss vor diesem Anwendungsaustausch erfolgen."}
:::

## Zwischen Subnetzen routen

Ein Router mit geeigneten Schnittstellen und Routen kann Datenverkehr zwischen Subnetzen weiterleiten. Ein Standardgateway ist lediglich ein durch eine Standardroute ausgewählter nächster Hop; es muss weder die erste verwendbare Adresse nutzen noch auf `.1` enden.

Die Trennung von Subnetzen schafft einen Ort, an dem Routing- und Filterrichtlinien angewandt werden können, ist aber nicht automatisch eine Sicherheitsgrenze. Wenn Weiterleitung ohne einschränkende Richtlinie erlaubt ist, können Hosts in unterschiedlichen Subnetzen weiterhin kommunizieren.

:::single-choice{#subnets-security-boundary} Blockiert das Erstellen zweier Subnetze automatisch den Datenverkehr zwischen ihnen?

::option[Ja, weil Router keine unterschiedlichen Präfixe verbinden können.]{#subnets-never-route explanation="Das Verbinden von Präfixen ist die Hauptaufgabe des Routings."}
::option[Nein; Routing- und Filterrichtlinien bestimmen den erlaubten Datenverkehr.]{#subnets-policy-required .correct explanation="Segmentierung ermöglicht die Durchsetzung von Richtlinien, definiert diese aber nicht von selbst."}
::option[Ja, sofern nicht beide die Hostadresse `.1` verwenden.]{#subnets-dot-one-security explanation="Eine Konvention für Hostnummern steuert keine Weiterleitung."}
:::

## Gründe für Subnetting

Subnetting kann die Adressvergabe ordnen, den Broadcastbereich der Verbindungsschicht begrenzen, Fehlerdomänen trennen und Richtliniengrenzen bereitstellen. Es kann außerdem die Komplexität von Routing, Firewall, DHCP, Überwachung und Dokumentation erhöhen. Entwirf Präfixe anhand tatsächlicher Skalierung, Wachstum, Redundanz und Sicherheitsanforderungen, statt anzunehmen, kleiner bedeute immer schneller.

:::single-choice{#subnets-design-tradeoff} Was ist ein tatsächlicher Kompromiss beim Subnetting?

::option[Kleinere Broadcast-Domänen benötigen weder Routing noch Dokumentation.]{#subnets-no-complexity explanation="Mehr Grenzen erfordern gewöhnlich mehr Verwaltung von Routen, Richtlinien, Adressen und Diensten."}
::option[Segmentierung kann die Organisation verbessern und zugleich die Richtlinienkomplexität erhöhen.]{#subnets-tradeoff .correct explanation="Subnetzgrenzen können die Steuerung unterstützen, fügen aber zu pflegenden Betriebszustand hinzu."}
::option[Jedes Subnetz garantiert dieselbe Latenz zum Internet.]{#subnets-equal-latency explanation="Pfad- und Arbeitslastbedingungen bestimmen die Latenz."}
:::

## Zusammenfassung

Du kannst ein IPv4-Präfix nun mit lokaler Zustellung und gerouteter Richtlinie in Beziehung setzen.

1. Drücke zusammenhängende Masken durch CIDR-Präfixlängen aus.
2. Berechne das Netzwerkpräfix aus Adressbits und Maske.
3. Verwende Routen, um direkte von Next-Hop-Zustellung zu unterscheiden.
4. Behandle Subnetzisolation als Gelegenheit für Richtlinien und nicht als Garantie.
