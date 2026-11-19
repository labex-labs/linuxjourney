---
lesson_id: "network-monitoring-flows"
course_id: "network-monitoring"
lang: "de"
order_index: 2
title: "Netzwerk-Flows"
description: "Lerne, Adressen, Ports, Zeiten und Bytezahlen in einer Flow-Übersicht zu lesen."
meta_title: "Netzwerk-Flows - Netzwerküberwachung"
meta_description: "Lerne, Adressen, Ports, Zeiten und Bytezahlen in einer Flow-Übersicht zu lesen."
meta_keywords: "Netzwerk-Flows, Netzwerküberwachung, Cybersicherheit, Linux Journey"
---

Ein **Flow** fasst Verkehr mit gemeinsamen Merkmalen wie Netzwerkadressen, Ports und Protokoll zusammen. Überwachungssysteme können die Bytes oder Pakete eines Flows zählen, ohne deren vollständigen Inhalt zu speichern.

## Beide Endpunkte ablesen

In dieser simulierten Übersicht erfasst das Überwachungssystem die Richtung von einer Quelle zu einem Ziel. Transportprotokolle wie TCP verwenden Portnummern. Mit ihnen lässt sich auf der Empfängerseite ein lauschender Dienst zuordnen.

```text
start=09:21:00Z protocol=TCP src=192.0.2.10:51600 dst=192.0.2.20:443 bytes=1800
start=09:21:00Z protocol=TCP src=192.0.2.20:443 dst=192.0.2.10:51600 bytes=8200
```

Die erste Zeile beschreibt Verkehr zu Port 443. Die zweite zeigt die Gegenrichtung. Manche Überwachungssysteme fassen beide Richtungen zusammen. Schau nach, welches Format du vor dir hast.

:::single-choice{#network-monitoring-flows-endpoint-direction} Welche Adresse und welcher Port empfangen den in der ersten Zeile erfassten Verkehr?

::option[192.0.2.10:51600.]{#network-monitoring-flows-endpoint-direction-a explanation="Das ist in der ersten Richtung der sendende Endpunkt."}
::option[Beide aufgeführten Endpunkte sind Ziele.]{#network-monitoring-flows-endpoint-direction-c explanation="Jede Zeile in diesem Beispiel erfasst eine Richtung."}
::option[192.0.2.20:443.]{#network-monitoring-flows-endpoint-direction-b .correct explanation="Das Zielfeld zeigt, wohin der Verkehr gesendet wurde."}
:::

## Die Mengen vergleichen

Das Beispiel zeigt mehr Bytes in der Richtung von Port 443 aus. Bei einer Webseite kann eine größere Antwort normal sein. Die Bytezahl allein verrät weder den Seiteninhalt noch das Konto oder den Grund für die Datenmenge.

:::single-choice{#network-monitoring-flows-byte-count} Was beschreiben die 8.200 Bytes in der zweiten Zeile?

::option[Den genauen Wortlaut der Antwort.]{#network-monitoring-flows-byte-count-b explanation="Die Flow-Übersicht erfasst die Datenmenge ohne den Inhalt der Nachricht."}
::option[Die erfasste Datenmenge in dieser Richtung.]{#network-monitoring-flows-byte-count-a .correct explanation="Die Bytezahl fasst die Verkehrsmenge zusammen. Quelle und Ziel geben die Richtung an."}
::option[Die Gewissheit, dass die Seite erfolgreich geladen wurde.]{#network-monitoring-flows-byte-count-c explanation="Die Datenmenge verrät das HTTP-Ergebnis nicht."}
:::

## Zusätzliche Informationen heranziehen

Nutze bekannte Angaben zum Dienst und die Uhrzeit, um relevante Flows zu erkennen. Wenn du wissen willst, was der Webserver zurückgegeben hat, ziehe seine Zugriffsprotokolle für dieselbe Zeit und Verbindung heran, sofern sie verfügbar sind.

:::single-choice{#network-monitoring-flows-next-source} Du möchtest den HTTP-Status der Webanfrage wissen. Welche zusätzliche Quelle hilft dir?

::option[Ein passender Eintrag im Webzugriffsprotokoll.]{#network-monitoring-flows-next-source-c .correct explanation="Ein Zugriffsprotokoll des Servers kann das HTTP-Ergebnis enthalten."}
::option[Die auf Hunderter gerundete Bytezahl des Flows.]{#network-monitoring-flows-next-source-a explanation="Die Rundung ändert die Genauigkeit und liefert keinen Antwortstatus."}
::option[Eine zweite Flow-Übersicht für dieselben Endpunkte.]{#network-monitoring-flows-next-source-b explanation="Eine Flow-Übersicht kann weitere Verkehrsbeobachtungen bestätigen. Sie enthält in der Regel keinen HTTP-Antwortstatus."}
:::

## Zusammenfassung

Du kannst jetzt die wichtigsten Felder einer Flow-Übersicht lesen.

1. Finde Adressen und Ports der Endpunkte.
2. Lies die Bytezahl für die erfasste Richtung.
3. Nutze bei Bedarf eine andere Quelle für das Ergebnis der Anwendung.
