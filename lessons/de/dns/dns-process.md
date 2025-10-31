---
index: 3
lang: "de"
title: "DNS-Prozess"
meta_title: "DNS-Prozess - DNS"
meta_description: "Erkunden Sie den schrittweisen DNS-Auflösungsprozess, von Root-Servern bis zum autoritativen DNS-Server. Verstehen Sie, wie ein Linux-Server eine Domain findet – ein entscheidendes Konzept für Produktionsumgebungen und Domain-Hosting."
meta_keywords: "DNS-Prozess, DNS-Abfrage, Domain-Auflösung, Linux DNS, Produktionsserver, Domain-Hosting, DNS-Server, TLD, Root-Server, autoritatives DNS"
---

## Lesson Content

Lassen Sie uns untersuchen, wie ein Computer, wie ein `Linux server`, eine `domain` wie `catzontheinterwebz.com` mithilfe von DNS findet. Der Prozess funktioniert wie ein Trichter, der die Suche eingrenzt, bis wir den spezifischen `DNS server` erreichen, der die Antwort enthält.

### Die anfängliche Abfrage

Zuerst fragt Ihr Host seinen konfigurierten rekursiven DNS-Server: „Wo ist `catzontheinterwebz.com`?“ Dieser rekursive Server, der oft von Ihrem ISP bereitgestellt wird, kennt die Antwort wahrscheinlich nicht direkt. Daher beginnt er den Auflösungsprozess, indem er die höchste Autorität kontaktiert: die Root-Server. Dieser erste Schritt ist derselbe, egal ob Sie von zu Hause aus surfen oder ein `production server` mit einer API kommuniziert.

### Root-Server

Die DNS-Hierarchie des Internets beginnt mit 13 logischen Root-Servern, die weltweit auf Hunderten von physischen Standorten gespiegelt werden. Diese Server kennen nicht die IP-Adresse für jede `domain`, aber sie wissen, wer die Top-Level-Domains (TLDs) wie `.com`, `.org` und `.net` verwaltet. Wenn sie nach `catzontheinterwebz.com` gefragt werden, antwortet ein Root-Server: „Ich weiß es nicht, aber Sie sollten den `.com`-TLD-Server fragen“, und gibt dessen IP-Adresse an.

### Top-Level-Domain-Server

Als Nächstes sendet der rekursive Server eine neue Abfrage an den `.com`-TLD-Server und fragt erneut nach dem Speicherort von `catzontheinterwebz.com`. Die Aufgabe des TLD-Servers ist es, auf die richtigen autoritativen Namenserver für diese spezifische `domain` zu verweisen. Er hat nicht die endgültige IP-Adresse, aber er weiß, welcher `DNS server` für die `domain` verantwortlich ist, eine Einstellung, die oft über Ihren `domain hosting`-Anbieter vorgenommen wird. Der TLD-Server antwortet mit der IP-Adresse dieses autoritativen Namenservers.

### Autoritative DNS-Server

Schließlich sendet der rekursive Server eine letzte Anfrage an den autoritativen `DNS server`. Dies ist der Server, der die tatsächlichen DNS-Einträge für die `domain` `catzontheinterwebz.com` enthält. Dieser Server überprüft seine Einträge, findet den 'A'-Eintrag für den Host und gibt die endgültige IP-Adresse zurück. Dies ist ein entscheidender Schritt für jeden, der eine Website oder Anwendung live `making` (schaltet), da dieser Server die endgültige Verbindung zwischen dem `domain`-Namen und der IP-Adresse des `production server` bereitstellt. Mit der IP-Adresse in der Hand kann Ihr Computer nun die Inhalte abrufen.

## Exercise

Übung macht den Meister! Hier sind einige praktische Labs, um Ihr Verständnis der DNS-Auflösung und -Verwaltung zu festigen:

1. **[DNS-Einträge unter Linux mit dig und nslookup abfragen](https://labex.io/de/labs/comptia-query-dns-records-in-linux-with-dig-and-nslookup-592796)** – Lernen Sie, DNS-Einträge wie A, PTR und MX abzufragen und Ihren Standard-DNS-Server zu identifizieren, was für die Netzwerkfehlerbehebung unerlässlich ist.
2. **[Einen lokalen autoritativen DNS-Server unter Linux einrichten](https://labex.io/de/labs/comptia-set-up-a-local-authoritative-dns-server-on-linux-592803)** – Sammeln Sie praktische Erfahrungen, indem Sie einen lokalen autoritativen DNS-Server installieren und konfigurieren, Zonen definieren und die DNS-Auflösung testen.
3. **[Lokale Hostnamenauflösung unter Linux verwalten](https://labex.io/de/labs/comptia-manage-local-hostname-resolution-in-linux-592792)** – Üben Sie die Verwaltung der lokalen Hostnamenauflösung durch Bearbeiten der Datei `/etc/hosts`, eine Schlüsselqualifikation für die Webentwicklung und Netzwerktests.

Diese Labs helfen Ihnen, die Konzepte in realen Szenarien anzuwenden und Vertrauen in DNS aufzubauen.

## Quiz Question

Was ist die Abkürzung für die Nameserver, auf denen .com, .net, .org usw. Adressen zu finden sind? Bitte antworten Sie nur mit Großbuchstaben des englischen Alphabets.

## Quiz Answer

TLD
