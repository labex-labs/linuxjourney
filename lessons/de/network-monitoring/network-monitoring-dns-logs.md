---
lesson_id: "network-monitoring-dns-logs"
course_id: "network-monitoring"
lang: "de"
order_index: 3
title: "DNS-Protokolle"
description: "Lerne, eine DNS-Abfrage, ihre Antwort und eine spätere Anwendungsverbindung zu unterscheiden."
meta_title: "DNS-Protokolle - Netzwerküberwachung"
meta_description: "Lerne, eine DNS-Abfrage, ihre Antwort und eine spätere Anwendungsverbindung zu unterscheiden."
meta_keywords: "DNS-Protokolle, Netzwerküberwachung, Cybersicherheit, Linux Journey"
---

Bevor ein Client über einen Namen eine Verbindung zu einem Dienst herstellt, kann er bei DNS nach der Adresse fragen. Ein Resolver kann die Abfrage und ihr Ergebnis aufzeichnen. Ein **Resolver** löst Namen für Clients auf.

## Die Abfrage bestimmen

Ein Eintrag im DNS-Protokoll kann die Uhrzeit, die Clientadresse, den Namen und den angefragten DNS-Datensatztyp enthalten. Eine `A`-Abfrage fragt nach einer IPv4-Adresse.

```text
09:21:00Z client=192.0.2.10 query=site.example type=A result=NOERROR answer=192.0.2.20
09:21:03Z client=192.0.2.10 query=preview.example type=A result=NXDOMAIN
```

Das erste Ergebnis enthält eine Adresse für `site.example`. Das zweite meldet, dass der Name `preview.example` bei dieser Abfrage aus Sicht des Resolvers nicht existiert.

:::single-choice{#network-monitoring-dns-logs-lookup-name} Welche Zeile lieferte eine IPv4-Adresse zum abgefragten Namen?

::option[Die Abfrage für site.example.]{#network-monitoring-dns-logs-lookup-name-a .correct explanation="Die Zeile enthält eine Antwort mit einer IPv4-Adresse."}
::option[Die Abfrage für preview.example.]{#network-monitoring-dns-logs-lookup-name-b explanation="NXDOMAIN meldet, dass der abgefragte Name aus Sicht des Resolvers nicht existiert."}
::option[Beide Zeilen, weil sie zum selben Client gehören.]{#network-monitoring-dns-logs-lookup-name-c explanation="Der Client ist derselbe, aber die Abfragen lieferten verschiedene Ergebnisse."}
:::

## Das Ergebnis lesen

`NOERROR` bedeutet, dass der DNS-Austausch keinen Protokollfehler gemeldet hat. Prüfe auch das Antwortfeld. Eine Antwort kann `NOERROR` lauten und keinen Adresseintrag des angefragten Typs enthalten. Eine fehlgeschlagene Abfrage kann sich auch anders zeigen, etwa durch eine vom Client protokollierte Zeitüberschreitung.

:::single-choice{#network-monitoring-dns-logs-no-answer} Eine DNS-Zeile meldet NOERROR, enthält aber keine Adresse in der Antwort. Was solltest du berichten?

::option[Der Client hat zwangsläufig eine IPv4-Adresse erhalten.]{#network-monitoring-dns-logs-no-answer-a explanation="Das Antwortfeld enthält die für die Abfrage zurückgegebenen Adressen."}
::option[Die Website hat die Verbindung des Browsers eindeutig abgelehnt.]{#network-monitoring-dns-logs-no-answer-c explanation="Die Zeile erfasst das Ergebnis einer DNS-Abfrage. Über Browseranfragen gibt sie keine Auskunft."}
::option[Der Austausch lieferte keinen Protokollfehler und diese Zeile nennt keine Adresse.]{#network-monitoring-dns-logs-no-answer-b .correct explanation="Das Ergebnisfeld und das Antwortfeld liefern unterschiedliche Informationen."}
:::

## Die Verbindung eigens prüfen

Ein Client kann erst einen Namen auflösen und dann eine Verbindung herstellen. Suche nach einem passenden Flow- oder Verbindungseintrag, um zu prüfen, ob das geschehen ist. Vergleiche Endpunkt und Uhrzeit. DNS-Ergebnisse können zwischengespeichert sein. Daher fehlt bei manchen Verbindungen eine neue Abfrage im verfügbaren Protokoll.

:::single-choice{#network-monitoring-dns-logs-dns-vs-flow} Was würde am besten zeigen, dass sich der Client später mit der zurückgegebenen Adresse verbunden hat?

::option[Eine weitere Ansicht derselben DNS-Antwort.]{#network-monitoring-dns-logs-dns-vs-flow-a explanation="Die Antwort nennt eine Adresse, die der Client verwenden kann."}
::option[Ein passender Verbindungs- oder Flow-Eintrag, der das Ziel nennt.]{#network-monitoring-dns-logs-dns-vs-flow-c .correct explanation="Damit verfolgst du den Verkehr nach der Namensabfrage."}
::option[Eine zweite DNS-Abfrage vom selben Client.]{#network-monitoring-dns-logs-dns-vs-flow-b explanation="Eine weitere Abfrage bestätigt eine wiederholte Namensauflösung. Ob danach eine Anwendungsverbindung zustande kam, bleibt offen."}
:::

## Zusammenfassung

Du kannst jetzt DNS-Protokolle lesen und sie von späterem Netzwerkverkehr unterscheiden.

1. Finde den Client, die Abfrage und den angefragten Datensatztyp.
2. Lies Ergebnis und Antwort gemeinsam.
3. Suche nach einem eigenen Eintrag für eine spätere Verbindung.
