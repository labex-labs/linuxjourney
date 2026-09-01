---
lesson_id: "path-of-a-packet"
course_id: "routing"
lang: "de"
order_index: 3
title: "Der Weg eines Pakets"
description: "Lerne, wie Routen, Nachbarerkennung, Frames und Router ein IP-Paket über einen Pfad transportieren."
meta_title: "Der Weg eines Pakets – Routing"
meta_description: "Erkunde den vollständigen Paketweg innerhalb eines lokalen Netzwerks und über das Internet. Lerne, wie IP- und MAC-Adressen, ARP und Routingtabellen zusammenarbeiten."
meta_keywords: "Paketweg, Netzwerkkommunikation, ARP, IP-Adresse, MAC-Adresse, Routingtabelle, Standardgateway, Linux-Vernetzung, Paketübertragung"
---

Ein Paketpfad ist eine Abfolge lokaler Entscheidungen. Der Quellhost, jeder Router und das Ziel wenden eigenen Routing-, Nachbar-, Filter- und Protokollzustand an; kein Endpunkt kennt normalerweise jede interne Entscheidung im Voraus.

## An ein direkt erreichbares Ziel senden

Bei einem Ziel, das von einer verbundenen Route umfasst wird, wählt die Quelle eine Schnittstelle und Quell-IP. Anschließend löst sie die Verbindungsadresse des Ziels auf – ARP für IPv4 über Ethernet oder Neighbor Discovery für IPv6 – und sendet einen Frame, der das IP-Paket trägt. Ein Switch kann den Frame weiterleiten, ohne zu einem IP-Hop zu werden.

