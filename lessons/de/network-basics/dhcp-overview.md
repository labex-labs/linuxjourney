---
lesson_id: "dhcp-overview"
course_id: "network-basics"
lang: "de"
order_index: 9
title: "Überblick über DHCP"
description: "Lerne, wie DHCPv4 Adressen und Netzwerkoptionen durch Erkennung, Auswahl und Erneuerung least."
meta_title: "Überblick über DHCP – Netzwerkgrundlagen"
meta_description: "Lerne die Grundlagen des Dynamic Host Configuration Protocol. Diese Anleitung behandelt die Vergabe von IP-Adressen durch DHCP, den vierstufigen DORA-Ablauf und seine Rolle bei der Netzwerkkonfiguration."
meta_keywords: "DHCP, Dynamic Host Configuration Protocol, DHCP-Schicht, IP-Adresse, Linux-Vernetzung, DHCP-Ablauf, DORA, Netzwerkkonfiguration"
---

Das Dynamic Host Configuration Protocol stellt Clients geleaste Netzwerkkonfiguration bereit. Bei DHCPv4 kann diese eine IPv4-Adresse, Subnetzmaske, Standardrouter, DNS-Server, Lease-Dauer und weitere von der lokalen Richtlinie ausgewählte Optionen umfassen.

## Clients, Server und Relays

Ein DHCP-Server verwaltet Bereiche oder Adresspools und den Lease-Zustand. Der Server muss sich nicht in jedem physischen Segment befinden: Ein DHCP-Relay kann den Austausch zwischen Clients in einem Subnetz und einem zentralen Server weiterleiten. Netzwerke mit ausschließlich statischer Konfiguration stellen möglicherweise überhaupt kein DHCP bereit.

DHCP ist ein Protokoll der Anwendungsschicht, das über UDP transportiert wird. DHCPv4-Server verwenden normalerweise UDP-Port 67 und Clients Port 68.

