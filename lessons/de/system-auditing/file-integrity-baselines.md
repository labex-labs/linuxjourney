---
lesson_id: "file-integrity-baselines"
course_id: "system-auditing"
lang: "de"
order_index: 4
title: "Referenzstände für die Integritätsprüfung"
description: "Lerne, einen Integritätsbericht zu lesen und zu entscheiden, wann ein neuer Referenzstand genehmigt werden kann."
meta_title: "Referenzstände für die Integritätsprüfung - Systemaudit"
meta_description: "Lerne, einen Integritätsbericht zu lesen und zu entscheiden, wann ein neuer Referenzstand genehmigt werden kann."
meta_keywords: "Referenzstand, Dateiintegrität, Systemaudit, Cybersicherheit, Linux Journey"
---

Ein **Referenzstand** ist eine vertrauenswürdige Aufzeichnung der erwarteten Dateieigenschaften zu einem bekannten Zeitpunkt. Eine spätere Integritätsprüfung kann die aktuellen Dateien damit vergleichen und Abweichungen melden.

## Einen Abweichungsbericht lesen

Dieser simulierte Auszug vergleicht einen Host mit seinem zuletzt genehmigten Stand.

```text
File                      Property  Previous  Current
/etc/journey/site.conf    content   hash-A    hash-B
/etc/journey/banner.txt   mode      644       640
/etc/journey/site.prev    present   yes       no
```

In der ersten Zeile hat sich der Dateiinhalt geändert. Die zweite zeigt geänderte Zugriffsrechte. Die dritte meldet, dass eine zuvor erfasste Datei bei der Prüfung fehlte.

:::single-choice{#file-integrity-baselines-report-mode} Welche Zeile meldet geänderte Zugriffsrechte?

::option[Die Zeile zu site.conf.]{#file-integrity-baselines-report-mode-a explanation="Sie meldet einen geänderten Hashwert des Inhalts."}
::option[Die Zeile zu banner.txt.]{#file-integrity-baselines-report-mode-b .correct explanation="Die Zugriffsrechte änderten sich von 644 auf 640."}
::option[Die Zeile zu site.prev.]{#file-integrity-baselines-report-mode-c explanation="Diese Zeile hält fest, ob der Pfad vorhanden war."}
:::

![Simulierter Integritätsbericht zum Vergleich von Dateiinhalt, Zugriffsrechten und Vorhandensein](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/system-auditing/file-integrity-baselines/reference-comparison.png)

## Die Referenz prüfen

Der Bericht ist nur aussagekräftig, wenn der frühere Referenzstand vertrauenswürdig ist. Bewahre seine Kennung und sein Erstellungsdatum auf. Wurde eine frühere Datei erfasst, als bereits etwas nicht stimmte, kann der Vergleich irreführend sein. Frage, welchen genehmigten Stand die Referenz abbildet.

:::single-choice{#file-integrity-baselines-reference-source} Welcher Referenzstand ist für die Prüfung der heutigen Konfiguration am hilfreichsten?

::option[Eine dokumentierte, genehmigte Kopie aus der Zeit vor der Änderung.]{#file-integrity-baselines-reference-source-a .correct explanation="Sie bietet einen bekannten Vergleichsstand, den die prüfende Person nachvollziehen kann."}
::option[Ein Referenzstand auf Grundlage der heutigen, ungeklärten Dateien.]{#file-integrity-baselines-reference-source-b explanation="Er würde die Abweichungen schon vor der Prüfung zum Vergleichsstandard machen."}
::option[Die Einstellungen eines anderen Hosts ohne Angaben zur Vergleichbarkeit.]{#file-integrity-baselines-reference-source-c explanation="Je nach Aufgabe eines Hosts können andere Dateien und Rechte vorgesehen sein."}
:::

## Vor der Aktualisierung prüfen

Gleiche jede Abweichung mit einer genehmigten Änderung ab und prüfe, wie sich der Dienst verhält. Wenn die Änderung der Bannerrechte geplant war, die Konfigurationsänderung aber ungeklärt ist, prüfe sie einzeln. Aktualisiere den Referenzstand, sobald die Abweichungen geklärt und genehmigt sind. Bewahre den früheren Referenzstand auf.

:::single-choice{#file-integrity-baselines-update-timing} Die Änderung der Bannerrechte ist genehmigt und die Änderung an site.conf ist ungeklärt. Was solltest du vor der Freigabe eines neuen Referenzstands tun?

::option[Genehmige alles, weil eine Zeile dem Plan entsprach.]{#file-integrity-baselines-update-timing-a explanation="Die Abweichungen betreffen zwei verschiedene Änderungen."}
::option[Verwirf den Abweichungsbericht.]{#file-integrity-baselines-update-timing-b explanation="Er hält fest, was noch geprüft werden muss."}
::option[Untersuche die ungeklärte Änderung an site.conf.]{#file-integrity-baselines-update-timing-c .correct explanation="Ein neuer Referenzstand sollte erst nach der Prüfung des aktuellen Zustands erstellt werden."}
:::

Mit [Überwachung der Dateiintegrität](https://labex.io/tutorials/linux-file-integrity-monitoring-fim-656122) kannst du in einer Übungsumgebung einen Referenzstand erstellen und Dateien damit vergleichen.

## Zusammenfassung

Du kannst jetzt einen Referenzstand als Beleg für einen konkreten Vergleich verwenden.

1. Unterscheide im Bericht zwischen Inhalt, Zugriffsrechten und Vorhandensein.
2. Prüfe, ob der Referenzstand einen vertrauenswürdigen Zustand abbildet.
3. Kläre unerwartete Abweichungen, bevor du einen neuen Referenzstand akzeptierst.