:::single-choice{#packet-path-switch-hop} Zählt ein gewöhnlicher Ethernet-Switch als IP-Routing-Hop?

::option[Nein; er leitet lokale Frames weiter, ohne das IP-Hop-Feld zu verringern.]{#packet-path-switch-not-hop .correct explanation="Ein gerouteter Hop entsteht, wenn ein Router das IP-Paket verarbeitet und weiterleitet."}
::option[Ja; jeder Switch ersetzt das IP-Ziel.]{#packet-path-switch-replaces-ip explanation="Weiterleitung auf Schicht 2 schreibt IP-Ziele normalerweise nicht um."}
::option[Ja; jeder Kabelanschluss ist ebenfalls ein IP-Hop.]{#packet-path-cable-hop explanation="Physische Komponenten führen kein IP-Routing aus."}
:::

## Über ein Gateway senden

Bei einem nicht direkt erreichbaren Ziel bezeichnet die ausgewählte Route einen Next-Hop-Router. Das IP-Ziel bleibt der entfernte Endpunkt, während das Ziel des lokalen Frames die Verbindungsadresse des Gateways ist. Der Host löst auf seiner lokalen Verbindung das Gateway und nicht den entfernten Server auf.

:::single-choice{#packet-path-gateway-mac} Wessen MAC-Adresse wird im ersten Ethernet-Frame zu einem nicht direkt erreichbaren Server verwendet?

::option[Die Adresse des entfernten Servers über alle dazwischenliegenden Netzwerke hinweg.]{#packet-path-remote-mac explanation="Die entfernte Verbindungsadresse besitzt im Quell-LAN keine Bedeutung."}
::option[Ein aus dem DNS-Namen des Servers berechneter Wert.]{#packet-path-dns-mac explanation="DNS-Namen codieren nicht die MAC des lokalen nächsten Hops."}
::option[Die Adresse des ausgewählten lokalen Gateways.]{#packet-path-local-gateway .correct explanation="Der Frame wird an den nächsten Hop zugestellt, während der IP-Header auf den endgültigen Endpunkt zielt."}
:::

## Verarbeitung an jedem Router

Ein Router entfernt die eingehende Verbindungskapselung, validiert und verarbeitet den IP-Header, verringert TTL oder Hop Limit, sucht das Ziel, wendet Richtlinien an und erstellt eine neue Kapselung für die ausgehende Verbindung. Bei IPv4 berücksichtigt die Headerprüfsumme die geänderte TTL. Erreicht das Hop-Feld null, verwirft der Router das Paket und kann eine ICMP-Time-Exceeded-Nachricht zurückgeben.

:::single-choice{#packet-path-router-change} Welches IP-Feld wird von jedem normalen gerouteten Hop geändert?

::option[Der Benutzername der Anwendung.]{#packet-path-username explanation="Router benötigen für grundlegende Weiterleitung keine Anwendungskontodaten."}
::option[IPv4-TTL oder IPv6-Hop-Limit.]{#packet-path-hop-field .correct explanation="Jeder Router verringert das Feld, um Routingschleifen zu begrenzen."}
::option[In jedem Fall der Transportzielport.]{#packet-path-port explanation="Gewöhnliches Routing bewahrt Transportendpunkte; NAT kann eine getrennte Umwandlung sein."}
:::

## Middleboxes und MTU berücksichtigen

Gewöhnliches Routing bewahrt Quell- und Ziel-IP-Adressen, doch NAT kann sie umschreiben und Tunnel können das ursprüngliche Paket einkapseln. Firewalls können Datenverkehr still verwerfen oder zurückweisen. Auch Verbindungs-MTUs unterscheiden sich; IPv4-Router können Pakete mitunter fragmentieren, während IPv6-Router weitergeleitete Pakete nicht fragmentieren und sich auf Path MTU Discovery verlassen.

:::single-choice{#packet-path-address-change-exception} Wann können sich Ende-zu-Ende-IP-Adressen entlang eines Pfads ändern?

::option[Immer, wenn ein Ethernet-Switch eine Quell-MAC lernt.]{#packet-path-switch-learning-ip explanation="Switchlernen beeinflusst eine Weiterleitungstabelle der Verbindungsschicht und keine IP-Endpunktadressen."}
::option[Wenn eine NAT-Richtlinie Paketheader übersetzt.]{#packet-path-nat-change .correct explanation="Übersetzung ist eine Middlebox-Funktion über gewöhnliche Routenweiterleitung hinaus."}
::option[Immer, wenn ein DNS-Cacheeintrag abläuft.]{#packet-path-dns-expiry explanation="Bestehende Pakete enthalten bereits numerische Adressen."}
:::

## Den Rückweg verfolgen

Das Ziel führt für die Antwort eine eigene Routensuche aus. Der Rückweg kann aufgrund von Routingrichtlinien, Lastverteilung oder Fehlern andere Router verwenden. Zustandsbehaftete Firewalls und NAT müssen den beobachteten Datenstrom berücksichtigen. Asymmetrie kann daher betrieblich relevant sein, obwohl IP sie erlaubt.

:::single-choice{#packet-path-return-symmetry} Muss eine Antwort dieselben Router in umgekehrter Reihenfolge durchqueren?

::option[Ja, weil IP in jedem Paket die vollständige ausgehende Route aufzeichnet.]{#packet-path-records-route explanation="Gewöhnliche IP-Pakete enthalten keine vorgeschriebene vollständige Rückroute."}
::option[Ja, sofern Quelle und Ziel keinen Hostnamen gemeinsam haben.]{#packet-path-hostname-symmetry explanation="Namen erzwingen keine Pfadsymmetrie."}
::option[Nein; jede Richtung wird unabhängig geroutet.]{#packet-path-independent-return .correct explanation="Richtlinien und Topologie können einen asymmetrischen, aber gültigen Pfad erzeugen."}
:::

## Zusammenfassung

Du kannst nun den sich ändernden Verbindungszustand um ein geroutetes IP-Paket verfolgen.

1. Löse den endgültigen Host nur auf, wenn er direkt erreichbar ist.
2. Kapsle nicht direkt erreichbaren Datenverkehr für das ausgewählte lokale Gateway.
3. Verfolge Routensuche und Hop-Limit-Verarbeitung an jedem Router.
4. Berücksichtige NAT, Filterung, Tunnel und MTU-Beschränkungen.
5. Behandle die Rückrichtung als unabhängige Route.
