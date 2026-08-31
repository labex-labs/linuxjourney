---
lesson_id: "routing-table"
course_id: "routing"
lang: "de"
order_index: 2
title: "Routingtabelle"
description: "Lerne, Linux-Routen zu lesen und die für ein Ziel ausgewählte Route zu untersuchen."
meta_title: "Routingtabelle – Routing"
meta_description: "Eine Anleitung zum Verständnis der Linux-Routingtabelle. Lerne die Ausgabe von Routingbefehlen mit Ziel, Gateway, Netzmaske und Schnittstelle zu interpretieren."
meta_keywords: "Linux-Routingtabelle, Linux-Routentabelle, genmask, eth0, route-Befehl, Netzwerkrouting, IP-Routing, Ziel, Gateway, Subnetzmaske, Linux-Vernetzung"
---

Der Linux-Routingzustand bestimmt, welche nächsten Hops, Schnittstellen und Quellen für ein IP-Ziel geeignet sind. Die ältere Ansicht `route -n` ist weiterhin anzutreffen, doch `ip route` stellt moderne Routingkonzepte des Kernels unmittelbarer dar.

## IPv4-Routen lesen

Eine Beispielausgabe kann so aussehen:

```text
$ ip -4 route show
default via 192.168.224.2 dev eth0 proto dhcp src 192.168.224.10 metric 100
192.168.224.0/24 dev eth0 proto kernel scope link src 192.168.224.10 metric 100
```

Die verbundene `/24`-Route sendet passende Ziele direkt über `eth0`. Die Standardroute verwendet das Next-Hop-Gateway `192.168.224.2`. `proto` beschreibt, wie die Route installiert wurde, `src` ist eine bevorzugte Quelle für passenden Datenverkehr, und ein Messwert hilft, ansonsten vergleichbare Routen zu ordnen.

