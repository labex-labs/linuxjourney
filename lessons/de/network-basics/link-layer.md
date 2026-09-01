---
lesson_id: "link-layer"
course_id: "network-basics"
lang: "de"
order_index: 8
title: "Verbindungsschicht"
description: "Lerne, wie Ethernet-Frames, Nachbarerkennung, Switches und Router Pakete auf einer lokalen Verbindung zustellen."
meta_title: "Verbindungsschicht – Netzwerkgrundlagen"
meta_description: "Erkunde die Grundlagen der TCP/IP-Verbindungsschicht. Lerne den Aufbau von Frames, die Auflösung von IP- in MAC-Adressen mit ARP und den Paketweg in einem lokalen Netzwerk kennen."
meta_keywords: "Verbindungsschicht, Verbindungsschicht-Header, ARP, TCP/IP, MAC-Adresse, Netzwerkgrundlagen, Linux-Vernetzung, Paketweg, Address Resolution Protocol"
---

Die Verbindungsschicht transportiert Pakete der Netzwerkschicht über ein lokales Medium oder eine virtuelle Verbindung. Ethernet und WLAN verwenden unterschiedliche Einzelheiten der Rahmung, stellen aber beide lokale Zustellung unterhalb von IP bereit.

## Ethernet-Frames

Ein Ethernet-Frame enthält Ziel- und Quell-MAC-Adressen, ein EtherType- oder Längenfeld, Nutzlast und eine Frame Check Sequence als Abschluss. Die physische Übertragung verwendet außerdem eine Präambel und einen Startbegrenzer. Die Frame Check Sequence erkennt Beschädigungen auf der Verbindung; sie repariert weder einen beschädigten Frame noch schützt sie ihn kryptografisch.

