---
index: 4
lang: "de"
title: "Netzwerkadressierung"
meta_title: "Netzwerkadressierung - Netzwerk-Grundlagen"
meta_description: "Lernen Sie die Grundlagen der Netzwerkadressierung: MAC- vs. IP-Adressen und Hostnamen. Verstehen Sie, wie Geräte in einem Netzwerk kommunizieren. Beginnen Sie Ihre Linux-Netzwerkreise!"
meta_keywords: "Netzwerkadressierung, MAC-Adresse, IP-Adresse, Hostname, Linux-Netzwerk, Anfänger, Tutorial, Anleitung"
---

## Lesson Content

Bevor wir uns ansehen, wie ein Paket über ein Netzwerk bewegt wird, müssen wir uns mit einigen Begriffen vertraut machen. Wenn Sie einen Brief verschicken, müssen Sie wissen, an wen er gesendet wird und woher er kommt. Pakete benötigen die gleiche Information. Unsere Hosts und andere Hosts werden mithilfe von MAC- (Media Access Control) Adressen und IP-Adressen identifiziert. Um es uns Menschen einfacher zu machen, verwenden wir Hostnamen, um einen Host zu identifizieren.

### MAC-Adressen

Eine MAC-Adresse ist ein eindeutiger Bezeichner, der als Hardware-Adresse verwendet wird. Diese Adresse wird sich niemals ändern. Wenn Sie Zugang zum Internet erhalten möchten, benötigt Ihr Computer ein Gerät namens Netzwerkschnittstellenkarte. Dieser Netzwerkadapter hat seine eigene Hardware-Adresse, die zur Identifizierung Ihres Computers verwendet wird. Eine MAC-Adresse für ein Ethernet-Gerät sieht etwa so aus: `00:C4:B5:45:B2:43`. MAC-Adressen werden Netzwerkadaptern bei der Herstellung zugewiesen. Jeder Hersteller hat einen Organizationally Unique Identifier (OUI), um ihn als Hersteller zu identifizieren. Dieser OUI wird durch die ersten 3 Bytes der MAC-Adresse gekennzeichnet. Zum Beispiel hat Dell `00-14-22`, sodass ein Netzwerkadapter von Dell eine MAC-Adresse wie `00-14-22-34-B2-C2` haben könnte.

### IP-Adressen

Eine IP-Adresse wird verwendet, um ein Gerät in einem Netzwerk zu identifizieren. Sie sind hardwareunabhängig und können je nachdem, ob Sie IPv4 oder IPv6 verwenden, in der Syntax variieren (mehr dazu später). Vorerst gehen wir davon aus, dass Sie IPv4 verwenden, sodass eine typische IP-Adresse wie folgt aussehen würde: `10.24.12.4`. IP-Adressen werden auf der Softwareseite der Vernetzung verwendet. Jedes Mal, wenn ein System mit dem Internet verbunden ist, sollte es eine IP-Adresse haben. Sie können sich auch ändern, wenn sich Ihr Netzwerk ändert, und sind im gesamten Internet eindeutig (dies ist nicht immer der Fall, sobald wir NAT kennenlernen).

Denken Sie daran, dass sowohl Software als auch Hardware erforderlich sind, um Pakete über Netzwerke zu bewegen, daher haben wir zwei Bezeichner für jeden: MAC (Hardware) und IP (Software).

### Hostnamen

Eine letzte Möglichkeit, Ihre Maschinen zu identifizieren, sind Hostnamen. Hostnamen nehmen Ihre IP-Adresse und ermöglichen es Ihnen, diese Adresse mit einem menschenlesbaren Namen zu verknüpfen. Anstatt sich `192.12.41.4` zu merken, können Sie sich einfach `myhost.com` merken.

## Exercise

Übung macht den Meister! Hier sind einige praktische Übungen, um Ihr Verständnis von Netzwerkidentifikatoren wie MAC-Adressen, IP-Adressen und Hostnamen zu vertiefen:

1. **[MAC- und IP-Adressen in Linux identifizieren](https://labex.io/de/labs/linux-identify-mac-and-ip-addresses-in-linux-592731)** – Üben Sie die Verwendung des Befehls `ip a`, um Netzwerkinformationen, einschließlich MAC- und IP-Adressen, auf einem Linux-System zu identifizieren.
2. **[IP-Adresstypen und Erreichbarkeit in Linux erkunden](https://labex.io/de/labs/linux-explore-ip-address-types-and-reachability-in-linux-592780)** – Erkunden Sie verschiedene IP-Adresstypen und testen Sie die Netzwerkerreichbarkeit mit `ping` und `ip a`.
3. **[Lokale Hostnamenauflösung in Linux verwalten](https://labex.io/de/labs/linux-manage-local-hostname-resolution-in-linux-592792)** – Lernen Sie, die lokale Hostnamenauflösung zu verwalten, indem Sie die Datei `/etc/hosts` bearbeiten und Ihre Änderungen testen.

Diese Labs helfen Ihnen, die Konzepte in realen Szenarien anzuwenden und Vertrauen in die grundlegende Linux-Vernetzung aufzubauen.

## Quiz Question

Wie viele Bytes hat eine IPv4-Adresse?

## Quiz Answer

4
