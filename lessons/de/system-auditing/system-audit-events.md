---
lesson_id: "system-audit-events"
course_id: "system-auditing"
lang: "de"
order_index: 1
title: "Audit-Ereignisse"
description: "Lerne, protokollierbare Ereignisse passend zu einer Frage über eine geschützte Datei auszuwählen."
meta_title: "Audit-Ereignisse - Systemaudit"
meta_description: "Lerne, protokollierbare Ereignisse passend zu einer Frage über eine geschützte Datei auszuwählen."
meta_keywords: "Audit-Ereignisse, Systemaudit, Cybersicherheit, Linux Journey"
---

Ein Dienstprotokoll kann melden, dass eine Seite geladen wurde. Ein **Auditdatensatz** kann eine Aktion beschreiben, für deren Erfassung dein System eingerichtet wurde, etwa das Schreiben einer Dienstkonfiguration. Lege zuerst fest, welche Aktion wichtig ist und welche Angaben du für die Prüfung brauchst.

## Eine Audit-Frage formulieren

Angenommen, die Konfiguration des Webdienstes regelt, wer eine Vorschau öffnen darf. Du möchtest Änderungen an dieser Datei prüfen. Ein aussagekräftiger Datensatz würde Zielobjekt, Vorgang, Uhrzeit, Kontodaten und Ergebnis nennen. Jedes Feld trägt dazu bei, einen Teil der Aktion nachzuvollziehen.

:::single-choice{#system-audit-events-choose-object} Welche Angabe sollte ein Auditdatensatz für diese Prüfung enthalten?

::option[Nur die Zahl der Webanfragen an diesem Tag.]{#system-audit-events-choose-object-b explanation="Das Anfragevolumen beschreibt eine andere Aktivität."}
::option[Die Konfigurationsdatei, auf die der Vorgang gerichtet war.]{#system-audit-events-choose-object-a .correct explanation="Am Zielobjekt erkennst du, welche Änderung diese Datei betrifft und welche Schreibzugriffe andere Ziele hatten."}
::option[Nur die Art des Vorgangs, etwa einen Schreibzugriff.]{#system-audit-events-choose-object-c explanation="Der Vorgang zeigt, was versucht wurde. An der Zieldatei erkennst du, ob der Versuch für die Prüfung wichtig war."}
:::

## Das Ergebnis lesen

Ein Datensatz kann einen erfolgreichen Schreibzugriff oder einen fehlgeschlagenen Versuch beschreiben. Achte sowohl auf den Vorgang als auch auf sein Ergebnis. Ein abgelehnter Schreibzugriff kann einen Versuch belegen. Ein erfolgreicher Schreibzugriff erlaubt andere Schlüsse.

:::single-choice{#system-audit-events-operation-result} Ein Datensatz nennt einen Schreibzugriff auf die Konfiguration und als Ergebnis eine Ablehnung. Was geht daraus hervor?

::option[Der aufgezeichnete Schreibversuch wurde abgelehnt.]{#system-audit-events-operation-result-b .correct explanation="Vorgang und Ergebnis beschreiben zusammen die beobachtete Aktion."}
::option[Die Datei wurde definitiv ersetzt.]{#system-audit-events-operation-result-a explanation="Eine Ablehnung belegt keine erfolgreiche Änderung."}
::option[Die erwartete Seite hat HTTP 200 zurückgegeben.]{#system-audit-events-operation-result-c explanation="Hier wird kein Seitenaufruf beschrieben."}
:::

## Den Umfang der Aufzeichnung prüfen

Das Auditsystem erfasst nur Ereignisse, die es mit seinen Mechanismen und Regeln beobachten kann. Bevor du dich auf eine Suche ohne Treffer stützt, prüfe, ob die Regeln für den richtigen Pfad, die richtigen Vorgänge und den fraglichen Zeitraum galten. Notiere, welche Quelle du geprüft hast.

:::single-choice{#system-audit-events-empty-audit} Du findest im ausgewählten Protokoll keinen Schreibzugriff. Welche Prüfung hilft, bevor du daraus schließt, dass es keine Schreibzugriffe gab?

::option[Zähle die installierten Editoren.]{#system-audit-events-empty-audit-a explanation="Aus der installierten Software geht nicht hervor, was das Auditsystem erfasst."}
::option[Suche im selben Zeitraum ausschließlich unter einem zweiten Kontonamen.]{#system-audit-events-empty-audit-b explanation="Eine zusätzliche Suche kann helfen, wenn die Erfassung nachweislich funktioniert. Prüfe zuerst, ob die fraglichen Ereignisse überhaupt hätten aufgezeichnet werden können."}
::option[Prüfe die Audit-Regeln und den Zeitraum, für den Aufzeichnungen vorliegen.]{#system-audit-events-empty-audit-c .correct explanation="Bei Lücken in der Erfassung kann ein passender Eintrag fehlen, obwohl eine Aktion stattgefunden hat."}
:::

## Zusammenfassung

Du kannst jetzt passende Auditdaten für die Prüfung einer geschützten Ressource auswählen.

1. Bestimme den Vorgang und das Objekt, die du prüfen willst.
2. Lies das aufgezeichnete Ergebnis zusammen mit dem angeforderten Vorgang.
3. Prüfe den Umfang der Aufzeichnung, bevor du eine erfolglose Suche als Beleg verwendest.
