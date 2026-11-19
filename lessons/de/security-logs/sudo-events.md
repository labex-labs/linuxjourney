---
lesson_id: "sudo-events"
course_id: "security-logs"
lang: "de"
order_index: 3
title: "sudo-Ereignisse"
description: "Lerne, aus sudo-Protokollen abzulesen, wer einen Befehl angefordert hat, unter welchem Konto er laufen sollte und ob die Anfrage erlaubt war."
meta_title: "sudo-Ereignisse – Sicherheitsprotokolle"
meta_description: "Unterscheide in sudo-Einträgen das anfragende Konto, das Zielkonto, den Befehl und die Entscheidung über die Berechtigung."
meta_keywords: "sudo-Ereignisse, sudo-Protokolle, sudo-Berechtigung, Zielkonto, Linux-Berechtigungen"
---

Jemand meldet sich mit einem gewöhnlichen Konto an und muss später eine Aufgabe erledigen, die mehr Rechte erfordert. Auf einem System mit `sudo` kann die Person anfragen, ob sie einen Befehl unter einem anderen Konto ausführen darf. Der Eintrag dazu kann zeigen, welche Berechtigung angefragt wurde und wie das System entschieden hat.

## Die beiden Konten erkennen

In den simulierten Einträgen bezeichnet `account` das Konto, das die Anfrage gestellt hat, und `target` das Konto, unter dem der Befehl laufen soll. Das Konto `root` hat Administrationsrechte. Eine Anfrage mit `sudo` kann auch ein anderes Zielkonto wie `backup` nennen.

```text
t=09:15:10Z source=sudo host=web-01 account=alex target=root
command=systemctl status nginx decision=allowed session=42
```

Die zweite Zeile setzt denselben Eintrag fort. Hier hat `alex` angefragt, den Befehl als `root` auszuführen.

:::single-choice{#sudo-events-account-target} Welches Konto hat bei `account=sam target=backup` die Anfrage gestellt und als welches Konto soll der Befehl laufen?

::option[Backup stellte die Anfrage, um den Befehl als sam auszuführen.]{#sudo-events-target-swapped explanation="Account nennt das anfragende Konto und target die gewünschte Identität für den Befehl."}
::option[Sam stellte die Anfrage, um den Befehl als backup auszuführen.]{#sudo-events-target-backup .correct explanation="Account ist das anfragende Konto. Target nennt das Konto, unter dem der Befehl laufen soll."}
::option[Sam stellte die Anfrage, um den Befehl als root auszuführen.]{#sudo-events-target-root explanation="Root ist ein mögliches Zielkonto. In diesem Eintrag steht backup."}
:::

## Den angefragten Befehl lesen

Das Feld `command` nennt den Befehl, auf den sich die Anfrage bezieht. `systemctl status nginx` fragt im Beispiel den Zustand des Nginx-Webdiensts ab. Ein anderer Eintrag könnte `systemctl restart nginx` enthalten. Dieser Befehl soll den Dienst anhalten und erneut starten. Beide Befehle nennen denselben Dienst, verlangen aber unterschiedliche Aktionen.

:::single-choice{#sudo-events-command-scope} Welche Anfrage soll den Betriebszustand des Webdiensts ändern?

::option[`systemctl restart nginx`]{#sudo-events-command-restart .correct explanation="Restart fordert an, den Dienst anzuhalten und erneut zu starten. Das kann seinen Zustand ändern."}
::option[`systemctl status nginx`]{#sudo-events-command-status explanation="Status fragt Informationen zum Dienst ab und fordert keinen Neustart an."}
::option[Beide Anfragen, weil sie nginx nennen.]{#sudo-events-command-both explanation="Der Dienstname ist gleich. An der Aktion erkennst du, was angefragt wurde."}
:::

## Die Entscheidung lesen

Die **Richtlinie** ist der Regelsatz, nach dem `sudo` eine Anfrage erlaubt oder verweigert. In diesen Beispielen bedeutet `decision=allowed`, dass die Richtlinie die Anfrage zulässt. Bei `decision=denied` wurde sie von `sudo` abgelehnt.

```text
t=09:16:00Z source=sudo host=web-01 account=alex target=root
command=systemctl restart nginx decision=denied session=42
```

Eine Erlaubnis sagt etwas über Berechtigungen aus. Wenn du wissen willst, wie der Befehl ausgegangen ist, suche nach einem Ergebniseintrag, sofern das System einen bereitstellt.

![LabEx-Terminal mit simulierten sudo-Einträgen für eine erlaubte Statusabfrage und einen verweigerten Neustart](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/security-logs/sudo-events/sudo-decisions.png)

Vergleiche in diesen beiden Beispielen die angefragten Befehle mit den jeweiligen Entscheidungen.

:::single-choice{#sudo-events-denied-request} Was steht im zweiten Beispiel zur Neustartanfrage?

::option[Sudo hat die Neustartanfrage abgelehnt.]{#sudo-events-denied-refused .correct explanation="Der Befehl nennt die gewünschte Aktion. Denied zeigt, dass sie nicht erlaubt wurde."}
::option[Der Dienst wurde erfolgreich neu gestartet.]{#sudo-events-denied-success explanation="Dieser Eintrag zeigt eine Ablehnung und belegt keinen erfolgreichen Neustart."}
::option[Die frühere Statusabfrage wurde ebenfalls abgelehnt.]{#sudo-events-denied-earlier explanation="Jede Entscheidung gilt für ihre eigene Anfrage. Im früheren Eintrag steht allowed."}
:::

## Das Anmeldekonto im Blick behalten

Beide Beispiele nennen `alex` als anfragendes Konto und enthalten `session=42`. Die Nummer bezeichnet die Anmeldesitzung, also die Aktivität nach dem Anmelden. Damit kannst du die zugehörigen Anmeldeeinträge suchen. Das Zielkonto gilt jeweils für diese eine Befehlsanfrage. Gib beim Beschreiben beide Konten an.

:::single-choice{#sudo-events-session-interpretation} Welche Zusammenfassung passt zum ersten Beispiel?

::option[Root hat sich direkt angemeldet und Sitzung 42 eröffnet.]{#sudo-events-session-root-login explanation="Hier geht es um sudo. Das Zielkonto beschreibt keine separate Anmeldung."}
::option[Alex hat für alle Befehle in der Sitzung Root-Rechte angefragt.]{#sudo-events-session-all-commands explanation="Der Eintrag nennt einen bestimmten Befehl und erfasst nicht alle Befehle der Sitzung."}
::option[Alex hat in Sitzung 42 angefragt, einen bestimmten Befehl als root auszuführen.]{#sudo-events-session-one-command .correct explanation="Diese Aussage stützt sich auf das anfragende Konto, das Zielkonto, den Befehl und die Sitzungs-ID."}
:::

## Zusammenfassung

Du kannst jetzt einen sudo-Eintrag lesen und zwischen der Berechtigung und dem Ergebnis des Befehls unterscheiden.

1. Anfragendes Konto und Zielkonto erkennen.
2. Die konkrete Anfrage mithilfe des Befehlsfelds beschreiben.
3. Erlaubte und verweigerte Anfragen unterscheiden.
4. Bei der Beschreibung einer Anfrage die Anmeldesitzung berücksichtigen.
