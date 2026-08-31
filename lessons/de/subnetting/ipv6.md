---
lesson_id: "ipv6"
course_id: "subnetting"
lang: "de"
order_index: 7
title: "IPv6"
description: "Lerne, IPv6-Adressen, Präfixe, Geltungsbereiche, Autokonfiguration und Linux-Routingzustand zu lesen."
meta_title: "IPv6 – Subnetting"
meta_description: "Eine Einführung in das IPv6-Protokoll. Erfahre, warum IPv6 entwickelt wurde, wie es sich von IPv4 unterscheidet und wie seine Adressierung in modernen Linux-Netzwerken funktioniert."
meta_keywords: "IPv6, IPv4, IP-Adresse, Linux-Vernetzung, Netzwerkprotokolle, Internetprotokoll, Adressknappheit, Einsteiger, Tutorial, Anleitung"
---

IPv6 verwendet 128-Bit-Adressen und wurde für einen wesentlich größeren Adressraum sowie aktualisiertes Paket- und Nachbarerkennungsverhalten entworfen. IPv4 und IPv6 sind getrennte Protokolle; Dual-Stack-Hosts können während des Übergangs beide ausführen.

## IPv6-Notation lesen

Eine IPv6-Adresse wird als acht hexadezimale 16-Bit-Gruppen geschrieben:

```text
2001:0db8:0000:0000:0000:0000:0000:0025
```

Führende Nullen jeder Gruppe können weggelassen werden, und eine zusammenhängende Folge von Nullgruppen kann mit `::` komprimiert werden:

```text
2001:db8::25
```

`::` darf nur einmal vorkommen, weil die Anzahl ausgelassener Gruppen andernfalls mehrdeutig wäre. `2001:db8::/32` ist für Dokumentationsbeispiele reserviert.