:::single-choice{#dhcp-relay-purpose}
Was ermöglicht ein DHCP-Relay?

::option[Jedem Client, eine Adresse ohne jede Richtlinie auszuwählen.]{#dhcp-client-any-address explanation="Der Server wendet weiterhin Bereichs- und Lease-Richtlinien an."}
::option[Clients in einem anderen Subnetz, einen zentralen DHCP-Server zu erreichen.]{#dhcp-central-server .correct explanation="Das Relay leitet den DHCP-Austausch über eine Routinggrenze weiter und kennzeichnet das Clientnetzwerk."}
::option[Ethernet-Switches, alle IP-Router zu ersetzen.]{#dhcp-switch-router explanation="Die DHCP-Weiterleitung beseitigt keine gerouteten Netzwerkgrenzen."}
:::

## Erster DHCPv4-Austausch

Der gewöhnliche anfängliche Ablauf wird als DORA bezeichnet:

1. `DHCPDISCOVER`: Ein Client sucht nach verfügbaren Servern.
2. `DHCPOFFER`: Ein Server schlägt eine Adresse und Optionen vor.
3. `DHCPREQUEST`: Der Client wählt ein angebotenes Lease aus und fordert es an.
4. `DHCPACK`: Der ausgewählte Server bestätigt Lease und Optionen.

Einzelheiten zu Broadcast und Unicast unterscheiden sich je nach Clientzustand, Relay-Verwendung und Serverfähigkeiten. Ein Angebot ist noch nicht das abschließend verwendbare Lease; die Bestätigung schließt den normalen Auswahlaustausch ab.

:::single-choice{#dhcp-dora-order}
Was ist die normale anfängliche DHCPv4-Reihenfolge?

::option[OFFER, DISCOVER, ACK, REQUEST.]{#dhcp-wrong-order-one explanation="Ein Client sucht, bevor ein Server anbietet, und fordert vor der Bestätigung an."}
::option[DISCOVER, OFFER, REQUEST, ACK.]{#dhcp-correct-order .correct explanation="Die Abfolge sucht, schlägt vor, wählt aus und bestätigt."}
::option[REQUEST, ACK, DISCOVER, OFFER.]{#dhcp-wrong-order-two explanation="Ein neuer Client benötigt normalerweise Erkennung und Angebot, bevor er ein Lease auswählt."}
:::

## Lease-Erneuerung

Ein Lease läuft ab, wenn es nicht erneuert wird. Ein Client beginnt die Erneuerung normalerweise vor Ablauf und kontaktiert häufig zuerst den ursprünglichen Server direkt. Bleibt die Erneuerung erfolglos, erweitert er später den Rebinding-Versuch. Die genauen Timer werden vom Protokoll geliefert oder daraus abgeleitet.

Eine als dynamisch zugewiesen angezeigte Adresse beweist nicht, dass ihr Lease für immer bestehen bleibt. Erfasse bei der Fehlersuche zu Änderungen das aktive Lease, seine Laufzeit, den Server und die Optionen.

:::single-choice{#dhcp-lease-expiration}
Was geschieht mit einem DHCP-Adress-Lease ohne erfolgreiche Erneuerung?

::option[Es wird zu einer dauerhaften Hardware-MAC-Adresse.]{#dhcp-lease-mac explanation="Ein IP-Lease verändert die Identität der Verbindungsschicht nicht."}
::option[Es läuft schließlich ab, und der Client darf es nicht mehr als gültig behandeln.]{#dhcp-lease-expires .correct explanation="Leasing ermöglicht, Adressen und Optionen gemäß Serverrichtlinie zurückzufordern oder zu ändern."}
::option[Es macht den Client zur autoritativen DNS-Wurzel.]{#dhcp-lease-dns-root explanation="DHCP-Leasing verleiht keine DNS-Autorität."}
:::

## Das Ergebnis untersuchen

Überprüfe nach der DHCP-Konfiguration eines Clients den gesamten erforderlichen Zustand und nicht nur die Adresse:

```bash
$ ip address show
$ ip route show
$ resolvectl status
```

Der Resolverbefehl unterscheidet sich je nach System. Untersuche außerdem Leasedaten und Protokolle des aktiven Netzwerkmanagers. Doppelte Adressen können weiterhin durch nicht autorisierte Server, statische Zuweisungen innerhalb eines Pools, veralteten Zustand oder manuelle Konfiguration entstehen. DHCP verringert Fehler, kann aber nicht jeden Konflikt allein verhindern.

:::single-choice{#dhcp-result-verification}
Was sollte geprüft werden, nachdem ein DHCP-Lease angenommen wurde?

::option[Nur der angezeigte Name der Schnittstelle.]{#dhcp-interface-name-only explanation="Ein Schnittstellenname belegt weder Adressierung noch Routing oder Namensauflösung."}
::option[Nur, ob die Tastatur reagiert.]{#dhcp-keyboard explanation="Tastatureingaben haben nichts mit der Netzwerkkonfiguration eines Leases zu tun."}
::option[Adresse, Routen, DNS und Lease-Details.]{#dhcp-check-complete-state .correct explanation="Eine verwendbare Konfiguration hängt von mehreren Optionen und ihrem angewandten Systemzustand ab."}
:::

## DHCPv6 und IPv6-Konfiguration

IPv6-Hosts können Stateless Address Autoconfiguration, DHCPv6, statische Konfiguration oder Kombinationen verwenden. DHCPv6 verwendet nicht den DORA-Austausch von IPv4, und Informationen zum Standardrouter stammen normalerweise aus IPv6 Router Advertisements statt aus DHCPv6.

:::single-choice{#dhcp-ipv6-default-router}
Woher erfährt ein IPv6-Host normalerweise seine Standardrouterinformationen?

::option[Aus IPv6 Router Advertisements.]{#dhcp-router-advertisement .correct explanation="DHCPv6 kann andere Konfiguration bereitstellen, doch Router kündigen sich über Neighbor Discovery an."}
::option[Aus einem Ethernet-FCS-Abschluss.]{#dhcp-ipv6-fcs explanation="Die FCS erkennt Verbindungsbeschädigungen und enthält keine Routerkonfiguration."}
::option[Nur aus IPv4-DHCPACK.]{#dhcp-ipv4-ack explanation="IPv4-DHCP-Nachrichten konfigurieren kein IPv6-Routing."}
:::

## Zusammenfassung

Du kannst nun erklären, wie DHCPv4 die Netzwerkkonfiguration eines Hosts least und erneuert.

1. Unterscheide DHCP-Server von Relays und Clientsubnetzen.
2. Verfolge den Austausch DISCOVER, OFFER, REQUEST und ACK.
3. Behandle Adressen und Optionen als zeitlich begrenzten Lease-Zustand.
4. Überprüfe Adresse, Routen, DNS und Lease-Metadaten gemeinsam.
5. Halte DHCPv4-Verhalten von IPv6-Autokonfiguration getrennt.