:::single-choice{#link-layer-fcs-purpose} Wofür wird die Ethernet Frame Check Sequence verwendet?

::option[Zum Erkennen von Framebeschädigungen auf der Verbindung.]{#link-layer-detect-corruption .correct explanation="Ein Empfänger kann einen Frame verwerfen, der die Integritätsprüfung nicht besteht."}
::option[Zum Verschlüsseln der Nutzlast für alle gerouteten Hops.]{#link-layer-fcs-encryption explanation="FCS ist ein Fehlererkennungscode und keine Verschlüsselung oder Authentifizierung."}
::option[Zum Auswählen einer Anwendung anhand des TCP-Ports.]{#link-layer-fcs-port explanation="Transportports werden innerhalb der IP-Nutzlast übertragen."}
:::

## Switches und lokale Zustellung

Ein Ethernet-Switch lernt, an welchen Ports Quell-MAC-Adressen erscheinen, und leitet bekannte Unicast-Frames zum erlernten Zielport weiter. Broadcasts und mancher Datenverkehr mit unbekanntem Ziel werden innerhalb der Broadcast-Domäne geflutet. VLANs können ein Switching-System in getrennte logische Verbindungsdomänen unterteilen.

:::single-choice{#link-layer-switch-learning} Welche Informationen lernt ein Ethernet-Switch normalerweise aus Frames?

::option[Anwendungspasswörter und HTTP-Cookies.]{#link-layer-switch-passwords explanation="Eine grundlegende Weiterleitungstabelle verwendet Verbindungsadressen und keine Anmeldedaten von Anwendungen."}
::option[Die vollständige Internet-Routingtabelle jedes Routers.]{#link-layer-switch-routing-table explanation="Switching auf Schicht 2 und weltweiter Routenaustausch sind unterschiedliche Funktionen."}
::option[Quell-MAC-Adressen und die zugehörigen Switchports.]{#link-layer-switch-source .correct explanation="Dieses Lernen erstellt die Weiterleitungstabelle für späteren bekannten Unicast-Datenverkehr."}
:::

## Die Adresse des nächsten Hops auflösen

Bei IPv4 über Ethernet ordnet das Address Resolution Protocol einer direkt erreichbaren IPv4-Adresse des nächsten Hops eine MAC-Adresse zu. Der Host prüft zuerst seinen Nachbarcache. Falls nötig, sendet er eine ARP-Anfrage als Broadcast, und der Eigentümer oder ein autorisierter Proxy antwortet.

Bei einem nicht direkt erreichbaren IP-Ziel löst der Host die MAC-Adresse des standardmäßigen oder ausgewählten Gateways auf – nicht die MAC-Adresse des entfernten Ziels. IPv6 verwendet statt ARP die Neighbor Discovery über ICMPv6.

:::single-choice{#link-layer-remote-destination-mac} Welche MAC-Adresse verwendet ein Host für ein nicht direkt erreichbares IPv4-Ziel?

::option[Die MAC-Adresse des ausgewählten Next-Hop-Routers.]{#link-layer-gateway-mac .correct explanation="Das IP-Paket bleibt an den entfernten Host adressiert, während der lokale Frame an den Router geht."}
::option[Die MAC-Adresse des entfernten Servers über jeden Router hinweg.]{#link-layer-remote-mac explanation="MAC-Adressen sind Kennungen lokaler Verbindungen und werden nicht von Ende zu Ende übertragen."}
::option[Eine aus dem TCP-Zielport abgeleitete MAC-Adresse.]{#link-layer-port-mac explanation="Transportports bestimmen keine Verbindungsadressen."}
:::

## Nachbarzustand untersuchen

Zeige Einträge von IPv4-ARP und IPv6 Neighbor Discovery an mit:

```bash
$ ip neighbor show
```

Zustände wie `REACHABLE`, `STALE`, `DELAY`, `PROBE` und `FAILED` beschreiben den Prozess zur Erkennung nicht erreichbarer Nachbarn. `STALE` bedeutet nicht defekt; es bedeutet, dass die zwischengespeicherte Erreichbarkeitsbestätigung nicht mehr aktuell ist und bei Verwendung geprüft werden kann.

:::single-choice{#link-layer-stale-neighbor} Was zeigt ein Nachbareintrag mit dem Zustand `STALE` an?

::option[Der Nachbar wird dauerhaft von der Firewall blockiert.]{#link-layer-stale-blocked explanation="Der Zustand beschreibt keine Firewallrichtlinie."}
::option[Die MAC-Adresse wurde als Sicherung auf den Datenträger geschrieben.]{#link-layer-stale-backup explanation="Nachbarzustand ist eine betriebliche Cacheinformation."}
::option[Der zwischengespeicherten Zuordnung fehlt eine aktuelle Erreichbarkeitsbestätigung.]{#link-layer-stale-confirmation .correct explanation="Der Stack kann sie weiterhin verwenden und bei Bedarf eine Erreichbarkeitserkennung durchführen."}
:::

## Kapselung über einen Router hinweg

Der Sender legt ein IP-Paket in einen Frame, der an seinen nächsten Hop adressiert ist. Der Router validiert und entfernt den eingehenden Frame, verarbeitet den IP-Header, wählt eine ausgehende Route und erstellt einen neuen Frame für diese Verbindung. Der Empfänger kehrt die Kapselung um und übergibt die Transportnutzlast an den passenden Socket.

:::single-choice{#link-layer-router-reframing} Was bleibt bei gewöhnlicher Weiterleitung gleich, während sich die Ethernet-Kapselung an einem Router ändert?

::option[Das IP-Ziel, sofern keine Middlebox wie NAT es verändert.]{#link-layer-ip-destination .correct explanation="Gewöhnliche Router leiten zum endgültigen IP-Ziel weiter und ersetzen dabei die hoplokalen Frames."}
::option[Die Frame Check Sequence des eingehenden Frames.]{#link-layer-same-fcs explanation="Ein neuer ausgehender Frame erhält seinen eigenen Integritätswert für die Verbindung."}
::option[Die Ziel-MAC-Adresse auf jeder Verbindung.]{#link-layer-same-mac explanation="Jede Verbindung verwendet die passende Verbindungsadresse des nächsten Hops."}
:::

## Zusammenfassung

Du kannst ein IP-Paket nun durch einen lokalen Zustellungsschritt verfolgen.

1. Erkenne die wichtigsten Felder eines Ethernet-Frames und seinen Integritätsabschluss.
2. Erkläre, wie ein Switch lokale Weiterleitungsorte lernt.
3. Löse einen IPv4-Next-Hop mit ARP und IPv6-Nachbarn mit NDP auf.
4. Interpretiere den Zustand des Nachbarcaches, ohne vorschnell einen Fehler zu behaupten.
5. Erkenne, dass Router Frames für jede ausgehende Verbindung neu erstellen.
