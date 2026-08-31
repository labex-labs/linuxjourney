---
lesson_id: "what-is-dns"
course_id: "dns"
lang: "de"
order_index: 1
title: "Was ist DNS?"
description: "Lerne, wie DNS verteilte Namen und typisierte Resource Records organisiert und auflöst."
meta_title: "Was ist DNS? – DNS"
meta_description: "Lerne das Domain Name System als verteilte, hierarchische Datenbank kennen, die Namen mit typisierten Einträgen für Adressen, E-Mail und Dienste verknüpft."
meta_keywords: "DNS, Domain Name System, IP Adresse, Linux lernen, Hostname, Linux Netzwerk, Resource Records, Namensauflösung"
---

Das Domain Name System ist eine verteilte, hierarchische Datenbank und ein Abfrageprotokoll. Clients können damit typisierte Informationen zu Namen abrufen, darunter Adressen, E-Mail-Routing, autoritative Server, Dienstdaten und Verifizierungseinträge.

## Namen und Resource Records

DNS übersetzt nicht nur einen Hostnamen in eine IP-Adresse. Ein `A`-Eintrag enthält eine IPv4-Adresse, `AAAA` eine IPv6-Adresse, `MX` Daten zum E-Mail-Routing und `NS` die Namen autoritativer Server; zahlreiche weitere Typen enthalten andere Daten. Ein Name kann mehrere Einträge oder überhaupt keinen Adresseintrag besitzen.

:::single-choice{#dns-purpose-beyond-address}
Warum ist DNS mehr als eine Liste aus Hostnamen und Adressen?

::option[Es weist jedem Ethernet-Frame dauerhaft MAC-Adressen zu.]{#dns-mac-frames explanation="Die Nachbarerkennung auf der Sicherungsschicht verwendet DNS nicht auf diese Weise."}
::option[Es speichert typisierte Einträge für verschiedene Arten von Dienst- und Delegierungsdaten.]{#dns-typed-records .correct explanation="Adress-, E-Mail-, Autoritäts-, Alias- und richtlinienbezogene Einträge besitzen unterschiedliche Bedeutungen."}
::option[Es garantiert, dass jede benannte Anwendung funktionsfähig ist.]{#dns-health-guarantee explanation="DNS-Daten können erfolgreich aufgelöst werden, obwohl der Zieldienst nicht verfügbar ist."}
:::

## Hierarchische Namen

Ein vollständig qualifizierter Domainname bezeichnet einen Pfad im DNS-Baum. In `www.example.com.` steht der abschließende Punkt für die Wurzel, `com` liegt darunter, `example` unter `com` und `www` ist ein Name innerhalb dieser Domain. In Benutzeroberflächen wird der abschließende Punkt häufig weggelassen. In Konfigurationen ist er jedoch wichtig, um absolute von lokal relativen Namen zu unterscheiden.

:::single-choice{#dns-trailing-dot}
Wofür steht der abschließende Punkt in `www.example.com.`?

::option[Für die DNS-Wurzel und einen absoluten Namen.]{#dns-root-dot .correct explanation="Der Punkt beendet den vollständigen Pfad vom benannten Knoten bis zur Wurzel."}
::option[Für einen Platzhalter für jede Top-Level-Domain.]{#dns-dot-wildcard explanation="Ein Platzhalter verwendet eine Bezeichnung wie `*` und nicht das Wurzelabschlusszeichen."}
::option[Für die Anweisung, ausschließlich IPv4 zu verwenden.]{#dns-dot-ipv4 explanation="Der Eintragstyp bestimmt die angeforderte Adressfamilie."}
:::

## Verteilte Autorität

DNS-Autorität wird entlang der Hierarchie nach unten delegiert. Root-Server verweisen Resolver an die Server der Top-Level-Domains, die sie wiederum an die autoritativen Server delegierter Zonen weiterleiten. Organisationen verwalten ihre eigenen autoritativen Daten, ohne den gesamten globalen Namensraum auf einem zentralen Server zu speichern.

:::single-choice{#dns-authoritative-data}
Wer liefert die maßgeblichen Daten für eine delegierte DNS-Zone?

::option[Jeder Browser, der die Website zuvor besucht hat.]{#dns-browser-authority explanation="Ein Browsercache ist für die Zone nicht autoritativ."}
::option[Die konfigurierten autoritativen Nameserver der Zone.]{#dns-authoritative-servers .correct explanation="Die Delegierung bezeichnet die Server, die für autoritative Antworten zuständig sind."}
::option[Jeder Router, der ein Paket zu der Adresse weiterleitet.]{#dns-router-authority explanation="Paketweiterleitung und DNS-Autorität sind getrennte Aufgaben."}
:::

## Auflösung und Caching

Der Stub-Resolver eines Hosts sendet eine Abfrage üblicherweise an einen rekursiven Resolver. Dieser kann aus einem gültigen Cache antworten oder die Hierarchie im Auftrag des Clients abfragen. Die TTL eines Eintrags begrenzt, wie lange Cacheeinträge normalerweise wiederverwendet werden dürfen. Das verbessert die Skalierbarkeit, verzögert aber die Sichtbarkeit von Änderungen, bis sich die Caches erneuern.

Eine erfolgreiche DNS-Auflösung beweist weder Route noch Transport-, TLS- oder Anwendungszustand. Ein DNS-Fehler kann außerdem bereits vor einer externen Abfrage entstehen, weil `/etc/hosts`, Suchsuffixe, lokale Caches oder die Richtlinie des Namensdienstes den Systemresolver beeinflussen.

:::single-choice{#dns-cache-ttl-role}
Was steuert die TTL eines DNS-Eintrags in erster Linie?

::option[Wie viele Router ein IP-Paket durchqueren darf.]{#dns-ip-hop-limit explanation="IP-TTL beziehungsweise Hop Limit ist ein anderes Protokollfeld."}
::option[Wie lange die Anwendung funktionsfähig bleiben muss.]{#dns-app-health-time explanation="DNS-Caching garantiert keine Dienstverfügbarkeit."}
::option[Wie lange ein Resolver den Eintrag unter normalen Regeln zwischenspeichern darf.]{#dns-cache-lifetime .correct explanation="Kürzeres oder längeres Caching beeinflusst Abfragelast und Verbreitung von Änderungen."}
:::

## Zusammenfassung

Du kannst DNS nun als typisiertes, zwischengespeichertes und hierarchisches Datensystem beschreiben.

1. Unterscheide DNS-Resource-Record-Typen nach ihrem Zweck.
2. Lies einen vollständig qualifizierten Namen von der Wurzel abwärts.
3. Erkenne Delegierung und autoritative Zuständigkeit.
4. Trenne Namensauflösung von der Verbindung zur Anwendung.
