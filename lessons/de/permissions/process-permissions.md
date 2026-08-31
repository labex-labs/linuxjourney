---
lesson_id: "process-permissions"
course_id: "permissions"
lang: "de"
order_index: 7
title: "Prozessberechtigungen"
description: "Erfahre, wie reale, effektive und gespeicherte Benutzer-IDs Linux-Prozessen helfen, Aufrufer nachzuverfolgen und Privilegien zu verwalten."
meta_title: "Prozessberechtigungen – Berechtigungen"
meta_description: "Lerne Linux-Prozessberechtigungen kennen, darunter reale, effektive und gespeicherte Benutzer-IDs. Verstehe, wie UIDs Sicherheit und Befehlsausführung beeinflussen. Beginne noch heute mit dem Lernen!"
meta_keywords: "Linux-Prozessberechtigungen, reale UID, effektive UID, gespeicherte UID, Linux-Sicherheit, passwd-Befehl, Linux-Tutorial, Linux für Einsteiger"
---

Linux-Autorisierungsprüfungen wirken auf Prozesszugangsdaten und nicht unmittelbar auf einen eingegebenen Benutzernamen. Ein Prozess besitzt mehrere verwandte Benutzer- und Gruppen-IDs, die jeweils eine andere Aufgabe erfüllen. Die meisten gewöhnlichen Programme starten mit übereinstimmenden Identitäten, während privilegierte Programme bewusst unterschiedliche Werte verwenden können.

## Reale Benutzer-ID

Die reale Benutzer-ID kennzeichnet das Konto, das den Prozess oder seine übergeordnete Anmeldesitzung gestartet hat. Programme können sie prüfen, um den Aufrufer von einer erhöhten effektiven Identität zu unterscheiden.

Bei einem gewöhnlichen, von Benutzer Bob gestarteten Befehl entspricht die reale Benutzer-ID normalerweise Bobs UID. Das Erstellen eines weiteren Prozesses erzeugt weder ein neues Konto noch ändert es diese Identität von selbst.

