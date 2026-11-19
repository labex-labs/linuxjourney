---
lesson_id: "web-authentication"
course_id: "web-security"
lang: "de"
order_index: 4
title: "Authentifizierung"
description: "Lerne, wie ein Webdienst eine Identität prüft und warum zwei Faktoren unterschiedliche Nachweise liefern können."
meta_title: "Authentifizierung - Websicherheit"
meta_description: "Lerne, wie ein Webdienst eine Identität prüft und warum zwei Faktoren unterschiedliche Nachweise liefern können."
meta_keywords: "Authentifizierung, Websicherheit, Cybersicherheit, Linux Journey"
---

Bei der **Authentifizierung** prüft der Dienst die Identität, die ein Nutzer angibt. Ein Anmeldeformular kann nach Kontoname und Passwort fragen. Mit dem Namen gibt der Nutzer an, wer er ist. Das Passwort dient als Nachweis, den der Dienst prüfen kann.

## Die angegebene Identität erkennen

Angenommen, ein Nutzer gibt den Kontonamen `alex` ein. Jeder, der den Namen kennt, kann ihn eingeben. Der Dienst prüft den vorgelegten Nachweis anhand der Daten und Regeln für dieses Konto.

:::single-choice{#web-authentication-username-claim} Welche Eingabe gibt an, bei welchem Konto sich der Nutzer anmelden möchte?

::option[Das Ergebnis der Passwortprüfung.]{#web-authentication-username-claim-a explanation="Dieses Ergebnis hilft dem Dienst, die angegebene Identität zu bestätigen oder abzulehnen."}
::option[Der Kontoname.]{#web-authentication-username-claim-b .correct explanation="Er zeigt dem Dienst, welche Identität zu prüfen ist."}
::option[Das Antwortformat der Startseite.]{#web-authentication-username-claim-c explanation="Der Inhaltstyp hat mit der Anmeldeidentität nichts zu tun."}
:::

## Authentifizierungsfaktoren vergleichen

Ein **Faktor** ist eine Art von Nachweis. Ein Passwort beruht auf etwas, das der Nutzer weiß. Ein registrierter Sicherheitsschlüssel beruht auf etwas, das er besitzt. Ein Passwort und ein separater registrierter Schlüssel liefern zwei verschiedene Arten von Nachweisen.

:::single-choice{#web-authentication-independent-factors} Welches Beispiel kombiniert Wissen und Besitz?

::option[Ein Passwort und ein registrierter Sicherheitsschlüssel.]{#web-authentication-independent-factors-a .correct explanation="Mit dem Passwort weist der Nutzer Wissen nach, mit dem Sicherheitsschlüssel den Besitz des Schlüssels."}
::option[Ein Passwort und ein zweites auswendig gelerntes Passwort.]{#web-authentication-independent-factors-b explanation="Beide beruhen auf Wissen."}
::option[Ein Benutzername und ein Seitentitel.]{#web-authentication-independent-factors-c explanation="Diese Bezeichnungen liefern kaum einen Nachweis der Identität."}
:::

## Eine erfolgreiche Anmeldung einordnen

Nach der Prüfung kann der Dienst dem Nutzer erlauben, eine Sitzung zu starten. Eine erfolgreiche Identitätsprüfung bestimmt, welches Konto der Dienst als angemeldet behandelt. Welche Rechte das Konto dabei hat, geht daraus allein nicht hervor. Bei Anfragen zu einzelnen Ressourcen wendet der Dienst seine Zugriffsregeln an.

:::single-choice{#web-authentication-auth-limit} Ein Konto wurde erfolgreich angemeldet und fordert eine Administrationsseite an. Was sollte als Nächstes geschehen?

::option[Jedes angemeldete Konto sollte die Seite automatisch erhalten.]{#web-authentication-auth-limit-a explanation="Das Konto braucht weiterhin das für die Seite erforderliche Recht."}
::option[Der ursprüngliche Seitentitel sollte über den Zugriff entscheiden.]{#web-authentication-auth-limit-b explanation="Ein Seitentitel legt keine Benutzerrechte fest."}
::option[Die Anwendung sollte prüfen, ob das Konto auf diese Ressource zugreifen darf.]{#web-authentication-auth-limit-c .correct explanation="Identitätsprüfung und Ressourcenzugriff beantworten unterschiedliche Fragen."}
:::

## Zusammenfassung

Du kannst jetzt erklären, was eine Authentifizierung bestätigt.

1. Unterscheide die angegebene Identität vom zugehörigen Nachweis.
2. Erkenne zwei unterschiedliche Arten von Authentifizierungsfaktoren.
3. Nutze für Entscheidungen zum Ressourcenzugriff die Autorisierungsregeln des Dienstes.
