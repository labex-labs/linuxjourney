---
lesson_id: "web-access-logs"
course_id: "web-security"
lang: "de"
order_index: 7
title: "Webzugriffsprotokolle"
description: "Lerne, anhand von HTTP-Zugriffsprotokollen herauszufinden, was ein Dienst zurückgegeben hat, ohne Zugangsdaten offenzulegen."
meta_title: "Webzugriffsprotokolle - Websicherheit"
meta_description: "Lerne, anhand von HTTP-Zugriffsprotokollen herauszufinden, was ein Dienst zurückgegeben hat, ohne Zugangsdaten offenzulegen."
meta_keywords: "Webzugriffsprotokolle, Websicherheit, Cybersicherheit, Linux Journey"
---

Ein Webserver kann für jede Anfrage einen Eintrag im **Zugriffsprotokoll** speichern. Ein Eintrag kann Uhrzeit, Pfad, Antwortcode und Anfrage-ID enthalten. Verwende nur die Felder, die du für deine Frage brauchst.

## Das Ergebnis einer Anfrage lesen

Dieser simulierte Auszug verwendet benannte Felder. Die beiden Anfragen gingen an verschiedene Pfade.

```text
t=09:18:01Z request=r31 method=GET path=/health status=200
t=09:18:04Z request=r32 method=GET path=/staff status=403
```

Ein Statuscode `403` zeigt, dass der Dienst die Anfrage abgelehnt hat. Prüfe den genauen Pfad und die Anfrage-ID, bevor du die Antwort mit einem anderen Eintrag vergleichst.

:::single-choice{#web-access-logs-log-result} Welcher Anfrage solltest du nachgehen, um die Ablehnung zu untersuchen?

::option[r31 an /health.]{#web-access-logs-log-result-a explanation="Diese Zeile meldet einen erfolgreichen Healthcheck."}
::option[r32 an /staff.]{#web-access-logs-log-result-b .correct explanation="Diese Zeile hat den Status 403 und zeigt damit die Ablehnung im Auszug."}
::option[Beiden, als wären sie dieselbe Anfrage.]{#web-access-logs-log-result-c explanation="Anfrage-IDs und Pfade unterscheiden die beiden Einträge."}
:::

## Nach der Zugriffsentscheidung suchen

Das Zugriffsprotokoll hält fest, was der Server zurückgegeben hat. Warum der Zugriff erlaubt oder abgelehnt wurde, steht dort möglicherweise nicht. Falls die Anwendung auch Autorisierungsentscheidungen protokolliert, gleiche Anfrage-ID und Uhrzeit ab. So kannst du im Beispiel herausfinden, welche Regel angewendet wurde.

:::single-choice{#web-access-logs-refusal-reason} Im Zugriffsprotokoll steht 403. Welcher zusätzliche Eintrag würde den Grund am besten erklären?

::option[Die Zugriffsentscheidung der Anwendung für r32.]{#web-access-logs-refusal-reason-a .correct explanation="Der passende Eintrag kann zeigen, welche Regel angewendet wurde."}
::option[Eine erfolgreiche Antwort von einer anderen Website.]{#web-access-logs-refusal-reason-b explanation="Sie hat keinen Bezug zu dieser Ablehnung."}
::option[Eine frühere Anfrage an den Pfad für Healthchecks.]{#web-access-logs-refusal-reason-c explanation="Sie beschreibt einen anderen Vorgang und ein anderes Ergebnis."}
:::

## Zugangsdaten aus Protokollen heraushalten

Vermeide es, Werte zu protokollieren, mit denen jemand eine fremde Sitzung nutzen könnte, etwa ein vollständiges Sitzungscookie oder ein Autorisierungstoken. Für die Fehlersuche reichen oft Anfrage-ID und Antwortstatus. Entferne vor der Weitergabe eines Protokollauszugs sensible Felder und behalte nur Angaben, die du für die Untersuchung brauchst.

:::single-choice{#web-access-logs-safe-fields} Welche beiden Angaben helfen, der abgelehnten Anfrage nachzugehen, ohne Zugangsdaten zu kopieren?

::option[Das vollständige Sitzungscookie und das Kontopasswort.]{#web-access-logs-safe-fields-a explanation="Beide Werte sind sensibel und gehören nicht in weitergegebene Protokolle."}
::option[Das Autorisierungstoken und ein öffentlicher Pfad.]{#web-access-logs-safe-fields-b explanation="Der Pfad kann hilfreich sein, das Token ist jedoch ein vertraulicher Zugangsnachweis."}
::option[Die Anfrage-ID und der Antwortstatus.]{#web-access-logs-safe-fields-c .correct explanation="Damit kannst du passende Einträge abgleichen, ohne Sitzungsdaten offenzulegen."}
:::

## Einen kleinen Auszug weitergeben

Stell dir vor, jemand braucht für die Prüfung einer abgelehnten Anfrage mehr Kontext. Wenn Uhrzeit, ID, Methode, bereinigter Pfad und Status genügen, behalte diese Felder bei. Bei manchen Pfaden enthalten die Abfrageparameter vertrauliche Werte. Prüfe den Auszug vor der Weitergabe.

:::single-choice{#web-access-logs-final-application} Welcher Auszug eignet sich für diese Prüfung am besten?

::option[Standardmäßig die gesamte Anfrage mit allen Headern.]{#web-access-logs-final-application-b explanation="Anfragen können Zugangsdaten oder unnötige personenbezogene Daten enthalten."}
::option[Nur der Statuscode, ohne jede Kennung.]{#web-access-logs-final-application-c explanation="Allein anhand des Codes kann es schwierig sein, den passenden Eintrag zur Zugriffsentscheidung zu finden."}
::option[Ein bereinigter Pfad mit Uhrzeit, Anfrage-ID und Antwortstatus.]{#web-access-logs-final-application-a .correct explanation="Der Auszug enthält die nötigen Angaben zum Abgleich, ohne Sitzungsdaten offenzulegen."}
:::

## Zusammenfassung

Du kannst jetzt ein einfaches Zugriffsprotokoll lesen und die für die Prüfung wichtigen Angaben sicher festhalten.

1. Ordne Anfrage-ID, Pfad und Antwort einander zu.
2. Suche den zugehörigen Eintrag zur Zugriffsentscheidung, wenn du den Grund brauchst.
3. Halte Zugangsdaten aus aufgezeichneten und weitergegebenen Protokollen heraus.
