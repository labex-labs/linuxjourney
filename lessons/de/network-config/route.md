---
lesson_id: "route"
course_id: "network-config"
lang: "de"
order_index: 2
title: "route"
description: "Lerne, Linux-Routen mit ip zu untersuchen, hinzuzufügen, zu ersetzen, zu löschen und sicher zu überprüfen."
meta_title: "route – Netzwerkkonfiguration"
meta_description: "Lerne, die Linux-Routingtabelle zu verwalten. Diese Anleitung behandelt das Hinzufügen und Löschen von Netzwerkrouten mit dem modernen Befehl ip route und dem älteren route-Befehl."
meta_keywords: "ip route-Befehl unter Linux, Linux ip route-Befehl, Route hinzufügen, Route löschen, Routingtabelle, Netzwerkrouting, Linux-Vernetzung, ip route"
---

Manuelle Routen verändern, wie der Kernel eine ausgehende Schnittstelle und den nächsten Hop auswählt. Ein Fehler kann den Host trennen oder vertraulichen Datenverkehr umleiten. Untersuche deshalb die wirksame Route, den Konfigurationseigentümer und den Wiederherstellungsweg, bevor du den Zustand änderst.

## Die aktuelle Entscheidung untersuchen

Erfasse relevante Routen und frage den Kernel, wie er das Ziel aktuell erreicht:

```bash
$ ip -4 route show
$ ip route get 192.168.2.25
```

Untersuche außerdem Richtlinienregeln und alternative Tabellen, falls vorhanden. Die Routensuche ist ein lokaler Beleg; sie sendet keinen Datenverkehr.

:::single-choice{#route-get-before-change} Warum solltest du `ip route get DESTINATION` vor einer Routenänderung ausführen?

::option[Der Befehl erfasst die aktuelle lokale Entscheidung für Vergleich und Rücknahme.]{#route-get-baseline .correct explanation="Ausgewählte Schnittstelle, nächster Hop und Quelle helfen, die beabsichtigte Änderung zu definieren."}
::option[Er reserviert das Ziel dauerhaft auf jedem Router.]{#route-get-reserves explanation="Der Befehl führt eine lokale Suche aus und verändert keinen entfernten Zustand."}
::option[Er deaktiviert alle Richtlinienroutingregeln.]{#route-get-disables-policy explanation="Die Suche wertet Richtlinien aus, statt sie zu entfernen."}
:::

## Eine Route hinzufügen oder ersetzen

Füge eine Route zum kanonischen Präfix über einen erreichbaren nächsten Hop hinzu:

```bash
$ sudo ip route add 192.168.2.0/23 via 10.11.12.3 dev enp1s0
```

Das Gateway muss über die betreffende Verbindung oder einen ausdrücklich gültigen On-link-Entwurf erreichbar sein. `add` schlägt fehl, wenn bereits eine gleichwertige Route besteht. `replace` erstellt oder ändert eine Route, was für idempotente Konfiguration nützlich ist, aber funktionierenden Zustand überschreiben kann; prüfe zuerst das genaue Ziel.

:::single-choice{#route-add-existing} Was geschieht gewöhnlich, wenn `ip route add` auf eine bereits vorhandene Route zielt?

::option[Der Befehl löscht still das alte Zielpräfix.]{#route-add-deletes explanation="Add meldet normalerweise einen Fehler wegen eines bestehenden Objekts, statt es zu ersetzen."}
::option[Er schlägt fehl, statt die bestehende Route zu ersetzen.]{#route-add-fails .correct explanation="Verwende `replace` nur bewusst, nachdem du geprüft hast, welcher Eintrag sich ändern wird."}
::option[Er startet das ausgewählte Gateway neu.]{#route-add-reboots explanation="Lokale Routenkonfiguration kann auf diese Weise keinen entfernten Neustart anfordern."}
:::

## Genau löschen

Lösche die genauen Routenattribute, wenn mehrere Kandidaten oder Tabellen bestehen können:

```bash
$ sudo ip route del 192.168.2.0/23 via 10.11.12.3 dev enp1s0
```

Eine Löschung nur anhand des Ziels kann breiter als beabsichtigt oder mehrdeutig passen. Erfasse vor dem Entfernen den ursprünglichen Befehl, mit dem sich die Route wiederherstellen lässt.

:::single-choice{#route-delete-precision} Warum solltest du beim Löschen einer Route den nächsten Hop und das Gerät angeben?

::option[Um den beabsichtigten Eintrag genauer zu identifizieren.]{#route-delete-exact .correct explanation="Ausdrückliche Attribute verringern die Gefahr, eine andere Route mit demselben Präfix zu entfernen."}
::option[Um den physischen Netzwerkadapter ebenfalls zu löschen.]{#route-delete-adapter explanation="Das Löschen einer Route entfernt nicht das Verbindungsobjekt des Kernels."}
::option[Um die DNS-Zone des Ziels zu löschen.]{#route-delete-dns explanation="Routing und autoritative DNS-Daten sind getrennte Systeme."}
:::

## Dauerhaftigkeit und Sicherheit bei Fernzugriff

Ein `ip route`-Befehl verändert nur den aktuellen Kernelzustand. NetworkManager, systemd-networkd, Netplan, ifupdown, DHCP, Routing-Daemons oder Orchestrierung können ihn später ersetzen. Speichere die Route erst nach dem Testen des Laufzeitverhaltens beim aktiven Eigentümer.

Bewahre bei einem entfernten Host eine unabhängige Konsole und verwende eine Rücknahme, die nicht von der zu ändernden Route abhängt. Überprüfe anschließend Routensuche, Nachbarzustand, beide Datenverkehrsrichtungen und den tatsächlichen Dienst.

:::single-choice{#route-runtime-persistence} Was kann mit einer manuell hinzugefügten Route nach dem Neuladen eines Netzwerkmanagers geschehen?

::option[Sie wird für immer zu einer unveränderlichen Kernelfunktion.]{#route-manual-immutable explanation="Laufzeitrouten können entfernt oder ersetzt werden."}
::option[Sie erscheint automatisch auf jedem Host im Subnetz.]{#route-manual-all-hosts explanation="Der Befehl verändert nur den aktuellen Netzwerknamensraum."}
::option[Sie kann verschwinden, wenn sie in der dauerhaften Richtlinie fehlt.]{#route-manual-disappears .correct explanation="Der Manager gleicht den Kernelzustand mit seinen konfigurierten Profilen ab."}
:::

## Zusammenfassung

Du kannst nun eine begrenzte Linux-Routenänderung mit einem wiederherstellbaren Ablauf vornehmen.

1. Erfasse aktuelle Routen, Regeln und die wirksame Suche.
2. Verwende ein kanonisches Präfix und einen erreichbaren nächsten Hop.
3. Unterscheide Hinzufügen von bewusstem Ersetzen.
4. Lösche die genaue Route und bewahre einen Wiederherstellungsbefehl.
5. Speichere sie über den aktiven Manager und überprüfe beide Richtungen.
