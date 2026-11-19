---
lesson_id: "incident-recovery"
course_id: "incident-response"
lang: "de"
order_index: 5
title: "Wiederherstellung"
description: "Lerne, den genehmigten Zustand eines Dienstes zu prüfen, bevor du die Wiederherstellung abschließt."
meta_title: "Wiederherstellung - Reaktion auf Sicherheitsvorfälle"
meta_description: "Lerne, den genehmigten Zustand eines Dienstes zu prüfen, bevor du die Wiederherstellung abschließt."
meta_keywords: "Wiederherstellung, Vorfallreaktion, Cybersicherheit, Linux Journey"
---

Bei der **Wiederherstellung** stellst du den erwarteten Dienstbetrieb wieder her und prüfst, ob der Dienst nutzbar bleibt. Ein neu gestarteter Prozess ist ein erster Anhaltspunkt. Das Team braucht auch Belege dafür, dass Konfiguration, Abhängigkeiten und Verhalten aus Nutzersicht dem vorgesehenen Zustand entsprechen.

## Den wiederhergestellten Zustand ermitteln

Halte fest, welche Version und Konfiguration für die Wiederherstellung genehmigt sind. Wenn ein Dienst isoliert wurde, prüfe, welche Zugänge gesperrt bleiben sollen. Das Wiederöffnen eines Zugriffswegs kann die Grenze der Eindämmung verändern.

:::single-choice{#incident-recovery-restore-target} Welches Ergebnis zeigt, ob du die vorgesehene Version wiederhergestellt hast?

::option[Ein neuer Zeitstempel auf einer anderen virtuellen Maschine.]{#incident-recovery-restore-target-b explanation="Daran erkennst du den wiederhergestellten Dienst nicht."}
::option[Nur eine Liste verfügbarer Pakete.]{#incident-recovery-restore-target-c explanation="Aus verfügbaren Paketen geht nicht hervor, welches Programm gerade Anfragen verarbeitet."}
::option[Eine Antwort oder ein Bereitstellungseintrag, der die genehmigte Version am Ziel ausweist.]{#incident-recovery-restore-target-a .correct explanation="Damit verknüpfst du den laufenden Dienst mit der vom Team ausgewählten Version."}
:::

## Das gemeldete Problem erneut prüfen

Im simulierten Vorfall sahen Besucher auf der öffentlichen Startseite den Status `503`. Rufe nach der Wiederherstellung denselben Pfad von einem geeigneten Teststandort aus auf. Prüfe, ob die erwartete erfolgreiche Antwort kommt, und beobachte aktuelle Anfragefehler. Eine funktionierende interne Vorschau prüft den öffentlichen Pfad nicht.

:::single-choice{#incident-recovery-verify-original-path} Welcher Test zeigt am besten, dass der ursprüngliche Fehler aus Nutzersicht verschwunden ist?

::option[Prüfe nur, ob die Programmdatei des Dienstes existiert.]{#incident-recovery-verify-original-path-a explanation="Die Datei kann vorhanden sein, ohne öffentliche Anfragen zu verarbeiten."}
::option[Prüfe die öffentliche Startseite über den Zugriffsweg der betroffenen Clients.]{#incident-recovery-verify-original-path-b .correct explanation="Damit wiederholst du die Prüfung, die ursprünglich fehlschlug."}
::option[Prüfe nur die interne Vorschau.]{#incident-recovery-verify-original-path-c explanation="Dieser Pfad unterscheidet sich vom betroffenen Pfad."}
:::

## Den Dienst weiter beobachten

Vereinbare einen kurzen Beobachtungszeitraum und Kriterien für den Erfolg. Prüfe relevante Signale wie Fehler, Latenz und abgelehnte Zugriffe. Halte Einschränkungen, offene Maßnahmen und den nächsten Prüftermin fest. Bewahre die Belege zur Wiederherstellung zusammen mit den Aufzeichnungen zum Vorfall auf.

:::single-choice{#incident-recovery-observation-period} Die erste Prüfung ist erfolgreich, aber der Fehler trat nur zeitweise auf. Was sollte vor Abschluss der Wiederherstellungsprüfung geschehen?

::option[Beobachte die vereinbarten Signale während des vorgesehenen Zeitfensters weiter.]{#incident-recovery-observation-period-c .correct explanation="So sammelst du Belege dafür, dass der Dienst stabil bleibt."}
::option[Schließe die Prüfung sofort ab, weil eine Antwort eingetroffen ist.]{#incident-recovery-observation-period-a explanation="Eine einzelne Beobachtung kann einen sporadischen Fehler übersehen."}
::option[Verwirf alle Vergleichsdaten.]{#incident-recovery-observation-period-b explanation="Die früheren Ergebnisse zeigen, was sich verbessert hat."}
:::

## Zusammenfassung

Du kannst nach der Wiederherstellung den Zustand des Dienstes und sein Verhalten aus Nutzersicht prüfen.

1. Bestimme die genehmigte Version und Konfiguration.
2. Prüfe erneut das Fehlerbild, das die Nutzer beobachtet haben.
3. Beobachte die vereinbarten Signale, bevor du die Wiederherstellungsprüfung abschließt.
