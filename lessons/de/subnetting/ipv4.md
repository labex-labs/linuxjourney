---
lesson_id: "ipv4"
course_id: "subnetting"
lang: "de"
order_index: 1
title: "IPv4"
description: "Lerne, wie IPv4-Adressen, Präfixe, Geltungsbereiche und die Linux-Schnittstellenausgabe zusammenpassen."
meta_title: "IPv4 – Subnetting"
meta_description: "Beginne mit IPv4-Adressen in Linux. Diese Einführung behandelt IP-Aufbau, Präfixe und wichtige Befehlszeilenwerkzeuge wie ip addr."
meta_keywords: "IPv4, IP-Adresse, Linux für Einsteiger, Linux lernen, Linux-Tutorial, Linux-Netzwerkkurs, Linux-Vernetzung, ifconfig, ip addr"
---

IPv4 stellt 32-Bit-Quell- und Zieladressen für geroutete Pakete bereit. Eine Adresse ist zusammen mit ihrem Präfix, ihrer Schnittstelle, ihrem Geltungsbereich, ihrer Routenrichtlinie und Laufzeit aussagekräftig – nicht als dauerhafte Kennung eines gesamten Geräts.

## Punktgetrennte Dezimalschreibweise

IPv4 wird als vier durch Punkte getrennte Acht-Bit-Oktette dargestellt:

```text
192.0.2.165
```

Jedes Oktett reicht von 0 bis 255, sodass die vollständige Adresse vier Byte enthält. Die Präfixlänge gibt an, wie viele führende Bits zum Netzwerkpräfix gehören, wie in `192.0.2.165/24`.

:::single-choice{#ipv4-address-size}
Wie groß ist eine IPv4-Adresse?

::option[32 Bit in vier Oktetten.]{#ipv4-thirty-two-bits .correct explanation="Vier Gruppen zu je acht Bit ergeben die punktgetrennte Dezimaldarstellung."}
::option[24 Bit in jedem Netzwerk.]{#ipv4-always-twenty-four explanation="Ein `/24` ist eine Präfixlänge und nicht die Größe jeder IPv4-Adresse."}
::option[128 Byte, getrennt durch Doppelpunkte.]{#ipv4-128-bytes explanation="IPv6 besitzt 128 Bit und verwendet eine durch Doppelpunkte getrennte hexadezimale Schreibweise."}
:::

## Adressbereich und Zweck

Nicht jede IPv4-Adresse ist weltweit routbar. Beispiele sind Loopback `127.0.0.0/8`, Link-Local `169.254.0.0/16`, private Bereiche wie `10.0.0.0/8` und Dokumentationsbereiche wie `192.0.2.0/24`. Multicast- und begrenzte Broadcast-Adressen besitzen andere Semantik.

Private Adressen können in getrennten Netzwerken wiederverwendet werden. NAT kann sie für externe Kommunikation übersetzen, ist für die Kommunikation innerhalb der privaten gerouteten Domäne aber nicht erforderlich.

:::single-choice{#ipv4-private-reuse}
Warum kann `10.0.0.1` in vielen Organisationen vorkommen?

::option[Jede Instanz identifiziert denselben physischen Router.]{#ipv4-same-router explanation="Die Adresse besitzt innerhalb jedes Netzwerks Bedeutung und ist nicht weltweit eindeutig."}
::option[IPv4-Router ignorieren das erste Oktett.]{#ipv4-ignore-octet explanation="Alle Adressbits wirken an der Routenübereinstimmung mit."}
::option[Sie liegt in einem Adressbereich, der zur Wiederverwendung in privaten Netzwerken vorgesehen ist.]{#ipv4-private-range .correct explanation="Getrennte private Netzwerke können dieselben Adressen verwenden, ohne sie weltweit anzukündigen."}
:::

## Linux-IPv4-Adressen untersuchen

Zeige IPv4-Zuweisungen an mit:

```bash
$ ip -4 address show
```

Eine solche Zeile meldet mehr als die Adresse:

```text
inet 192.0.2.165/24 brd 192.0.2.255 scope global dynamic eth0
```

Sie zeigt Präfix, Broadcast, Geltungsbereich, Kennzeichnung des dynamischen Ursprungs und Schnittstelle. Weitere Zeilen können gültige und bevorzugte Laufzeiten anzeigen. Eine Schnittstelle kann mehrere IPv4-Adressen besitzen.

:::single-choice{#ipv4-ip-output-prefix}
Was bedeutet `/24` in `192.0.2.165/24`?

::option[Die Adresse läuft nach 24 Sekunden ab.]{#ipv4-prefix-seconds explanation="Die Laufzeit wird getrennt gemeldet."}
::option[Die ersten 24 Adressbits bilden das Netzwerkpräfix.]{#ipv4-prefix-bits .correct explanation="Die verbleibenden acht Bits identifizieren Positionen innerhalb dieses Präfixes."}
::option[Die Schnittstelle ist TCP-Port 24.]{#ipv4-prefix-port explanation="CIDR-Präfixnotation ist unabhängig von Transportports."}
:::

## Die ausgewählte Quelle bestimmen

Das Vorhandensein einer Adresse beweist nicht, dass Linux sie für ein Ziel verwendet. Routen, Richtlinienregeln, Messwerte und Anwendungsbindung beeinflussen die Quellauswahl. Frage die aktuelle Routingentscheidung ab:

```bash
$ ip route get 198.51.100.20
```

Lies den ausgewählten nächsten Hop, die Schnittstelle und Quelle und teste anschließend den tatsächlichen Anwendungspfad. Ändere auf einem entfernten Host keine Adressen ohne Konsolenzugang und Rücknahmeplan.

:::single-choice{#ipv4-route-get-purpose}
Was kann `ip route get DESTINATION` anzeigen?

::option[Die Konfiguration jedes Routers entlang des vollständigen Internetpfads.]{#ipv4-all-router-config explanation="Eine lokale Suche fragt keine Konfigurationen nachgelagerter Geräte ab."}
::option[Die lokale Routenentscheidung einschließlich Schnittstelle und bevorzugter Quelle.]{#ipv4-route-decision .correct explanation="Der Befehl wertet die aktuelle Host-Routingrichtlinie für das angegebene Ziel aus."}
::option[Das Passwort des Zielbenutzers.]{#ipv4-password explanation="Routingbefehle legen keine Anmeldedaten von Anwendungen offen."}
:::

## Zusammenfassung

Du kannst eine IPv4-Adresse nun als Teil des Schnittstellen- und Routingzustands lesen.

1. Erkenne IPv4 als vier Oktette mit insgesamt 32 Bit.
2. Interpretiere eine Adresse zusammen mit ihrem Präfix.
3. Unterscheide private, Loopback-, Link-Local- und weitere Geltungsbereiche.
4. Untersuche Zuweisungen und die für ein Ziel ausgewählte Quelle.
