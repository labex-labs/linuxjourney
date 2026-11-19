---
lesson_id: "deployment-rollbacks"
course_id: "deployment"
lang: "de"
order_index: 5
title: "Rollbacks"
description: "Lerne, eine nachweislich funktionierende Version auszuwählen und zu prüfen, ob ein Rollback der Anwendung ausreicht."
meta_title: "Rollbacks - Bereitstellung"
meta_description: "Lerne, eine nachweislich funktionierende Version auszuwählen und zu prüfen, ob ein Rollback der Anwendung ausreicht."
meta_keywords: "Rollback, Datenkompatibilität, Bereitstellung, DevOps, Linux Journey"
---

Ein **Rollback** setzt einen Dienst auf ein früheres Release zurück, das nachweislich funktioniert hat. Nutze den Bereitstellungsverlauf, um dieses Release auszuwählen. Prüfe vor dem Zurücksetzen, ob das Release auch gemeinsam genutzte Daten oder Einstellungen geändert hat.

## Ein früheres Release auswählen

In diesem Beispiel folgt auf ein neues Release eine fehlgeschlagene Anfrage. Version 2 war die letzte geprüfte Version. Die Bezeichnungen unten stehen stellvertretend für die vollständigen Image-Digests eines echten Eintrags.

```text
08:50  version 2  digest-B  homepage and version check passed
09:10  version 3  digest-C  homepage check failed
```

Version 2 kommt für das Rollback infrage, wenn sie mit der aktuellen Umgebung noch funktioniert. Nutze die aufgezeichnete Artefaktreferenz, um sie zu finden.

:::single-choice{#deployment-rollbacks-previous-version} Welches Image solltest du zuerst als Ziel für das Rollback prüfen?

::option[Das neueste Image im Cache des Hosts.]{#deployment-rollbacks-previous-version-a explanation="Die Cache-Reihenfolge zeigt nicht, welches Release funktionsfähig war."}
::option[Digest-C, weil diese Bereitstellung am kürzesten zurückliegt.]{#deployment-rollbacks-previous-version-c explanation="Der Eintrag ordnet dieses Artefakt der fehlgeschlagenen Prüfung zu."}
::option[Digest-B, weil es die relevanten Prüfungen zuvor bestanden hat.]{#deployment-rollbacks-previous-version-b .correct explanation="Laut Eintrag gehört es zur letzten verifizierten Version."}
:::

## Die Datenkompatibilität prüfen

Ein Anwendungsrelease kann auch eine Datenbank oder andere gemeinsam genutzte Ressourcen ändern. Wenn du ein älteres Image startest, bleibt dieser externe Zustand bestehen. Prüfe, ob die ältere Anwendung die aktuellen Daten lesen kann. Falls Daten wiederhergestellt werden müssen, verwende den Wiederherstellungsplan des Teams und berücksichtige Änderungen seit dem letzten Backup.

:::single-choice{#deployment-rollbacks-external-state} Version 3 hat das Datenbankformat geändert. Was musst du prüfen, bevor du Version 2 mit dieser Datenbank startest?

::option[Ob Version 2 die frühere Prüfung der Startseite bestanden hat.]{#deployment-rollbacks-external-state-b explanation="Die frühere Prüfung macht Version 2 zu einem möglichen Ziel. Über das aktuelle Datenbankformat sagt sie nichts aus."}
::option[Ob Version 2 das aktuelle Format unterstützt.]{#deployment-rollbacks-external-state-a .correct explanation="Beim Wechsel des Anwendungs-Images werden gemeinsam genutzte Daten nicht zurückgesetzt."}
::option[Ob der Name der Datenbank in den Release-Hinweisen steht.]{#deployment-rollbacks-external-state-c explanation="Entscheidend ist, ob der ältere Code mit den aktuellen Daten arbeiten kann."}
:::

## Das Ergebnis überprüfen

Prüfe nach dem Rollback die laufende Version. Wiederhole denselben Test aus Nutzersicht, der fehlgeschlagen ist, und prüfe wichtige Abhängigkeiten erneut. Halte Zeitpunkt, wiederhergestellte Version und Ergebnisse fest, damit sich der ursprüngliche Ausfall von der Wiederherstellung unterscheiden lässt.

:::single-choice{#deployment-rollbacks-rollback-proof} Der Rollback-Befehl ist abgeschlossen. Welches Ergebnispaar zeigt, dass sich der Dienst erholt hat?

::option[Der Endpunkt meldet Version 2, und der zuvor fehlgeschlagene Test besteht jetzt.]{#deployment-rollbacks-rollback-proof-c .correct explanation="Damit sind die Zielversion und das betroffene Verhalten überprüft."}
::option[Zwei Image-Downloads waren erfolgreich.]{#deployment-rollbacks-rollback-proof-a explanation="Downloads stellen Dateien bereit. Den laufenden Dienst prüfen sie nicht."}
::option[Ein älterer Screenshot von Version 2 liegt vor.]{#deployment-rollbacks-rollback-proof-b explanation="Der Screenshot zeigt einen früheren Zustand."}
:::

## Zusammenfassung

Du kannst jetzt anhand von Prüfergebnissen ein Rollback planen.

1. Wähle ein Release, das nachweislich funktioniert hat.
2. Prüfe die Kompatibilität mit gemeinsam genutzten Daten und Einstellungen.
3. Prüfe die wiederhergestellte Version und die betroffene Funktion aus Nutzersicht.