:::single-choice{#routing-table-via-meaning}
Was zeigt `via 192.168.224.2` an?

::option[Die einzige Anwendung, die die Route verwenden darf.]{#routing-table-application explanation="Anwendungsautorisierung wird nicht durch das Schlüsselwort `via` codiert."}
::option[Das Next-Hop-Gateway der Route.]{#routing-table-next-hop .correct explanation="Das Paket wird in einem Frame an diesen direkt erreichbaren Router gesendet, während sein IP-Ziel erhalten bleibt."}
::option[Den Dateisystemeinhängepunkt der Route.]{#routing-table-mount explanation="Routingeinträge betreffen Netzwerkweiterleitung und keine Dateisysteme."}
:::

## Verbundene und Standardrouten

Eine Route mit `scope link` und ohne nächsten Hop über `via` behandelt das Präfix als über die Schnittstelle direkt erreichbar. Eine Standardroute passt auf jede Adresse, verliert aber gegen jede geeignete spezifischere Route.

:::single-choice{#routing-table-connected-route}
Wie wird ein verbundenes Ziel mit `scope link` normalerweise erreicht?

::option[Über das Standardgateway, selbst wenn eine verbundene Route passt.]{#routing-table-connected-default explanation="Das verbundene Präfix ist spezifischer und besitzt keinen Gatewayoperanden."}
::option[Indem das Ziel in einen DNS-Server umgewandelt wird.]{#routing-table-connected-dns explanation="Der Namensdienst ist kein Bestandteil einer bereits ausgewählten IP-Route."}
::option[Nach der Nachbarauflösung direkt über die benannte Schnittstelle.]{#routing-table-direct .correct explanation="Der Host löst die direkt erreichbare Adresse des Ziels auf und kapselt den Datenverkehr lokal."}
:::

## Präfixlänge und Messwert

Die Routenauswahl berücksichtigt Richtlinienregeln und wählt das längste geeignete Präfix. Messwerte ordnen Routen innerhalb geeigneter vergleichbarer Mengen; eine Standardroute mit niedrigem Messwert setzt eine passende `/24`-Route nicht nur deshalb außer Kraft, weil ihre Zahl kleiner ist.

:::single-choice{#routing-table-prefix-before-default}
Welche Route passt spezifischer auf `192.168.224.50`?

::option[`192.168.224.0/24 dev eth0`]{#routing-table-twenty-four .correct explanation="Das passende 24-Bit-Präfix ist unter den aufgelisteten Routen am längsten."}
::option[`default via 192.168.224.2`]{#routing-table-default-less-specific explanation="Die Standardroute besitzt die Präfixlänge null."}
::option[`192.168.0.0/16 via 192.168.224.3`]{#routing-table-sixteen explanation="Dies umfasst die Adresse, legt aber weniger Bits fest als `/24`."}
:::

## Richtlinienregeln und mehrere Tabellen

Linux kann gemäß `ip rule` mehrere Routingtabellen anhand von Quelle, Markierung, Schnittstelle oder anderen Selektoren abfragen. Nur die Haupttabelle anzuzeigen kann deshalb den tatsächlichen Pfad verfehlen:

```bash
$ ip rule show
$ ip route show table all
```

Netzwerknamensräume und VRFs können ebenfalls getrennten Zustand besitzen. Führe die Untersuchung im selben Kontext wie der betroffene Prozess aus.

:::single-choice{#routing-table-policy-limit}
Warum erklärt `ip route show` allein möglicherweise nicht den Pfad einer Anwendung?

::option[Richtlinienregeln oder ein anderer Netzwerknamensraum können anderen Routingzustand auswählen.]{#routing-table-policy-context .correct explanation="Die wirksame Suche hängt von Paketattributen und dem Netzwerkkontext des Prozesses ab."}
::option[Linux-Routingtabellen enthalten keine Zielpräfixe.]{#routing-table-no-prefixes explanation="Zielpräfixe sind grundlegende Routenschlüssel."}
::option[Anwendungen senden niemals IP-Pakete.]{#routing-table-apps-never explanation="Anwendungsverkehr wird über Netzwerk- und Transportprotokolle übertragen."}
:::

## Eine wirksame Route abfragen

Bitte den Kernel, ein Ziel und eine optionale Quelle auszuwerten:

```bash
$ ip route get 203.0.113.10
$ ip route get 203.0.113.10 from 192.168.224.10
```

Das Ergebnis sagt die lokale Suche zu diesem Zeitpunkt voraus. Es sendet keine Prüfung und beweist weder Nachbar- noch nachgelagerte, Firewall- oder Anwendungserreichbarkeit.

:::single-choice{#routing-table-route-get-limit}
Was bewirkt `ip route get` nicht?

::option[Die ausgewählte lokale Schnittstelle und den nächsten Hop anzeigen.]{#routing-table-get-does-interface explanation="Dies sind Hauptfelder des Suchergebnisses."}
::option[Die aktuelle lokale Routenrichtlinie für ein Ziel auswerten.]{#routing-table-get-does-policy explanation="Der Befehl führt eine Kernel-Routensuche aus."}
::option[Erfolgreiche Zustellung über jeden nachgelagerten Hop beweisen.]{#routing-table-get-not-probe .correct explanation="Es handelt sich um eine lokale Entscheidungsabfrage und nicht um eine Ende-zu-Ende-Netzwerkprüfung."}
:::

## Zusammenfassung

Du kannst Linux-Routingeinträge nun lesen und die wirksame lokale Entscheidung abfragen.

1. Unterscheide verbundene Routen von Routen über ein Gateway.
2. Lies Präfix-, Schnittstellen-, Protokoll-, Quell- und Messwertfelder.
3. Wende die längste Präfixübereinstimmung an, bevor du relevante Messwerte vergleichst.
4. Berücksichtige Richtlinientabellen, Namensräume und VRFs.
5. Behandle `ip route get` als Suche und nicht als Erreichbarkeitstest.