:::single-choice{#ipv6-double-colon-rule}
Warum darf `::` höchstens einmal in einer IPv6-Adresse vorkommen?

::option[Mehrere `::`-Markierungen würden die Erweiterung mehrdeutig machen.]{#ipv6-compression-ambiguity .correct explanation="Eine Komprimierungsmarkierung kann auf die genaue Anzahl von Gruppen erweitert werden, die zum Erreichen von acht nötig ist."}
::option[IPv6-Adressen enthalten nur ein Nullbit.]{#ipv6-one-zero explanation="Eine Adresse kann viele Nullbits und Nullgruppen enthalten."}
::option[Die Markierung wählt TCP-Port null aus.]{#ipv6-port-zero explanation="Adresskomprimierung hat nichts mit Transportports zu tun."}
:::

## Adresstypen und Geltungsbereiche

Wichtige Adressen und Bereiche sind:

- `::1/128`: Loopback auf dem lokalen Host.
- `fe80::/10`: Link-Local-Unicast, normalerweise auf IPv6-Schnittstellen vorhanden.
- `2000::/3`: derzeit vergebener Global-Unicast-Bereich.
- `ff00::/8`: Multicast.

IPv6 besitzt keine Broadcast-Adresse; Multicast und Neighbor Discovery übernehmen Anwendungsfälle, für die IPv4 häufig Broadcast verwendet. Ein Link-Local-Ziel kann eine Schnittstellenzone wie `fe80::1%eth0` erfordern, weil auf jeder Verbindung dasselbe Präfix besteht.

:::single-choice{#ipv6-link-local-scope}
Was ist der normale Geltungsbereich einer `fe80::/10`-Adresse?

::option[Jeder Host im weltweiten Internet.]{#ipv6-global-link-local explanation="Global-Unicast-Adressen dienen dem gerouteten weltweiten Bereich."}
::option[Nur eine DNS-Zonendatei.]{#ipv6-dns-only explanation="Link-Local-Adressen werden Schnittstellen zugewiesen und in Netzwerken verwendet."}
::option[Eine lokale Verbindung.]{#ipv6-one-link .correct explanation="Router leiten gewöhnlichen Link-Local-Datenverkehr nicht zwischen Verbindungen weiter."}
:::

## Präfixe und Schnittstellenadressen

Die IPv6-CIDR-Notation verwendet eine Präfixlänge von `/0` bis `/128`. Ein `/64` ist die Standardgröße für die meisten LAN-Subnetze und unterstützt Stateless Address Autoconfiguration. Eine Schnittstelle kann gleichzeitig Link-Local-, stabile globale, temporäre Datenschutz- und weitere Adressen besitzen, jeweils mit bevorzugter und gültiger Laufzeit.

:::single-choice{#ipv6-address-multiplicity}
Warum kann eine Schnittstelle mehrere IPv6-Adressen anzeigen?

::option[IPv6 benötigt eine Adresse für jede hexadezimale Ziffer.]{#ipv6-one-per-digit explanation="Ziffern sind Darstellung und keine getrennten Schnittstellenzuweisungen."}
::option[Unterschiedliche Geltungsbereiche sowie Datenschutz- oder Laufzeitrollen können nebeneinander bestehen.]{#ipv6-several-roles .correct explanation="Link-Local- und eine oder mehrere globale beziehungsweise temporäre Adressen sind normal."}
::option[Jede Adresse identifiziert eine getrennte physische Netzwerkkarte.]{#ipv6-separate-card explanation="Eine Schnittstelle kann mehrere Adressen besitzen."}
:::

## Nachbar- und Routererkennung

IPv6 Neighbor Discovery verwendet ICMPv6 für Adressauflösung, Erkennung doppelter Adressen, Routererkennung und Erreichbarkeitsinformationen. Router Advertisements können Präfixe und Standardrouterinformationen bereitstellen. Hosts können SLAAC mit DHCPv6 für weitere Konfiguration kombinieren; DHCPv6 stellt normalerweise nicht den Standardrouter bereit.

Das Blockieren sämtlichen ICMPv6-Verkehrs zerstört wesentliches Protokollverhalten. Die Firewallrichtlinie sollte die erforderlichen Nachrichtentypen im passenden Geltungsbereich erlauben, statt ICMPv6 als optional zu behandeln.

:::single-choice{#ipv6-default-router-source}
Wie erfährt ein IPv6-Host normalerweise dynamisch einen Standardrouter?

::option[Durch Router Advertisements.]{#ipv6-router-advertisements .correct explanation="Router Discovery ist Teil von ICMPv6 Neighbor Discovery."}
::option[Aus einer Ethernet-Broadcast-Adresse.]{#ipv6-ethernet-broadcast explanation="IPv6 verwendet keine IP-Broadcast-Adresse."}
::option[Aus dem TCP-Drei-Wege-Handshake.]{#ipv6-tcp-handshake explanation="TCP stellt Transportzustand her, nachdem Routing bereits verfügbar ist."}
:::

## IPv6 untersuchen und testen

Untersuche Adressen, Routen und Nachbarn unabhängig:

```bash
$ ip -6 address show
$ ip -6 route show
$ ip -6 neighbor show
$ ping -6 -c 3 2001:db8::25
```

Verwende statt der gezeigten Dokumentationsadresse eine tatsächlich zugewiesene Testadresse. Eine Dual-Stack-Anwendung kann über IPv4 erfolgreich sein, während IPv6 defekt ist, oder umgekehrt. Teste deshalb jede Familie und ihre DNS-`A`- beziehungsweise `AAAA`-Datensätze ausdrücklich.

:::single-choice{#ipv6-dual-stack-test}
Warum solltest du IPv4 und IPv6 bei einem Dual-Stack-Dienst getrennt testen?

::option[Jedes IPv6-Paket muss zuerst zu einem IPv4-Broadcast werden.]{#ipv6-becomes-ipv4 explanation="Natives IPv6 und IPv4 sind unterschiedliche Protokollpfade."}
::option[Die beiden Familien können unterschiedliche DNS-Daten, Routen, Filter und Fehler besitzen.]{#ipv6-independent-paths .correct explanation="Ein erfolgreicher Ausweichpfad kann eine defekte bevorzugte Adressfamilie verbergen."}
::option[IPv6-Werkzeuge können keinen Schnittstellenzustand anzeigen.]{#ipv6-tools-cannot explanation="Die Befehle `ip -6` zeigen Adress-, Routen- und Nachbarzustand."}
:::

## Zusammenfassung

Du kannst häufigen IPv6-Schnittstellen- und Routingzustand nun lesen und testen.

1. Erweitere oder komprimiere acht hexadezimale Adressgruppen korrekt.
2. Unterscheide Loopback-, Link-Local-, globalen und Multicast-Geltungsbereich.
3. Erwarte mehrere IPv6-Adressen und Laufzeiten auf einer Schnittstelle.
4. Bewahre erforderlichen Neighbor-Discovery- und Router-Advertisement-Verkehr.
5. Teste IPv4- und IPv6-Pfade bei Dual-Stack-Diensten unabhängig.
