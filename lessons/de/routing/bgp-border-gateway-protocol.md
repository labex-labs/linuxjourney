---
lesson_id: "bgp-border-gateway-protocol"
course_id: "routing"
lang: "de"
order_index: 7
title: "Border Gateway Protocol"
description: "Lerne, wie BGP richtliniengesteuerte IP-Erreichbarkeit zwischen und innerhalb autonomer Systeme austauscht."
meta_title: "Border Gateway Protocol – Routing"
meta_description: "Erkunde die Grundlagen des Border Gateway Protocol als zentralem Protokoll des Internetroutings. Lerne, wie BGP autonome Systeme verbindet und richtliniengesteuerte Routen austauscht."
meta_keywords: "BGP, Border Gateway Protocol, Border-Gateway-Routing, Internetrouting, autonome Systeme, Linux-Vernetzung, BGP-Tutorial, Netzwerkprotokolle"
---

Das Border Gateway Protocol ist das Pfadvektor-Routingprotokoll des Internets. Es tauscht die Erreichbarkeit von IP-Präfixen und Pfadattribute aus, damit Netzwerke administrative Richtlinien anwenden können, statt Routen nur nach physischer Entfernung auszuwählen.

## Autonome Systeme und Sitzungen

Ein autonomes System ist eine Menge von Netzwerken unter gemeinsamer Routingverwaltung, die für BGP durch eine Autonomous System Number identifiziert wird. Externes BGP tauscht Routen zwischen autonomen Systemen aus; internes BGP verteilt BGP-Erreichbarkeit innerhalb eines AS.

BGP-Peers stellen eine Sitzung über TCP-Port 179 her. Eine funktionierende TCP-Sitzung ist nur die Transportgrundlage; auch BGP-Fähigkeiten, Richtlinien und Routenaustausch müssen erfolgreich sein.

