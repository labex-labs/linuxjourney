---
index: 3
lang: "de"
title: "DNS-Prozess"
meta_title: "DNS-Prozess - DNS"
meta_description: "Erfahren Sie Schritt für Schritt, wie DNS funktioniert, von Root-Servern bis zum autoritativen DNS. Verstehen Sie den DNS-Lookup-Prozess für Anfänger und fortgeschrittene Benutzer."
meta_keywords: "DNS-Prozess, DNS-Lookup, wie DNS funktioniert, DNS-Tutorial, DNS für Anfänger, Linux DNS, TLD, Root-Server"
---

## Lesson Content

Betrachten wir ein Beispiel, wie Ihr Host eine Domain (catzontheinterwebz.com) mit DNS findet. Im Wesentlichen arbeiten wir uns nach unten vor, bis wir den DNS-Server erreichen, der diese Domain kennt.

### Lokaler DNS-Server

Zuerst fragt unser Host: "Wo ist catzontheinterwebz.com?" Unser lokaler DNS-Server weiß es nicht, also beginnt er ganz oben im Trichter und fragt die Root-Server. Beachten Sie, dass unser Host diese Anfragen nicht direkt stellt, um catzontheinterwebz.com zu finden; die meisten Benutzer kommunizieren mit einem rekursiven DNS-Server, der von ihren ISPs bereitgestellt wird, und dieser Server ist dann damit beauftragt, den Standort von catzontheinterwebz.com zu finden.

### Root-Server

Es gibt 13 Root-Server für das Internet. Sie sind gespiegelt und weltweit verteilt, um DNS-Anfragen für das Internet zu bearbeiten, sodass tatsächlich Hunderte von Servern arbeiten. Sie werden von verschiedenen Organisationen kontrolliert und enthalten Informationen über Top-Level-Domains. Top-Level-Domains sind das, was Sie als .org-, .com-, .net- usw. Adressen kennen. Der Root-Server weiß also nicht, wo catzontheinterwebz.com ist, aber er weist uns an, den .com Top-Level-Domain-DNS-Server unter einer von ihm angegebenen IP-Adresse zu fragen.

### Top-Level-Domain

Jetzt senden wir eine weitere Anfrage an den Nameserver, der Informationen über ".com"-Adressen hat, und fragen, ob er weiß, wo catzontheinterwebz.com ist. Die TLD hat catzontheinterwebz.com nicht in ihren Zonendateien, aber sie sieht einen Eintrag für den Nameserver von catzontheinterwebz.com. Also gibt sie uns die IP-Adresse dieses Nameservers und weist uns an, dort nachzusehen.

### Autoritativer DNS-Server

Nun senden wir eine letzte Anfrage an den DNS-Server, der tatsächlich den gewünschten Eintrag hat. Der Nameserver sieht, dass er eine Zonendatei für catzontheinterwebz.com hat und dass es einen Resource Record für 'www' für diesen Host gibt. Er gibt uns dann die IP-Adresse dieses Hosts, und wir können endlich einige Katzen im Internet sehen.

## Exercise

Übung macht den Meister! Hier sind einige praktische Labs, um Ihr Verständnis der DNS-Auflösung und -Verwaltung zu vertiefen:

1. **[DNS-Einträge in Linux mit dig und nslookup abfragen](https://labex.io/de/labs/linux-query-dns-records-in-linux-with-dig-and-nslookup)** – Lernen Sie, DNS-Einträge wie A, PTR und MX abzufragen und Ihren Standard-DNS-Server zu identifizieren, was für die Netzwerk-Fehlerbehebung unerlässlich ist.
2. **[Einen lokalen autoritativen DNS-Server unter Linux einrichten](https://labex.io/de/labs/linux-set-up-a-local-authoritative-dns-server-on-linux)** – Sammeln Sie praktische Erfahrungen, indem Sie einen lokalen autoritativen DNS-Server installieren und konfigurieren, Zonen definieren und die DNS-Auflösung testen.
3. **[Lokale Hostnamen-Auflösung in Linux verwalten](https://labex.io/de/labs/linux-manage-local-hostname-resolution-in-linux)** – Üben Sie die Verwaltung der lokalen Hostnamen-Auflösung durch Bearbeiten der Datei `/etc/hosts`, eine wichtige Fähigkeit für die Webentwicklung und Netzwerktests.

Diese Labs helfen Ihnen, die Konzepte in realen Szenarien anzuwenden und Vertrauen im Umgang mit DNS aufzubauen.

## Quiz Question

Was ist die Abkürzung für die Nameserver, auf denen .com-, .net-, .org- usw. Adressen gefunden werden?

## Quiz Answer

TLD
