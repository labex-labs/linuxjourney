---
lesson_id: "ping"
course_id: "troubleshooting"
lang: "de"
order_index: 2
title: "ping"
description: "Lerne, begrenzte Ping-Tests auszuführen und Antworten, Verlust, RTT, TTL sowie Einschränkungen zu interpretieren."
meta_title: "ping – Fehlersuche"
meta_description: "Lerne, mit dem Linux-Befehl ping Netzwerkkonnektivität zu testen. Diese Anleitung erklärt die Ausgabe einschließlich icmp_seq, TTL und Umlaufzeit."
meta_keywords: "Linux ping, Netzwerkkonnektivität, ICMP, TTL, ping-Befehl, icmp_seq, ping seq, Bedeutung von icmp_seq, Linux-Vernetzung"
---

`ping` sendet ICMP Echo Requests und meldet beobachtete Antworten. Es testet einen Pfad für Steuernachrichten zu einer Adresse; es beweist nicht, dass TCP, UDP, DNS, Authentifizierung oder eine Anwendung funktioniert.

## Einen begrenzten Test ausführen

Sende bei üblichen iputils-Implementierungen drei IPv4-Anfragen mit einem Zeitlimit von zwei Sekunden pro Paket:

```bash
$ ping -4 -c 3 -W 2 example.com
```

Verwende `-6`, um IPv6 auszuwählen. Erfasse die aufgelöste Adresse, weil ein Hostname mehrere Adressen zurückgeben kann und wiederholte Läufe unterschiedlich auswählen können.

:::single-choice{#ping-count-option}
Was fordert `-c 3` an?

::option[Eine Paketnutzlast von genau drei Megabyte.]{#ping-three-megabytes explanation="Die Paketgröße verwendet eine andere Option."}
::option[Drei dauerhafte Routen zum Ziel.]{#ping-three-routes explanation="Ping sendet Prüfdatenverkehr und installiert keine Routen."}
::option[Drei Echo Requests, bevor der Befehl normal beendet wird.]{#ping-three-requests .correct explanation="Eine endliche Anzahl macht die Diagnose begrenzt und wiederholbar."}
:::

## Sequenz und Verlust

`icmp_seq` identifiziert Anfragen innerhalb eines Laufs. Fehlende Antworten tragen zum beobachteten Verlust bei, während Antworten außerhalb der Reihenfolge unterschiedliche Verzögerungen widerspiegeln können. Kleine Stichproben sind unruhig; vergleiche mehrere begrenzte Intervalle und die eigene Fehlerrate der Anwendung.

Verlust kann in beiden Richtungen auftreten, und ICMP-Ratenbegrenzung kann dazu führen, dass Ping-Verlust vom Anwendungsverlust abweicht.

:::single-choice{#ping-sequence-gap}
Worauf kann eine fehlende Antwort zu `icmp_seq` hindeuten?

::option[Das Ziel hat seine MAC-Adresse dauerhaft geändert.]{#ping-sequence-mac explanation="Eine Sequenzlücke allein erlaubt keine solche Schlussfolgerung auf Verbindungsschicht."}
::option[Anfrage oder Antwort ging verloren, wurde gefiltert, über das Zeitlimit hinaus verzögert oder ratenbegrenzt.]{#ping-sequence-possibilities .correct explanation="Die Sequenzlücke bezeichnet eine ausgebliebene beobachtete Antwort, aber weder die genaue Richtung noch Ursache."}
::option[Der Quelldatenträger besitzt keine freien Inodes.]{#ping-sequence-inodes explanation="Der Inode-Zustand des Dateisystems hat nichts mit einer ICMP-Sequenzantwort zu tun."}
:::

## Umlaufzeit

Das Feld `time` ist die Umlaufzeit in Millisekunden vom Senden der Anfrage bis zum Empfang ihrer Antwort. Es verbindet ausgehende Verzögerung, entfernte Verarbeitung und Rückwegverzögerung. Ohne synchronisierte Messungen an den Endpunkten kann es keine Einweglatenz zeigen.

:::single-choice{#ping-rtt-meaning}
Was misst ein gemeldetes `time=23.7 ms`?

::option[Nur die Einweglatenz des ausgehenden Pfads.]{#ping-outbound-only explanation="Ping misst das vollständige Anfrage-Antwort-Intervall."}
::option[Die Betriebsdauer des Zielsystems.]{#ping-target-uptime explanation="Der Wert ist die Zeitmessung der Prüfung und keine Bootdauer."}
::option[Die Umlaufzeit dieses Echos.]{#ping-round-trip .correct explanation="Sie umfasst beide Richtungen und die Verarbeitung am Endpunkt."}
:::

## TTL oder Hop Limit

Die angezeigte IPv4-TTL oder das IPv6-Hop-Limit ist der verbleibende Wert der empfangenen Antwort. Ohne den Anfangswert des Senders und die Rückroute zu kennen, ergibt seine Subtraktion keine genaue Hop-Anzahl. Eine Änderung kann einen anderen Antwortenden, Anfangswert oder Rückweg widerspiegeln.

:::single-choice{#ping-received-ttl}
Was ist die bei einer IPv4 Echo Reply ausgegebene TTL?

::option[Der verbleibende Wert, als die Antwort den lokalen Host erreichte.]{#ping-remaining-ttl .correct explanation="Jeder Router auf dem Rückweg verringerte den Anfangswert des Senders."}
::option[Eine genaue Anzahl der Router in beiden Richtungen.]{#ping-exact-hop-count explanation="Die anfängliche TTL und der gerichtete Pfad werden durch dieses Feld allein nicht festgestellt."}
::option[Die Cachelaufzeit des DNS-Datensatzes.]{#ping-dns-ttl explanation="DNS-TTL und IP-Paket-TTL sind unterschiedliche Felder."}
:::

## Die richtige Schicht testen

Wenn Ping erfolgreich ist, aber ein Dienst fehlschlägt, teste den tatsächlichen Port, TLS, das Protokoll und die Anfrage. Wenn Ping fehlschlägt, untersuche Namensauflösung, `ip route get`, Nachbarzustand, Firewallrichtlinie und Aufzeichnungen, bevor du den Host für ausgefallen erklärst.

:::single-choice{#ping-success-limit}
Was beweist ein erfolgreicher Ping nicht?

::option[Dass ein Pfad für eine ICMP-Anfrage und -Antwort funktioniert hat.]{#ping-icmp-worked explanation="Dies ist der unmittelbare Beleg der Antworten."}
::option[Dass die Antwort eine Sequenznummer enthielt.]{#ping-sequence-present explanation="Die normale Ausgabe meldet die Antwortsequenz unmittelbar."}
::option[Dass die beabsichtigte Anwendung Anfragen annimmt und abschließt.]{#ping-app-not-proven .correct explanation="Anwendungs- und Transportverhalten erfordern einen anwendungsgerechten Test."}
:::

## Zusammenfassung

Du kannst Ping nun als begrenzte ICMP-Messung mit ausdrücklichen Einschränkungen verwenden.

1. Wähle die Adressfamilie und erfasse die aufgelöste Adresse.
2. Begrenze Anzahl und Wartezeit für wiederholbare Tests.
3. Interpretiere Verlust, ohne Richtung oder Ursache anzunehmen.
4. Behandle RTT als Umlaufzeit und TTL als verbleibenden Wert.
5. Teste die tatsächliche Anwendung getrennt.
