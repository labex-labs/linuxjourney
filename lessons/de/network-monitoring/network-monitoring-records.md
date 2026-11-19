---
lesson_id: "network-monitoring-records"
course_id: "network-monitoring"
lang: "de"
order_index: 1
title: "Netzwerkaufzeichnungen"
description: "Lerne, für eine konkrete Frage zur Netzwerküberwachung eine passende Aufzeichnung auszuwählen."
meta_title: "Netzwerkaufzeichnungen - Netzwerküberwachung"
meta_description: "Lerne, für eine konkrete Frage zur Netzwerküberwachung eine passende Aufzeichnung auszuwählen."
meta_keywords: "Netzwerkaufzeichnungen, Netzwerküberwachung, Cybersicherheit, Linux Journey"
---

Eine Netzwerkbeobachtung beschreibt, was ein Werkzeug von einem bestimmten Punkt aus sehen konnte. Überlege zuerst, was du herausfinden möchtest. Verschiedene Quellen machen unterschiedliche Teile derselben Aktivität sichtbar.

## Eine Aufzeichnungsart wählen

Ein **Flow-Eintrag** fasst die Kommunikation zwischen Netzwerkendpunkten zusammen. Ein **DNS-Protokoll** erfasst Namensabfragen, die ein Resolver beobachtet hat. Ein **Paketmitschnitt** speichert Kopien einzelner Pakete, die am Erfassungspunkt sichtbar waren. Ein Endpunkt ist eine Seite der Kommunikation. Meist wird er durch Adresse und Port bezeichnet.

:::single-choice{#network-monitoring-records-choose-dns} Du willst wissen, was ein Resolver für site.example zurückgegeben hat. Welche Quelle eignet sich am besten?

::option[Die Zahl laufender Arbeitsprozesse des Webdienstes.]{#network-monitoring-records-choose-dns-b explanation="Die Anzahl der Arbeitsprozesse hat mit der Abfrage nichts zu tun."}
::option[Ein DNS-Protokoll dieses Resolvers.]{#network-monitoring-records-choose-dns-a .correct explanation="Der Resolver kann die bearbeitete Abfrage und die Antwort aufzeichnen."}
::option[Eine Flow-Übersicht, die nur die Verkehrsmenge zeigt.]{#network-monitoring-records-choose-dns-c explanation="In einer Flow-Übersicht können DNS-Abfrage und Antwort fehlen."}
:::

## Den Beobachtungspunkt bestimmen

Ein Paketmitschnitt auf einem Laptop enthält Pakete, die an der gewählten Schnittstelle sichtbar waren. Ein Serverprotokoll enthält, was den Server erreicht hat und was der Server erfasst hat. Eine Nutzeranfrage kann zum Beispiel scheitern, bevor sie den Server erreicht. Wähle eine Quelle, deren Beobachtungspunkt zu deiner Frage passt.

:::single-choice{#network-monitoring-records-capture-scope} Im Mitschnitt eines anderen Rechners findest du keine Anfrage. Was solltest du vor einer Schlussfolgerung prüfen?

::option[Ob die Schnittstelle den relevanten Zugriffsweg im betreffenden Zeitraum erfassen konnte.]{#network-monitoring-records-capture-scope-b .correct explanation="Ein fehlendes Paket kann daran liegen, was dieser Beobachtungspunkt erfassen konnte."}
::option[Ob der Mitschnitt einige andere Pakete enthält.]{#network-monitoring-records-capture-scope-a explanation="Andere Pakete zeigen, dass etwas aufgezeichnet wurde. Ob auch der fragliche Zugriffsweg zur fraglichen Zeit sichtbar war, bleibt offen."}
::option[Ob ein anderer Host zur selben Zeit Pakete aufgezeichnet hat.]{#network-monitoring-records-capture-scope-c explanation="Der gleichzeitige Mitschnitt eines anderen Hosts belegt nicht, was diese Schnittstelle sehen konnte."}
:::

## Die Stichprobe klein halten

Paketmitschnitte können Inhalte enthalten, die andere nicht weitergeben wollten. Verwende zum Üben einen vorbereiteten Mitschnitt mit unbedenklichem Übungsverkehr. Wenn du einen kleinen Auszug weitergibst, nenne den betrachteten Zeitraum und den Filter, damit andere die Grenzen des Auszugs verstehen.

:::single-choice{#network-monitoring-records-choosing-evidence} Mit welchem Beispiel lernst du am besten, eine DNS-Antwort zu erkennen?

::option[Mit einem langen Mitschnitt von anderem Netzwerkverkehr der Mitarbeitenden.]{#network-monitoring-records-choosing-evidence-a explanation="Das fügt unnötige Daten hinzu und kann private Informationen offenlegen."}
::option[Mit einer Übersicht ohne Felder zur Namensabfrage.]{#network-monitoring-records-choosing-evidence-b explanation="Dann fehlen die Angaben, die man für die Übung lesen soll."}
::option[Mit einem kleinen vorbereiteten Mitschnitt mit der Übungsabfrage und der zugehörigen Antwort.]{#network-monitoring-records-choosing-evidence-c .correct explanation="Er enthält genau den Austausch, den du für die Frage brauchst."}
:::

## Zusammenfassung

Du kannst jetzt eine Netzwerkaufzeichnung auswählen und erklären, was sie erfassen konnte.

1. Unterscheide Flow-Übersichten, DNS-Protokolle und Paketmitschnitte.
2. Gleiche den Beobachtungspunkt mit dem Netzwerkpfad ab.
3. Verwende für die Prüfung einen kleinen, passenden Ausschnitt.
