---
lesson_id: "dns-tools"
course_id: "dns"
lang: "de"
order_index: 6
title: "DNS-Werkzeuge"
description: "Lerne, die Systemauflösung und direkte DNS-Abfragen mit getent, resolvectl und dig zu vergleichen."
meta_title: "DNS-Werkzeuge – DNS"
meta_description: "Lerne DNS unter Linux mit getent, resolvectl und dig zu untersuchen. Vergleiche Systemresolver, direkte Serverabfragen, Flags, Reverse-Lookups und TCP."
meta_keywords: "dig Befehl, DNS Werkzeuge, Linux DNS, DNS Fehlersuche, getent, resolvectl, Nameserver Abfrage"
---

Bei der DNS-Fehlersuche musst du zuerst bestimmen, welche Ebene getestet wird. Werkzeuge für den Systemresolver beziehen lokale Dateien und Richtlinien ein, während `dig` und `nslookup` DNS-Abfragen senden und einen bestimmten Server direkt ansprechen können.

## Den Systemresolver testen

Verwende den normalen Namensdienstpfad des Hosts:

```bash
$ getent ahosts www.example.com
```

Untersuche auf einem Host mit systemd-resolved die Server, Suchdomains und den Protokollzustand pro Verbindung:

```bash
$ resolvectl status
$ resolvectl query www.example.com
```

Eine Anwendung kann weiterhin eine eigene Resolver-Bibliothek oder einen Proxy verwenden. Stelle die Abfrage deshalb über die Anwendung nach, wenn sich die Ausgaben unterscheiden.

