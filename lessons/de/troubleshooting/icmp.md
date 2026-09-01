---
lesson_id: "icmp"
course_id: "troubleshooting"
lang: "de"
order_index: 1
title: "ICMP"
description: "Lerne, wie ICMP IP-Fehler meldet, Diagnosen unterstützt und wesentliches IPv4- sowie IPv6-Verhalten ermöglicht."
meta_title: "ICMP – Fehlersuche"
meta_description: "Diese Linux-Anleitung erklärt das ICMP-Protokoll. Verstehe ICMP-Nachrichtentypen und -Codes für eine wirksame Netzwerkfehlersuche."
meta_keywords: "ICMP, ICMP-Protokoll, Netzwerkfehlersuche, ICMP-Typen, Linux-Vernetzung, Linux lernen, Linux-Tutorial, Einsteiger, Anleitung"
---

Das Internet Control Message Protocol transportiert zusammen mit IP Steuerungs-, Fehler- und Diagnoseinformationen. ICMP für IPv4 und ICMPv6 sind verwandte, aber getrennte Protokolle mit unterschiedlichen Nachrichtentypnummern und Aufgaben.

## Typen, Codes und Prüfsummen

Eine ICMP-Nachricht besitzt einen Typ, gegebenenfalls einen spezifischeren Code und eine Prüfsumme. Fehlermeldungen enthalten normalerweise einen Teil des auslösenden Pakets, damit der Sender den Fehler einem Datenstrom zuordnen kann.

:::single-choice{#icmp-code-purpose} Was stellt ein ICMP-Code bereit?

::option[Einen dauerhaften DNS-Namen für den meldenden Router.]{#icmp-code-dns explanation="Namensauflösung ist nicht als Zweck dieses Felds codiert."}
::option[Eine spezifischere Bedeutung innerhalb eines ICMP-Nachrichtentyps.]{#icmp-code-specific .correct explanation="Codes für Destination Unreachable unterscheiden beispielsweise mehrere Fehlerursachen."}
::option[Die vollständige Nutzlast jedes vorherigen Pakets.]{#icmp-code-all-payload explanation="Ein Fehler zitiert gemäß den Protokollregeln nur genug vom auslösenden Paket zur Identifizierung."}
:::

## Echo- und Fehlermeldungen

Bei ICMPv4 ist Echo Request Typ 8 und Echo Reply Typ 0. Destination Unreachable ist Typ 3 und Time Exceeded Typ 11. ICMPv6 verwendet andere Typnummern. Ermittle deshalb vor der Interpretation einer Aufzeichnung immer die Adressfamilie.

:::single-choice{#icmpv4-echo-request-type} Welchen Typ besitzt ICMPv4 Echo Request?

::option[0]{#icmp-type-zero explanation="Typ null ist ICMPv4 Echo Reply."}
::option[11]{#icmp-type-eleven explanation="Typ elf ist ICMPv4 Time Exceeded."}
::option[8]{#icmp-type-eight .correct explanation="Ping sendet gewöhnlich diese ICMPv4-Nachricht, um eine Echo-Antwort anzufordern."}
:::

## Path MTU und wesentliches ICMP

ICMP ist nicht bloß optionaler Ping-Datenverkehr. IPv4-Fehler zur erforderlichen Fragmentierung und ICMPv6-Packet-Too-Big-Nachrichten unterstützen Path MTU Discovery. ICMPv6 transportiert außerdem Neighbor Discovery und Router Advertisements. Das Blockieren sämtlichen ICMP-Verkehrs kann daher Blackholes erzeugen und den IPv6-Betrieb beeinträchtigen.

Filtere nach erforderlichem Typ, Richtung, Rate und Geltungsbereich, statt pauschale Annahmen anzuwenden. Angreifer können manche ICMP-Nachrichten fälschen; validiere deshalb den Kontext des zitierten Pakets und gleiche ihn mit lokalen Routen und Aufzeichnungen ab.

:::single-choice{#icmp-block-all-risk} Warum kann das Blockieren sämtlichen ICMP-Verkehrs gültigen Datenverkehr beeinträchtigen?

::option[Jede HTTP-Antwort wird innerhalb einer ICMP-Echo-Antwort transportiert.]{#icmp-http-echo explanation="HTTP verwendet normalerweise TCP oder QUIC und nicht ICMP Echo."}
::option[ICMP speichert alle Anwendungspasswörter.]{#icmp-passwords explanation="Es ist keine Anmeldedatendatenbank."}
::option[ICMP transportiert erforderliche Path-MTU- und IPv6-Steuerinformationen.]{#icmp-essential-control .correct explanation="Das Unterdrücken dieser Nachrichten kann korrekte Paketgrößen oder Nachbar- und Routererkennung verhindern."}
:::

## Schweigen interpretieren

Keine ICMP-Antwort kann Filterung, Ratenbegrenzung, asymmetrisches Routing, eine fehlende Rückroute, einen ausgeschalteten Host oder ein Gerät bedeuten, das auf diese Nachricht schlicht nicht antwortet. Umgekehrt kann ein ICMP-Fehler von einem Zwischengerät statt vom endgültigen Ziel erzeugt werden.

:::single-choice{#icmp-silence-meaning} Was beweist das Ausbleiben einer Echo Reply für sich allein?

::option[Die Zielanwendung ist sicher gestoppt.]{#icmp-silence-app-down explanation="Der Dienst kann funktionieren, während Echo-Datenverkehr gefiltert oder ignoriert wird."}
::option[Der Zielhostname wurde aus DNS gelöscht.]{#icmp-silence-dns-deleted explanation="Eine Prüfung einer numerischen Adresse kann unabhängig von DNS ohne Antwort bleiben."}
::option[Nur, dass dieser Echo-Austausch keine beobachtete Antwort ergab.]{#icmp-silence-limited .correct explanation="Zur Ermittlung der Ursache sind weitere Routen-, Transport-, Anwendungs- und Aufzeichnungsbelege erforderlich."}
:::

## Zusammenfassung

Du kannst ICMP nun als Steuerungsbeleg und nicht als binäres Konnektivitätsurteil interpretieren.

1. Lies Typ und Code in der richtigen IP-Familie.
2. Erkenne die Aufgaben von Echo, Unreachable und Time Exceeded.
3. Bewahre ICMP, das für Path MTU und IPv6-Betrieb nötig ist.
4. Verknüpfe Fehler und Schweigen mit weiteren Pfadbelegen.
