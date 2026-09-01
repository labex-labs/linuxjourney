---
lesson_id: "ownership-permissions"
course_id: "permissions"
lang: "de"
order_index: 3
title: "Eigentumsberechtigungen"
description: "Erfahre, wie du Benutzer- und Gruppeneigentum von Linux-Dateisystemobjekten prüfst und änderst."
meta_title: "Eigentumsberechtigungen – Berechtigungen"
meta_description: "Beherrsche Linux-Dateieigentum, indem du die Linux-Befehle chown und chgrp kennenlernst. Dieses Linux-Tutorial erklärt, wie du Benutzer- und Gruppeneigentum von Dateien änderst – eine wichtige Fähigkeit zur Verwaltung von Linux-Berechtigungen."
meta_keywords: "chown, chgrp, Linux-Dateieigentum, Dateieigentümer ändern, Dateigruppe ändern, Linux-Berechtigungen, Linux-Befehle, Linux-Tutorial, Linux-Leitfaden, Benutzereigentum, Gruppeneigentum"
---

Jedes Linux-Dateisystemobjekt erfasst einen Benutzereigentümer und einen Gruppeneigentümer. Diese Identitäten bestimmen, welches Berechtigungstripel für Eigentümer oder Gruppe gilt, gewähren aber selbst keine bestimmte Berechtigung. Prüfe mit `ls -l` sowohl das Eigentum als auch den Modus.

## Den Benutzereigentümer ändern

Verwende `chown`, kurz für change owner, um einen anderen Benutzereigentümer zuzuweisen:

```bash
$ sudo chown patty myfile
```

Dies ändert den Benutzereigentümer von `myfile` in `patty` und lässt seine Gruppe unverändert. Das Ändern des Benutzereigentümers einer Datei erfordert gewöhnlich entsprechende Privilegien, selbst wenn dir die Datei derzeit gehört. Diese Einschränkung verhindert, dass Benutzer Dateien übertragen, um Kontingente oder andere eigentumsbasierte Kontrollen zu umgehen.

