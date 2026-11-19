---
lesson_id: "linux-security-updates"
course_id: "linux-hardening"
lang: "de"
order_index: 7
title: "Sicherheitsupdates"
description: "Lerne, verfügbare Paketupdates zu prüfen und nach genehmigter Wartung die Funktion eines Dienstes zu überprüfen."
meta_title: "Sicherheitsupdates - Linux-Härtung"
meta_description: "Lerne, verfügbare Paketupdates zu prüfen und nach genehmigter Wartung die Funktion eines Dienstes zu überprüfen."
meta_keywords: "Sicherheitsupdates, Linux-Härtung, Cybersicherheit, Linux Journey"
---

Ein Sicherheitsupdate kann einen Fehler in installierter Software beheben. Prüfe zuerst, welche Softwareversion installiert ist und welche Korrektur es für dein Betriebssystem gibt. Plane die Änderung so, dass sie zu der Nutzung des Dienstes passt.

## Verfügbare Updates prüfen

Auf einem Ubuntu-Übungshost listet dieser Befehl Pakete auf, für die APT ein verfügbares Upgrade kennt. Er ändert nichts und verwendet die bereits auf dem Host vorhandenen Paketinformationen.

```bash
$ apt list --upgradable
```

Für ein aufgeführtes Paket gibt es laut den vorhandenen Paketdaten eine neuere Version. Prüfe in der Sicherheitsmeldung deiner Distribution, ob das Update die benötigte Korrektur enthält. Eine leere Liste kann auch bedeuten, dass die Paketinformationen veraltet sind.

:::single-choice{#linux-security-updates-candidate-is-listed} Ein Paket erscheint in der Liste. Was erfährst du daraus?

::option[Das Update wurde bereits installiert.]{#linux-security-updates-candidate-is-listed-a explanation="Die Liste zeigt eine für das Upgrade verfügbare Version."}
::option[APT kennt eine neuere Version des installierten Pakets.]{#linux-security-updates-candidate-is-listed-b .correct explanation="Das melden die lokalen Paketinformationen zum aktuellen Zeitpunkt."}
::option[Jede neuere Version ist ein Sicherheitsupdate.]{#linux-security-updates-candidate-is-listed-c explanation="Prüfe in der Meldung der Distribution, warum das Update bereitgestellt wurde."}
:::

## Die Änderung planen

Halte für eine genehmigte Änderung den Dienst, die Zielversion und das Wartungsfenster fest. Manche Updates werden erst nach einem Neustart des Dienstes oder des Hosts wirksam. Plane eine Testanfrage und einen Weg zur Wiederherstellung, bevor du den Host änderst.

:::single-choice{#linux-security-updates-reboot-check} Ein Paketupdate korrigiert Code, den ein dauerhaft laufender Dienst verwendet. Was solltest du nach der Installation prüfen?

::option[Ob der Dienst neu gestartet werden muss, um den aktualisierten Code zu verwenden.]{#linux-security-updates-reboot-check-a .correct explanation="Ein laufender Prozess kann noch den alten Code geladen haben."}
::option[Ob das Update vor der Installation in der Paketliste stand.]{#linux-security-updates-reboot-check-b explanation="Die Verfügbarkeit hilft bei der Planung. Sie sagt nichts darüber aus, welche Version ein Prozess geladen hat."}
::option[Ob die Paketliste jetzt keine weiteren Upgrades mehr zeigt.]{#linux-security-updates-reboot-check-c explanation="Auch ohne ausstehende Upgrades kann ein Prozess noch den alten Code verwenden."}
:::

## Das Ergebnis prüfen

Prüfe, ob die installierte Version der genehmigten Zielversion entspricht. Teste den Dienst über den erwarteten Zugriffsweg der Nutzer und halte das Ergebnis fest. Betrifft die Korrektur eine laufende Komponente, prüfe auch, ob die aktualisierte Version tatsächlich verwendet wird.

:::single-choice{#linux-security-updates-security-verification} Welche Kombination belegt am besten, dass das Dienstupdate abgeschlossen ist?

::option[Der Listenbefehl läuft zweimal.]{#linux-security-updates-security-verification-a explanation="Eine wiederholte Auflistung zeigt nicht, ob der Dienst funktioniert."}
::option[Das Wartungsticket hat einen neuen Titel.]{#linux-security-updates-security-verification-b explanation="Der Titel belegt nichts über den laufenden Dienst."}
::option[Die genehmigte Version ist aktiv und eine typische Anfrage ist erfolgreich.]{#linux-security-updates-security-verification-c .correct explanation="Damit prüfst du den Softwarestand und die Funktion, auf die sich Nutzer verlassen."}
:::

## Zwei Angaben zur Version einordnen

Ein installiertes Paket und das Programm, das gerade Anfragen verarbeitet, können vorübergehend unterschiedliche Versionsstände haben. Die Paketliste kann zum Beispiel bereits die korrigierte Version zeigen, während ein vor dem Update gestarteter Prozess weiterläuft. Ziehe zum Abschluss der Prüfung Angaben zum laufenden Prozess heran.

:::single-choice{#linux-security-updates-final-application} Was bleibt offen, wenn die installierte Version korrigiert ist und der alte Prozess noch läuft?

::option[Ob jeder andere Prozess auf dem Rechner ersetzt werden muss.]{#linux-security-updates-final-application-c explanation="Es geht um den aktualisierten Dienst und die dafür genehmigten Wartungsschritte."}
::option[Ob das aktualisierte Programm die Anfragen verarbeitet.]{#linux-security-updates-final-application-a .correct explanation="Die Paketliste bestätigt den Stand der installierten Dateien. Die Prozessprüfung bestätigt den Stand des laufenden Dienstes."}
::option[Ob es überhaupt ein Updatepaket gab.]{#linux-security-updates-final-application-b explanation="Das installierte Paket meldet bereits die korrigierte Version."}
:::

## Zusammenfassung

Du kannst jetzt ein Update von der verfügbaren Version bis zur abschließenden Prüfung beurteilen.

1. Unterscheide verfügbare Updates von installierten Änderungen.
2. Plane mögliche Neustarts und die Wiederherstellung ein.
3. Prüfe die laufende Version und das erwartete Verhalten des Dienstes.
