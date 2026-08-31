---
lesson_id: "dns-components"
course_id: "dns"
lang: "de"
order_index: 2
title: "DNS-Komponenten"
description: "Lerne, wie rekursive Resolver, autoritative Server, Zonen und Resource Records die DNS-Aufgaben aufteilen."
meta_title: "DNS-Komponenten – DNS"
meta_description: "Lerne die Rollen von Stub- und rekursiven Resolvern, autoritativen Nameservern, DNS-Zonen, Resource Records und TTLs kennen."
meta_keywords: "DNS Komponenten, Nameserver, DNS Zone, Resource Records, rekursiver Resolver, autoritativer Server, DNS Tutorial"
---

DNS trennt die clientseitige Rekursion von der autoritativen Veröffentlichung. Wer diese Grenze versteht, verwechselt eine zwischengespeicherte Antwort nicht mit dem Eigentümer einer Zone.

## Stub- und rekursive Resolver

Ein Stub-Resolver in einer Anwendung oder einem Betriebssystem sendet Abfragen an einen konfigurierten rekursiven Resolver. Dieser liefert ein endgültiges Ergebnis, einen Fehler oder das Ergebnis einer Weiterleitung, nachdem er seinen Cache genutzt und bei Bedarf iterative Abfragen ausgeführt hat. Seine Antwort kann das Kennzeichen für eine autoritative Antwort nur dann tragen, wenn der antwortende Server für die Daten autoritativ ist; Rekursion allein macht ihn nicht autoritativ.

