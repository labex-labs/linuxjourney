---
lesson_id: "linux-service-accounts"
course_id: "linux-hardening"
lang: "de"
order_index: 2
title: "Dienstkonten"
description: "Lerne, das Konto eines laufenden Linux-Prozesses zu ermitteln und seine Zugriffsrechte einzuschätzen."
meta_title: "Dienstkonten - Linux-Härtung"
meta_description: "Lerne, das Konto eines laufenden Linux-Prozesses zu ermitteln und seine Zugriffsrechte einzuschätzen."
meta_keywords: "Dienstkonten, Linux-Härtung, Cybersicherheit, Linux Journey"
---

Ein Webserver startet als Prozess. Linux ordnet jedem Prozess eine Identität zu, die mitbestimmt, was das Programm lesen oder ändern kann. Ein **Dienstkonto** ist ein eigenes Konto für ein Programm.

## Das Konto eines Prozesses ablesen

Im Terminal liefert `$$` die Prozess-ID der Shell. Damit kannst du feststellen, unter welchem Konto deine Shell läuft. Die Option `-p` wählt diesen Prozess aus und `-o` bestimmt die angezeigten Spalten. Mit den Gleichheitszeichen entfallen die Spaltenüberschriften.

```bash
$ ps -p "$$" -o user=,comm=
```

Im LabEx-Terminal könnte das Konto `labex` heißen. In der Befehlsspalte steht das Shell-Programm. Bei einem Dienstprozess zeigen dieselben Felder, welches Konto er verwendet, unabhängig davon, wer ihn gestartet hat.

:::single-choice{#linux-service-accounts-process-user} Welches Feld nennt das Konto des ausgewählten Prozesses?

::option[Die mit -p angegebene Prozess-ID.]{#linux-service-accounts-process-user-a explanation="Eine Prozess-ID wählt einen bestimmten laufenden Prozess aus."}
::option[Der Befehlsname in der letzten Spalte.]{#linux-service-accounts-process-user-c explanation="Er nennt das laufende Programm."}
::option[Das von ps ausgegebene Benutzerfeld.]{#linux-service-accounts-process-user-b .correct explanation="Das Benutzerfeld zeigt die Identität des Prozesses."}
:::

![Ps-Ausgabe mit dem Shell-Prozess von LabEx und seinem Konto labex](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/linux-hardening/linux-service-accounts/shell-identity.png)

## Ein eigenes Konto wählen

Stell dir einen Webdienst vor, der nur Seiten lesen und sein eigenes Protokoll schreiben soll. Ein eigenes Konto namens `site-web` kann genau diese Rechte erhalten. Mit den umfassenderen Rechten eines Administrators könnte das Programm wesentlich mehr am Host ändern, als es für seine Aufgabe braucht.

:::single-choice{#linux-service-accounts-isolate-service} Welche Rechte passen zu den Aufgaben des Dienstes?

::option[Erlaube site-web, die Dateien aller Nutzer zu bearbeiten.]{#linux-service-accounts-isolate-service-b explanation="Keine seiner Aufgaben braucht so weitreichende Rechte."}
::option[Erlaube site-web, Seiten zu lesen und in sein eigenes Protokoll zu schreiben.]{#linux-service-accounts-isolate-service-a .correct explanation="Diese Rechte passen zu den beiden genannten Aufgaben."}
::option[Lass site-web jede Anfrage mit Administratorrechten verarbeiten.]{#linux-service-accounts-isolate-service-c explanation="Für die meisten Anfragen reichen die begrenzten Rechte des Dienstes."}
:::

## Dienste mit mehreren Prozessen prüfen

Manche Dienste teilen ihre Aufgaben auf mehrere Prozesse auf. Prüfe den Prozess, der die Anfrage verarbeitet, um seine Berechtigungen zu bestimmen. Wenn du das Konto änderst, unter dem ein Dienst läuft, prüfe, ob der Dienst seine Eingaben weiterhin lesen kann und nur dort schreiben darf, wo es nötig ist.

:::single-choice{#linux-service-accounts-verify-identity} Ein Wartungswerkzeug meldet für den übergeordneten Prozess das Konto root. Woran erkennst du, welches Konto die Webanfragen verarbeitet?

::option[An der Identität des Arbeitsprozesses, der die Anfragen verarbeitet.]{#linux-service-accounts-verify-identity-c .correct explanation="Die Prüfung des zuständigen Prozesses ordnet das Konto der tatsächlichen Aufgabe zu."}
::option[Allein am Namen der Konfigurationsdatei des Dienstes.]{#linux-service-accounts-verify-identity-a explanation="Der Dateiname zeigt nicht, unter welchem Konto der Arbeitsprozess läuft."}
::option[Am Namen der Person, die das Terminal geöffnet hat.]{#linux-service-accounts-verify-identity-b explanation="Das Terminal und der Dienst können unter unterschiedlichen Konten laufen."}
:::

## Zusammenfassung

Du kannst jetzt feststellen, unter welchem Konto ein Linux-Prozess läuft.

1. Lies den Benutzer eines Prozesses in der Ausgabe von ps ab.
2. Wähle Rechte, die zur Aufgabe des Dienstes passen.
3. Prüfe in einem Dienst mit mehreren Prozessen den Prozess, der die Aufgabe tatsächlich ausführt.
