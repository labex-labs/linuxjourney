---
lesson_id: "dns-process"
course_id: "dns"
lang: "de"
order_index: 3
title: "DNS-Auflösungsprozess"
description: "Lerne, wie Stub- und rekursive Resolver Cache, Weiterleitungen, Glue und Autorität zur Beantwortung einer DNS-Abfrage verwenden."
meta_title: "DNS-Auflösungsprozess – DNS"
meta_description: "Verfolge eine DNS-Auflösung von lokaler Richtlinie und Cache über Root- und TLD-Server bis zum autoritativen Server und lerne Glue sowie DNSSEC kennen."
meta_keywords: "DNS Prozess, DNS Abfrage, Domain Auflösung, Linux DNS, DNS Server, TLD, Root Server, autoritatives DNS, Glue, DNSSEC"
---

Eine gewöhnliche Anwendung fragt den Stub-Resolver des Betriebssystems. Dieser berücksichtigt die lokale Namensdienstrichtlinie und sendet eine rekursive Abfrage an einen konfigurierten Resolver. Der rekursive Resolver durchläuft die Hierarchie nur, wenn die Frage nicht bereits aus einem gültigen Cache beantwortet werden kann.

## Mit lokaler Richtlinie und Cache beginnen

Der Systemresolver kann `/etc/hosts`, DNS und andere Quellen in der konfigurierten Reihenfolge berücksichtigen. Suchsuffixe können einen kurzen Namen in mehrere mögliche Namen umwandeln. Ein rekursiver Resolver prüft anschließend positive und negative Cacheeinträge, bevor er Abfragen an übergeordnete Server sendet.