:::single-choice{#bgp-external-session} Was tauscht externes BGP aus?

::option[Ethernet-Frame-Prüfsummen innerhalb eines Switches.]{#bgp-ethernet-fcs explanation="BGP arbeitet oberhalb von TCP und tauscht Erreichbarkeit der Netzwerkschicht aus."}
::option[Benutzerpasswörter zwischen Webbrowsern.]{#bgp-browser-passwords explanation="Anmeldedaten von Anwendungen sind keine Routingattribute."}
::option[Erreichbarkeits- und Pfadinformationen zwischen autonomen Systemen.]{#bgp-between-as .correct explanation="eBGP verbindet getrennte Routingverwaltungen und wendet domänenübergreifende Richtlinien an."}
:::

## Pfadvektorinformationen

Eine Ankündigung enthält ein Präfix und Attribute. `AS_PATH` listet durchquerte autonome Systeme auf und hilft, Schleifen zu erkennen. Weitere häufige Attribute sind `LOCAL_PREF`, `MED`, Ursprung, nächster Hop und Communities. Ihre Wirkung hängt von Richtung, Implementierung und Richtlinie ab.

:::single-choice{#bgp-as-path-loop} Wie hilft `AS_PATH`, Schleifen zwischen autonomen Systemen zu verhindern?

::option[Ein AS kann einen Pfad ablehnen, der bereits seine eigene Nummer enthält.]{#bgp-own-as-reject .correct explanation="Der Pfadvektor macht die AS-Abfolge zum angekündigten Präfix sichtbar."}
::option[Es verschlüsselt jedes Paket, das diese Systeme durchquert.]{#bgp-aspath-encryption explanation="Das Attribut beschreibt einen Routingpfad und bietet keine Nutzlastverschlüsselung."}
::option[Es weist jedem AS eine MAC-Adresse zu.]{#bgp-aspath-mac explanation="Nummern autonomer Systeme und Verbindungsadressen sind getrennte Namensräume."}
:::

## Richtliniengesteuerte Auswahl

Der „beste“ BGP-Pfad ist derjenige, der einen konfigurierten Entscheidungsprozess gewinnt. Betreiber können Kundenrouten bevorzugen, lokale Präferenz ändern, Präfixe filtern, Communities verwenden und Richtlinien zur Verkehrssteuerung anwenden. Ein kürzerer `AS_PATH` kann in einem Schritt relevant sein, setzt aber Attribute höherer Priorität nicht allgemein außer Kraft.

Nachdem BGP Kandidaten ausgewählt hat, verwendet die gewöhnliche IP-Weiterleitung weiterhin die längste Präfixübereinstimmung. Ein ausgewähltes `/24` wird für seine Ziele statt eines ausgewählten übergeordneten `/16` verwendet.

:::single-choice{#bgp-best-path-meaning} Was stellt ein bester BGP-Pfad dar?

::option[Die Route, die den lokalen Attribut- und Richtlinienentscheidungsprozess gewinnt.]{#bgp-policy-winner .correct explanation="Administrative Absicht ist für die domänenübergreifende Pfadauswahl zentral."}
::option[In jedem Fall die physisch kürzeste Kabelroute.]{#bgp-shortest-cable explanation="BGP besitzt keine vollständige Karte physischer Entfernungen."}
::option[Eine Garantie der derzeit niedrigsten Anwendungslatenz.]{#bgp-lowest-latency explanation="Die BGP-Auswahl optimiert standardmäßig nicht fortlaufend die Endbenutzerlatenz."}
:::

## Ankündigung und Erreichbarkeit

Die Ankündigung eines Präfixes behauptet Erreichbarkeit gemäß einer Richtlinie; sie erstellt weder die zugrunde liegende Route noch stellt sie den Rückweg sicher. Sorge vor dem Ankündigen eines Präfixes für gültige Weiterleitung, korrektes Aggregationsverhalten, Filter, Failover und eine Autorisierung des Eigentümers.

:::single-choice{#bgp-advertisement-limit} Was garantiert die Ankündigung eines Präfixes nicht?

::option[Dass Peers eine Route auf der Steuerungsebene empfangen können.]{#bgp-peers-control explanation="Erfolgreiche Ankündigung und Annahme können diese begrenzte Tatsache der Steuerungsebene belegen."}
::option[Dass das Präfix Adressbits enthält.]{#bgp-prefix-bits explanation="Ein IP-Präfix ist durch Adressbits und Länge definiert."}
::option[Dass Pakete für das gesamte Präfix zugestellt werden können.]{#bgp-data-plane-not-guaranteed .correct explanation="Zugrunde liegende Routen, nächste Hops, Filterung und Dienstzustand müssen weiterhin überprüft werden."}
:::

## Routingsicherheit und Änderungskontrolle

Route Leaks und Hijacks können Datenverkehr weit über einen Router hinaus beeinflussen. Betreiber verwenden strenge Import- und Exportfilter, Grenzen für maximale Präfixanzahlen, Peer-Richtlinien, Überwachung und gegebenenfalls Ursprungsvalidierung mit der Resource Public Key Infrastructure. Die RPKI-Ursprungsvalidierung prüft, ob ein AS zur Ankündigung eines Präfixes autorisiert ist; sie validiert nicht den vollständigen AS-Pfad.

BGP-Änderungen erfordern schrittweise Einführung, Prüfung von Routendifferenzen, Out-of-Band-Zugang, Rücknahme sowie Überprüfung auf Steuerungs- und Datenebene.

:::single-choice{#bgp-rpki-limit} Was prüft die RPKI-Ursprungsvalidierung?

::option[Ob jede Paketnutzlast frei von Schadsoftware ist.]{#bgp-payload-malware explanation="RPKI untersucht keine Anwendungsinhalte."}
::option[Ob der vollständige AS-Pfad die geringste Latenz besitzt.]{#bgp-path-latency explanation="Ursprungsvalidierung ist weder Leistungsauswahl noch vollständige Pfadvalidierung."}
::option[Ob das Ursprungs-AS autorisiert ist.]{#bgp-origin-authorized .correct explanation="Sie validiert die Ursprungsautorisierung und nicht jede Transitbeziehung im AS-Pfad."}
:::

## Zusammenfassung

Du kannst BGP nun als richtliniengesteuertes Pfadvektorrouting beschreiben.

1. Unterscheide externe von internen BGP-Sitzungen.
2. Verwende `AS_PATH` als Pfad- und Schleifeninformation.
3. Interpretiere den besten Pfad anhand lokaler Attribute und Richtlinien.
4. Überprüfe die Weiterleitung hinter jedem angekündigten Präfix.
5. Wende Filterung, Ursprungsvalidierung, Überwachung und Rücknahme an.
