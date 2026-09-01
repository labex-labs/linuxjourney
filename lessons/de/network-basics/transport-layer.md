---
lesson_id: "transport-layer"
course_id: "network-basics"
lang: "de"
order_index: 6
title: "Transportschicht"
description: "Lerne, wie TCP und UDP Ports sowie unterschiedliche Zustellungssemantiken zwischen Anwendungsendpunkten verwenden."
meta_title: "Transportschicht – Netzwerkgrundlagen"
meta_description: "Erkunde die Transportschicht der Linux-Vernetzung. Diese Lektion behandelt TCP, UDP, Netzwerkports, Datensegmentierung und den TCP-Handshake für zuverlässige Datenübertragung."
meta_keywords: "Linux-Transportschicht, TCP, UDP, TCP-Handshake, Netzwerkports, Datensegmentierung, Linux-Vernetzung, Netzwerkprotokolle, zuverlässige Datenübertragung"
---

Die Transportschicht verbindet Anwendungsendpunkte über ein IP-Netzwerk. TCP und UDP verwenden beide 16-Bit-Portnummern, stellen Anwendungen jedoch unterschiedliche Kommunikationsmodelle und Garantien bereit.

## Ports und Sockets

Ein Zielport hilft dem Betriebssystem, Datenverkehr an einen lauschenden Socket zuzustellen. Eine Verbindung oder ein Datenstrom wird durch mehr als einen Port identifiziert: Protokoll, Quell- und Zieladressen sowie Quell- und Zielports sind alle relevant. Derselbe Serverport kann deshalb viele gleichzeitige Clients bedienen.

