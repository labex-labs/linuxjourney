---
lesson_id: "nat-network-address-translation"
course_id: "subnetting"
lang: "de"
order_index: 6
title: "NAT"
description: "Lerne, wie Quell-, Ziel- und Portübersetzung IPv4-Datenströme und Verbindungszustand verändern."
meta_title: "NAT – Subnetting"
meta_description: "Lerne Network Address Translation unter Linux, ihre Funktionsweise und ihre Rolle beim Verbinden privater und öffentlicher IPv4-Netze kennen."
meta_keywords: "NAT, Network Address Translation, Linux-Vernetzung, private IP, öffentliche IP, Linux-Tutorial, Einsteiger-Anleitung"
---

Network Address Translation schreibt Adressfelder und häufig Transportports um, wenn Pakete ein übersetzendes Gerät durchqueren. Sie wird verbreitet eingesetzt, um privat adressierte IPv4-Netzwerke über eine kleinere Menge extern routbarer Adressen zu verbinden.

## Quellübersetzung

Source NAT ersetzt die Quelladresse eines Pakets, wenn es ein Netzwerk verlässt. Many-to-one-Installationen übersetzen zusätzlich Quellports, damit mehrere interne Datenströme eine externe Adresse gemeinsam verwenden können. Diese portbezogene Form wird häufig NAPT, PAT oder – bei veränderlicher externer Adresse – Masquerading genannt.

Der Übersetzer verfolgt Zuordnungen, damit Antwortpakete zum ursprünglichen internen Endpunkt zurückübersetzt werden können. Er leitet normalerweise denselben Transportdatenstrom weiter und muss keine getrennte Proxyverbindung öffnen, wie es ein Anwendungsproxy tun würde.

:::single-choice{#nat-source-translation} Was verändert Source NAT an einem ausgehenden Paket?

::option[Nur die Dateiberechtigungen der Zielanwendung.]{#nat-file-permissions explanation="NAT wirkt auf Netzwerk- und Transportheader und nicht auf entfernte Dateisysteme."}
::option[Die Quelladresse und bei Many-to-one-Nutzung häufig den Quellport.]{#nat-source-fields .correct explanation="Die Zuordnung ermöglicht, Rückverkehr mit dem ursprünglichen internen Datenstrom zu verbinden."}
::option[Den dauerhaft vom Client gespeicherten DNS-Namen.]{#nat-dns-name explanation="Die Übersetzung schreibt die Namensdienstdatenbank des Clients nicht um."}
:::

## Zielübersetzung

Destination NAT schreibt Zieladresse oder -port um, gewöhnlich um einen internen Dienst über einen externen Endpunkt zu veröffentlichen. Eine Portweiterleitungsregel kann einen externen TCP-Port einer anderen internen Adresse und einem anderen Port zuordnen. Rückverkehr benötigt eine konsistente Rückübersetzung.

:::single-choice{#nat-port-forward} Welche NAT-Form implementiert gewöhnlich eine eingehende Portweiterleitung?

::option[Nur Source NAT vor der Routensuche.]{#nat-snat-port-forward explanation="Die Veröffentlichung eines internen Ziels erfordert die Übersetzung von Zielfeldern."}
::option[Überhaupt keine Adress- oder Portübersetzung.]{#nat-no-translation explanation="Eine Portweiterleitungsregel ist definitionsgemäß eine Übersetzungsrichtlinie."}
::option[Destination NAT.]{#nat-dnat .correct explanation="DNAT ordnet das externe Ziel dem ausgewählten internen Dienstendpunkt zu."}
:::

## NAT und Firewallrichtlinie

NAT ist keine Firewall. Ein zustandsbehafteter Übersetzer besitzt möglicherweise keine Zuordnung für unaufgeforderten eingehenden Datenverkehr, doch ausdrückliche Weiterleitung, Zielübersetzung, Filterung und Anwendungsoffenlegung bestimmen die Erreichbarkeit. Sicherheitsrichtlinien sollten durch Firewallregeln, Dienste mit geringstmöglichen Berechtigungen und Ende-zu-Ende-Kontrollen ausgedrückt und auditiert werden, statt sie aus Adressumschreibung abzuleiten.

:::single-choice{#nat-not-firewall} Warum sollte NAT nicht für sich allein als Sicherheitsrichtlinie behandelt werden?

::option[NAT verschlüsselt automatisch jede Nutzlast.]{#nat-encrypts explanation="Adressübersetzung bietet keine Vertraulichkeit der Nutzlast."}
::option[Übersetzungs- und Verkehrsfilterregeln besitzen unterschiedliche Zwecke.]{#nat-filter-separate .correct explanation="Erreichbarkeit und Autorisierung erfordern auch bei vorhandener Übersetzung ausdrückliche Filter- und Dienstrichtlinien."}
::option[NAT verhindert, dass Administratoren Firewallregeln definieren.]{#nat-prevents-firewall explanation="Übersetzung und Firewallrichtlinien bestehen gewöhnlich nebeneinander."}
:::

## Betriebliche Folgen

NAT kann Adress- und Portzuordnungen erschöpfen, Peer-to-Peer-Protokolle erschweren, ursprüngliche Quellen vor Anwendungen verbergen und Sonderbehandlung für Protokolle erfordern, die Adressen einbetten. Protokolle müssen Zeitstempel und Details der Übersetzungszuordnung bewahren, wenn Datenströme zurückverfolgt werden sollen.

Unter Linux werden aktuelle Richtlinien gewöhnlich mit nftables und Connection Tracking konfiguriert. Untersuche vor Änderungen den tatsächlichen Regelsatz:

```bash
$ sudo nft list ruleset
$ sudo conntrack -L
```

Der zweite Befehl erfordert Conntrack-Werkzeuge und erhöhte Berechtigungen. Änderungen am Regelsatz können den Fernzugriff trennen; verwende deshalb Konsolenwiederherstellung, atomare Konfiguration, Validierung und Rücknahme.

:::single-choice{#nat-trace-flow} Welche Belege sind nötig, um einen Datenstrom mit gemeinsam genutzter Adresse zu einem internen Client zurückzuverfolgen?

::option[Nur die externe Adresse ohne Zeit oder Port.]{#nat-address-only explanation="Viele Clients und Datenströme können diese Adresse gemeinsam verwenden."}
::option[Nur der angezeigte Hostname des Clients.]{#nat-hostname-only explanation="Der Übersetzer ordnet Pakettupel und nicht unbedingt Hostnamen zu."}
::option[Eine zeitlich verknüpfte Übersetzungszuordnung einschließlich Protokoll und Ports.]{#nat-correlated-mapping .correct explanation="Das vollständige Tupel und der Zeitstempel unterscheiden gleichzeitig übersetzte Datenströme."}
:::

## Zusammenfassung

Du kannst Adressübersetzung nun von Routing, Proxying und Firewallrichtlinien unterscheiden.

1. Erkenne Quellübersetzung bei ausgehenden Datenströmen.
2. Erkenne Zielübersetzung bei veröffentlichten Diensten.
3. Verstehe, wie Portzuordnungen die gemeinsame Nutzung von Adressen ermöglichen.
4. Wende ausdrückliche Filterung an, statt NAT als Sicherheit zu behandeln.
5. Bewahre bei Änderungen Zuordnungsbelege und Wiederherstellungszugang.
