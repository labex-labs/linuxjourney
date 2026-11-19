---
lesson_id: "deployment-staging"
course_id: "deployment"
lang: "de"
order_index: 3
title: "Staging"
description: "Lerne, was du in Staging prüfen kannst und warum sich dasselbe Artefakt in verschiedenen Umgebungen unterschiedlich verhalten kann."
meta_title: "Staging - Bereitstellung"
meta_description: "Lerne, was du in Staging prüfen kannst und warum sich dasselbe Artefakt in verschiedenen Umgebungen unterschiedlich verhalten kann."
meta_keywords: "Staging, Testumgebung, Bereitstellung, DevOps, Linux Journey"
---

Ein Release ist fast fertig. Führe das Artefakt in **Staging** aus, einer Testumgebung, die dem späteren Produktivdienst möglichst nahekommt. So prüfst du das Release unter realistischen Einstellungen, bevor es Anfragen aus der Produktion verarbeitet.

## Dasselbe Artefakt in die nächste Umgebung übernehmen

Verwende das Image, das getestet und freigegeben wurde. Wenn sich die Abhängigkeiten geändert haben, kann ein neuer Build ein anderes Artefakt erzeugen. Halte die vollständige Image-Referenz bei jeder Bereitstellung fest.

```text
Environment  Artifact      Page configuration
staging      site@digest-A Internal preview
production   site@digest-A Public website
```

Der Digest im Beispiel ist ein Platzhalter. Beide Umgebungen verwenden dasselbe Artefakt, aber unterschiedliche Einstellungen.

:::single-choice{#deployment-staging-same-artifact} Woran erkennst du, dass sich derselbe verpackte Code in die Produktion übernehmen lässt?

::option[In beiden Bereitstellungseinträgen steht dieselbe Artefaktreferenz.]{#deployment-staging-same-artifact-b .correct explanation="Die genaue Referenz verbindet beide Umgebungen mit demselben Build."}
::option[Beide Umgebungen bezeichnen einen Port gleich.]{#deployment-staging-same-artifact-a explanation="Eine gemeinsame Einstellung zeigt nicht, ob das Artefakt identisch ist."}
::option[Die Bereitstellungen fanden am selben Tag statt.]{#deployment-staging-same-artifact-c explanation="Aus dem Datum geht nicht hervor, was bereitgestellt wurde."}
:::

## Repräsentative Prüfungen auswählen

In Staging solltest du wichtige Funktionen ausprobieren können, etwa die Seite laden und Daten aus einem Testsystem lesen, von dem sie abhängt. Verwende dafür freigegebene Testkonten und Testdaten. Ein erfolgreicher Staging-Test erhöht das Vertrauen in das geprüfte Szenario. Unterschiede bei Datenverkehr, Daten oder Konfiguration können in Produktion weiterhin eine Rolle spielen.

:::single-choice{#deployment-staging-staging-scope} Die Staging-Seite lädt mit einer Testdatenbank. Was solltest du nach der Bereitstellung in Produktion noch prüfen?

::option[Ob das Artefakt keine Versionsangabe mehr braucht.]{#deployment-staging-staging-scope-b explanation="Versionseinträge bleiben bei der Prüfung und bei einer Wiederherstellung nützlich."}
::option[Ob alle zukünftigen Produktionsanfragen erfolgreich sein werden.]{#deployment-staging-staging-scope-c explanation="Eine kleine Stichprobe kann nicht für alle künftigen Anfragen sprechen."}
::option[Ob der Zugriff in Produktion mit den dort freigegebenen Einstellungen funktioniert.]{#deployment-staging-staging-scope-a .correct explanation="Die Staging-Anfrage hat die Produktionsumgebung nicht geprüft."}
:::

## Die Zielumgebung vor der Änderung prüfen

Lies den Namen und die Adresse der Zielumgebung, bevor du die Bereitstellung ausführst. Verwende anschließend dieselbe Adresse, um die neue Version und wichtige Funktionen zu prüfen. Halte Staging und Produktion in deinen Notizen eindeutig fest, damit jedes Ergebnis der richtigen Umgebung zugeordnet werden kann.

:::single-choice{#deployment-staging-correct-target} Du möchtest in Staging bereitstellen, aber der Befehl zeigt die Produktionsadresse. Was solltest du zuerst tun?

::option[Führe den Befehl aus und bezeichne das Ergebnis als Staging.]{#deployment-staging-correct-target-a explanation="Die Adresse bestimmt, welcher Dienst die Änderung erhält."}
::option[Halte an und prüfe die vorgesehene Zielumgebung.]{#deployment-staging-correct-target-c .correct explanation="So vermeidest du, die Änderung in der falschen Umgebung auszuführen."}
::option[Prüfe das Ergebnis nach der Bereitstellung in einem anderen Browser.]{#deployment-staging-correct-target-b explanation="Korrigiere die Zieladresse, bevor die Änderung beginnt."}
:::

Ein praktisches CI/CD-Beispiel findest du unter [Kontinuierliche Bereitstellung in Staging](https://labex.io/tutorials/cd-deployment-to-staging-636593).

## Zusammenfassung

Du kannst jetzt ein freigegebenes Artefakt in Staging prüfen, bevor es in die nächste Umgebung kommt.

1. Behalte in allen Umgebungen dieselbe Artefaktreferenz bei.
2. Wähle Prüfungen, die wichtige Abläufe für die Nutzer abdecken.
3. Prüfe die Zielumgebung, bevor du sie änderst.
