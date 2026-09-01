---
lesson_id: "dns-setup"
course_id: "dns"
lang: "de"
order_index: 5
title: "DNS einrichten"
description: "Lerne, autoritative oder rekursive DNS-Dienste auszuwählen, abzusichern, zu validieren und zu betreiben."
meta_title: "DNS einrichten – DNS"
meta_description: "Lerne DNS-Software wie BIND, Unbound, dnsmasq und PowerDNS nach ihrer Rolle auszuwählen sowie Konfiguration, Sicherheit und Betrieb zu planen."
meta_keywords: "Linux DNS, BIND, Unbound, dnsmasq, PowerDNS, DNS Server Einrichtung, autoritativer DNS, rekursiver Resolver"
---

DNS-Software sollte nach ihrer Rolle und den betrieblichen Anforderungen ausgewählt werden, nicht anhand eines universell „besten Servers“. Ein autoritativer Dienst veröffentlicht Zonen; ein rekursiver Dienst beantwortet Clientanfragen durch Auflösung und Caching; ein weiterleitender Resolver sendet Abfragen an einen anderen Resolver. Das Verbinden dieser Rollen verändert die Angriffsfläche.

## Rolle und Implementierung auswählen

- BIND kann mit umfassender Standardunterstützung autoritative und rekursive Dienste bereitstellen.
- Unbound wird häufig als validierender rekursiver Resolver eingesetzt.
- dnsmasq bietet leichtgewichtige Weiterleitung, Caching und DHCP-Funktionen für kleinere kontrollierte Netzwerke.
- PowerDNS bietet getrennte autoritative und rekursive Produkte mit verschiedenen Daten-Backends.

Funktionen und Paketierung ändern sich. Ziehe deshalb die offizielle Dokumentation der installierten Version heran. Stelle nur die benötigte Rolle bereit und deaktiviere unbeabsichtigte Rekursion oder Zonenbereitstellung.

