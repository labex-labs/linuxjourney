---
lesson_id: "network-addressing"
course_id: "network-basics"
lang: "de"
order_index: 4
title: "Netzwerkadressierung"
description: "Lerne, wie Verbindungsadressen, IP-Adressen und Hostnamen unterschiedliche Teile der Netzwerkkommunikation identifizieren."
meta_title: "Netzwerkadressierung – Netzwerkgrundlagen"
meta_description: "Entdecke die Grundlagen der Netzwerkadressierung. Diese Anleitung erklärt MAC-Adressen, IP-Adressen und Hostnamen als zentrale Konzepte der Linux-Vernetzung."
meta_keywords: "Netzwerkadressierung, MAC-Adresse, IP-Adresse, Hostname, Netzwerkkennungen, Linux-Vernetzung, Netzwerkgrundlagen, Einsteiger, Tutorial, Anleitung"
---

Netzwerkkommunikation verwendet in unterschiedlichen Geltungsbereichen verschiedene Kennungen. Adressen der Verbindungsschicht stellen Frames auf einer lokalen Verbindung zu, IP-Adressen ermöglichen geroutete Zustellung, und Namen helfen Anwendungen und Menschen bei der Auswahl von Diensten.

## Adressen der Verbindungsschicht

Eine Ethernet-MAC-Adresse ist 48 Bit lang und wird gewöhnlich als sechs hexadezimale Oktette wie `00:c4:b5:45:b2:43` geschrieben. Eine Quelladresse identifiziert eine Schnittstelle auf der aktuellen Verbindung, während ein Ziel Unicast, Multicast oder Broadcast sein kann.

MAC-Adressen sind weder garantiert dauerhaft noch weltweit eindeutig. Software kann eine lokal verwaltete Adresse zuweisen, virtuelle Schnittstellen erzeugen Adressen und WLAN-Datenschutzfunktionen können sie zufällig wählen. Router ersetzen gewöhnlich die Ethernet-Kapselung an jedem Hop, sodass ein entfernter Server die ursprüngliche lokale Ethernet-Quelladresse nicht erhält.

:::single-choice{#network-addressing-mac-scope}
Was ist der normale Geltungsbereich einer Ethernet-MAC-Adresse bei der Paketzustellung?

::option[Die aktuelle lokale Verbindung.]{#network-addressing-local-link .correct explanation="Router erstellen für nachfolgende Hops neue Kapselungen der Verbindungsschicht."}
::option[Jeder geroutete Hop bis zum endgültigen Internetserver.]{#network-addressing-all-hops explanation="Der ursprüngliche Frame durchquert Router nicht unverändert."}
::option[Nur die Textcodierung der Anwendung.]{#network-addressing-text-encoding explanation="Eine MAC-Adresse gehört zur Kapselung der Verbindungsschicht."}
:::

## IP-Adressen und Präfixe

IPv4-Adressen sind 32 Bit beziehungsweise vier Oktette lang, während IPv6-Adressen 128 Bit umfassen. Eine IP-Adresse wird gewöhnlich einer Schnittstelle zugewiesen und zusammen mit einer Präfixlänge wie `192.0.2.10/24` oder `2001:db8::10/64` interpretiert. Das Präfix gibt an, welche führenden Bits das Netzwerk beschreiben.

Eine Schnittstelle kann mehrere IP-Adressen besitzen, und eine Adresse kann sich durch DHCP, Datenschutzadressierung, Failover oder Verwaltung ändern. Private IPv4-Adressen können in getrennten Netzwerken wiederverwendet werden; öffentliche Routing- und NAT-Richtlinien bestimmen die externe Erreichbarkeit.

:::single-choice{#network-addressing-ipv4-size}
Wie groß ist eine IPv4-Adresse?

::option[32 Bit in vier Oktetten.]{#network-addressing-thirty-two .correct explanation="Jede angezeigte Dezimalkomponente stellt acht Bit dar."}
::option[4 Bit in einer einzelnen hexadezimalen Ziffer.]{#network-addressing-four-bits explanation="Vier Bit stellen nur eine hexadezimale Ziffer dar."}
::option[128 Bit in sechzehn Oktetten.]{#network-addressing-128-octets explanation="IPv6 ist 128 Bit und nicht 128 Oktette lang."}
:::

## Hostnamen und Namensauflösung

Ein Hostname ist ein Name und keine Adresse. Die Namensauflösung kann entsprechend der Namensdienstkonfiguration des Hosts `/etc/hosts`, DNS, Multicast-Systeme oder andere Quellen abfragen. Ein Name kann in mehrere Adressen aufgelöst werden, und mehrere Namen können auf einen Dienst verweisen.

Verwende zum Testen dessen, was eine Anwendung wahrscheinlich sieht, den Resolverpfad des Systems:

```bash
$ getent ahosts example.com
```

DNS-Antworten können sich ändern oder zwischengespeichert werden, und eine erfolgreiche Auflösung beweist nicht, dass der Dienst erreichbar ist.

:::single-choice{#network-addressing-getent-purpose}
Warum solltest du bei einer Prüfung der Namensauflösung `getent ahosts` verwenden?

::option[Der Befehl weist die zurückgegebene Adresse dauerhaft jeder Schnittstelle zu.]{#network-addressing-getent-assign explanation="Der Befehl fragt Datenbanken ab und konfiguriert keine Schnittstellen."}
::option[Er fragt den konfigurierten Namensdienstpfad des Systems nach Adressen.]{#network-addressing-system-resolver .correct explanation="Dieser kann gemäß der Hostrichtlinie lokale Dateien und DNS umfassen."}
::option[Er garantiert, dass eine Anwendung auf jedem zurückgegebenen Host fehlerfrei ist.]{#network-addressing-getent-health explanation="Namensabfrage und Anwendungszustand sind getrennte Tests."}
:::

## Einen Linux-Host untersuchen

Zeige Verbindungs- und IP-Konfiguration getrennt an:

```bash
$ ip -brief link
$ ip -brief address
```

Untersuche bei der Diagnose der Erreichbarkeit anschließend Routen und Nachbarzustand. Leite die richtige Quellschnittstelle oder -adresse niemals nur aus der Benennung ab; Routenauswahl, Richtlinienregeln, Namensräume und Tunnel können den Pfad verändern.

:::single-choice{#network-addressing-ip-link-versus-address}
Welche Befehlsansicht konzentriert sich auf zugewiesene IP-Adressen?

::option[`ip -brief address`]{#network-addressing-address-view .correct explanation="Das Adressobjekt zeigt IPv4- und IPv6-Zuweisungen auf Schnittstellen an."}
::option[Nur `ip -brief link`.]{#network-addressing-link-only explanation="Die Verbindungsansicht konzentriert sich auf Schnittstellen- und Verbindungsschichtzustand."}
::option[`pwd`]{#network-addressing-pwd explanation="Pwd gibt das Arbeitsverzeichnis der Shell aus."}
:::

## Zusammenfassung

Du kannst Namen und Adressen nun nach ihrem Netzwerkbereich unterscheiden.

1. Behandle MAC-Adressen als veränderliche Kennungen lokaler Verbindungen.
2. Lies IPv4- und IPv6-Adressen zusammen mit ihren Präfixlängen.
3. Erkenne, dass Schnittstellen mehrere logische Adressen besitzen können.
4. Frage Hostnamen über den konfigurierten Systemresolver ab.
