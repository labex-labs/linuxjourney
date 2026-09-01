---
lesson_id: "dhclient"
course_id: "network-config"
lang: "de"
order_index: 3
title: "dhclient"
description: "Lerne, wann und wie du dhclient verwendest, ohne mit dem Netzwerkmanager des Systems in Konflikt zu geraten."
meta_title: "dhclient – Netzwerkkonfiguration"
meta_description: "Lerne dhclient kennen, erfahre, wie er IP-Adressen über DHCP bezieht und Netzwerk-Leases verwaltet, und verstehe dhclient.conf sowie dhclient.leases."
meta_keywords: "dhclient, DHCP, Linux-Vernetzung, IP-Adresse, Netzwerkkonfiguration, Linux-Tutorial, Einführung"
---

`dhclient` ist ein ISC-DHCP-Client, der auf manchen Linux-Systemen vorhanden ist. Viele aktuelle Installationen lassen stattdessen NetworkManager, systemd-networkd oder einen anderen Dienst einen eigenen DHCP-Client ausführen. Das Starten eines zweiten Clients auf einer verwalteten Schnittstelle kann konkurrierende Adressen, Routen, DNS-Einstellungen und Lease-Zustände erzeugen.

## Den aktiven Client ermitteln

Untersuche vor dem Aufruf von `dhclient` den Konfigurationseigentümer und die Prozesse:

```bash
$ nmcli device status
$ networkctl status
$ ps -ef | grep '[d]hclient'
```

Verwende die auf dem Host vorhandenen Werkzeuge. Wenn ein Manager die Schnittstelle verwaltet, fordere DHCP über diesen Manager an, statt einen getrennten Client zu starten.

:::single-choice{#dhclient-second-client-risk} Warum solltest du `dhclient` nicht auf einer bereits verwalteten Schnittstelle starten?

::option[DHCP kann nur Loopback-Adressen zuweisen.]{#dhclient-loopback-only explanation="DHCP weist gewöhnlich Netzwerkkonfiguration außerhalb von Loopback zu."}
::option[Zwei Clients können um Adressen, Routen, DNS und Leases konkurrieren.]{#dhclient-competing-state .correct explanation="Normalerweise sollte nur der ermittelte Konfigurationseigentümer die Schnittstelle abgleichen."}
::option[Jede DHCP-Anfrage formatiert den lokalen Datenträger neu.]{#dhclient-reformats explanation="Das Protokoll verändert Netzwerkzustand und kein Datenträgerformat."}
:::

## Ein Lease ausdrücklich anfordern

Gib auf einer nicht verwalteten Testschnittstelle, für die `dhclient` der beabsichtigte Eigentümer ist, die Schnittstelle an und verwende ausführliche Ausgabe:

```bash
$ sudo dhclient -v enp1s0
```

Ein Lauf ohne Schnittstelle kann auf mehrere geeignete Schnittstellen wirken. Konfigurations- und Lease-Pfade unterscheiden sich je nach Paket und Aufruf; häufige Namen sind `dhclient.conf` und `dhclient.leases`, doch nimm keinen festen Speicherort an.

:::single-choice{#dhclient-interface-operand} Warum solltest du bei einer manuellen Anfrage `enp1s0` angeben?

::option[Um nur auf die beabsichtigte Netzwerkschnittstelle zu zielen.]{#dhclient-scope-interface .correct explanation="Ein nicht eingeschränkter Clientaufruf kann mehr Schnittstellen als beabsichtigt berücksichtigen."}
::option[Um TCP-Port 1 für DHCP auszuwählen.]{#dhclient-tcp-port explanation="DHCP verwendet UDP, und der Schnittstellenname ist kein Port."}
::option[Um das Lease dauerhaft zu machen.]{#dhclient-permanent explanation="DHCP-Konfiguration bleibt zeitlich begrenzter Lease-Zustand."}
:::

## Ein Lease freigeben

`dhclient -r INTERFACE` fordert die Freigabe an und kann verwendbare Konfiguration entfernen. Dies ist unterbrechend und garantiert nicht, dass der Server erreichbar ist und die Freigabe empfängt. Gib ein Lease nicht nur frei, um es zu untersuchen, insbesondere nicht auf einem Fernverwaltungspfad.

:::single-choice{#dhclient-release-effect} Welches betriebliche Risiko birgt `dhclient -r enp1s0`?

::option[Der Befehl gibt nur das aktuelle Lease aus, ohne Änderungen vorzunehmen.]{#dhclient-release-readonly explanation="Die Freigabe verändert den Zustand."}
::option[Er erneuert jedes Lease für einen unbegrenzten Zeitraum.]{#dhclient-release-renews explanation="Freigeben und Erneuern sind gegensätzliche Vorgänge."}
::option[Er kann die aktuelle DHCP-Konnektivität entfernen.]{#dhclient-release-connectivity .correct explanation="Der Freigabeablauf gibt Lease-Zustand auf und kann den Fernzugriff beenden."}
:::

## Das angewandte Lease überprüfen

Überprüfe nach einer kontrollierten Anfrage mehr als die Adresse:

```bash
$ ip address show dev enp1s0
$ ip route show
$ resolvectl status
```

Untersuche die Protokolle des Managers oder Clients sowie die Lease-Laufzeit und teste anschließend die beabsichtigte Namensauflösung und Anwendung. Ein DHCPACK kann falsche Optionen enthalten, und die erfolgreiche Zuweisung einer Adresse beweist weder Gateway- noch DNS-Erreichbarkeit.

:::single-choice{#dhclient-verify-state} Was sollte nach dem Bezug eines Leases überprüft werden?

::option[Adresse, Routen, DNS, Lease und Anwendungsverhalten.]{#dhclient-complete-verify .correct explanation="Das Lease konfiguriert mehrere zusammengehörige Komponenten, die gemeinsam funktionieren müssen."}
::option[Nur, dass eine Adresszeichenfolge erscheint.]{#dhclient-address-only explanation="Routen, DNS, Laufzeit und Ende-zu-Ende-Funktion können weiterhin falsch sein."}
::option[Nur der Desktophintergrund.]{#dhclient-wallpaper explanation="Das Erscheinungsbild des Desktops hat nichts mit DHCP-Zustand zu tun."}
:::

## Zusammenfassung

Du kannst `dhclient` nun nur dann verwenden, wenn er der beabsichtigte Eigentümer einer Schnittstelle ist.

1. Ermittle den aktiven Netzwerkmanager und DHCP-Client.
2. Vermeide konkurrierende Clients auf einer Schnittstelle.
3. Beschränke eine manuelle Anfrage auf eine benannte Testschnittstelle.
4. Behandle die Freigabe als unterbrechend und überprüfe das vollständige Lease-Ergebnis.