:::single-choice{#dns-tools-system-resolver}
Welcher Befehl durchläuft den konfigurierten Namensdienstpfad des Systems?

::option[Nur `dig @SERVER NAME`.]{#dns-tools-dig-direct explanation="Dig sendet eine DNS-Abfrage und liest normalerweise keine Zuordnungen der Hosts-Datei."}
::option[`ip link set down`]{#dns-tools-link-down explanation="Dieser Befehl unterbricht die Schnittstelle, statt die Auflösung zu testen."}
::option[`getent ahosts NAME`]{#dns-tools-getent .correct explanation="Der Befehl kann `/etc/hosts`, DNS und andere Name-Service-Switch-Quellen widerspiegeln."}
:::

## Mit dig abfragen

Gib einen Namen und einen Eintragstyp an:

```bash
$ dig www.example.com A
$ dig www.example.com AAAA
$ dig example.com MX
```

Die Ausgabe bezeichnet den antwortenden Server, Status, Flags, Frage, Antwort, Autoritäts- und Zusatzdaten, Abfragezeit sowie Transportmetadaten. `+short` ist für Skripte praktisch, verbirgt aber für die Diagnose benötigte Belege.

:::single-choice{#dns-tools-record-type}
Welche Abfrage fordert IPv6-Adresseinträge an?

::option[`dig NAME AAAA`]{#dns-tools-aaaa .correct explanation="AAAA-Einträge enthalten IPv6-Adressen."}
::option[`dig NAME MX`]{#dns-tools-mx explanation="MX fordert Mail-Exchanger-Einträge an."}
::option[`dig NAME PTR` mit dem Vorwärtsnamen.]{#dns-tools-ptr-forward explanation="PTR wird normalerweise über einen Namen für die Rückwärtsauflösung abgefragt."}
:::

## Einen Server auswählen

Sprich einen Resolver oder autoritativen Server ausdrücklich an:

```bash
$ dig @192.0.2.53 www.example.com A
```

Vergleiche den konfigurierten rekursiven Resolver, einen zweiten genehmigten Resolver und jeden autoritativen Server, um Cache und Autorität voneinander abzugrenzen. Ein Status `NOERROR` kann ohne angeforderte Antwortdaten zurückkommen; `NXDOMAIN` bedeutet, dass der abgefragte Name nicht existiert, während `SERVFAIL` bedeutet, dass der Server die Abfrage nicht abschließen konnte.

:::single-choice{#dns-tools-noerror-empty}
Kann `NOERROR` einen leeren Antwortabschnitt besitzen?

::option[Ja, wenn der Name existiert, aber die Daten des angeforderten Eintragstyps fehlen.]{#dns-tools-noerror-nodata .correct explanation="Status und Anzahl der Antworten müssen gemeinsam ausgewertet werden."}
::option[Nein, der Status garantiert mindestens einen Adresseintrag.]{#dns-tools-noerror-always-answer explanation="Der Name kann existieren, ohne Daten des angeforderten Typs zu besitzen."}
::option[Nein, leere Antworten sind immer Ethernet-Fehler.]{#dns-tools-empty-ethernet explanation="Eine gültige No-Data-Antwort wird durch DNS-Semantik und nicht durch die Frame-Bildung der Verbindung erklärt."}
:::

## Rekursion und Autorität prüfen

`rd` in der Abfrage fordert Rekursion an; `ra` in einer Antwort zeigt an, dass der Server sie anbietet. `aa` bedeutet, dass die Antwort autoritativ ist. Frage einen autoritativen Server mit `+norecurse` ab, damit du einen rekursiven Cache nicht mit bereitgestellten Zonendaten verwechselst.

`dig +trace NAME` führt selbst einen iterativen Durchlauf aus, der bei den Root-Hinweisen beginnt. Das Ergebnis kann sich von einem produktiven Resolver unterscheiden, weil dessen Cache, Weiterleitung, Richtlinie, DNSSEC-Validierung und Netzwerkstandort umgangen werden.

:::single-choice{#dns-tools-aa-flag}
Was bedeutet das Antwort-Flag `aa`?

::option[Die Abfrage hat zwei identische IPv4-Adressen verwendet.]{#dns-tools-two-addresses explanation="Das Flag steht weder mit der Antwortanzahl noch mit der Adressfamilie in Zusammenhang."}
::option[Die Antwort wurde mit Anmeldedaten der Anwendung verschlüsselt.]{#dns-tools-aa-encrypted explanation="DNS-Flags stellen keinen verschlüsselten Transport her."}
::option[Die Antwort ist autoritativ.]{#dns-tools-authoritative-answer .correct explanation="Der antwortende Server beansprucht Autorität für die Antwortdaten."}
:::

## Reverse- und TCP-Abfragen testen

Verwende `-x`, um eine rückwärts gerichtete PTR-Abfrage aufzubauen:

```bash
$ dig -x 192.0.2.25
```

Teste DNS über TCP, wenn du abgeschnittene Antworten, Zonenübertragungen oder Unterschiede in der Firewall untersuchst:

```bash
$ dig +tcp @192.0.2.53 example.com SOA
```

Modernes DNS kann UDP oder TCP auf Port 53 verwenden; beide müssen dort zugelassen sein, wo sie benötigt werden. Eine UDP-Antwort mit gesetztem Truncation-Flag veranlasst konforme Clients, die Abfrage über einen geeigneten Transport zu wiederholen.

:::single-choice{#dns-tools-tcp-test}
Was verändert `dig +tcp`?

::option[Die DNS-Abfrage wird über TCP statt des standardmäßigen ersten UDP-Versuchs gesendet.]{#dns-tools-use-tcp .correct explanation="Damit lassen sich Transportfilterung und Antworten untersuchen, die einen größeren zuverlässigen Datenstrom benötigen."}
::option[Es werden nur TCP-Dienstnameneinträge angefordert.]{#dns-tools-tcp-records explanation="Der gewünschte DNS-Typ wird weiterhin getrennt angegeben."}
::option[Die Resolver-Konfiguration des Servers wird dauerhaft verändert.]{#dns-tools-tcp-persistent explanation="Eine Abfrage bearbeitet keine Servereinstellungen."}
:::

## Zusammenfassung

Du kannst nun ein DNS-Werkzeug passend zur untersuchten Resolver-Ebene auswählen.

1. Verwende `getent` für den konfigurierten Systemresolver-Pfad.
2. Verwende `dig` mit ausdrücklichen Eintragstypen und Servern.
3. Werte Status, Flags, Abschnitte und antwortenden Server gemeinsam aus.
4. Trenne den rekursiven Cache von autoritativen Daten.
5. Teste Reverse-Abfragen und beide erforderlichen DNS-Transporte.
