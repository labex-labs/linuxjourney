---
lesson_id: "web-authorization"
course_id: "web-security"
lang: "de"
order_index: 6
title: "Autorisierung"
description: "Lerne, die Anfrage eines angemeldeten Nutzers mit den Zugriffsregeln einer Anwendung abzugleichen."
meta_title: "Autorisierung - Websicherheit"
meta_description: "Lerne, die Anfrage eines angemeldeten Nutzers mit den Zugriffsregeln einer Anwendung abzugleichen."
meta_keywords: "Autorisierung, Websicherheit, Cybersicherheit, Linux Journey"
---

Ein angemeldeter Nutzer kann für eine bestimmte Aktion keine Berechtigung haben. Bei der **Autorisierung** entscheidet die Anwendung, ob ein bestimmtes Konto eine Aktion an einer Ressource ausführen darf.

## Eine Zugriffsrichtlinie lesen

Eine **Rolle** fasst Berechtigungen unter einem Namen zusammen. Diese Übungsrichtlinie gilt für einen Vorschaudienst.

```text
Role       View published page   Edit draft
Reader    Yes                   No
Editor    Yes                   Yes
```

Lies die Zeile für die Rolle des Nutzers und die Spalte für die angeforderte Aktion. Ein Redakteur darf die veröffentlichte Seite ansehen und einen Entwurf bearbeiten. Ein Leser darf die veröffentlichte Seite ansehen.

:::single-choice{#web-authorization-read-policy} Ein angemeldeter Leser möchte einen Entwurf bearbeiten. Was sagt die Tabelle?

::option[Die Aktion ist für Reader nicht erlaubt.]{#web-authorization-read-policy-b .correct explanation="In der Zeile Reader steht unter Edit draft der Wert No."}
::option[Die Aktion ist für jedes angemeldete Konto erlaubt.]{#web-authorization-read-policy-a explanation="Für die angeforderte Aktion gilt eine Einstellung je nach Rolle."}
::option[Der Nutzer muss zu HTTPS wechseln, um Bearbeitungsrechte zu bekommen.]{#web-authorization-read-policy-c explanation="Der Schutz der Verbindung vergibt keine Berechtigungen in der Anwendung."}
:::

## Die richtige Ressource prüfen

In vielen Systemen gelten je nach Ressource verschiedene Rechte. Ein Redakteur kann im eigenen Projekt Entwürfe ändern dürfen und in einem anderen Projekt nur Seiten ansehen. Die Prüfung braucht sowohl die Aktion als auch die Zielressource.

:::single-choice{#web-authorization-target-resource} Maya darf Projekt A bearbeiten. Welche Information entscheidet darüber, ob sie Projekt B bearbeiten darf?

::option[Der Titel von Projekt A.]{#web-authorization-target-resource-b explanation="Der Titel gibt keine Auskunft über den Zugriff auf ein anderes Projekt."}
::option[Die Tatsache, dass ihre Anmeldung erfolgreich war.]{#web-authorization-target-resource-c explanation="Die Authentifizierung identifiziert Mayas Konto. Die Entscheidung über den Ressourcenzugriff steht noch aus."}
::option[Die Zugriffsregeln für Maya und Projekt B.]{#web-authorization-target-resource-a .correct explanation="Die frühere Berechtigung galt für eine bestimmte Ressource."}
:::

## Die Rechte im Dienst prüfen

Eine Benutzeroberfläche kann Bedienelemente zum Bearbeiten für Leser ausblenden. Der Server sollte seine Richtlinie bei jeder Anfrage durchsetzen. Verwende beim Übungsdienst normale, genehmigte Aktionen, um erlaubte und gesperrte Fälle zu prüfen.

:::single-choice{#web-authorization-decision-location} Eine Anwendung blendet die Schaltfläche Edit für Leser aus. Wo sollte sie die Zugriffsregeln ebenfalls durchsetzen?

::option[Nur im Browser, wenn er auswählt, welche Schaltfläche er zeigt.]{#web-authorization-decision-location-a explanation="Der Browser kann die Oberfläche anpassen. Der Dienst entscheidet über den Zugriff bei der eingehenden Anfrage."}
::option[Im Dienst, der die Anfrage zur Aktion entgegennimmt.]{#web-authorization-decision-location-c .correct explanation="Der Dienst kann bei jeder Anfrage Konto, Aktion und Zielressource prüfen."}
::option[Nur auf der Seite mit der Rollenliste.]{#web-authorization-decision-location-b explanation="Einen Rollennamen anzuzeigen setzt keine Zugriffsbeschränkung durch."}
:::

## Zusammenfassung

Du kannst jetzt nachvollziehen, wie eine Anwendung über den Zugriff entscheidet.

1. Gleiche die Rolle des Kontos mit der angeforderten Aktion ab.
2. Beziehe die konkrete Ressource in die Prüfung ein.
3. Prüfe, ob der Dienst seine Richtlinie bei Anfragen durchsetzt.
