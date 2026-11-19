---
lesson_id: "incident-containment"
course_id: "incident-response"
lang: "de"
order_index: 4
title: "Eindämmung"
description: "Lerne, genehmigte Maßnahmen zur Eindämmung nach ihrem Zweck, ihren Auswirkungen und den benötigten Belegen zu vergleichen."
meta_title: "Eindämmung - Reaktion auf Sicherheitsvorfälle"
meta_description: "Lerne, genehmigte Maßnahmen zur Eindämmung nach ihrem Zweck, ihren Auswirkungen und den benötigten Belegen zu vergleichen."
meta_keywords: "Eindämmung, Vorfallreaktion, Cybersicherheit, Linux Journey"
---

Die **Eindämmung** soll weiteren Schaden begrenzen, während das Team den Vorfall untersucht. Welche kurzfristige Maßnahme passt, hängt davon ab, was betroffen ist und welche Zugänge weiterhin gebraucht werden.

## Die Grenze festlegen

Stell dir vor, eine interne Vorschauoberfläche ist über einen öffentlichen Pfad erreichbar. Die Startseite soll weiterhin öffentlich bleiben. Eine Möglichkeit ist, den Zugang zur Vorschau einzuschränken. Eine weitergehende Möglichkeit ist, die gesamte Website vom Netz zu nehmen. Vergleiche, welche Zugänge sich in beiden Fällen ändern würden.

:::single-choice{#incident-containment-narrow-action} Welche Maßnahme sperrt den öffentlichen Vorschauzugang und hält die Startseite erreichbar?

::option[Schalte alle öffentlichen Pfade unabhängig von ihrer Funktion ab.]{#incident-containment-narrow-action-b explanation="Damit wäre auch die Startseite nicht mehr erreichbar."}
::option[Schränke den betroffenen Vorschaupfad ein und prüfe beide Pfade.]{#incident-containment-narrow-action-a .correct explanation="Damit begrenzt du den gemeldeten Zugriff und stellst sicher, dass der benötigte Dienst erreichbar bleibt."}
::option[Ändere den Namen des Vorschaudienstes.]{#incident-containment-narrow-action-c explanation="Der Name verhindert nicht, dass Anfragen den Dienst erreichen."}
:::

## Belege und Zugriff einplanen

Ziehe den Plan zur Vorfallreaktion und die Personen heran, die die Änderung freigeben dürfen. Halte fest, wer sie genehmigt hat, wie lange sie gelten soll und welche Belege du zuerst sichern solltest, sofern die Umstände das erlauben. Prüfe, ob die Maßnahme die Dienstprotokollierung oder den Zugang des Einsatzteams unterbrechen könnte.

:::single-choice{#incident-containment-action-impact} Die geplante Isolierung könnte auch das Untersuchungsteam daran hindern, Aufzeichnungen abzurufen. Was sollte das Team prüfen?

::option[Welche Belege zu sichern sind und wie die berechtigten Personen ihren Zugang behalten.]{#incident-containment-action-impact-b .correct explanation="Damit berücksichtigst du das Ziel der Eindämmung und die laufende Untersuchung."}
::option[Nur ob die Konfigurationsdatei einen kurzen Namen hat.]{#incident-containment-action-impact-a explanation="Der Name sichert weder Aufzeichnungen noch den Zugang."}
::option[Ob Zugangsdaten veröffentlicht werden sollen, damit sich alle wieder verbinden können.]{#incident-containment-action-impact-c explanation="Zugangsdaten sollten geschützt bleiben und der Zugriff sollte weiterhin kontrolliert werden."}
:::

## Die Eindämmung überprüfen

Prüfe, ob der unerwünschte Zugriffsweg gesperrt ist. Teste einen vorgesehenen Zugriffsweg gesondert, um Nebenwirkungen zu erkennen. Halte fest, wann du die Änderung vorgenommen hast und wann das Team sie erneut bewerten soll. Die Eindämmung kann gelingen, während die Ursache noch ungeklärt ist.

:::single-choice{#incident-containment-containment-success} Der öffentliche Vorschaupfad ist gesperrt und die Startseite funktioniert weiterhin. Welche Aussage stützen diese Prüfungen?

::option[Die Ursache wurde definitiv behoben.]{#incident-containment-containment-success-a explanation="Die Prüfungen bestätigen die Zugriffsgrenze. Ob die Ursache behoben ist, bleibt offen."}
::option[Alle möglichen Zugriffswege zur Vorschau wurden getestet.]{#incident-containment-containment-success-b explanation="Die Prüfungen decken die tatsächlich verwendeten Zugriffswege ab."}
::option[Der getestete öffentliche Vorschaupfad ist gesperrt und die benötigte Startseite bleibt erreichbar.]{#incident-containment-containment-success-c .correct explanation="Die Aussage beschreibt das Ergebnis im Rahmen der durchgeführten Prüfungen."}
:::

## Zusammenfassung

Du kannst jetzt eine kurzfristige Eindämmungsmaßnahme beurteilen.

1. Nenne den Pfad oder Zugang, den die Maßnahme einschränken soll.
2. Prüfe Freigabe, zu sichernde Belege und erwartete Auswirkungen.
3. Prüfe die vorgesehene Einschränkung und den benötigten Dienst einzeln.