:::single-choice{#transport-layer-many-clients} Wie kann ein TCP-Serverport mehrere Clients gleichzeitig bedienen?

::option[Jede Verbindung besitzt eine eigene Kombination aus Endpunktadressen und Ports.]{#transport-layer-connection-tuple .correct explanation="Das vollständige Transporttupel unterscheidet gleichzeitige Verbindungen, die denselben lauschenden Port verwenden."}
::option[Der Server benennt seinen Port nach jedem Paket dauerhaft um.]{#transport-layer-renames-port explanation="Der lauschende Port kann unverändert bleiben, während angenommene Verbindungen unterschiedliche Peer-Tupel besitzen."}
::option[IP entfernt vor der Zustellung alle Quelladressen.]{#transport-layer-removes-source explanation="Quelladressen helfen, Kommunikationspartner und Pfad zu identifizieren."}
:::

## TCP-Byteströme

TCP stellt einen geordneten, zuverlässigen Bytestrom bereit, solange die Verbindung funktionsfähig bleibt. Es verwendet Sequenznummern, Bestätigungen, erneute Übertragung, Flusskontrolle und Überlastungskontrolle. TCP bewahrt keine Nachrichtengrenzen der Anwendung: Ein Schreibvorgang kann über mehrere Lesevorgänge eintreffen, oder mehrere Schreibvorgänge können von einem Lesevorgang zurückgegeben werden. Anwendungen definieren ihre eigene Rahmung.

Zuverlässigkeit bedeutet keine absolute Zustellung. Eine Verbindung kann das Zeitlimit überschreiten, zurückgesetzt werden oder fehlschlagen, und eine Bestätigung beweist nicht, dass eine Anwendung die Daten dauerhaft gespeichert hat.

:::single-choice{#transport-layer-tcp-boundaries} Was geschieht in TCP mit Nachrichtengrenzen der Anwendung?

::option[TCP stellt einen geordneten Bytestrom bereit, ohne Schreibgrenzen zu bewahren.]{#transport-layer-byte-stream .correct explanation="Das Anwendungsprotokoll muss definieren, wie Nachrichten abgegrenzt oder in ihrer Größe angegeben werden."}
::option[Jeder Schreibvorgang wird genau ein IP-Paket und ein Lesevorgang.]{#transport-layer-one-write-packet explanation="Segmentierung, Pufferung und Empfangsschnittstellen bewahren diese Zuordnung nicht."}
::option[TCP wandelt jede Nachricht in einen DNS-Datensatz um.]{#transport-layer-tcp-dns explanation="DNS ist ein getrenntes Anwendungsprotokoll."}
:::

## Der TCP-Handshake

Eine normale TCP-Verbindung beginnt mit einem Drei-Wege-Handshake:

1. Der Initiator sendet `SYN` mit seinen anfänglichen Sequenzinformationen.
2. Der lauschende Endpunkt antwortet mit `SYN-ACK`, eigenen Sequenzinformationen und einer Bestätigung.
3. Der Initiator sendet `ACK` zurück.

Dies richtet in beiden Endpunkten Transportzustand ein. Es authentifiziert weder den Anwendungsserver noch beweist es, dass der angeforderte Anwendungsvorgang erfolgreich sein wird.

:::single-choice{#transport-layer-handshake-order} Was ist die normale Reihenfolge des TCP-Drei-Wege-Handshakes?

::option[SYN, SYN-ACK, ACK.]{#transport-layer-syn-order .correct explanation="Der Austausch synchronisiert und bestätigt den anfänglichen Verbindungszustand in beiden Richtungen."}
::option[ACK, ACK, SYN.]{#transport-layer-ack-ack-syn explanation="Der Initiator fordert zuerst die Synchronisierung an."}
::option[SYN, FIN, RST.]{#transport-layer-syn-fin-rst explanation="FIN und RST schließen beziehungsweise verwerfen Zustand, statt einen normalen Handshake zu bilden."}
:::

## UDP-Datagramme

UDP bewahrt Datagrammgrenzen und bietet prüfsummenbasierte Fehlererkennung, aber keinen TCP-artigen Verbindungszustand, keine Reihenfolge, erneute Übertragung, Flusskontrolle oder Überlastungskontrolle. Eine Anwendung kann benötigte Zuverlässigkeit oder Überlastungssteuerung selbst ergänzen. UDP ist nicht automatisch schneller; die Leistung hängt von Protokollentwurf, Arbeitslast, Pfad und Implementierung ab.

:::single-choice{#transport-layer-udp-boundaries} Welche Eigenschaft stellt UDP Anwendungen bereit?

::option[Einen automatisch erneut übertragenen geordneten Bytestrom.]{#transport-layer-udp-stream explanation="Dies beschreibt TCP-artige Dienste und nicht grundlegendes UDP."}
::option[Bewahrte Grenzen zwischen eingereichten Datagrammen.]{#transport-layer-udp-datagrams .correct explanation="Ein empfangenes UDP-Datagramm entspricht einem gesendeten Datagramm, sofern es nicht verloren geht."}
::option[Garantierte Zustellung vor einer festen Frist.]{#transport-layer-udp-deadline explanation="UDP bietet keine Garantie für eine Zustellungsfrist."}
:::

## Transportendpunkte untersuchen

Verwende `ss`, um lauschende und verbundene Sockets zu untersuchen, ohne sie zu verändern:

```bash
$ ss -lntup
$ ss -tn state established
```

Prozessdetails können erhöhte Berechtigungen erfordern. Ein lauschender Socket beweist lokale Bereitschaft nur an der Transportgrenze; Firewall, Routing, Adressfamilie, TLS und Anwendungszustand benötigen weiterhin geeignete Tests.

:::single-choice{#transport-layer-listener-proof} Was belegt ein lauschender TCP-Socket?

::option[Jede entfernte Firewall erlaubt die Verbindung.]{#transport-layer-all-firewalls explanation="Lokaler Socketzustand zeigt nicht alle Richtlinien entlang des Pfads."}
::option[Die Anwendung hat jede Zustandsprüfung bestanden.]{#transport-layer-all-health explanation="Lauschen ist ein schwächerer Beleg als eine erfolgreiche Anwendungstransaktion."}
::option[Ein lokaler Prozess ist bereit, passende TCP-Verbindungen anzunehmen.]{#transport-layer-local-listener .correct explanation="Entfernte Erreichbarkeit und korrekte Anwendungsantworten bleiben getrennte Fragen."}
:::

## Zusammenfassung

Du kannst das TCP-Stromverhalten nun vom UDP-Datagrammverhalten unterscheiden.

1. Identifiziere einen Datenstrom anhand von Protokoll, Adressen und Ports.
2. Behandle TCP als zuverlässigen geordneten Bytestrom ohne Nachrichtengrenzen.
3. Erkenne, was der TCP-Handshake beweist und was nicht.
4. Behandle UDP-Zuverlässigkeit und Überlastungsverhalten als Entscheidungen des Anwendungsentwurfs.
5. Überprüfe den Anwendungszustand über den lokalen Socketzustand hinaus.
