---
lesson_id: "linux-history"
course_id: "getting-started"
lang: "de"
order_index: 1
title: "Die Geschichte von Linux"
description: "Lerne, wie UNIX, GNU und der Linux-Kernel zu modernen Linux-Systemen beigetragen haben."
meta_title: "Die Geschichte von Linux – Erste Schritte"
meta_description: "Beginne deine Linux-Reise mit seiner Geschichte: Erfahre, wie UNIX, das GNU-Projekt und Linus Torvalds' Linux-Kernel moderne Systeme geprägt haben."
meta_keywords: "Geschichte von Linux, Linux Geschichte, Linux Reise, UNIX, GNU Projekt, Linus Torvalds, Linux Kernel, Linux Anfänger"
---

Willkommen zu deiner **Linux-Reise**! Wenn du bereit bist, in die leistungsfähige Welt von Linux einzutauchen, bist du hier richtig. Mein Name ist Penguin Pete und ich begleite dich. Zum Einstieg sehen wir uns kurz die **Geschichte von Linux** an.

## Die Vorgänger von Linux

Um die Entstehung von Linux zu verstehen, gehen wir zurück ins Jahr 1969. Damals entwickelten Ken Thompson und Dennis Ritchie von den Bell Laboratories das Betriebssystem UNIX. Es wurde später in der Programmiersprache C neu geschrieben, wodurch es portabel wurde und sich weit verbreiten konnte.