:::single-choice{#process-permissions-real-uid}
Was kennzeichnet die reale Benutzer-ID eines Prozesses gewöhnlich?

::option[Den Eigentümer der zuletzt geöffneten Datei.]{#process-permissions-real-opened-file explanation="Das Öffnen einer Datei ersetzt die reale UID des Prozesses nicht durch den Eigentümer dieser Datei."}
::option[Das Konto, das mit dem ursprünglichen Aufrufer des Prozesses verbunden ist.]{#process-permissions-real-caller .correct explanation="Die reale UID erfasst die beim Start des Prozesses übernommene Benutzeridentität des Aufrufers."}
::option[Die für jede Zugriffsprüfung ausgewählte Gruppe.]{#process-permissions-real-group explanation="Eine UID ist eine Benutzeridentität; Gruppenprüfungen verwenden getrennte Gruppenzugangsdaten."}
:::

## Effektive Benutzer-ID

Die effektive Benutzer-ID ist die Benutzerzugangsangabe, die für viele Dateisystem- und Privilegienprüfungen verwendet wird. Gewöhnlich stimmt sie mit der realen UID überein. Bei der Ausführung eines berücksichtigten setuid-Programms kann sie stattdessen aus dem Eigentümer der ausführbaren Datei initialisiert werden.

Ein sorgfältig entwickeltes Passwortwerkzeug kann beispielsweise mit erhöhter effektiver UID laufen, um geschützte Authentifizierungsdaten zu aktualisieren. Das Programm muss dennoch Richtlinien anhand des Aufrufers, des angeforderten Kontos, der PAM-Ergebnisse und weiterer Zusammenhänge durchsetzen. Der Besitz einer effektiven UID macht nicht automatisch jeden angeforderten Vorgang rechtmäßig.

:::single-choice{#process-permissions-effective-uid}
Welche Benutzer-ID wird für viele Zugriffsentscheidungen im Namen eines Prozesses verwendet?

::option[Die effektive Benutzer-ID.]{#process-permissions-effective-active .correct explanation="Die effektive UID ist die aktive Benutzerzugangsangabe, die bei vielen Autorisierungsprüfungen herangezogen wird."}
::option[Ausschließlich die gespeicherte Benutzer-ID.]{#process-permissions-effective-saved-only explanation="Die gespeicherte ID unterstützt Übergänge zwischen Zugangsdaten, ist aber im Allgemeinen nicht die aktive Identität für Zugriffsprüfungen."}
::option[Die im aktuellen Verzeichnis gespeicherte UID.]{#process-permissions-effective-directory explanation="Dateisystemeigentum sind Objektmetadaten und nicht die aktive Benutzerzugangsangabe des Prozesses."}
:::

## Gespeicherte Set-User-ID

Mit der gespeicherten Set-User-ID kann ein Programm eine Identität behalten, die es später gemäß den Regeln der Systemaufrufe wiederherstellen kann. Ein privilegiertes Programm kann seine effektive UID vorübergehend auf einen weniger privilegierten Wert umstellen, gewöhnliche Arbeiten mit geringeren Befugnissen ausführen und die gespeicherte Identität nur für einen eng begrenzten Vorgang wiederherstellen.

Das ist sicherer, als während des gesamten Programms erhöhte Befugnisse beizubehalten – allerdings nur bei korrekter Umsetzung. Programme sollten Privilegien dauerhaft ablegen, sobald sie nicht mehr benötigt werden, und jeden Aufruf zur Änderung von Zugangsdaten auf Fehler prüfen.

:::single-choice{#process-permissions-saved-uid}
Warum kann ein privilegiertes Programm eine gespeicherte Set-User-ID behalten?

::option[Um seine effektive Identität für kontrollierte privilegierte und unprivilegierte Phasen zu wechseln.]{#process-permissions-saved-switch .correct explanation="Die gespeicherte Identität kann eine vorübergehende Verringerung der Privilegien und eine später erlaubte Wiederherstellung unterstützen."}
::option[Um diese UID automatisch jeder gelesenen Datei zuzuweisen.]{#process-permissions-saved-file-owner explanation="Das Lesen einer Datei ändert ihr Eigentum nicht in die gespeicherte UID des Prozesses."}
::option[Um die Systemkontodatenbank für den Prozess zu ersetzen.]{#process-permissions-saved-database explanation="Prozesszugangsdaten ersetzen weder Kontoeinträge noch Daten von Namensdiensten."}
:::

## Benutzer-IDs sind nur ein Teil des Zugangsdatenbestands

Prozesse besitzen außerdem reale, effektive, gespeicherte und ergänzende Gruppenzugangsdaten. Dateisystem-IDs, Capabilities, Namensräume, Sicherheitsmodule, ACLs, Einhängeoptionen und Dienstrichtlinien können die Autorisierung weiter beeinflussen. Daher ist „die UID erlaubt es“ häufig nur ein Teil einer vollständigen Erklärung.

Verwende unter Linux Werkzeuge wie `ps` und `/proc/PROCESS/status`, um Zugangsdaten zu prüfen. Verfügbare Felder und Anzeigeformate unterscheiden sich. Lies daher die lokale Dokumentation und ändere Zugangsdaten nicht bloß zum Experimentieren auf einem gemeinsam genutzten System.

:::single-choice{#process-permissions-ordinary-identities}
Wie verhalten sich bei den meisten gewöhnlichen Befehlen ohne Privilegienübergang die reale und die effektive UID zueinander?

::option[Die effektive UID ist immer null.]{#process-permissions-effective-root explanation="Gewöhnliche Befehle erhalten nicht automatisch die UID von root."}
::option[Die reale UID entspricht immer dem Eigentümer der ausführbaren Datei.]{#process-permissions-real-file-owner explanation="Der Eigentümer der ausführbaren Datei beeinflusst das setuid-Verhalten und nicht die gewöhnliche reale UID."}
::option[Sie entsprechen gewöhnlich der UID des aufrufenden Benutzers.]{#process-permissions-uids-match .correct explanation="Ohne setuid oder eine ausdrückliche Änderung der Zugangsdaten laufen gewöhnliche Prozesse meist mit übereinstimmenden realen und effektiven Identitäten."}
:::

## Zusammenfassung

Du kannst nun erklären, warum ein Linux-Prozess mehrere Benutzeridentitäten besitzen kann.

1. Verwende die reale UID, um den ursprünglichen Aufrufer zu bestimmen.
2. Setze die effektive UID mit aktiven Autorisierungsprüfungen in Beziehung.
3. Nutze die gespeicherte Identität zum Verständnis kontrollierter Privilegienübergänge.
4. Berücksichtige Gruppen-IDs und zusätzliche Sicherheitsmechanismen als Teil der vollständigen Entscheidung.
