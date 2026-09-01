---
lesson_id: "network-basics"
course_id: "network-basics"
lang: "de"
order_index: 1
title: "Netzwerkgrundlagen"
description: "Lerne, wie Hosts, Verbindungen, Switches, Router und Pakete lokale und weitreichende Netzwerke bilden."
meta_title: "Netzwerkgrundlagen – Netzwerkgrundlagen"
meta_description: "Beginne mit den Netzwerkgrundlagen und lerne Komponenten wie WAN, LAN, Router und Hosts kennen. Eine verständliche Einführung für Einsteiger."
meta_keywords: "Netzwerkgrundlagen, Linux-Grundlagen, Linux lernen, WAN, LAN, WLAN, Netzwerk-Tutorial, Netzwerk-Anleitung"
---

Ein Netzwerk verbindet Schnittstellen, damit Anwendungen auf unterschiedlichen Hosts Daten austauschen können. Wenn du verstehst, welches Gerät, welche Adresse und welche Verbindung die einzelnen Teile des Pfads verarbeitet, kannst du spätere Linux-Befehle leichter interpretieren.

## Hosts und Schnittstellen

Ein Host ist ein Endpunkt oder vernetztes System, etwa ein Laptop, Server, Telefon oder eine virtuelle Maschine. Ein Host kann mehrere Schnittstellen besitzen: Ethernet, WLAN, Loopback, Tunnel, Bridges oder virtuelle Adapter. Jede Schnittstelle kann eine für ihre Technologie geeignete Konfiguration auf Verbindungs- und Netzwerkschicht besitzen.

Untersuche die Schnittstellen und Adressen eines Linux-Hosts mit:

```bash
$ ip address show
```

Dass eine Schnittstelle vorhanden oder administrativ aktiv ist, beweist keine Ende-zu-Ende-Verbindung.

:::single-choice{#network-basics-host-interface} Was ist eine Netzwerkschnittstelle?

::option[Eine dauerhafte Kopie jedes Pakets im Internet.]{#network-basics-interface-copy explanation="Eine Schnittstelle sendet und empfängt Datenverkehr; sie ist kein weltweites Paketarchiv."}
::option[Der Anschlusspunkt eines Hosts an ein Netzwerk oder eine virtuelle Verbindung.]{#network-basics-interface-attachment .correct explanation="Ein Host kann mehrere physische oder virtuelle Schnittstellen mit getrennter Konfiguration besitzen."}
::option[Ein menschenlesbarer Alias für eine Rechnung des Internetanbieters.]{#network-basics-interface-invoice explanation="Abrechnungsbezeichnungen haben nichts mit Netzwerkanbindungen eines Hosts zu tun."}
:::

## Lokale Netzwerke

Ein lokales Netzwerk, kurz LAN, deckt eine begrenzte Umgebung wie ein Zuhause, Büro oder Rechenzentrumssegment ab. Ethernet-Switches leiten Frames zwischen Ports einer lokalen Verbindung weiter. Ein drahtloses LAN, kurz WLAN, verwendet drahtlose Verbindungstechnik. Kabelgebundene und drahtlose Schnittstellen können dennoch zum selben IP-Subnetz gehören, wenn eine Bridge oder ein Access Point sie verbindet.

:::single-choice{#network-basics-wlan-relationship} In welchem Verhältnis steht ein WLAN zu einem LAN?

::option[Ein WLAN ist immer ein getrenntes weltweites Internet.]{#network-basics-wlan-global explanation="Es ist ein lokales Netzwerk mit drahtloser Verbindungstechnik."}
::option[Ein WLAN ist eine von Routern verwendete Datenträgerpartition.]{#network-basics-wlan-disk explanation="Der Begriff beschreibt Vernetzung und keine Speicheraufteilung."}
::option[Ein WLAN ist eine drahtlose Form eines lokalen Netzwerks.]{#network-basics-wlan-local .correct explanation="Drahtlose und kabelgebundene Verbindungen können sogar zu einer lokalen Broadcast-Domäne gebrückt werden."}
:::

## Router und weitreichende Netzwerke

Ein Router leitet Netzwerkschichtpakete gemäß seiner Routingtabelle zwischen IP-Netzwerken weiter. Ein Heimgerät verbindet häufig Routing, Switching, WLAN-Zugang, Firewall, NAT und DHCP, doch dies bleiben unterschiedliche Funktionen.

Ein Weitverkehrsnetz, kurz WAN, erstreckt sich über größere geografische oder administrative Grenzen. Ein Internetanbieter kann ein Kundennetz mit anderen Netzwerken verbinden, aber „WAN“ bezeichnet nicht einfach jedes Gerät außerhalb eines Hauses.

:::single-choice{#network-basics-router-role} Was ist die kennzeichnende Aufgabe eines Routers?

::option[Pakete zwischen Netzwerken der Netzwerkschicht weiterleiten.]{#network-basics-forward-networks .correct explanation="Routing wählt nächste Hops über Grenzen von IP-Netzwerken hinweg aus."}
::option[Die Dateien jedes Benutzers zwingend als Sicherung speichern.]{#network-basics-router-backup explanation="Dateiaufbewahrung ist nicht die kennzeichnende Routingfunktion."}
::option[Jeden Hostnamen ohne Abfrage von DNS übersetzen.]{#network-basics-router-hostnames explanation="Namensauflösung und Paketweiterleitung sind getrennte Funktionen."}
:::

## Pakete, Frames und Datenströme

Anwendungen erzeugen Daten, die Protokollschichten zur Übertragung aufteilen und kapseln. IP transportiert Pakete über Netzwerke; eine lokale Verbindung trägt jedes Paket in einem technologiespezifischen Frame. Router ersetzen bei jedem Hop gewöhnlich die Kapselung der Verbindungsschicht, während sie das IP-Paket weiterleiten.

Eine Unterhaltung kann viele Pakete in beiden Richtungen umfassen. Verlust, Umordnung, Fragmentierung, erneute Übertragung und Pfadänderungen bedeuten, dass ein einzelnes aufgezeichnetes Paket selten die gesamte Anwendungstransaktion beschreibt.

:::single-choice{#network-basics-router-frame} Was geschieht an einem Router-Hop normalerweise mit der Kapselung der Verbindungsschicht?

::option[Der Router entfernt den eingehenden Frame und erstellt einen Frame für die nächste Verbindung.]{#network-basics-reframe .correct explanation="Das weitergeleitete IP-Paket wird in einem neuen, zur ausgehenden Schnittstelle passenden Frame der Verbindungsschicht transportiert."}
::option[Der gleiche Ethernet-Frame durchquert unverändert das gesamte Internet.]{#network-basics-same-frame explanation="Frames gelten für ihre jeweilige Verbindung und werden an gerouteten Hops ersetzt."}
::option[Die Anwendung löscht die IP-Adressen dauerhaft.]{#network-basics-delete-ip explanation="Routing ist auf Netzwerkschichtadressen angewiesen."}
:::

## Zusammenfassung

Du kannst nun die Hauptbestandteile eines grundlegenden Netzwerkpfads beschreiben.

1. Unterscheide Hosts von ihren physischen und virtuellen Schnittstellen.
2. Erkenne kabelgebundene und drahtlose Formen lokaler Netzwerke.
3. Trenne Routing von anderen Funktionen eines kombinierten Heimgeräts.
4. Unterscheide Frames lokaler Verbindungen von gerouteten IP-Paketen.
