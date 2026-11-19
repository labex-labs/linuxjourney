---
lesson_id: "network-monitoring-alerts"
course_id: "network-monitoring"
lang: "de"
order_index: 6
title: "Netzwerkwarnungen"
description: "Lerne, aus einer Netzwerkwarnung abzuleiten, welche Belege du für die nächste Schutzmaßnahme brauchst."
meta_title: "Netzwerkwarnungen - Netzwerküberwachung"
meta_description: "Lerne, aus einer Netzwerkwarnung abzuleiten, welche Belege du für die nächste Schutzmaßnahme brauchst."
meta_keywords: "Netzwerkwarnungen, Netzwerküberwachung, Cybersicherheit, Linux Journey"
---

Eine Netzwerkwarnung zeigt, dass eine Überwachungsbedingung erfüllt war. Lies die Bedingung und prüfe ihre Datenquelle, bevor du entscheidest, was passiert ist. Warnungen können auf unerwarteten Verkehr, wiederholte Fehler oder fehlende Messdaten hinweisen.

## Den Umfang der Warnung lesen

Die folgende simulierte Warnung beruht auf DNS-Einträgen. Sie zählt Fehler pro Client innerhalb von fünf Minuten.

```text
Window: 09:20–09:25 UTC
Client: 192.0.2.10
Condition: at least 10 failed name lookups
Observed: 12 failures
```

Das gibt Anlass, die Abfragen und ihre Ergebnisse zu prüfen. Aus der Warnung geht nicht hervor, welches Programm sie gesendet hat.

:::single-choice{#network-monitoring-alerts-alert-scope} Was hat die Warnung unmittelbar erfasst?

::option[Zwölf fehlgeschlagene Namensabfragen für den angegebenen Client in diesem Zeitfenster.]{#network-monitoring-alerts-alert-scope-b .correct explanation="Das sind die Anzahl und der Umfang, die die Warnung angibt."}
::option[Einen bestätigten Datenverlust.]{#network-monitoring-alerts-alert-scope-a explanation="Die Regel zählt fehlgeschlagene Namensabfragen."}
::option[Zwölf verschiedene Clients.]{#network-monitoring-alerts-alert-scope-c explanation="Die Warnung fasst Einträge für eine einzelne Clientadresse zusammen."}
:::

## Passende Aufzeichnungen auf dem Host suchen

Angenommen, die meisten Fehler betrafen `preview.example`. Ein Dienstprotokoll auf dem Client könnte zeigen, dass eine veraltete Einstellung zu wiederholten Versuchen führte. Suche ungefähr zur selben Zeit nach Einträgen des Programms, von dem du solche Abfragen erwartest. Prüfe die Host-Kennung der Überwachung, bevor du die Aktivität zuordnest.

:::single-choice{#network-monitoring-alerts-evidence-choice} Welcher Eintrag würde dir helfen zu prüfen, ob ein Dienst die Abfrage wiederholt hat?

::option[Ein späterer Aufruf der öffentlichen Seite auf einem anderen Host.]{#network-monitoring-alerts-evidence-choice-b explanation="Endpunkt und Uhrzeit stimmen nicht mit dem untersuchten Muster überein."}
::option[Eine Liste installierter Anwendungen ohne Angaben zu ihrer Aktivität.]{#network-monitoring-alerts-evidence-choice-c explanation="Aus der installierten Software allein geht nicht hervor, wer die Abfrage gesendet hat."}
::option[Ein passendes Dienstprotokoll, das die fehlgeschlagene Abfrage im Zeitfenster der Warnung nennt.]{#network-monitoring-alerts-evidence-choice-a .correct explanation="Das kann das Abfragemuster mit dem Programm in Verbindung bringen."}
:::

## Die nächste Entscheidung festhalten

Wenn das Dienstprotokoll dazu passt, halte die Ursache fest. Prüfe nach der Korrektur der genehmigten Konfiguration eine typische Namensabfrage. Bleiben die Belege unvollständig, halte fest, was fehlt. Bewahre die Warnung, den zugehörigen Eintrag und das Prüfergebnis gemeinsam auf.

:::single-choice{#network-monitoring-alerts-uncertainty} Du hast die DNS-Warnung, aber keine passenden Host-Aufzeichnungen. Was solltest du melden?

::option[Das genaue Programm wurde ermittelt.]{#network-monitoring-alerts-uncertainty-a explanation="Aus den DNS-Daten allein ging der Prozess nicht hervor."}
::option[Das Abfragemuster ist bestätigt und das verantwortliche Programm ist unbekannt.]{#network-monitoring-alerts-uncertainty-c .correct explanation="Das hält sowohl die Beobachtung als auch die offene Frage fest."}
::option[Die Warnung enthält überhaupt keine verwertbaren Angaben.]{#network-monitoring-alerts-uncertainty-b explanation="Sie beschreibt weiterhin die Bedingung, die der Resolver beobachtet hat."}
:::

## Ein erwartetes Wiederholungsmuster prüfen

Angenommen, ein Team hat einen Auftrag geplant, der einen Test-Hostnamen wiederholt auflöst. Vergleiche den geplanten Zeitpunkt, die Namen in den DNS-Einträgen und das eigene Protokoll des Auftrags. Stimmen mehrere dieser Angaben überein, stützt das die Erklärung. Halte Fehler, die sich dem Auftrag nicht zuordnen lassen, für weitere Prüfungen fest.

:::single-choice{#network-monitoring-alerts-final-application} Welcher Befund würde am stärksten dafür sprechen, dass der geplante Auftrag die Warnung ausgelöst hat?

::option[Die Warnung betrifft einen Host, auf dem weitere geplante Aufträge laufen.]{#network-monitoring-alerts-final-application-c explanation="Der Host allein verrät nicht, welches Programm die Abfragen gesendet hat."}
::option[Das Auftragsprotokoll nennt denselben Hostnamen und erneute Abfragen im Zeitfenster der Warnung.]{#network-monitoring-alerts-final-application-a .correct explanation="Wenn Name und Zeitpunkt passen, lässt sich das Muster mit dem bekannten Auftrag in Verbindung bringen."}
::option[Der Auftrag war irgendwann für diesen Tag eingeplant.]{#network-monitoring-alerts-final-application-b explanation="Damit sind weder das Zeitfenster der Warnung noch die abgefragten Namen überprüft."}
:::

## Zusammenfassung

Du kannst jetzt aus einer Netzwerkwarnung eine gezielte Folgeprüfung ableiten.

1. Bestimme die Erkennungsregel und ihren Geltungsbereich.
2. Wähle eine passende Aufzeichnung, um eine Erklärung zu prüfen.
3. Dokumentiere die Beobachtung und die verbleibende Unsicherheit.