:::single-choice{#dns-setup-authoritative-role} Welche Rolle veröffentlicht die maßgeblichen Einträge der von ihr bereitgestellten Zonen?

::option[Ein autoritativer DNS-Server.]{#dns-setup-authoritative .correct explanation="Er antwortet aus der konfigurierten Zonenautorität, statt beliebige Namen rekursiv zu suchen."}
::option[Ein Ethernet-Switch.]{#dns-setup-switch explanation="Ein Switch leitet Frames der Sicherungsschicht weiter und veröffentlicht keine DNS-Zonen."}
::option[Ein rekursiver Resolver, der beliebige Clientabfragen beantwortet.]{#dns-setup-stub explanation="Ein Stub sendet Abfragen an einen rekursiven Dienst und hostet keine autoritativen Zonen."}
:::

## Vor der Installation planen

Definiere Zonen, Clients, Abfragevolumen, Aktualisierungsmechanismus, DNSSEC-Bedarf, Protokollierung, Überwachung, Sicherungen und Wiederherstellung. Autoritative Zonen benötigen redundante Server und richtig registrierte Delegierungen. Ein rekursiver Dienst braucht ausdrückliche Client-Zugriffskontrollen, Cache-Richtlinien, Erreichbarkeit von Upstreams oder der iterativen Hierarchie und Schutz vor Missbrauch.

Stelle niemals uneingeschränkte Rekursion im Internet bereit. Offene Resolver können für Reflexionsangriffe missbraucht werden und lokale Ressourcen verbrauchen.

:::single-choice{#dns-setup-open-recursion} Warum sollten rekursive Abfragen auf autorisierte Clients beschränkt werden?

::option[Rekursives DNS kann keine Einträge zwischenspeichern.]{#dns-setup-no-cache explanation="Caching ist eine Kernfunktion rekursiver Resolver."}
::option[Autoritative Delegierungen verlangen, dass jeder Benutzer root ist.]{#dns-setup-all-root explanation="Eine DNS-Delegierung gewährt keine Betriebssystemprivilegien."}
::option[Offene Rekursion kann für Verstärkung und Ressourcenverbrauch missbraucht werden.]{#dns-setup-recursion-abuse .correct explanation="Zugriffskontrollen verringern die Nutzung des Resolvers als öffentliche Angriffsinfrastruktur."}
:::

## Konfiguration und Zonendaten validieren

Verwende vor einem Neuladen die Syntax- und Zonenprüfwerkzeuge der Implementierung. Häufige Beispiele für BIND sind:

```bash
$ named-checkconf
$ named-checkzone example.com /etc/bind/zones/db.example.com
```

Führe sie mit den für den Host passenden Berechtigungen und Pfaden aus. Eine erfolgreiche Parserprüfung beweist weder Delegierung und Verbreitung der Seriennummer noch DNSSEC-Vertrauenskette, Firewall-Erreichbarkeit oder richtige Antworten. Führe deshalb kontrollierte Abfragen durch.

:::single-choice{#dns-setup-zone-validation-limit} Was beweist eine erfolgreiche Syntaxprüfung der Zone nicht?

::option[Dass Delegierung und autoritative Antworten von Ende zu Ende funktionieren.]{#dns-setup-not-end-to-end .correct explanation="Elterndaten, Dienstaktivierung, Netzwerkrichtlinie und Laden zur Laufzeit bleiben getrennte Aspekte."}
::option[Dass der Prüfer den Zonentext einlesen kann.]{#dns-setup-parser-proves explanation="Genau dafür liefert die Prüfung einen direkten Beleg."}
::option[Dass die Datei in ihren Einträgen ein Eigentümerfeld besitzt.]{#dns-setup-record-owner explanation="Das Einlesen gültiger Einträge prüft bereits strukturelle Merkmale."}
:::

## Sicher anwenden und testen

Bewahre die aktuelle Konfiguration und den Wiederherstellungszugang, validiere und lade anschließend neu, statt den Dienst neu zu starten, sofern dies unterstützt wird. Frage jeden autoritativen Server bei deaktivierter Rekursion direkt ab und vergleiche SOA-Seriennummer, NS-Gruppe, positive Einträge, nicht vorhandene Namen sowie das Verhalten über UDP und TCP:

```bash
$ dig @192.0.2.53 example.com SOA +norecurse
$ dig @192.0.2.53 missing.example.com A +norecurse
$ dig @192.0.2.53 example.com SOA +norecurse +tcp
```

Teste für Rekursion zugelassene und abgelehnte Clientnetze, DNSSEC-Validierung, Cache-Verhalten und den Ausfall von Upstream-Abhängigkeiten.

:::single-choice{#dns-setup-norecurse-test} Warum fragst du einen autoritativen Server mit `+norecurse` ab?

::option[Um autoritative Antworten zu testen, ohne Rekursion anzufordern.]{#dns-setup-authority-only .correct explanation="Dadurch wird die Zonenbereitstellung von möglichem rekursivem Verhalten getrennt."}
::option[Um jeden Eintrag aus seiner Zone zu entfernen.]{#dns-setup-remove-records explanation="Eine Abfrage bearbeitet keine autoritativen Daten."}
::option[Um alle Antworten durch HTTP zu zwingen.]{#dns-setup-force-http explanation="Die Option steuert das Recursion-Desired-Flag von DNS."}
:::

## Den Dienst betreiben

Überwache Abfragefehler, Latenz, Cache-Verhalten, Ressourcenverbrauch, Zonenübertragungen, Konsistenz der Seriennummern, DNSSEC-Ablauf und Zustand der Delegierung. Sichere Quellkonfiguration und Signaturmaterial geschützt, prüfe aber auch, ob eine frische Instanz die Zonen laden und richtige Antworten bereitstellen kann. Aktualisiere unterstützte Versionen und begrenze Steuerungsschnittstellen, dynamische Aktualisierungen und den Zugriff auf Übertragungen.

:::single-choice{#dns-setup-redundancy-verification} Was sollte die Redundanzprüfung für autoritatives DNS umfassen?

::option[Jeden Server abfragen und den Betrieb testen, während ein anderer nicht verfügbar ist.]{#dns-setup-test-each-server .correct explanation="Mehrere NS-Einträge allein beweisen nicht, dass jeder unabhängige Dienst erreichbar und aktuell ist."}
::option[Nur prüfen, ob alle Server ähnliche Hostnamen besitzen.]{#dns-setup-hostname-similarity explanation="Namen beweisen weder Datensynchronisierung noch Verfügbarkeit."}
::option[Einen gemeinsam genutzten Prozess und Datenträger für jeden angekündigten Server verwenden.]{#dns-setup-shared-failure explanation="Eine gemeinsame Ausfalldomäne schwächt die Redundanz."}
:::

## Zusammenfassung

Du kannst eine DNS-Bereitstellung nun um ausdrückliche Autoritäts- oder Rekursionsrollen herum entwerfen.

1. Wähle Software erst nach Festlegung der benötigten Rolle.
2. Beschränke Rekursion und Verwaltungsschnittstellen.
3. Validiere Konfiguration und Zonen vor dem Neuladen.
4. Teste Autorität, Ablehnung, Transport und Client-Richtlinie direkt.
5. Überwache Redundanz, DNSSEC, Datenkonsistenz und Wiederherstellung.
