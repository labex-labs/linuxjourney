---
lesson_id: "linux-least-privilege"
course_id: "linux-hardening"
lang: "de"
order_index: 3
title: "Minimale Rechte"
description: "Lerne, Datei- und Verwaltungsrechte passend zu einer konkreten Dienstaufgabe auszuwählen."
meta_title: "Minimale Rechte - Linux-Härtung"
meta_description: "Lerne, Datei- und Verwaltungsrechte passend zu einer konkreten Dienstaufgabe auszuwählen."
meta_keywords: "Minimale Rechte, Linux-Härtung, Cybersicherheit, Linux Journey"
---

Das **Prinzip der minimalen Rechte** besagt, dass ein Konto nur die Rechte erhält, die es für seine Aufgabe braucht. Überlege zuerst, was das Konto tun soll. Vielleicht muss es eine Datei lesen und eine andere schreiben, aber keine Verwaltungsaufgaben ausführen.

## Rechte an die Aufgabe anpassen

Ein Arbeitsprozess des Webdienstes muss `index.html` lesen. Das Konto für die Bereitstellung aktualisiert die Datei. Für diese beiden Aufgaben lassen sich unterschiedliche Rechte vergeben. Der Arbeitsprozess darf die Seite lesen und das Bereitstellungskonto darf sie schreiben.

:::single-choice{#linux-least-privilege-read-only-page} Welches Recht an der Seite braucht der Arbeitsprozess in diesem Beispiel?

::option[Leserecht.]{#linux-least-privilege-read-only-page-a .correct explanation="Um die Datei auszuliefern, muss der Prozess ihren Inhalt lesen."}
::option[Schreibrecht.]{#linux-least-privilege-read-only-page-b explanation="Das Bereitstellungskonto ändert die Seite."}
::option[Das Recht, andere Dienste zu verwalten.]{#linux-least-privilege-read-only-page-c explanation="Das gehört nicht zur Aufgabe des Arbeitsprozesses."}
:::

## Den gesamten Pfad prüfen

Neben den Dateirechten braucht der Prozess unter Linux auch Zugang zu den Verzeichnissen auf dem Weg zur Datei. Das Ausführungsrecht an einem Verzeichnis erlaubt dem Programm, es zu durchqueren, wenn es den gesuchten Namen kennt. Eine lesbare Datei bleibt für den Arbeitsprozess unerreichbar, wenn er eines der Verzeichnisse auf dem Pfad nicht durchqueren darf.

:::single-choice{#linux-least-privilege-path-boundary} Laut Dateirechten darf der Arbeitsprozess index.html lesen, aber er darf das übergeordnete Verzeichnis nicht betreten. Was solltest du prüfen?

::option[Ob die Seite mehr Speicherplatz belegt.]{#linux-least-privilege-path-boundary-a explanation="Die Dateigröße gewährt keinen Zugang zum Verzeichnis."}
::option[Ob alle die Seite bearbeiten dürfen sollten.]{#linux-least-privilege-path-boundary-c explanation="Schreibrecht behebt den fehlenden Zugang über den Pfad nicht."}
::option[Ob der Arbeitsprozess das Verzeichnis durchqueren darf.]{#linux-least-privilege-path-boundary-b .correct explanation="Der Arbeitsprozess braucht sowohl Zugang über den Pfad als auch Leserecht an der Datei."}
:::

## Verwaltungsaufgaben begrenzen

Verwaltungswerkzeuge wie `sudo` können berechtigten Nutzern bestimmte Wartungsaufgaben erlauben. Lege fest, um welche Aktion es geht, wer sie ausführen darf und wie du den neuen Zugriff prüfst. Überprüfe, dass die vorgesehene Wartung funktioniert und dass dieselbe Richtlinie eine fachfremde Verwaltungsaktion weiterhin sperrt.

:::single-choice{#linux-least-privilege-policy-test} Eine Wartungsrolle soll den Dienststatus prüfen können. Welcher Testplan prüft die vorgesehenen Rechte am besten?

::option[Prüfe, ob jetzt sämtliche Administrationsbefehle funktionieren.]{#linux-least-privilege-policy-test-a explanation="Diese zusätzlichen Rechte würden über die festgelegte Aufgabe hinausgehen."}
::option[Prüfe, ob die Rolle den Status lesen kann und ob andere privilegierte Änderungen gesperrt bleiben.]{#linux-least-privilege-policy-test-c .correct explanation="Damit prüfst du den nötigen Zugriff und die vorgesehene Grenze."}
::option[Prüfe nur, ob der Benutzername existiert.]{#linux-least-privilege-policy-test-b explanation="Die Existenz eines Kontos zeigt nicht, welche Rechte es hat."}
:::

## Zusammenfassung

Du kannst jetzt einschätzen, welche Mindestrechte eine Aufgabe benötigt.

1. Unterscheide Lese-, Schreib- und Verwaltungsaufgaben.
2. Prüfe den Zugang durch alle Verzeichnisse eines Pfads.
3. Prüfe für eine Rolle sowohl die erlaubten als auch die eingeschränkten Aktionen.
