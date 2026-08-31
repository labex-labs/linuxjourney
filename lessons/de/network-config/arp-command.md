---
lesson_id: "arp-command"
course_id: "network-config"
lang: "de"
order_index: 5
title: "arp"
description: "Lerne, den Zustand des Linux-Nachbarcaches für IPv4-ARP und IPv6 zu untersuchen und zu interpretieren."
meta_title: "arp – Netzwerkkonfiguration"
meta_description: "Lerne den Linux-ARP-Befehl und die Anzeige des ARP-Caches kennen. Verstehe die Rolle von ARP bei der Netzwerkkommunikation."
meta_keywords: "Linux ARP, ARP-Cache, ip neighbour show, Netzwerkbefehle, Linux-Vernetzung, Linux für Einsteiger, Linux-Tutorial"
---

Linux speichert kürzlich aufgelöste Verbindungsadressen der nächsten Hops in der Nachbartabelle. Bei IPv4 über Ethernet werden Einträge durch ARP gelernt; IPv6 verwendet Neighbor Discovery. Der ältere Befehl `arp` zeigt nur einen Teil dieses Zustands, während `ip neighbor` beide Adressfamilien verarbeitet.

## Nachbareinträge anzeigen

Untersuche alle Einträge oder eine einzelne Schnittstelle:

```bash
$ ip neighbor show
$ ip neighbor show dev enp1s0
```

Ein Eintrag enthält eine IP-Adresse, Verbindungsschichtadresse, ein Gerät und einen Erreichbarkeitszustand. Die Tabelle kann nach dem Bootvorgang leer sein und sich füllen, wenn Datenverkehr lokale nächste Hops benötigt.

:::single-choice{#arp-command-modern-view}
Welcher Befehl zeigt den Zustand der modernen Linux-Nachbartabelle an?

::option[`pwd neighbor`]{#arp-command-pwd explanation="Pwd meldet das Arbeitsverzeichnis der Shell."}
::option[`ip neighbor show`]{#arp-command-ip-neighbor .correct explanation="Er meldet sowohl aus IPv4-ARP abgeleitete als auch IPv6-Neighbor-Discovery-Einträge."}
::option[`route --passwords`]{#arp-command-route-passwords explanation="Eine solche Routenuntersuchung sollte keine Anmeldedaten offenlegen."}
:::

## Einen IPv4-Nachbarn auflösen

Wenn eine direkt erreichbare IPv4-Zuordnung fehlt, sendet ein Host eine ARP-Anfrage als Broadcast und fragt, wem die Zieladresse gehört. Das Ziel oder ein Router, der ausdrücklich Proxy-ARP ausführt, antwortet. Der Sender speichert die Zuordnung zwischen und überträgt den wartenden Frame.

Bei einem entfernten IP-Ziel löst der Host die Adresse des ausgewählten Gateways auf und nicht die MAC-Adresse des entfernten Hosts.

:::single-choice{#arp-command-remote-target}
Welchen IPv4-Nachbarn löst ein Host für ein nicht direkt erreichbares Ziel auf?

::option[Den endgültigen entfernten Server über alle Router hinweg.]{#arp-command-final-server explanation="Seine MAC-Adresse besitzt auf der Quellverbindung keine Bedeutung."}
::option[Jeden in der Resolverkonfiguration aufgeführten DNS-Server.]{#arp-command-all-dns explanation="Nachbarauflösung folgt der ausgewählten Route und nicht der Resolverliste."}
::option[Das ausgewählte direkt erreichbare Gateway.]{#arp-command-gateway .correct explanation="Der lokale Ethernet-Frame wird an den Router adressiert, der das IP-Paket weiterleitet."}
:::

## Zustände interpretieren

Häufige Zustände sind `REACHABLE`, `STALE`, `DELAY`, `PROBE`, `INCOMPLETE` und `FAILED`. `STALE` bedeutet, dass die aktuelle Erreichbarkeitsbestätigung abgelaufen ist; die zwischengespeicherte Adresse kann weiterhin verwendet werden, während der Stack bei Bedarf prüft. `FAILED` zeigt an, dass Auflösung oder Erreichbarkeitserkennung nicht erfolgreich war. Ursachen können jedoch Verbindung, VLAN, Adresse, Route, Filterung oder ein ausgeschalteter Kommunikationspartner sein.

:::single-choice{#arp-command-stale-state}
Bedeutet `STALE`, dass der Nachbar nachweislich nicht erreichbar ist?

::option[Nein; es fehlt eine aktuelle Bestätigung, und bei Verwendung kann geprüft werden.]{#arp-command-stale-probe .correct explanation="Der Zustand entspricht nicht `FAILED`."}
::option[Ja, und der Eintrag kann nie wieder verwendet werden.]{#arp-command-stale-dead explanation="Veraltete Einträge bleiben Kandidaten und können nach Erreichbarkeitsprüfungen ihren Zustand wechseln."}
::option[Ja, weil sein DNS-Datensatz abgelaufen ist.]{#arp-command-stale-dns explanation="Nachbarzustand und DNS-Zwischenspeicherung sind getrennt."}
:::

## Nachbarzustand mit Bedacht ändern

Statische Einträge und das Leeren des Caches verändern den Zustand und können aktiven Datenverkehr unterbrechen oder die ursprünglichen Belege verbergen. Erfasse zuerst aktuelle Routen, Paketzähler und Nachbarzustand. Bevorzuge auf einem autorisierten Testnetzwerk eine gezielte Prüfung und Paketaufzeichnung, bevor du eine gesamte Schnittstelle leerst.

ARP besitzt keine eingebaute Authentifizierung. Doppelte Adressen oder gefälschte Antworten können deshalb Zuordnungen vergiften. Schutzfunktionen von Switches, Segmentierung, Überwachung und Authentifizierung auf höheren Schichten helfen, die Auswirkungen zu begrenzen.

:::single-choice{#arp-command-flush-first}
Warum solltest du nicht als ersten Diagnoseschritt die gesamte Nachbartabelle leeren?

::option[Nachbareinträge werden nur auf DNS-Rootservern gespeichert.]{#arp-command-neighbors-dns explanation="Sie werden vom lokalen Netzwerkstack verwaltet."}
::option[Das Leeren entfernt die Schnittstellenhardware dauerhaft.]{#arp-command-flush-hardware explanation="Es entfernt Cacheeinträge und keine physischen Geräte."}
::option[Es verändert Belege und kann ansonsten funktionierende nächste Hops unterbrechen.]{#arp-command-flush-disrupts .correct explanation="Schreibgeschützte Untersuchung und gezielte Tests bewahren den Zustand, der zur Diagnose der Ursache nötig ist."}
:::

## Zusammenfassung

Du kannst die Nachbarauflösung nun untersuchen, ohne jeden Cachezustand als Fehler zu behandeln.

1. Verwende `ip neighbor` für IPv4- und IPv6-Zustand.
2. Löse das Ziel nur auf, wenn es direkt erreichbar ist.
3. Löse ein Gateway für nicht direkt erreichbaren IP-Datenverkehr auf.
4. Bewahre Cachebelege vor gezielten Zustandsänderungen.
