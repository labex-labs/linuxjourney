---
lesson_id: "ssh-login-events"
course_id: "security-logs"
lang: "de"
order_index: 2
title: "SSH-Anmeldungen"
description: "Lerne, angenommene und abgelehnte SSH-Anmeldungen zu erkennen und Versuche derselben Verbindung zusammenzufassen."
meta_title: "SSH-Anmeldungen – Sicherheitsprotokolle"
meta_description: "Lies Zielkonto, Gegenstellenadresse, Anmeldeverfahren und Ergebnis im SSH-Protokoll und ordne Versuche anhand ihrer Verbindungs-ID zu."
meta_keywords: "SSH-Anmeldungen, SSH-Protokolle, erfolgreiche Anmeldung, abgelehnte Anmeldung, Authentifizierung"
---

**SSH** steht für Secure Shell und ermöglicht die Anmeldung an einem anderen Rechner über das Netzwerk. Der empfangende Rechner kann jeden Versuch protokollieren. Der Eintrag nennt das Konto und gibt an, ob der Server den vorgelegten Nachweis akzeptiert hat.

## Das Ergebnis lesen

Hier sind zwei simulierte SSH-Einträge. Das Feld `login` enthält das Ergebnis. Ein abgelehnter Versuch hat die Anmeldeprüfung nicht bestanden. Ein akzeptierter Versuch war erfolgreich.

```text
t=09:13:48Z source=ssh host=web-01 account=alex login=rejected
t=09:14:02Z source=ssh host=web-01 account=alex login=accepted
```

Der erste Eintrag meldet eine Ablehnung für `alex`. Der zweite meldet einen erfolgreichen Versuch für dasselbe Konto. Jedes Ergebnis bezieht sich auf seinen eigenen Versuch.

