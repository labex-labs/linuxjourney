---
index: 4
lang: "de"
title: "Netzwerkadressierung"
meta_title: "Netzwerkadressierung - Netzwerk Grundlagen"
meta_description: "Entdecken Sie die Grundlagen der Netzwerkadressierung. Dieser Leitfaden erklärt MAC-Adressen, IP-Adressen und Hostnamen, Schlüsselkonzepte zum Verständnis der Gerätekommunikation in der Linux-Netzwerknutzung."
meta_keywords: "Netzwerkadressierung, MAC-Adresse, IP-Adresse, Hostname, Netzwerk-Identifikatoren, Linux-Netzwerk, Netzwerk-Grundlagen, Anfänger, Tutorial, Anleitung"
---

## Lesson Content

Bevor wir untersuchen, wie Datenpakete sich über ein Netzwerk bewegen, ist es wichtig, einige Kernterminologien zu verstehen. So wie ein physischer Brief eine Ziel- und eine Absenderadresse benötigt, erfordern Netzwerkpakete ähnliche Informationen, um ihr Ziel zu erreichen. In der Netzwerkkommunikation werden Geräte mithilfe von MAC-Adressen (Media Access Control) und IP-Adressen identifiziert. Um es für Menschen einfacher zu machen, verwenden wir auch Hostnamen.

### MAC-Adressen

A MAC-Adresse ist eine eindeutige, permanente Hardware-Kennung, die einer Netzwerkkarte (NIC) zugewiesen wird. Diese Adresse wird während der Herstellung in das Gerät eingebrannt und ändert sich nicht. Jedes Gerät, das sich mit einem Netzwerk verbindet, wie Ihr Computer oder Smartphone, verfügt über eine NIC mit einer eindeutigen MAC-Adresse. Diese Hardware-Adresse ist für die Kommunikation in einem lokalen Netzwerksegment von entscheidender Bedeutung. Eine Ethernet-MAC-Adresse sieht typischerweise so aus: `00:C4:B5:45:B2:43`. Die ersten drei Bytes der Adresse bilden die Organizationally Unique Identifier (OUI), die den Hersteller identifiziert. Dell verwendet beispielsweise den OUI `00-14-22`, sodass eine Dell-NIC eine MAC-Adresse wie `00-14-22-34-B2-C2` haben könnte.

### IP-Adressen

Eine IP-Adresse ist eine logische Kennung für ein Gerät in einem Netzwerk, wodurch es über verschiedene Netzwerke, einschließlich des Internets, erreichbar ist. Im Gegensatz zu einer MAC-Adresse ist eine IP-Adresse nicht an die Hardware gebunden und kann dynamisch zugewiesen werden. Wir konzentrieren uns vorerst auf IPv4, wobei eine Adresse wie `10.24.12.4` aussieht. IP-Adressen sind für die Softwareseite der Netzwerkkonfiguration von grundlegender Bedeutung und ermöglichen Routing und globale Kommunikation. Während öffentliche IP-Adressen im gesamten Internet eindeutig sind, können sie sich ändern, und Technologien wie Network Address Translation (NAT) ermöglichen private, nicht eindeutige Adressen innerhalb eines lokalen Netzwerks. Es ist wichtig zu bedenken, dass sowohl MAC- (Hardware) als auch IP-Adressen (Software) für eine erfolgreiche Netzwerkkommunikation notwendig sind.

### Hostnamen

Obwohl IP-Adressen für Computer effektiv sind, sind sie für Menschen schwer zu merken. Hostnamen lösen dieses Problem, indem sie einen benutzerfreundlichen Namen einer IP-Adresse zuordnen. Es ist zum Beispiel viel einfacher, sich `myhost.com` zu merken als die entsprechende IP-Adresse, wie z. B. `192.12.41.4`. Diese Zuordnung wird vom Domain Name System (DNS) übernommen, das als Telefonbuch des Internets fungiert und einprägsame Hostnamen in die numerischen IP-Adressen übersetzt, die für das Netzwerk-Routing erforderlich sind.

## Exercise

Übung macht den Meister! Hier sind einige praktische Labs, um Ihr Verständnis von Netzwerk-Identifikatoren wie MAC-Adressen, IP-Adressen und Hostnamen zu festigen:

1. **[MAC- und IP-Adressen in Linux identifizieren](https://labex.io/de/labs/comptia-identify-mac-and-ip-addresses-in-linux-592731)** - Üben Sie die Verwendung des Befehls `ip a`, um Informationen zur Netzwerkadressierung, einschließlich MAC- und IP-Adressen, auf einem Linux-System zu identifizieren.
2. **[IP-Adress-Typen und Erreichbarkeit in Linux erkunden](https://labex.io/de/labs/comptia-explore-ip-address-types-and-reachability-in-linux-592780)** - Erkunden Sie verschiedene IP-Adress-Typen und testen Sie die Netzwerkerreichbarkeit mit `ping` und `ip a`.
3. **[Lokale Namensauflösung in Linux verwalten](https://labex.io/de/labs/comptia-manage-local-hostname-resolution-in-linux-592792)** - Lernen Sie, die lokale Namensauflösung zu verwalten, indem Sie die Datei `/etc/hosts` bearbeiten und Ihre Änderungen testen.

Diese Labs helfen Ihnen, die Konzepte in realen Szenarien anzuwenden und Vertrauen in die grundlegenden Linux-Netzwerkfunktionen aufzubauen.

## Quiz Question

Wie viele Bytes hat eine IPv4-Adresse?

## Quiz Answer

4
