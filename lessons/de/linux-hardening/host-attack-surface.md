---
lesson_id: "host-attack-surface"
course_id: "linux-hardening"
lang: "de"
order_index: 1
title: "Angriffsfläche"
description: "Lerne zu erkennen, welche Zugänge ein Linux-Host braucht und welche du prüfen solltest."
meta_title: "Angriffsfläche - Linux-Härtung"
meta_description: "Lerne zu erkennen, welche Zugänge ein Linux-Host braucht und welche du prüfen solltest."
meta_keywords: "Angriffsfläche, Linux-Härtung, Cybersicherheit, Linux Journey"
---

Auf einem Linux-Host kann es eine öffentliche Website, einen Wartungszugang und Hintergrunddienste geben. Notiere zunächst, was die einzelnen Dienste tun und wer sie erreichen soll. Anschließend kannst du nach Zugängen ohne klaren Zweck suchen.

## Vorgesehene Zugänge erfassen

Eine einfache Bestandsliste ordnet jeder Ressource die Personen oder Programme zu, die sie benötigen. Hier ist ein Beispiel für einen Übungshost.

```text
Resource           Intended access
Public homepage    Visitors
Maintenance SSH    Operations team
Preview panel      Local staff on this host only
```

Ein **Zugriffsweg** ist der Weg, auf dem ein Nutzer oder Programm eine Ressource erreicht. Die erreichbaren Schnittstellen, über die jemand auf ein System einwirken könnte, gehören zu seiner **Angriffsfläche**.

:::single-choice{#host-attack-surface-intended-audience} Welche Ressource in dieser Liste muss über das öffentliche Netz erreichbar sein?

::option[Der SSH-Zugang für die Wartung.]{#host-attack-surface-intended-audience-b explanation="Er ist für das Betriebsteam vorgesehen."}
::option[Die öffentliche Startseite.]{#host-attack-surface-intended-audience-a .correct explanation="Sie ist auch für Besucher außerhalb des Hosts gedacht."}
::option[Die Vorschauoberfläche.]{#host-attack-surface-intended-audience-c explanation="Sie ist laut Liste nur für die lokale Nutzung auf dem Host gedacht."}
:::

## Vorgesehene und beobachtete Zugänge vergleichen

Angenommen, die Vorschau ist übers Netz erreichbar, obwohl in der Liste nur lokaler Zugriff vorgesehen ist. Kläre das mit der zuständigen Person und überprüfe den tatsächlichen Zugriffsweg, bevor du etwas änderst. Ein Dienst muss möglicherweise laufen, braucht aber keine Anfragen aus dem Netz anzunehmen.

:::single-choice{#host-attack-surface-mismatch} Welche Beobachtung solltest du nach der beschriebenen Vorgabe prüfen?

::option[Ein Besucher kann auf die Vorschauoberfläche zugreifen.]{#host-attack-surface-mismatch-b .correct explanation="Damit ist die Oberfläche auch außerhalb ihres vorgesehenen Nutzerkreises erreichbar."}
::option[Ein Besucher kann die Startseite laden.]{#host-attack-surface-mismatch-a explanation="Dafür ist die Startseite vorgesehen."}
::option[Das Personal kann die Vorschau lokal auf dem Host öffnen.]{#host-attack-surface-mismatch-c explanation="Der lokale Zugriff entspricht dem vorgesehenen Bedarf."}
:::

## Prüfungen priorisieren

Beginne mit Zugängen, die unnötig sind und erhebliche Folgen haben können. In einem Übungsbeispiel hat eine Vorschauoberfläche, über die sich die Website ändern lässt, Vorrang vor einem ungenutzten Dienst ohne wichtige Daten. Notiere, wer Zugriff braucht, welcher Zugang tatsächlich besteht und wie du prüfst, ob die vorgesehene Einschränkung funktioniert, ohne berechtigte Nutzer zu behindern.

:::single-choice{#host-attack-surface-priority-check} Welche zwei Beobachtungen bestätigen nach einer Änderung am Vorschauzugang, dass die Einschränkung ihr Ziel erreicht?

::option[Die Oberfläche nimmt weiterhin lokale Anfragen an.]{#host-attack-surface-priority-check-a explanation="Das bestätigt den nötigen Zugang. Der unerwünschte Fernzugriff bleibt ungeprüft."}
::option[Der Rechner wurde neu gestartet und hat denselben Hostnamen.]{#host-attack-surface-priority-check-b explanation="Der Zustand des Hosts zeigt nicht, ob die Zugriffsvorgabe eingehalten wird."}
::option[Das Personal hat weiterhin lokalen Zugriff und der unerwünschte Fernzugriff ist gesperrt.]{#host-attack-surface-priority-check-c .correct explanation="Zusammen bestätigen diese Prüfungen den erforderlichen Zugang und die Einschränkung."}
:::

## Zusammenfassung

Du kannst jetzt erkennen, welche Zugriffswege du bei der Härtung prüfen solltest.

1. Beschreibe die Ressource und den vorgesehenen Nutzerkreis.
2. Vergleiche die vorgesehenen mit den beobachteten Zugängen.
3. Prüfe nach einer Änderung sowohl den Schutz als auch den berechtigten Zugriff.