:::single-choice{#ssh-login-events-outcome-order} Welche Aussage ergibt sich aus diesen beiden Einträgen?

::option[Der spätere Versuch hat die Anmeldeprüfung bestanden.]{#ssh-login-events-outcome-later .correct explanation="Im zweiten Eintrag steht um 09:14:02 Uhr login=accepted."}
::option[Beide Versuche haben die Anmeldeprüfung bestanden.]{#ssh-login-events-outcome-both explanation="Die frühere Zeile hält eine abgelehnte Anmeldung fest."}
::option[Der spätere Versuch hat die Anmeldeprüfung nicht bestanden.]{#ssh-login-events-outcome-failed explanation="Abgelehnt wurde der erste Versuch. Der zweite wurde akzeptiert."}
:::

## Adressen und Anmeldeverfahren lesen

Die Adresse der Gegenstelle zeigt, woher die Verbindung aus Sicht des empfangenden Rechners kam. Im Beispiel steht sie im Feld `peer`. Mehrere Personen können dieselbe Netzwerkadresse verwenden. Allein aus dem Feld geht nicht hervor, wer sie benutzt hat.

```text
t=09:14:02Z source=ssh host=web-01 account=alex login=accepted
peer=192.0.2.10 method=publickey connection=17
```

Die zweite Zeile gehört noch zum selben Eintrag. Das Feld `method` bezeichnet die Art des Nachweises, den SSH geprüft hat. Bei `password` hat SSH ein Passwort geprüft. Bei `publickey` hat die Gegenstelle nachgewiesen, dass sie einen für dieses Konto akzeptierten Schlüssel verwenden konnte.

:::single-choice{#ssh-login-events-method-evidence} Was lässt sich über den akzeptierten Versuch sagen?

::option[Der Server hat eine Anmeldung mit Passwort akzeptiert.]{#ssh-login-events-method-password explanation="Die Anmeldung per Passwort würde als eigene Methode angezeigt. Hier steht die Methode mit öffentlichem Schlüssel."}
::option[Der Server hat die Person hinter der Adresse identifiziert.]{#ssh-login-events-method-person explanation="Die Adresse beschreibt, wie die Verbindung am Server ankam. Sie zeigt nicht, wer am Rechner saß."}
::option[Der Server hat eine Anmeldung mit Schlüssel akzeptiert.]{#ssh-login-events-method-key .correct explanation="Im Eintrag stehen sowohl login=accepted als auch method=publickey."}
:::

## Versuche nach Verbindung gruppieren

Eine **Verbindung** ist der Netzwerkkanal, über den SSH Nachrichten austauscht. In diesen Beispielen weist der Host jeder Verbindung eine Kennung zu. Über eine Verbindung sind mehrere Anmeldeversuche möglich. Von derselben Adresse kann außerdem eine weitere Verbindung aufgebaut werden.

```text
t=09:13:48Z host=web-01 account=alex peer=192.0.2.10 connection=17 login=rejected
t=09:13:55Z host=web-01 account=alex peer=192.0.2.10 connection=18 login=rejected
t=09:14:02Z host=web-01 account=alex peer=192.0.2.10 connection=17 login=accepted
```

Auf `web-01` gehören die erste und die letzte Zeile zur Verbindung 17. Lies diese Kennung zusammen mit dem Host.

![LabEx-Terminal mit simulierten SSH-Anmeldeversuchen von einer Adresse und den Verbindungs-IDs 17 und 18](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/security-logs/ssh-login-events/ssh-connections.png)

Das Terminal zeigt die drei simulierten Versuche zusammen, damit du ihre Verbindungsnummern vergleichen kannst.

:::single-choice{#ssh-login-events-group-connection} Welche Einträge beziehen sich auf Verbindung 18 auf web-01?

::option[Die Versuche um 09:13:48 und 09:14:02 Uhr.]{#ssh-login-events-group-seventeen explanation="Beide Zeilen gehören zu Verbindung 17."}
::option[Nur der Versuch um 09:13:55 Uhr.]{#ssh-login-events-group-eighteen .correct explanation="Nur diese Zeile zeigt auf web-01 die Verbindung 18."}
::option[Alle drei Versuche von 192.0.2.10.]{#ssh-login-events-group-address explanation="Beide Verbindungsnummern erscheinen unter derselben Adresse."}
:::

## Eine erfolgreiche Anmeldung weiterverfolgen

Eine erfolgreiche Anmeldung zeigt, dass SSH den Nachweis für das Konto akzeptiert hat. Willst du wissen, was danach geschah, suche einen Eintrag über die Eröffnung einer **Sitzung**. Eine Anmeldesitzung erfasst Aktivitäten nach der Anmeldung. Der Eintrag über eine erfolgreiche Anmeldung beschreibt zunächst nur das Ergebnis der Prüfung.

:::single-choice{#ssh-login-events-after-accepted} Welcher Eintrag hilft dir zu prüfen, ob auf eine erfolgreiche Anmeldung eine Sitzung folgte?

::option[Ein weiterer Eintrag, der dieselbe erfolgreiche Anmeldung meldet.]{#ssh-login-events-after-accepted-again explanation="Er wiederholt nur das Ergebnis der Anmeldeprüfung."}
::option[Eine frühere Ablehnung desselben Kontos auf einem anderen Host.]{#ssh-login-events-after-other-host explanation="Das ist ein eigener Versuch auf einem anderen Rechner."}
::option[Ein Eintrag, der die Sitzungseröffnung für diese Anmeldung meldet.]{#ssh-login-events-after-session .correct explanation="Ein solcher Eintrag beschreibt den nächsten Schritt und kann ihn mit der erfolgreichen Anmeldung verknüpfen."}
:::

## Zusammenfassung

Du kannst jetzt das Ergebnis eines SSH-Anmeldeversuchs lesen und zusammengehörige Einträge erkennen.

1. Akzeptierte und abgelehnte Anmeldeversuche unterscheiden.
2. Mit Gegenstellenadresse und Anmeldeverfahren einen Versuch beschreiben.
3. Einträge nach Host und Verbindung gruppieren, wenn eine Kennung vorliegt.
4. In einem Sitzungseintrag nachsehen, was nach erfolgreicher Anmeldung geschah.
