---
index: 2
lang: "de"
title: "Subnetze"
meta_title: "Subnetze - Subnetting"
meta_description: "Meistern Sie die Grundlagen von Linux-Subnetzen und Subnetzmasken. Dieser Leitfaden erklärt Subnetting, Subnetze, Netzwerkpräfixe und wie man die Netzwerksegmentierung in einer Subnetz-Linux-Umgebung verwaltet."
meta_keywords: "subnet linux, linux subnetz, linux subnetzmaske, subnetting subnetze, subnetze, subnetzmaske, netzwerkpräfix, Linux-Netzwerk, IP-Adresse"
---

## Lesson Content

Wie können Sie feststellen, ob sich zwei Computer im selben Netzwerk befinden? Die Antwort liegt im Verständnis des Subnetzes, kurz für Subnetzwerk. Ein Subnetz ist eine logische Unterteilung eines IP-Netzwerks, die Hosts mit ähnlichen IP-Adressen gruppiert. Diese Hosts befinden sich typischerweise in räumlicher Nähe, was einen effizienten Datentransfer zwischen ihnen ermöglicht. Stellen Sie es sich wie das Versenden von Post innerhalb derselben Postleitzahl vor; es ist viel schneller und einfacher, als es in einen anderen Bundesstaat zu senden.

Damit ein Host zu einem **linux subnet** gehört, wird seine IP-Adresse in zwei Teile unterteilt: ein Netzwerkpräfix und eine Host-Kennung. Wenn ein Host beispielsweise die IP 192.168.1.8 und ein anderer 192.168.1.9 hat, teilen sie sich wahrscheinlich dasselbe Netzwerkpräfix. Der gemeinsame Teil identifiziert das Netzwerk, während die eindeutigen Zahlen (8 und 9) die einzelnen Hosts identifizieren.

### Verständnis der Linux-Subnetzmaske

Eine **linux subnet mask** bestimmt, welcher Teil einer IP-Adresse der Netzwerkanteil und welcher der Host-Anteil ist. Eine typische Subnetzmaske sieht wie folgt aus:

```plaintext
255.255.255.0
```

Um dies zu verstehen, müssen wir in Binär denken. Jede Zahl in einer IP-Adresse oder Subnetzmaske ist ein Oktett und repräsentiert 8 Bits. In Binär bedeutet eine `1` „an“ und eine `0` „aus“. Wenn Sie die Binärzahl `11111111` in Dezimal umwandeln, erhalten Sie 255. Das bedeutet, ein Oktett kann von 0 (`00000000`) bis 255 (`11111111`) reichen.

Die `255`er in der Maske „maskieren“ den Netzwerkanteil der IP-Adresse aus. Bei einer Maske von `255.255.255.0` und einer IP von `192.168.1.8` ist also der Teil `192.168.1` das Netzwerk und `8` der Host. Wir bezeichnen eine **subnet linux**-Konfiguration oft durch ihr Netzwerkpräfix gefolgt von der Subnetzmaske, wie z. B. `192.168.1.0/255.255.255.0`.

### Der Zweck von Subnetting Subnets

Warum erstellen wir Subnetze? Die Praxis des **subnetting subnets** ist entscheidend für die effektive Organisation und Verwaltung von Netzwerken. Sie beinhaltet die Aufteilung eines größeren Netzwerks in kleinere, besser handhabbare Segmente. Dies bietet mehrere wichtige Vorteile:

- **Verbesserte Leistung:** Durch die Segmentierung eines Netzwerks reduzieren Sie das Volumen des Broadcast-Verkehrs innerhalb jedes Subnetzes, was zu weniger Überlastung und besserer Gesamtleistung führt.
- **Erhöhte Sicherheit:** Subnetze ermöglichen es Ihnen, verschiedene Teile Ihres Netzwerks zu isolieren. Ein Host in einem Subnetz kann ohne Router nicht direkt mit einem Host in einem anderen interagieren, wodurch eine Sicherheitsgrenze entsteht. Sie können Zugriffsregeln auf dem Router implementieren, um den Datenverkehr zwischen Subnetzen zu steuern.
- **Vereinfachte Verwaltung:** Die Aufteilung eines großen Netzwerks in kleinere logische Einheiten erleichtert die Verwaltung, Fehlerbehebung und Anwendung von Netzwerkrichtlinien.

### Verbinden von Subnetzen

Was ist, wenn Sie sich mit Hosts in einem anderen Netzwerk verbinden müssen, wie z. B. yahoo.com? Um verschiedene Subnetze zu verbinden, benötigen Sie ein Gerät, das mit mehr als einem Subnetz verbunden ist: einen Router.

Zum Beispiel kann ein Host unter `192.168.1.129` in einem Netzwerk mit einer Maske von `255.255.255.0` jeden anderen Host im Netzwerk `192.168.1.0` erreichen. Um auf das Internet zuzugreifen, muss er den Verkehr über sein Gateway senden, welches der Router ist. In vielen Heimnetzwerken ist die Adresse des Routers oft die `.1` des Subnetzes (z. B. `192.168.1.1`). Dieser Router verfügt über eine weitere Verbindung zu einem anderen Subnetz (wie dem Netzwerk Ihres ISP), was die Kommunikation mit dem weiteren Internet ermöglicht.

## Exercise

Übung macht den Meister! Hier sind einige praktische Übungen, um Ihr Verständnis von IP-Adressierung und Subnetting zu festigen:

1.  **[MAC- und IP-Adressen in Linux identifizieren](https://labex.io/de/labs/comptia-identify-mac-and-ip-addresses-in-linux-592731)** – Üben Sie die Verwendung des Befehls `ip a`, um Informationen zur Netzwerkadressierung zu identifizieren, einschließlich IPv4-Adressen, was grundlegend für das Verständnis von Subnetzen ist.
2.  **[IP-Adress-Typen und Erreichbarkeit in Linux erkunden](https://labex.io/de/labs/comptia-explore-ip-address-types-and-reachability-in-linux-592780)** – Lernen Sie, verschiedene IP-Adress-Typen zu erkunden und die Netzwerkerreichbarkeit zu testen, um zu überprüfen, ob sich Hosts im selben Netzwerk befinden.
3.  **[IP-Subnetting und Binärkonvertierung im Linux-Terminal durchführen](https://labex.io/de/labs/comptia-perform-ip-subnetting-and-binary-conversion-in-the-linux-terminal-592782)** – Meistern Sie IP-Subnetting und Binärkonvertierung und wenden Sie die im Unterricht besprochenen Konzepte von Netzwerkpräfixen und Host-Identifizierung direkt an.

Diese Labs helfen Ihnen, die Konzepte in realen Szenarien anzuwenden und Selbstvertrauen im Umgang mit Netzwerkadressierung und Subnetting aufzubauen.

## Quiz Question

Ein Subnetz wird durch ein Netzwerkpräfix und eine Subnetzmaske definiert. Wahr oder Falsch? (Bitte antworten Sie mit 'True' oder 'False'. Die Antwort ist groß-/kleingeschrieben und muss auf Englisch sein.)

## Quiz Answer

True
