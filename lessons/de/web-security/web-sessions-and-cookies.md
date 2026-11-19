---
lesson_id: "web-sessions-and-cookies"
course_id: "web-security"
lang: "de"
order_index: 5
title: "Sitzungen und Cookies"
description: "Lerne, wie ein Cookie Browseranfragen einer Websitzung zuordnet."
meta_title: "Sitzungen und Cookies - Websicherheit"
meta_description: "Lerne, wie ein Cookie Browseranfragen einer Websitzung zuordnet."
meta_keywords: "Sitzungen, Cookies, Websicherheit, Cybersicherheit, Linux Journey"
---

Nach einer erfolgreichen Anmeldung sendet der Browser oft weitere Anfragen. Eine **Sitzung** ermöglicht es der Anwendung, diese Anfragen dem angemeldeten Konto zuzuordnen. Häufig speichert der Browser dazu eine kurze Kennung in einem Cookie.

## Ein Cookie verfolgen

Diese Beispiele sind gekürzt. Die Antwort sendet ein Cookie namens `session` mit einem erfundenen Token zur Veranschaulichung.

```http
Set-Cookie: session=sample-token; Secure; HttpOnly; SameSite=Lax
```

Der Browser kann das Cookie anschließend mit einer Anfrage senden, die den Regeln des Cookies entspricht.

```http
Cookie: session=sample-token
```

Der Server verwendet das Token, um die zuvor eingerichtete Sitzung nachzuschlagen.

:::single-choice{#web-sessions-and-cookies-direction} Welcher Header sendet den Cookie-Wert in einer passenden Anfrage zurück?

::option[Set-Cookie.]{#web-sessions-and-cookies-direction-a explanation="Diesen Header sendet der Server in der Antwort, um das Cookie zu setzen."}
::option[Content-Type.]{#web-sessions-and-cookies-direction-c explanation="Dieser Header beschreibt das Format des Nachrichteninhalts."}
::option[Cookie.]{#web-sessions-and-cookies-direction-b .correct explanation="Der Browser sendet diesen Anfrageheader, wenn die Regeln für das Cookie erfüllt sind."}
:::

## Die Attribute lesen

`Secure` beschränkt die gewöhnliche Übertragung des Cookies auf HTTPS. `HttpOnly` verhindert, dass Skripte der Webseite das Cookie über die übliche Cookie-Schnittstelle des Browsers lesen. `SameSite` steuert, wann der Browser es bei Anfragen mitsendet, die von einer anderen Website ausgehen. Jede Einstellung betrifft einen anderen Teil des Browserverhaltens.

:::single-choice{#web-sessions-and-cookies-secure-attribute} Welches Attribut beschränkt die Übertragung dieses Cookies auf HTTPS?

::option[HttpOnly.]{#web-sessions-and-cookies-secure-attribute-b explanation="Dieses Attribut beschränkt den Zugriff von Seitenskripten auf das Cookie."}
::option[Secure.]{#web-sessions-and-cookies-secure-attribute-a .correct explanation="Dieses Attribut betrifft die geschützte Übertragung des Cookies."}
::option[Der Name session.]{#web-sessions-and-cookies-secure-attribute-c explanation="Der Name eines Cookies ist eine Bezeichnung, die die Anwendung auswählt."}
:::

## Eine Sitzung beenden

Bei der Abmeldung kann der Dienst die Sitzung auf dem Server ungültig machen und den Browser anweisen, das gespeicherte Cookie zu löschen. Die serverseitige Ungültigkeit ist wichtig, weil der Browser den alten Wert noch kurz gespeichert haben kann. Behandle ein echtes Sitzungstoken wie Zugangsdaten und lass es in Screenshots und weitergegebenen Protokollen weg.

:::single-choice{#web-sessions-and-cookies-after-sign-out} Was sollte geschehen, wenn ein ungültig gewordenes Sitzungstoken wieder beim Server ankommt?

::option[Der Server sollte die Anfrage als nicht authentifiziert behandeln.]{#web-sessions-and-cookies-after-sign-out-c .correct explanation="Die zu diesem Wert gehörende Sitzung auf dem Server ist nicht mehr gültig."}
::option[Der Server sollte die alte Sitzung automatisch wiederherstellen.]{#web-sessions-and-cookies-after-sign-out-a explanation="Die alte Sitzung wurde beendet."}
::option[Der Server sollte das Cookie akzeptieren, weil es noch einen Namen hat.]{#web-sessions-and-cookies-after-sign-out-b explanation="Der Name eines Cookies macht seinen Wert nicht gültig."}
:::

## Zusammenfassung

Du kannst jetzt ein Sitzungscookie zwischen Browser und Dienst verfolgen.

1. Erkenne den Header, der ein Cookie setzt, und den Header, der es zurücksendet.
2. Erkläre die Aufgabe gängiger Cookie-Attribute.
3. Beschreibe, wie das Ungültigmachen auf dem Server eine Sitzung beendet.
