---
lesson_id: "traceroute"
course_id: "troubleshooting"
lang: "de"
order_index: 3
title: "traceroute"
description: "Lerne, wie traceroute antwortende Hops ermittelt und wie du Lücken, Zeitmessungen und Pfadänderungen interpretierst."
meta_title: "traceroute – Fehlersuche"
meta_description: "Lerne mit dem Linux-Befehl traceroute Netzwerkrouten zu verfolgen und Konnektivitätsprobleme zu untersuchen. Diese Anleitung erklärt die Pfaderkennung mit TTL."
meta_keywords: "traceroute, traceroute Linux, Linux-Vernetzung, Netzwerkfehlersuche, TTL, Paketrouting, Linux-Befehle, Einsteiger, Tutorial"
---

`traceroute` sendet Prüfungen mit steigenden IPv4-TTL- oder IPv6-Hop-Limit-Werten. Router, bei denen der Wert abläuft, können Time-Exceeded-Nachrichten zurückgeben und dadurch manche antwortenden Punkte entlang des Hinwegs sichtbar machen.

## Funktionsweise der Hop-Erkennung

Prüfungen beginnen mit einem Hop-Limit von eins, das schrittweise erhöht wird. Der erste Router verringert eins auf null und kann einen ICMP-Fehler zurückgeben. Ein Limit von zwei erreicht vor dem Ablauf den zweiten Router, und der Vorgang läuft weiter, bis das Ziel antwortet oder der Höchstwert erreicht ist.

