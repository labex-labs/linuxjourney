---
index: 4
lang: "de"
title: "Netzwerkadressierung"
meta_title: "Netzwerkadressierung - Netzwerkgrundlagen"
meta_description: "Lernen Sie die Grundlagen der Netzwerkadressierung: MAC- vs. IP-Adressen und Hostnamen. Verstehen Sie, wie Geräte in einem Netzwerk kommunizieren. Beginnen Sie Ihre Linux-Netzwerkreise!"
meta_keywords: "Netzwerkadressierung, MAC-Adresse, IP-Adresse, Hostname, Linux-Netzwerk, Anfänger, Tutorial, Anleitung"
---

## Lesson Content

Bevor wir uns ansehen, wie ein Paket über ein Netzwerk bewegt wird, müssen wir uns mit einigen Begriffen vertraut machen. Wenn Sie einen Brief verschicken, müssen Sie wissen, an wen er gesendet wird und woher er kommt. Pakete benötigen die gleichen Informationen. Unsere Hosts und andere Hosts werden mithilfe von MAC- (Media Access Control) Adressen und IP-Adressen identifiziert. Um es uns Menschen einfacher zu machen, verwenden wir Hostnamen, um einen Host zu identifizieren.

### MAC Addresses

Eine MAC-Adresse ist ein eindeutiger Bezeichner, der als Hardware-Adresse verwendet wird. Diese Adresse wird sich niemals ändern. Wenn Sie Zugang zum Internet erhalten möchten, muss Ihr Computer ein Gerät namens Netzwerkschnittstellenkarte besitzen. Dieser Netzwerkadapter hat seine eigene Hardware-Adresse, die zur Identifizierung Ihres Computers verwendet wird. Eine MAC-Adresse für ein Ethernet-Gerät sieht etwa so aus: `00:C4:B5:45:B2:43`. MAC-Adressen werden Netzwerkadaptern bei der Herstellung zugewiesen. Jeder Hersteller hat einen Organizationally Unique Identifier (OUI), um ihn als Hersteller zu identifizieren. Dieser OUI wird durch die ersten 3 Bytes der MAC-Adresse gekennzeichnet. Zum Beispiel hat Dell `00-14-22`, sodass ein Netzwerkadapter von Dell eine MAC-Adresse wie `00-14-22-34-B2-C2` haben könnte.

### IP Addresses

Eine IP-Adresse wird verwendet, um ein Gerät in einem Netzwerk zu identifizieren. Sie sind hardwareunabhängig und können je nach Verwendung von IPv4 oder IPv6 (mehr dazu später) in der Syntax variieren. Vorerst gehen wir davon aus, dass Sie IPv4 verwenden, daher würde eine typische IP-Adresse so aussehen: `10.24.12.4`. IP-Adressen werden auf der Softwareseite der Vernetzung verwendet. Jedes Mal, wenn ein System mit dem Internet verbunden ist, sollte es eine IP-Adresse haben. Sie können sich auch ändern, wenn sich Ihr Netzwerk ändert, und sind im gesamten Internet eindeutig (dies ist nicht immer der Fall, sobald wir NAT kennenlernen).

Denken Sie daran, dass sowohl Software als auch Hardware erforderlich sind, um Pakete über Netzwerke zu bewegen, daher haben wir zwei Bezeichner für jedes: MAC (Hardware) und IP (Software).

### Hostnames

Eine letzte Möglichkeit, Ihre Maschinen zu identifizieren, sind Hostnamen. Hostnamen nehmen Ihre IP-Adresse und ermöglichen es Ihnen, diese Adresse mit einem menschenlesbaren Namen zu verknüpfen. Anstatt sich `192.12.41.4` zu merken, können Sie sich einfach `myhost.com` merken.

## Exercise

Keine Übungen für diese Lektion.

## Quiz Question

Wie viele Bytes hat eine IPv4-Adresse?

## Quiz Answer

4
