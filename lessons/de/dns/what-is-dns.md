---
index: 1
lang: "de"
title: "Was ist DNS?"
meta_title: "Was ist DNS? - DNS"
meta_description: "Erfahren Sie, was DNS ist und wie es Domainnamen in IP-Adressen übersetzt. Verstehen Sie dieses zentrale Internetkonzept mit unserem anfängerfreundlichen Linux-Leitfaden."
meta_keywords: "DNS, Domain Name System, IP-Adresse, Hostname, Linux-Netzwerk, Anfänger, Tutorial, Leitfaden"
---

## Lesson Content

Stellen Sie sich vor, jedes Mal, wenn Sie bei Google suchen wollten, müssten Sie `http://192.78.12.4` anstelle von `www.google.com` eingeben. Nun, ohne DNS ("Domain Name System") wäre genau das der Fall. Die Netzwerkkommunikation auf niedriger Ebene versteht nur die rohe IP-Adresse, um einen Host zu identifizieren. DNS ermöglicht es uns Menschen, Websites und Hosts anhand ihres Namens anstelle einer IP-Adresse zu verfolgen. Es ist wie eine Kontaktliste für das Internet. Wenn Sie den Namen einer Person kennen, aber ihre Telefonnummer nicht wissen, können Sie sie einfach in Ihrer Kontaktliste nachschlagen.

DNS ist im Grunde eine verteilte Datenbank von Hostnamen zu IP-Adressen. Wir verwalten unsere Datenbank, damit die Leute wissen, wie sie zu unserer Website/Domain gelangen, und an anderer Stelle verwaltet eine andere Person ihre Datenbank, damit andere zu ihrer Domain gelangen können. Diese Domains können dann miteinander kommunizieren und eine riesige Kontaktliste des Internets aufbauen.

In diesem Kurs werden wir einige Grundlagen des DNS behandeln, aber seien Sie sich bewusst, dass DNS ein sehr umfangreiches Thema ist, und wenn Sie wirklich tief in die Materie eintauchen möchten, müssen Sie zusätzliche Recherchen anstellen.

## Exercise

Übung macht den Meister! Hier sind einige praktische Übungen, um Ihr Verständnis von DNS und der Hostnamenauflösung zu vertiefen:

1. **[DNS-Einträge in Linux mit dig und nslookup abfragen](https://labex.io/de/labs/linux-query-dns-records-in-linux-with-dig-and-nslookup)** – Lernen Sie, grundlegende Linux-Tools wie `dig` und `nslookup` zu verwenden, um verschiedene DNS-Eintragstypen abzufragen. Dies hilft Ihnen zu verstehen, wie Hostnamen in IP-Adressen aufgelöst werden.
2. **[Lokale Hostnamenauflösung in Linux verwalten](https://labex.io/de/labs/linux-manage-local-hostname-resolution-in-linux)** – Üben Sie das Bearbeiten der Datei `/etc/hosts`, um die lokale Hostnamenauflösung zu verwalten. Dies ist eine grundlegende Fähigkeit, um zu steuern, wie Ihr Linux-System Namen auflöst, ohne sich auf externe DNS-Server zu verlassen.
3. **[Einen lokalen autoritativen DNS-Server unter Linux einrichten](https://labex.io/de/labs/linux-set-up-a-local-authoritative-dns-server-on-linux)** – Sammeln Sie praktische Erfahrungen, indem Sie Ihren eigenen lokalen autoritativen DNS-Server mit `bind9` einrichten und konfigurieren. Dies ermöglicht Ihnen, tiefer in die Verwaltung von DNS-Zonen und -Einträgen einzutauchen.

Diese Übungen helfen Ihnen, die Konzepte in realen Szenarien anzuwenden und Vertrauen in DNS und die Hostnamenauflösung in einer Linux-Umgebung aufzubauen.

## Quiz Question

Wahr oder falsch: DNS hilft uns, MAC-Adressen für Hostnamen zu finden?

## Quiz Answer

False
