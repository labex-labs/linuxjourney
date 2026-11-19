---
lesson_id: "linux-ssh-access"
course_id: "linux-hardening"
lang: "de"
order_index: 6
title: "SSH-Zugang"
description: "Lerne, Serveridentität, Benutzerauthentifizierung und Anmelderegeln bei SSH zu unterscheiden."
meta_title: "SSH-Zugang - Linux-Härtung"
meta_description: "Lerne, Serveridentität, Benutzerauthentifizierung und Anmelderegeln bei SSH zu unterscheiden."
meta_keywords: "SSH-Zugang, Linux-Härtung, Cybersicherheit, Linux Journey"
---

Bei der Wartung über SSH prüfen beide Seiten der Verbindung etwas. Dein Client muss wissen, welchen Server er erreicht hat. Der Server muss wissen, ob sich das Konto anmelden darf.

## Die Serveridentität prüfen

Ein SSH-Server präsentiert einen **Hostschlüssel**. Der Client kann ihn mit der bekannten Identität des Hosts abgleichen. Ändert sich ein Schlüssel unerwartet, prüfe den neuen Schlüssel über eine freigegebene, unabhängige Quelle. Das kann die Host-Bestandsliste des Teams sein oder eine für die Wartung zuständige Person, die du über einen vertrauenswürdigen Kanal erreichst.

:::single-choice{#linux-ssh-access-unexpected-key} Dein Client meldet, dass sich der Hostschlüssel des Servers geändert hat. Was solltest du zuerst prüfen?

::option[Bestätige den erwarteten neuen Hostschlüssel über eine vertrauenswürdige Quelle.]{#linux-ssh-access-unexpected-key-b .correct explanation="So prüfst du die Identität, bevor du dich auf die Verbindung verlässt."}
::option[Probiere verschiedene Benutzernamen aus, bis einer funktioniert.]{#linux-ssh-access-unexpected-key-a explanation="Ein Benutzername bestätigt die Serveridentität nicht."}
::option[Lösche alle gespeicherten Hostschlüssel und fahre fort.]{#linux-ssh-access-unexpected-key-c explanation="Damit würdest du bekannte Identitätsdaten verwerfen, bevor du die Änderung geklärt hast."}
:::

## Den Benutzerzugang prüfen

Ein Benutzerschlüssel kann nachweisen, dass der Client ein bestimmtes Konto verwenden darf. Der Hostschlüssel dient zur Prüfung der Serveridentität. Die Richtlinie des Servers kann festlegen, welche Konten und Anmeldeverfahren er akzeptiert. Laut der Übersicht für diese Übung meldet sich `ops` mit einem Schlüssel an.

:::single-choice{#linux-ssh-access-distinguish-keys} Wessen Identität prüft der Server, wenn er den Benutzerschlüssel für ops auswertet?

::option[Den Namen der öffentlichen Website.]{#linux-ssh-access-distinguish-keys-b explanation="Der Webinhalt ist von der SSH-Authentifizierung unabhängig."}
::option[Die Identität des Servers selbst.]{#linux-ssh-access-distinguish-keys-c explanation="Für diese Prüfung verwendet der Client den Hostschlüssel."}
::option[Die Identität des Clients, der sich als ops anmelden will.]{#linux-ssh-access-distinguish-keys-a .correct explanation="Bei der Benutzerauthentifizierung geht es um das Konto, mit dem sich der Client anmelden möchte."}
:::

## Einen Wartungszugang offen halten

Lege vor genehmigten Änderungen der SSH-Regeln fest, welche Konten und Anmeldeverfahren vorgesehen sind. Verwende eine eigene Testverbindung und halte den eingerichteten Zugang zur Wiederherstellung offen, bis die vorgesehene Anmeldung gelingt. Eine laufende Sitzung kann eine Änderung überstehen, obwohl eine neue Anmeldung fehlschlägt.

:::single-choice{#linux-ssh-access-test-new-login} Nach einer Regeländerung bleibt eine bestehende Sitzung offen. Was bestätigt, dass sich das Wartungsteam weiterhin anmelden kann?

::option[Allein eine Ping-Antwort.]{#linux-ssh-access-test-new-login-a explanation="Eine Netzwerkantwort zeigt nicht, ob die SSH-Authentifizierung erfolgreich war."}
::option[Eine neue genehmigte SSH-Sitzung mit dem vorgesehenen Konto und Anmeldeverfahren.]{#linux-ssh-access-test-new-login-c .correct explanation="Damit prüfst du direkt die Regeln, die bei einer künftigen Anmeldung gelten."}
::option[Die alte Sitzung bleibt geöffnet und ungenutzt.]{#linux-ssh-access-test-new-login-b explanation="Sie wurde unter den vorherigen Bedingungen authentifiziert."}
:::

## Zusammenfassung

Du kannst jetzt die beteiligten Identitäten und Anmeldeverfahren beim SSH-Wartungszugang prüfen.

1. Prüfe die Serveridentität anhand des Hostschlüssels.
2. Unterscheide diese Prüfung von der Benutzerauthentifizierung.
3. Teste nach einer Änderung eine neue genehmigte Verbindung.