![Zeitleiste von Unix](https://file.labex.io/images/ed9c245d-e8be-4287-bf34-67750b042542.jpg)

:::single-choice{#understand-unix-portability} Was war eine wichtige Folge davon, UNIX in C neu zu schreiben?

::option[Es wurde zum freien Kernel des GNU-Systems.]{#unix-became-gnu-kernel explanation="UNIX existierte vor dem GNU-Projekt und war nicht dessen Kernel. GNU begann später mit der Entwicklung eines getrennten Kernels namens Hurd."}
::option[Es ließ sich leichter auf unterschiedliche Hardwaresysteme übertragen.]{#portable-across-hardware .correct explanation="Die Umsetzung in C machte UNIX portabler. Diese Portabilität unterstützte seine Verbreitung über die ursprüngliche Hardware hinaus."}
::option[Es wurde zu einer ausschließlich bei Bell Labs verwendeten Befehlsshell.]{#unix-became-shell explanation="UNIX ist ein Betriebssystem und nicht nur eine Shell. Die Umsetzung in C unterstützte die Verbreitung über Bell Labs hinaus."}
:::

Mehr als ein Jahrzehnt später startete Richard Stallman das GNU-Projekt. GNU ist ein rekursives Akronym für „GNU's Not UNIX“. Ziel war ein vollständig freies und quelloffenes UNIX-ähnliches Betriebssystem. Das Projekt schuf viele grundlegende Komponenten und die GNU General Public License (GPL). Sein eigener Kernel, GNU Hurd, war jedoch noch nicht allgemein einsatzbereit, als Linux verfügbar wurde.

:::single-choice{#identify-gnu-missing-component} Welche wichtige GNU-Komponente war noch nicht fertig, als Linux verfügbar wurde?

::option[Ein produktionsreifer Kernel]{#gnu-kernel .correct explanation="GNU hatte zahlreiche Systemkomponenten geschaffen, doch sein eigener Kernel GNU Hurd war noch nicht allgemein einsatzbereit."}
::option[Eine Lizenz für freie Software]{#gnu-license explanation="Das GNU-Projekt hatte die GNU General Public License bereits geschaffen. Als Systemkomponente fehlte ein verwendbarer Kernel."}
::option[Grundlegende Systemwerkzeuge]{#gnu-tools explanation="GNU hatte bereits viele grundlegende Werkzeuge geschaffen. Der Kernel blieb der wichtige unvollendete Teil des Systems."}
:::

## Die Rolle des Kernels

Der Kernel ist die Kernkomponente eines Betriebssystems. Er bildet die Brücke für die Kommunikation zwischen Hardware und Software. Der Kernel verwaltet Systemressourcen wie CPU, Arbeitsspeicher und Peripheriegeräte. Ein vollständiges Betriebssystem benötigt neben den von Menschen verwendeten Werkzeugen und Anwendungen diesen ressourcenverwaltenden Kern.

:::single-choice{#recognize-kernel-role} Welche Aufgabe gehört zum Betriebssystem-Kernel?

::option[Jeden in der Shell eingegebenen Befehl verfassen]{#write-shell-commands explanation="Menschen oder Skripte geben Shellbefehle vor. Der Kernel stellt die tieferliegenden Ressourcen bereit, wenn Programme diese Befehle ausführen."}
::option[Die Lizenz jeder installierten Anwendung auswählen]{#choose-software-licenses explanation="Softwareautoren und Distributoren wählen Anwendungslizenzen. Diese Auswahl ist keine Aufgabe der Ressourcenverwaltung des Kernels."}
::option[CPU, Arbeitsspeicher und angeschlossene Geräte verwalten]{#manage-system-resources .correct explanation="Der Kernel verwaltet Hardwareressourcen und stellt sie Software bereit. CPU-Zeit, Arbeitsspeicher und Geräte sind zentrale Beispiele."}
:::

## Die Geburt des Linux-Kernels

Damit kommen wir ins Jahr 1991, als der finnische Student Linus Torvalds als persönliches Projekt mit der Entwicklung eines neuen Kernels begann. Dieser wurde als Linux-Kernel bekannt. Nachdem Linux 1992 als freie Software veröffentlicht worden war, ließ es sich mit dem nahezu vollständigen GNU-System zu einem vollständigen freien Betriebssystem verbinden, das häufig GNU/Linux genannt wird. Dieser Meilenstein war ein entscheidender Moment in der **Geschichte von Linux**.

![Linus Torvalds im Jahr 2018](https://file.labex.io/images/3e1311fd-b8ca-45e7-8d02-9aac6377bb36.jpg)

_Linus Torvalds im Jahr 2018 (Quelle: [Wikipedia](https://en.wikipedia.org/wiki/Linus_Torvalds))_

:::single-choice{#identify-linux-kernel-creator} Wer begann 1991 mit der Entwicklung des Linux-Kernels?

::option[Richard Stallman]{#richard-stallman explanation="Richard Stallman startete das GNU-Projekt. GNU stellte viele Systemkomponenten bereit, doch Linus Torvalds begann mit dem Linux-Kernel."}
::option[Dennis Ritchie]{#dennis-ritchie explanation="Dennis Ritchie wirkte an UNIX und der Programmiersprache C mit. Das Linux-Kernel-Projekt begann später durch Linus Torvalds."}
::option[Linus Torvalds]{#linus-torvalds .correct explanation="Linus Torvalds begann 1991 mit dem Kernel-Projekt. Daraus entstand der Linux-Kernel."}
:::

Setze deine **Linux-Reise** mit diesen praktischen Labs fort, um grundlegende Befehle zu üben und Sicherheit in der Befehlszeilenumgebung aufzubauen.

1. **[Erste Schritte mit Linux](https://labex.io/labs/linux-getting-started-with-linux-446315)** – Beginne deine Linux-Reise mit grundlegenden Terminalbefehlen wie `echo`, `date` und einfachen Berechnungen. Ideal für vollständige Einsteiger.
2. **[Dein erstes Linux-Lab](https://labex.io/labs/linux-your-first-linux-lab-270253)** – Dieses einführende Lab führt dich durch das klassische „Hello, World!“-Programm unter Linux und vermittelt einige grundlegende Befehle.
3. **[Eine persönliche Terminalbegrüßung erstellen](https://labex.io/labs/linux-create-personalized-terminal-greeting-446322)** – Eine kurze unterhaltsame Aufgabe, in der du mit grundlegenden Linux-Terminalbefehlen eine ansprechende Willkommensnachricht erstellst.

## Zusammenfassung

Du kannst nun erklären, wie UNIX, GNU und der Linux-Kernel zu modernen Linux-Systemen beigetragen haben.

1. Beschreibe, warum die Portabilität von UNIX wichtig war.
2. Erkenne den Kernel als die wichtige fehlende GNU-Komponente.
3. Erkläre die Rolle des Kernels bei der Verwaltung von Systemressourcen.
4. Benenne Linus Torvalds als Schöpfer des Linux-Kernels.