:::single-choice{#dns-process-cache-first} Warum muss ein rekursiver Resolver für eine Abfrage möglicherweise keinen autoritativen Server kontaktieren?

::option[DNS verlangt, dass jede Abfrage zuerst lokal fehlschlägt.]{#dns-process-requires-failure explanation="Ein Resolver kann unmittelbar aus seinem Cache antworten."}
::option[Er besitzt eine noch gültige zwischengespeicherte Antwort.]{#dns-process-valid-cache .correct explanation="Caching vermeidet die erneute Abfrage der Hierarchie, bis die Lebensdauer des Eintrags abläuft."}
::option[Autoritative Server akzeptieren ausschließlich Ethernet-Frames von Clients.]{#dns-process-authoritative-ethernet explanation="DNS arbeitet über IP-Transporte in gerouteten Netzwerken."}
:::

## Einen Root-Server abfragen

Bei einem Cache-Fehlschlag kann ein rekursiver Resolver einen Root-Server fragen. Die DNS-Wurzel besitzt 13 benannte Serveridentitäten von A bis M, die durch Anycast und andere ausfallsichere Bereitstellungstechniken von vielen physischen Instanzen bedient werden. Die Antwort verweist den Resolver normalerweise an autoritative Server der betreffenden Top-Level-Domain, statt die endgültige Hostadresse zurückzugeben.

:::single-choice{#dns-process-root-response} Was gibt ein Root-Server bei einer nicht zwischengespeicherten Abfrage nach `www.example.com` normalerweise zurück?

::option[Eine Weiterleitung zu den Servern der Top-Level-Domain `com`.]{#dns-process-root-referral .correct explanation="Die Hierarchie delegiert die Zuständigkeit, statt jeden endgültigen Hosteintrag an der Wurzel zu speichern."}
::option[Die unter `www.example.com` bereitgestellte Webseite.]{#dns-process-root-webpage explanation="DNS liefert Resource-Record-Daten und keine Anwendungsinhalte."}
::option[Die Ethernet-MAC-Adresse des Ziels.]{#dns-process-root-mac explanation="MAC-Adressen werden auf lokalen Verbindungen und nicht über die DNS-Hierarchie aufgelöst."}
:::

## Weiterleitungen von TLD- und autoritativen Servern folgen

Der Resolver fragt einen autoritativen `com`-Server. Dieser gibt die delegierten autoritativen Nameserver für `example.com` zurück. Die Weiterleitung kann Glue-Adresseinträge enthalten, wenn sie zum Erreichen eines Servers erforderlich sind, dessen Name innerhalb der delegierten untergeordneten Zone liegt. Danach fragt der Resolver einen autoritativen Server nach dem gewünschten Eintrag.

:::single-choice{#dns-process-glue-purpose} Welches Problem hilft DNS-Glue zu lösen?

::option[Die Verschlüsselung von HTTP-Inhalten nach der DNS-Auflösung.]{#dns-process-glue-http explanation="TLS oder andere Anwendungssicherheit verschlüsselt die Inhalte."}
::option[Die Auswahl des schnellsten Ports eines Ethernet-Switches.]{#dns-process-glue-switch explanation="Glue sind Adressdaten einer Delegierung und keine Richtlinie für die Weiterleitung auf der Sicherungsschicht."}
::option[Das Erreichen eines zonenintern benannten Servers ohne zirkuläre Auflösung.]{#dns-process-glue-reachability .correct explanation="Der Elternknoten stellt die Adressdaten bereit, die zum Kontaktieren eines innerhalb der untergeordneten Zone benannten Servers nötig sind."}
:::

## Aliasen und Eintragstypen folgen

Eine Antwort kann einen CNAME-Alias enthalten, der eine weitere Namensauflösung verlangt, oder anwendungsspezifische Einträge, die zusätzliche Abfragen auslösen. Eine Abfrage nach `A` liefert ausschließlich IPv4-Adresseinträge und zugehörige Kettendaten; IPv6-Adressen werden mit einer getrennten `AAAA`-Abfrage abgerufen. Die endgültige Antwort trägt einen Status wie `NOERROR`, `NXDOMAIN` oder `SERVFAIL`, die jeweils unterschiedliche Bedeutungen besitzen.

:::single-choice{#dns-process-nxdomain-meaning} Was meldet `NXDOMAIN`?

::option[Der abgefragte Domainname existiert gemäß einem autoritativen Ergebnis nicht.]{#dns-process-name-does-not-exist .correct explanation="Das unterscheidet sich von einem vorhandenen Namen, dem lediglich der angeforderte Eintragstyp fehlt."}
::option[Der Name existiert und besitzt immer einen leeren A-Eintrag.]{#dns-process-empty-a explanation="Ein vorhandener Name ohne angeforderte Daten erzeugt normalerweise eine No-Data-Antwort und kein NXDOMAIN."}
::option[Der Resolver hat die maximale Ethernet-Frame-Größe erreicht.]{#dns-process-frame-size explanation="Der Status betrifft die Existenz des Namens."}
:::

## Validierung, Caching und Anwendungsnutzung

Ein validierender rekursiver Resolver kann mit DNSSEC-Signaturen und der Vertrauenskette eine authentifizierte Nichtvorhandenseinsauskunft oder die Integrität eines Eintrags prüfen. DNSSEC verschlüsselt keine Abfragen und beweist nicht, dass die Anwendung an der zurückgegebenen Adresse vertrauenswürdig ist.

Der Resolver speichert Ergebnisse innerhalb der TTL-Regeln zwischen und gibt sie an den Stub zurück. Die Anwendung wählt anschließend eine Adresse aus und versucht ihre eigenen Netzwerk- und Sicherheitsprotokolle.

:::single-choice{#dns-process-dnssec-limit} Was bietet eine DNSSEC-Validierung nicht?

::option[Integrität und Ursprungsauthentifizierung für signierte DNS-Daten.]{#dns-process-dnssec-does-integrity explanation="Dies sind zentrale Ziele von DNSSEC."}
::option[Eine authentifizierte Nichtvorhandenseinsauskunft für signierte, nicht vorhandene Daten.]{#dns-process-authenticated-denial explanation="Signierte Mechanismen für Nichtvorhandensein können diese Validierung bereitstellen."}
::option[Vertraulichkeit für DNS-Abfrage und -Antwort.]{#dns-process-no-confidentiality .correct explanation="Verschlüsselung erfordert einen getrennten geschützten DNS-Transport wie DoT oder DoH."}
:::

## Zusammenfassung

Du kannst eine rekursive DNS-Auflösung nun von der lokalen Richtlinie bis zur zwischengespeicherten endgültigen Antwort verfolgen.

1. Prüfe zuerst lokale Quellen und den Resolver-Cache.
2. Folge Weiterleitungen von Root- und Top-Level-Domain-Servern.
3. Nutze Glue zum Erreichen der passenden delegierten Server.
4. Unterscheide Aliase, No-Data-Antworten und nicht vorhandene Namen.
5. Trenne DNSSEC-Integrität von der Vertraulichkeit des Transports.