:::single-choice{#ownership-permissions-change-user} Welcher Befehl ändert den Benutzereigentümer von `myfile` in `patty` und lässt die Gruppe unverändert?

::option[`chown patty myfile`]{#ownership-permissions-user-with-chown .correct explanation="Ein Benutzername allein als Eigentumsoperand von `chown` ändert den Benutzereigentümer und behält die Gruppe bei."}
::option[`chgrp patty myfile`]{#ownership-permissions-user-with-chgrp explanation="`chgrp` ändert den Gruppeneigentümer und nicht den Benutzereigentümer."}
::option[`chmod patty myfile`]{#ownership-permissions-user-with-chmod explanation="`chmod` ändert Modusbits und akzeptiert keinen Benutzernamen als neuen Eigentümer."}
:::

## Den Gruppeneigentümer ändern

Verwende `chgrp`, um einen anderen Gruppeneigentümer zuzuweisen:

```bash
$ chgrp whales myfile
```

Auf typischen Systemen kann ein unprivilegierter Eigentümer die Gruppe einer Datei nur in eine Gruppe ändern, der dieser Benutzer angehört. Privilegierte Prozesse können umfassendere Änderungen vornehmen. Die entsprechende Form von `chown` beginnt mit einem Doppelpunkt:

```bash
$ chown :whales myfile
```

Anschließend gelten die Modusbits der Gruppe, wenn der Kernel die Gruppenklasse auswählt. Die Änderung der Gruppe fügt nicht automatisch Lese-, Schreib- oder Ausführungsbits hinzu.

:::single-choice{#ownership-permissions-change-group} Was ändert `chgrp whales myfile`?

::option[Den für `myfile` erfassten Benutzereigentümer.]{#ownership-permissions-group-not-user explanation="Der Benutzereigentümer wird mit `chown` und nicht mit `chgrp` geändert."}
::option[Die in der Gruppe `whales` aufgeführten Mitglieder.]{#ownership-permissions-group-members explanation="Der Befehl ändert Dateimetadaten und bearbeitet nicht die Gruppenmitgliedschaftsdatenbank des Systems."}
::option[Den für `myfile` erfassten Gruppeneigentümer.]{#ownership-permissions-group-owner .correct explanation="`chgrp` weist die benannte Gruppe als Gruppeneigentümer des Dateisystemobjekts zu."}
:::

## Benutzer und Gruppe gemeinsam ändern

Gib `USER:GROUP` an `chown` weiter, um beide Felder in einem Vorgang zu aktualisieren:

```bash
$ sudo chown patty:whales myfile
```

Der Befehl weist `patty` als Benutzereigentümer und `whales` als Gruppeneigentümer zu. Überprüfe das Ergebnis, statt einen Erfolg anzunehmen:

```bash
$ ls -l myfile
```

:::single-choice{#ownership-permissions-change-both} Welche Eigentumsangabe weist in einem einzigen `chown`-Befehl den Benutzer `patty` und die Gruppe `whales` zu?

::option[`patty:whales`]{#ownership-permissions-both-colon .correct explanation="Ein Doppelpunkt trennt Benutzer- und Gruppennamen in der kombinierten Eigentumsangabe."}
::option[`patty/whales`]{#ownership-permissions-both-slash explanation="Ein Schrägstrich ist nicht das hier eingeführte Trennzeichen für einen Benutzer- und Gruppenoperanden von `chown`."}
::option[`patty+whales`]{#ownership-permissions-both-plus explanation="Ein Pluszeichen wird nicht verwendet, um die beiden Eigentumsfelder für `chown` zu verbinden."}
:::

## Rekursive Änderungen vorsichtig behandeln

Die Option `-R` ändert Eigentum rekursiv, doch ein weit gefasster rekursiver Befehl kann unerwartete Verzeichnisbäume durchqueren oder Dienstdaten beeinflussen. Bestätige das genaue Ziel, verstehe das Verhalten deiner Implementierung bei symbolischen Links, zeige den Baum vorab an und überprüfe eine kleine Stichprobe, bevor du eine große Hierarchie änderst. Übertrage privilegierte Eigentumsbefehle aus Beispielen nicht auf reale Systeme, ohne ihren Umfang zu prüfen.

:::single-choice{#ownership-permissions-mode-separate} Was geschieht nach der Änderung des Gruppeneigentümers einer Datei mit ihren gewöhnlichen Gruppenberechtigungsbits?

::option[Sie werden immer automatisch auf Lesen und Schreiben gesetzt.]{#ownership-permissions-mode-read-write explanation="`chgrp` wählt nicht automatisch einen festen Gruppenmodus aus."}
::option[Sie werden aus dem Berechtigungstripel des Eigentümers kopiert.]{#ownership-permissions-mode-copied explanation="Die Tripel für Eigentümer und Gruppe bleiben bei einer Eigentumsänderung unabhängig voneinander."}
::option[Sie bleiben unverändert, sofern kein gesonderter Vorgang sie ändert.]{#ownership-permissions-mode-unchanged .correct explanation="Eigentumsfelder und Modusbits sind getrennte Metadaten; die Änderung der Gruppe gewährt nicht von sich aus neue Gruppenbits."}
:::

Das Lab [Linux-Benutzer, -Gruppen und Dateiberechtigungen](https://labex.io/labs/linux-linux-user-group-and-file-permissions-18002) behandelt in einer isolierten Übungsumgebung das Prüfen und Ändern von Eigentum zusammen mit Dateimodi.

## Zusammenfassung

Du kannst nun Eigentumsmetadaten von Berechtigungsbits unterscheiden und sie gezielt ändern.

1. Verwende `chown USER FILE`, um den Benutzereigentümer zu ändern.
2. Verwende `chgrp GROUP FILE` oder `chown :GROUP FILE`, um den Gruppeneigentümer zu ändern.
3. Verwende `chown USER:GROUP FILE`, um beide Felder festzulegen.
4. Überprüfe Ergebnisse und den Umfang rekursiver Änderungen sorgfältig.