:::single-choice{#dns-components-recursive-role}
Was übernimmt ein rekursiver Resolver für einen Stub-Client?

::option[Er ermittelt mithilfe seines Caches und anderer Nameserver ein endgültiges DNS-Ergebnis.]{#dns-components-recursive-result .correct explanation="Der Client überträgt die mehrstufige Suche an den rekursiven Dienst."}
::option[Er ersetzt jeden Netzwerkrouter auf dem Paketpfad.]{#dns-components-replaces-router explanation="Namensauflösung und IP-Weiterleitung sind getrennte Aufgaben."}
::option[Er wird für jeden zwischengespeicherten Eintrag autoritativ.]{#dns-components-cache-authority explanation="Zwischengespeicherte Daten behalten die Autorität ihrer Quelle; der Resolver wird dadurch nicht zum Eigentümer der Zone."}
:::

## Autoritative Nameserver

Ein autoritativer Server antwortet aus Zonendaten, für die er Autorität besitzt. Eine Zone sollte mehrere autoritative Server mit synchronisierten Daten und voneinander unabhängigen Ausfallrisiken besitzen. Ein ausschließlich autoritativer Server muss für beliebige Clients keine Rekursion durchführen.

:::single-choice{#dns-components-authoritative-role}
Wodurch ist ein Server für eine Zone autoritativ?

::option[Er hat die Zone einmal über einen öffentlichen Resolver abgefragt.]{#dns-components-once-queried explanation="Eine Abfrage oder Zwischenspeicherung verleiht keine Autorität."}
::option[Er stellt die Zonendaten gemäß der betreffenden Delegierung und Konfiguration bereit.]{#dns-components-serves-zone .correct explanation="Autorität entsteht durch die DNS-Delegierung und die geladene Zone des Servers, nicht durch eine zwischengespeicherte Kopie."}
::option[Er antwortet auf einen Ping am schnellsten.]{#dns-components-fastest-ping explanation="ICMP-Laufzeiten definieren keine DNS-Autorität."}
:::

## Zonen und Zonenspeicher

Eine Zone ist ein administrativ bereitgestellter Teil des DNS-Namensraums. Sie beginnt an einem Zonen-Apex und kann untergeordnete Zonen delegieren. Zonendaten können in einer Text-Zonendatei gespeichert, aus einer Datenbank erzeugt, über eine API geladen oder von Software synthetisiert werden. Eine „Zonendatei“ ist keine zwingende physische Implementierung.

Der Zonen-Apex besitzt normalerweise einen SOA-Eintrag und eine Gruppe von NS-Einträgen. Delegierungsdaten beim Elternknoten bezeichnen die autoritativen Server der untergeordneten Zone. Mitunter werden sie durch Glue-Adresseinträge ergänzt, die zum Erreichen von Servernamen innerhalb der delegierten Zone erforderlich sind.

:::single-choice{#dns-components-zone-meaning}
Was ist eine DNS-Zone?

::option[Ein administrativ bereitgestellter Teil des Namensraums.]{#dns-components-admin-portion .correct explanation="Sie kann unabhängig vom Speicher-Backend Einträge und Delegierungen enthalten."}
::option[Eine zwingend erforderliche einzelne Textdatei auf jedem Client.]{#dns-components-client-file explanation="Autoritative Implementierungen können verschiedene Speicherformen verwenden; Clients halten nicht jede Zone vor."}
::option[Eine durch ein VLAN bezeichnete Ethernet-Broadcast-Domain.]{#dns-components-vlan explanation="DNS-Zonen und Segmente der Sicherungsschicht sind voneinander unabhängige Konzepte."}
:::

## Felder eines Resource Records

Ein Resource Record besitzt Eigentümername, TTL, Klasse, Typ und typspezifische RDATA. Beispiel:

```text
www.example.com.  300  IN  A  192.0.2.25
```

Der Eigentümer ist `www.example.com.`, die TTL beträgt 300 Sekunden, die Klasse ist Internet, der Typ eine IPv4-Adresse und RDATA ist die Adresse. Regeln für ausgelassene Felder und relative Namen in der Zonendateisyntax erfordern einen sorgfältigen Umgang mit dem Origin.

:::single-choice{#dns-components-mx-type}
Welcher Eintragstyp veröffentlicht Priorität und Hostnamen von Mail Exchangern?

::option[`A`]{#dns-components-a explanation="Ein A-Eintrag speichert eine IPv4-Adresse."}
::option[`NS`]{#dns-components-ns explanation="NS-Einträge bezeichnen autoritative Nameserver."}
::option[`MX`]{#dns-components-mx .correct explanation="MX-RDATA enthält die Priorität und den Namen eines Mail Exchangers."}
:::

## TTL und negatives Caching

Positive Einträge begrenzen mit TTLs ihre Wiederverwendung aus Caches. Auch negative Antworten, etwa ein nachweislich nicht vorhandener Name, können gemäß aus dem SOA abgeleiteten Regeln zwischengespeichert werden. Das Absenken einer TTL kurz vor einer geplanten Änderung wirkt sich nur auf Einträge aus, die nach dem Bekanntwerden des niedrigeren Werts abgerufen werden. Zuvor mit einer längeren TTL zwischengespeicherte Einträge bleiben bis zu ihrem Ablauf erhalten.

:::single-choice{#dns-components-lower-ttl-timing}
Warum sollte eine DNS-TTL lange vor einer geplanten Adressänderung abgesenkt werden?

::option[Die TTL verändert die Ethernet-MTU des Servers.]{#dns-components-ttl-mtu explanation="Cache-Lebensdauer und Paketgröße der Sicherungsschicht stehen in keinem Zusammenhang."}
::option[Eine niedrigere TTL garantiert, dass die neue Anwendung funktioniert.]{#dns-components-ttl-health explanation="Sie beeinflusst das Caching und nicht die Korrektheit des Dienstes."}
::option[Vorhandene Caches brauchen Zeit, um mit der alten längeren TTL gelernte Einträge ablaufen zu lassen.]{#dns-components-old-cache-expiry .correct explanation="Eine Änderung autoritativer Daten kann die verbleibende Lebensdauer eines bereits zwischengespeicherten Eintrags nicht rückwirkend verkürzen."}
:::

## Zusammenfassung

Du kannst DNS-Rekursion, Autorität, Namensraumverwaltung und zwischengespeicherte Einträge nun voneinander trennen.

1. Erkenne die Rollen von Stub- und rekursivem Resolver.
2. Definiere Autorität durch die Bereitstellung einer delegierten Zone.
3. Betrachte eine Zone als Zuständigkeit im Namensraum und nicht als zwingend erforderliche Datei.
4. Lies Eigentümer-, TTL-, Klassen-, Typ- und RDATA-Felder.
5. Plane Cache-Lebensdauern vor DNS-Änderungen.
