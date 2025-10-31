---
index: 2
lang: "de"
title: "Ping"
meta_title: "Ping - Fehlerbehebung"
meta_description: "Erfahren Sie, wie Sie den Linux-Ping-Befehl zur Überprüfung der Netzwerkverbindung verwenden. Diese Anleitung erklärt die Ping-Ausgabe, einschließlich der Bedeutung von icmp_seq, TTL und Roundtrip-Zeit. Verstehen Sie, wie Sie die Ping-Sequenz interpretieren, um Netzwerkprobleme zu diagnostizieren."
meta_keywords: "Linux Ping, Netzwerkverbindung, ICMP, TTL, Ping-Befehl, icmp_seq, Ping Sequenz, icmp seq, icmp_seq Bedeutung, Ping icmp_seq, Linux Netzwerk"
---

## Lesson Content

Der Befehl **ping** ist eines der grundlegendsten Netzwerk-Tools, das verwendet wird, um zu testen, ob ein entfernter Host über ein IP-Netzwerk erreichbar ist. Er funktioniert, indem er ICMP ("Internet Control Message Protocol") "Echo Request"-Pakete an den Zielhost sendet und auf eine ICMP "Echo Reply" wartet. Ein erfolgreicher Ping tritt auf, wenn das Anforderungspaket gesendet und eine Antwort empfangen wird.

Betrachten wir einen typischen `ping`-Befehl in Aktion:

```plaintext
pete@icebox:~$ ping -c 3 www.google.com
PING www.google.com (74.125.239.112) 56(84) bytes of data.
64 bytes from nuq05s01-in-f16.1e100.net (74.125.239.112): icmp_seq=1 ttl=128 time=29.0 ms
64 bytes from nuq05s01-in-f16.1e100.net (74.125.239.112): icmp_seq=2 ttl=128 time=23.7 ms
64 bytes from nuq05s01-in-f16.1e100.net (74.125.239.112): icmp_seq=3 ttl=128 time=15.1 ms
```

In diesem Beispiel verwenden wir `ping`, um die Konnektivität zu `www.google.com` zu überprüfen. Die Option `-c 3` weist `ping` an, genau drei Echo-Anforderungspakete zu senden und dann zu stoppen. Standardmäßig sendet `ping` ein Paket pro Sekunde.

### Verständnis der Ping-Ausgabe

Die Ausgabe des `ping icmp_seq`-Befehls liefert wertvolle Diagnoseinformationen. Lassen Sie uns die Schlüsselkomponenten aufschlüsseln.

### ICMP-Sequenz (icmp_seq)

Das Feld `icmp_seq` zeigt die Sequenznummer jedes ICMP-Pakets an. In unserem Beispiel haben wir drei Pakete gesendet, und die Ausgabe zeigt, dass alle drei (`icmp_seq=1`, `icmp_seq=2`, `icmp_seq=3`) erfolgreich zurückgesendet wurden. Die `ping seq` ist entscheidend für die Diagnose von Paketverlusten. Wenn Sie fehlende Sequenznummern bemerken, deutet dies auf ein Verbindungsproblem hin, bei dem einige Pakete ihr Ziel nicht erreichen oder nicht zurückkehren. Wenn die `icmp seq`-Nummern außer der Reihe erscheinen, kann dies auf Netzwerküberlastung oder Latenz hindeuten, da die Pakete länger als das Standardintervall von einer Sekunde für den Roundtrip benötigen. Das Verständnis der `icmp_seq meaning` ist der Schlüssel zur Fehlerbehebung.

### Time To Live (TTL)

Das Feld "Time To Live" (TTL) fungiert als Hop-Zähler für das Paket. Jedes Mal, wenn das Paket einen Router (einen "Hop") passiert, wird der TTL-Wert um eins dekrementiert. Wenn der Zähler Null erreicht, bevor das Paket sein Ziel erreicht, wird es verworfen. Dieser Mechanismus verhindert, dass Pakete endlos im Netzwerk zirkulieren.

### Zeit (Time)

Das Feld `time` misst die Roundtrip-Zeit – die Dauer, die das Paket benötigte, um von Ihrem Gerät zum Zielhost zu gelangen und für die Echo-Antwort zurückzukehren. Dieser Wert wird typischerweise in Millisekunden (ms) gemessen und ist ein primärer Indikator für die Netzwerklatenz.

## Exercise

Übung ist unerlässlich, um Netzwerkdiagnosen zu meistern. Diese praktischen Labs helfen, Ihr Verständnis des `ping`-Befehls zu festigen:

1.  **[Erkunden Sie die Interaktion auf der Netzwerkebene mit ping und arp unter Linux](https://labex.io/de/labs/comptia-explore-network-layer-interaction-with-ping-and-arp-in-linux-592746)** - Verwenden Sie `ping` und `arp`, um Interaktionen auf der Netzwerk- und Datenverbindungsschicht zu untersuchen und zu beobachten, wie das Standard-Gateway den Datenverkehr zu entfernten Zielen verarbeitet.
2.  **[Erkunden Sie IP-Adresstypen und Erreichbarkeit unter Linux](https://labex.io/de/labs/comptia-explore-ip-address-types-and-reachability-in-linux-592780)** - Nutzen Sie `ping` und `ip a`, um den lokalen TCP/IP-Stack zu testen, die öffentliche Internetverbindung zu überprüfen und die Netzwerkerreichbarkeit zu erkunden.
3.  **[Simulieren Sie die Konnektivität auf der Netzwerkebene unter Linux](https://labex.io/de/labs/comptia-simulate-network-layer-connectivity-in-linux-592752)** - Lernen Sie, statische IP-Adressen mit `ip addr` zuzuweisen und die Konnektivität mit `ping` im selben und in verschiedenen Subnetzen zu testen.

Diese Labs helfen Ihnen, die Konzepte der Netzwerkerreichbarkeit und des `ping`-Befehls in realen Szenarien anzuwenden und Ihr Vertrauen in die Netzwerkdiagnose unter Linux zu stärken.

## Quiz Question

What is the roundtrip time unit of measurement? Please answer in English, paying attention to case sensitivity.

## Quiz Answer

ms
