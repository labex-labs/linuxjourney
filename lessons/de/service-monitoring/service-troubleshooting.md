---
lesson_id: "service-troubleshooting"
course_id: "service-monitoring"
lang: "de"
order_index: 7
title: "Fehlersuche bei Diensten"
description: "Lerne, bei gestoppten Diensten, Fehlern in Abhängigkeiten und langsamen Anfragen die passende nächste Prüfung zu wählen."
meta_title: "Fehlersuche bei Diensten - Dienstüberwachung"
meta_description: "Lerne, bei gestoppten Diensten, Fehlern in Abhängigkeiten und langsamen Anfragen die passende nächste Prüfung zu wählen."
meta_keywords: "Fehlersuche, Dienstüberwachung, DevOps, Linux Journey"
---

Beginne mit einem konkreten Fehlerbild, etwa einem fehlgeschlagenen Aufruf der Startseite. Vergleiche dann Beobachtungen aus ungefähr derselben Zeit und von dem Standort aus, von dem die Nutzer zugreifen.

## Wenn ein Server stoppt

Im ersten Fall meldet der Browser eine abgelehnte Verbindung. Beim Container des Dienstes steht `Exited (1)`. Beide Beobachtungen geben Anlass zu prüfen, warum das Programm gestoppt wurde. Lies seine gespeicherten Protokolle und achte beim Vergleich mit anderen Ereignissen auf die Uhrzeit, zu der es beendet wurde.

:::single-choice{#service-troubleshooting-stopped-case} Welche Prüfung erklärt am ehesten, warum der Prozess gestoppt wurde?

::option[Rufe dieselbe Startseite noch einmal auf, um einen aktuelleren Status zu erhalten.]{#service-troubleshooting-stopped-case-a explanation="Ein erneuter Aufruf prüft das Fehlerbild. Die vorhandenen Protokolle können erklären, warum sich das Programm beendet hat."}
::option[Lies die letzten verfügbaren Zeilen des Containerprotokolls.]{#service-troubleshooting-stopped-case-b .correct explanation="Meldungen zum Start oder Ende können zeigen, an welcher Stelle das Programm stoppte."}
::option[Prüfe die Protokolle eines anderen laufenden Containers mit demselben Image.]{#service-troubleshooting-stopped-case-c explanation="Dieser Container hat einen eigenen Verlauf. Der Fehler ist dort möglicherweise nie aufgetreten."}
:::

## Wenn eine Abhängigkeit ausfällt

Im zweiten Fall läuft der Webprozess, aber die Seite liefert einen Serverfehler. Das Protokoll meldet für Anfrage `r17` eine Zeitüberschreitung beim Zugriff auf den Katalogdienst. Prüfe deshalb dessen Einträge zur selben Anfrage. Dass der erste Dienst erreichbar ist, sagt noch nichts über die übrigen Dienste aus.

:::single-choice{#service-troubleshooting-dependency-case} Welchen Anhaltspunkt solltest du für r17 als Nächstes suchen?

::option[Den Eintrag des Katalogdienstes zu dieser Anfrage und Uhrzeit.]{#service-troubleshooting-dependency-case-a .correct explanation="Der Eintrag zeigt, was beim Aufruf der Abhängigkeit passiert ist."}
::option[Die Größe des archivierten Docker-Images.]{#service-troubleshooting-dependency-case-b explanation="Sie beschreibt den laufenden Aufruf nicht."}
::option[Eine unabhängige, erfolgreiche Prüfung der Startseite vom Vortag.]{#service-troubleshooting-dependency-case-c explanation="Sie bezieht sich auf eine andere Zeit und kann diese Anfrage nicht erklären."}
:::

## Wenn Anfragen langsamer werden

In einem dritten Beispiel sind die meisten Antworten erfolgreich, aber Nutzer melden Verzögerungen. Im selben Zeitfenster steigen die Latenz und die Zahl wartender Aufträge. Prüfe zunächst die Nachfrage und die Aktivität der Arbeitsprozesse. Wiederhole nach einer Änderung die Prüfung aus Nutzersicht und sieh dir dieselben Signale erneut an.

:::single-choice{#service-troubleshooting-slow-case} Welcher Vergleich prüft am besten, ob eine Änderung hier geholfen hat?

::option[Screenshots des Quellcode-Repositorys vor und nach der Änderung.]{#service-troubleshooting-slow-case-a explanation="Darauf sind weder Anfragedauer noch Warteschlangen zu sehen."}
::option[Die Cache-Größe im Verhältnis zur Anzahl bereitgestellter Branches.]{#service-troubleshooting-slow-case-b explanation="Beide Werte geben keinen Aufschluss über die gemeldete Wartezeit."}
::option[Vergleichbare Anfragezeiten aus Nutzersicht und Warteschlangen vor und nach der Änderung.]{#service-troubleshooting-slow-case-c .correct explanation="Damit prüfst du das ursprüngliche Problem und den vermuteten Engpass."}
:::

## Widersprüchliche Prüfergebnisse einordnen

Angenommen, eine lokale Testanfrage funktioniert, aber Nutzer sehen weiterhin Fehler. Halte fest, welchen Zugriffsweg jede Prüfung verwendet hat. Eine lokale Prüfung kann zeigen, dass ein Prozess auf dem Host antwortet. Eine Clientanfrage kann gleichzeitig ein Problem auf dem Weg zu diesem Host aufdecken.

:::single-choice{#service-troubleshooting-final-application} Welches Ergebnis hilft bei der weiteren Untersuchung für betroffene Nutzer am meisten?

::option[Eine Prüfung über denselben Zugriffsweg und vom selben Standort wie die Nutzer.]{#service-troubleshooting-final-application-a .correct explanation="Sie beobachtet den Abschnitt des Dienstes, auf dem die Nutzer das Problem gemeldet haben."}
::option[Nur das Ergebnis auf dem Host.]{#service-troubleshooting-final-application-b explanation="Das hilft bei der Eingrenzung, lässt aber den Zugriffsweg von außen ungeprüft."}
::option[Die aktuelle Kapazität der Image-Registry.]{#service-troubleshooting-final-application-c explanation="Die Registry kann Images bereitstellen, während auf dem Zugriffsweg der Nutzer ein eigenes Problem vorliegt."}
:::

## Zusammenfassung

Du kannst jetzt anhand der vorhandenen Anhaltspunkte den nächsten Prüfschritt wählen.

1. Untersuche einen gestoppten Dienst anhand des Prozessstatus und der Protokolle.
2. Verfolge eine fehlgeschlagene Anfrage bis zu ihrer Abhängigkeit.
3. Prüfe eine Verbesserung anhand des ursprünglich aus Nutzersicht beobachteten Problems.