:::single-choice{#traceroute-expiring-field}
Welches Feld lässt aufeinanderfolgende Prüfungen an späteren Routern ablaufen?

::option[Die DNS-Cache-TTL des Zielnamens.]{#traceroute-dns-ttl explanation="Die Laufzeit eines DNS-Datensatzes steuert keine Paketweiterleitungs-Hops."}
::option[Die Ethernet-Quell-MAC-Adresse.]{#traceroute-source-mac explanation="Verbindungsadressen enthalten keinen Ende-zu-Ende-Hop-Zähler."}
::option[IPv4-TTL oder IPv6-Hop-Limit.]{#traceroute-hop-field .correct explanation="Die Erhöhung dieses begrenzten Weiterleitungszählers macht antwortende geroutete Hops sichtbar."}
:::

## Prüfmethoden

Herkömmliches Linux-traceroute sendet gewöhnlich UDP-Prüfungen an hohe Zielports. Das Ziel kann den Abschluss durch ICMP Port Unreachable melden. Optionen können stattdessen ICMP-Echo- oder TCP-SYN-Prüfungen verwenden, die Filter unterschiedlich durchqueren können:

```bash
$ traceroute -n example.com
$ traceroute -I -n example.com
$ traceroute -T -p 443 -n example.com
```

Berechtigungen und unterstützte Optionen unterscheiden sich. Verwende für das Ziel autorisierte Methoden und erfasse die Methode beim Vergleich von Ergebnissen.

:::single-choice{#traceroute-default-destination-response}
Was beendet gewöhnlich ein herkömmliches Linux-UDP-traceroute?

::option[Eine ICMP-Port-Unreachable-Antwort des Ziels.]{#traceroute-port-unreachable .correct explanation="Hohe UDP-Ports sind normalerweise unbenutzt, sodass sich das Ziel durch diesen Fehler erkennen lässt."}
::option[Eine vorgeschriebene HTTP-200-Antwort von jedem Router.]{#traceroute-http-every-router explanation="Router geben Netzwerksteuerungsfehler und keine HTTP-Antworten zurück."}
::option[Ein Ethernet-Broadcast des Ziels über das Internet.]{#traceroute-ethernet-broadcast explanation="Broadcasts der Verbindungsschicht durchqueren keine gerouteten Pfade."}
:::

## Sternchen interpretieren

Ein Sternchen bedeutet, dass vor dem Zeitlimit keine Antwort für diese Prüfung beobachtet wurde. Der Router kann Transitverkehr weiterleiten und zugleich Diagnoseantworten filtern oder ratenbegrenzen. Wenn spätere Hops antworten, hat der stille Hop eindeutig zumindest manche Prüfungen weitergeleitet.

:::single-choice{#traceroute-asterisk-meaning}
Was beweist `*` an einem Hop?

::option[Der Router verwirft dauerhaft alle Transitpakete.]{#traceroute-star-all-drop explanation="Spätere Antworten können die fortgesetzte Weiterleitung belegen."}
::option[Nur, dass vor dem Prüfzeitlimit keine passende Antwort eintraf.]{#traceroute-star-no-response .correct explanation="Filterung, Ratenbegrenzung, Verlust und Rückwegprobleme können sämtlich Schweigen verursachen."}
::option[Das Ziel besitzt keine IP-Adresse.]{#traceroute-star-no-address explanation="Die Prüfung zielt bereits auf eine Adresse, und ein stiller Hop entfernt sie nicht."}
:::

## Zeitmessung und Pfadänderungen

Die Zeiten pro Hop messen Umlaufzeiten zu Steuerantworten und nicht die vom Link zwischen benachbarten ausgegebenen Zeilen hinzugefügte Latenz. Router können Antworten der Steuerungsebene nachrangig behandeln. Lastverteilung kann Prüfungen über unterschiedliche Pfade senden, und Namensauflösung kann die Anzeige verzögern; `-n` vermeidet Rückwärtsauflösungen.

Der Rückweg jeder ICMP-Antwort kann vom Hinweg abweichen. Wiederhole Tests und setze sie zu Anwendungszeitmessungen an den Endpunkten in Beziehung, bevor du einen Engpass benennst.

:::single-choice{#traceroute-hop-rtt-limit}
Warum sollten RTT-Werte benachbarter Hops nicht als genaue Verbindungslatenz voneinander abgezogen werden?

::option[Traceroute meldet alle Zeiten in Byte statt Millisekunden.]{#traceroute-times-bytes explanation="Die angezeigten Prüfzeiten werden normalerweise in Millisekunden angegeben."}
::option[Antworten können unterschiedliche Rückwege und Verarbeitung der Steuerungsebene verwenden.]{#traceroute-rtt-asymmetry .correct explanation="Die Messungen sind getrennte Ende-zu-Hop-Umlaufzeiten und keine synchronisierten Einwegstichproben einer Verbindung."}
::option[Jeder Router besitzt dieselbe Uhr wie die Quelle.]{#traceroute-router-clock explanation="Die Messung beruht nicht auf synchronisierten entfernten Uhren."}
:::

## Mit der Anwendung vergleichen

Ein traceroute kann das Ziel erreichen, während der Dienst blockiert ist, und der Dienst kann funktionieren, während Zwischenrouter ihre Antworten verbergen. Teste dieselbe Adressfamilie, dasselbe Ziel, Transportprotokoll und denselben Port wie die Anwendung und verwende traceroute anschließend als unterstützenden Pfadbeleg.

:::single-choice{#traceroute-service-proof}
Beweist ein abgeschlossenes traceroute, dass ein HTTPS-Dienst fehlerfrei ist?

::option[Ja, weil jeder Hop das Serverzertifikat validiert.]{#traceroute-validates-cert explanation="Router führen nicht die TLS-Validierung des Clients aus."}
::option[Nein; Transport-, TLS- und HTTP-Verhalten benötigen eigene Tests.]{#traceroute-not-app-proof .correct explanation="Pfaderkennung und Anwendungszustand sind unterschiedliche Diagnoseschichten."}
::option[Ja, aber nur, wenn Rückwärts-DNS-Namen ausgegeben werden.]{#traceroute-rdns-proof explanation="Namen belegen keine Anwendungsfunktion."}
:::

## Zusammenfassung

Du kannst traceroute nun als Folge von Prüfungen mit begrenzter Hop-Anzahl interpretieren und nicht als vollständiges Pfadorakel.

1. Erkläre die Hop-Erkennung durch Ablauf von TTL oder Hop Limit.
2. Erfasse, ob UDP-, ICMP- oder TCP-Prüfungen verwendet wurden.
3. Behandle Sternchen als fehlende Antworten und nicht als bewiesene Ausfälle.
4. Leite aus RTTs benachbarter Hops keine genaue Verbindungslatenz ab.
5. Verknüpfe Pfadbelege mit der tatsächlichen Anwendung.
