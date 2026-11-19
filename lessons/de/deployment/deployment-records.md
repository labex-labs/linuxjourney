---
lesson_id: "deployment-records"
course_id: "deployment"
lang: "de"
order_index: 6
title: "Bereitstellungsprotokolle"
description: "Lerne, aus einem kurzen Release-Verlauf eine Bereitstellung und das anschließende Rollback nachzuvollziehen."
meta_title: "Bereitstellungsprotokolle - Bereitstellung"
meta_description: "Lerne, aus einem kurzen Release-Verlauf eine Bereitstellung und das anschließende Rollback nachzuvollziehen."
meta_keywords: "Bereitstellungsprotokolle, Release-Verlauf, Rollback, DevOps, Linux Journey"
---

Ein Bereitstellungsprotokoll hilft anderen, ein für Nutzer sichtbares Ergebnis mit einer Änderung zu verbinden. Notiere zuerst den Zeitpunkt, die Umgebung, die Quellrevision und das Artefakt. Ergänze das Prüfergebnis und die Maßnahmen, die danach ergriffen wurden.

## Festhalten, was geändert wurde

Dieses Übungsprotokoll verfolgt eine einzelne Bereitstellung. Die Kennungen sind zur besseren Lesbarkeit gekürzt.

```text
UTC    Target   Commit   Artifact  Observation
09:00  staging  8a61e1   digest-C  version 3, home returned 200
09:12  prod     8a61e1   digest-C  version 3, home returned 503
09:18  prod     72b110   digest-B  version 2, home returned 200
```

HTTP 200 steht für eine erfolgreiche Antwort. HTTP 503 meldet, dass der Dienst für diese Anfrage nicht verfügbar war. Halte in einem echten Protokoll auch fest, wie und an welcher Adresse du geprüft hast.

:::single-choice{#deployment-records-first-prod-change} Welche Zeile zeigt das erste beobachtete Verhalten von digest-C in Produktion?

::option[Die Zeile 09:12 prod.]{#deployment-records-first-prod-change-b .correct explanation="Dort stehen das in Produktion bereitgestellte Artefakt und die fehlgeschlagene Prüfung."}
::option[Die Zeile 09:00 staging.]{#deployment-records-first-prod-change-a explanation="Diese Prüfung fand in einer anderen Umgebung statt."}
::option[Die Zeile 09:18 prod.]{#deployment-records-first-prod-change-c explanation="Diese Zeile protokolliert nach dem Rollback ein anderes Artefakt."}
:::

![Simulierter Release-Verlauf mit erfolgreichem Staging-Test, HTTP 503 in Produktion und Rollback auf Version 2](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/deployment/deployment-records/release-timeline.png)

## Das Rollback erklären

Die letzte Zeile zeigt die Rückkehr zu digest-B. Die Versionsprüfung und das Ergebnis der Anfrage an die Startseite beschreiben den Zustand nach dem Rollback. Für die genaue Ursache des früheren Fehlers reichen diese Befunde nicht aus. Halte Vermutungen getrennt fest, bis du sie mit weiteren Beobachtungen stützen kannst.

:::single-choice{#deployment-records-rollback-evidence} Was kannst du über das Ergebnis um 09:18 Uhr sagen?

::option[Um 09:12 Uhr fehlte eine Datenbank.]{#deployment-records-rollback-evidence-b explanation="Dieser Eintrag enthält keinen Befund zu Abhängigkeiten."}
::option[Ab diesem Zeitpunkt waren alle Anfragen erfolgreich.]{#deployment-records-rollback-evidence-c explanation="Die erfolgreiche Prüfung belegt nur das Ergebnis dieser einen Anfrage."}
::option[In Produktion lief wieder Version 2, und die Anfrage an die Startseite war erfolgreich.]{#deployment-records-rollback-evidence-a .correct explanation="Die Zeile enthält die wiederhergestellte Version und die beobachtete HTTP-Antwort."}
:::

## Das Protokoll übergeben

Die nächste Person, die das Protokoll prüft, sollte die Beobachtung nachvollziehen können. Gib die Prüfmethode, den Zeitpunkt mit Zeitzone und, falls verfügbar, einen Link zum Build an. Wenn die Ursache noch unklar ist, halte fest, was als Nächstes untersucht werden sollte.

:::single-choice{#deployment-records-handoff-detail} Welche Angabe hilft, die Prüfung der Startseite zu wiederholen?

::option[Nur die Kennung des früheren Releases.]{#deployment-records-handoff-detail-a explanation="Die frühere Version hilft beim Vergleich. Aus ihrer Kennung geht nicht hervor, wo und wann die Prüfung lief."}
::option[Die genaue Zieladresse und der Zeitpunkt der Prüfung.]{#deployment-records-handoff-detail-c .correct explanation="Damit kann jemand denselben Pfad prüfen und andere Signale im relevanten Zeitraum vergleichen."}
::option[Der Zeitpunkt, an dem der Quell-Commit erstellt wurde.]{#deployment-records-handoff-detail-b explanation="Dieser Zeitpunkt bezeichnet ein früheres Ereignis. Für die Überprüfung sind Zeitpunkt und Ziel der Anfrage nötig."}
:::

## Aufzeichnen, welches Image tatsächlich lief

Ein Tag in einer Bereitstellungsnotiz kann nach dem Release neu zugeordnet werden. Wenn der Dienst bereits Version 2 meldet, halte zusätzlich zu dieser lesbaren Bezeichnung auch das tatsächlich laufende Artefakt fest. Beide Angaben helfen beim späteren Vergleich, selbst wenn der Tag in der Registry inzwischen verschoben wurde.

:::single-choice{#deployment-records-final-application} In der Release-Notiz steht site:2. Welche zusätzliche Angabe macht einen späteren Vergleich zuverlässiger?

::option[Der Digest des letzten Abrufs von site:2.]{#deployment-records-final-application-c explanation="Ein späterer Abruf kann einen anderen Inhalt liefern als den, den der laufende Dienst verwendet."}
::option[Der vollständige Digest des Images, das tatsächlich lief.]{#deployment-records-final-application-a .correct explanation="Damit lässt sich der verwendete Inhalt auch dann identifizieren, wenn der lesbare Tag später auf etwas anderes verweist."}
::option[Derselbe Tag in einem zweiten Feld.]{#deployment-records-final-application-b explanation="Die Wiederholung macht den Tag nicht eindeutiger."}
:::

## Zusammenfassung

Du kannst jetzt einen Release-Verlauf lesen und an andere weitergeben.

1. Ermittle Umgebung, Revision und Artefakt aus dem Protokoll.
2. Beschreibe das Rollback anhand der beobachteten Ergebnisse.
3. Halte alle Angaben fest, die für die nächste Prüfung nötig sind.
