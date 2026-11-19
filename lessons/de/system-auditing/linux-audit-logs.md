---
lesson_id: "linux-audit-logs"
course_id: "system-auditing"
lang: "de"
order_index: 2
title: "Linux-Auditprotokolle"
description: "Lerne, Linux-Auditdatensätze zusammenzuführen, die zu demselben aufgezeichneten Vorgang gehören."
meta_title: "Linux-Auditprotokolle - Systemaudit"
meta_description: "Lerne, Linux-Auditdatensätze zusammenzuführen, die zu demselben aufgezeichneten Vorgang gehören."
meta_keywords: "Linux-Auditprotokolle, Systemaudit, Cybersicherheit, Linux Journey"
---

Linux Audit kann zu einem Ereignis mehrere Datensätze schreiben. Eine Zeile kann den Vorgang beschreiben und eine andere den Pfad angeben. Stelle die zugehörigen Zeilen zusammen, bevor du sie auswertest.

## Zusammengehörige Ereignisdaten lesen

Die folgenden Werte sind gekürzte Übungsdatensätze vom selben Host und Datum. Die Zahl nach dem Doppelpunkt in der Audit-Ereignisreferenz hilft, Datensätze mit demselben Zeitstempel und derselben Ereignis-ID zusammenzuführen. Beide Zeilen gehören zum selben Ereignis.

```text
type=SYSCALL msg=audit(1763456400.120:42) success=yes auid=1001 euid=0
type=PATH    msg=audit(1763456400.120:42) name="/etc/journey/site.conf"
```

Die erste Zeile nennt das Ergebnis und die Kontodaten. Die Pfadzeile nennt eine Datei, die zum Ereignis gehört.

:::single-choice{#linux-audit-logs-group-rows} Mit welchen Angaben ordnest du in diesem Beispiel den Vorgang dem Pfad zu?

::option[Allein mit den Datensatztypen SYSCALL und PATH.]{#linux-audit-logs-group-rows-a explanation="Die Typen beschreiben, wozu die jeweilige Zeile dient. Viele Ereignisse können dieselben Typen enthalten."}
::option[Damit, dass beide Zeilen mit type beginnen.]{#linux-audit-logs-group-rows-c explanation="Zeilen können einen Typ angeben und trotzdem zu verschiedenen Ereignissen gehören."}
::option[Mit der übereinstimmenden Audit-Ereignisreferenz auf demselben Host.]{#linux-audit-logs-group-rows-b .correct explanation="Sie verbindet die Zeilen, die das Ereignis 42 beschreiben."}
:::

![Simulierte SYSCALL- und PATH-Zeilen von Linux Audit mit derselben Ereignisreferenz](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/system-auditing/linux-audit-logs/grouped-event.png)

## Zwei Identitäten ablesen

In diesem Beispiel ist `auid` die Audit-Benutzer-ID der Anmeldung und `euid` die effektive Benutzer-ID für den Vorgang. Ein Programm kann mit einer anderen effektiven Identität laufen als der, mit der sich jemand angemeldet hat. Eine numerische ID bezeichnet ein Konto auf dem Host. Um die Person dahinter zu bestimmen, können weitere Aufzeichnungen nötig sein.

:::single-choice{#linux-audit-logs-identify-login} Welches Feld zeigt die Audit-Identität der Anmeldung?

::option[Das Feld euid mit dem Wert 0.]{#linux-audit-logs-identify-login-b explanation="Es zeigt die effektive Identität des Programms für das Ereignis."}
::option[Das Feld auid mit dem Wert 1001.]{#linux-audit-logs-identify-login-a .correct explanation="Auid bezeichnet die Audit-Benutzer-ID der Anmeldung, euid die effektive Identität."}
::option[Die Ereignisnummer 42.]{#linux-audit-logs-identify-login-c explanation="Die Nummer fasst Datensätze zusammen und hat mit den Kontoidentitäten nichts zu tun."}
:::

## Den Befund eingrenzen

Das Ergebnisfeld meldet, dass der aufgezeichnete Vorgang erfolgreich war. Lies das vollständige Ereignis, um den Vorgang zu bestimmen. Vergleiche die Datei mit einer bekannten Referenz, wenn du prüfen willst, ob sich ihr Inhalt geändert hat.

:::single-choice{#linux-audit-logs-useful-follow-up} Was hilft dir festzustellen, ob der Inhalt von der genehmigten Datei abweicht?

::option[Ein Vergleich mit einer genehmigten Referenzkopie oder einem Integritätsnachweis.]{#linux-audit-logs-useful-follow-up-c .correct explanation="Damit lässt sich zeigen, was sich an der Datei geändert hat."}
::option[Ein zweiter Audit-Eintrag über einen weiteren erfolgreichen Vorgang.]{#linux-audit-logs-useful-follow-up-a explanation="Das kann einen weiteren aufgezeichneten Vorgang belegen. Die aktuellen Bytes der Datei werden dabei nicht mit der genehmigten Kopie verglichen."}
::option[Die Konto-ID der Anmeldung aus demselben Ereignis.]{#linux-audit-logs-useful-follow-up-b explanation="Sie gibt Aufschluss über das verwendete Konto. Über geänderte Bytes sagt sie nichts aus."}
:::

## Zusammenfassung

Du kannst jetzt die zusammengehörigen Datensätze eines einzelnen Audit-Ereignisses lesen.

1. Ordne die Datensätze anhand von Host und Audit-Ereignisreferenz einander zu.
2. Lies Anmeldeidentität und effektive Identität einzeln ab.
3. Wähle eine Folgeprüfung, wenn das aufgezeichnete Ergebnis eine Frage offenlässt.
