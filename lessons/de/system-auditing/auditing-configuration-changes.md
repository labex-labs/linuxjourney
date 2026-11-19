---
lesson_id: "auditing-configuration-changes"
course_id: "system-auditing"
lang: "de"
order_index: 5
title: "Konfigurationsänderungen"
description: "Lerne, eine genehmigte Änderung mit einem Dateiabweichungsbericht und einem Audit-Ereignis abzugleichen."
meta_title: "Konfigurationsänderungen - Systemaudit"
meta_description: "Lerne, eine genehmigte Änderung mit einem Dateiabweichungsbericht und einem Audit-Ereignis abzugleichen."
meta_keywords: "Konfigurationsänderungen, Systemaudit, Cybersicherheit, Linux Journey"
---

Ein Änderungsticket hält fest, was geplant ist. Ein Dateivergleich zeigt, was sich inzwischen unterscheidet. Ein Audit-Ereignis beschreibt eine Aktion, die das Auditsystem erfasst hat. Ziehe alle drei Quellen heran, um festzustellen, welche Aussagen über eine Konfigurationsänderung möglich sind.

## Geplante Änderung abgleichen

Lies diesen simulierten Wartungseintrag.

```text
Approved: change banner.txt mode to 640
Window: 09:00–09:30 UTC
Host: web-01
```

Darin steht, welche Datei und welche Eigenschaft geändert werden durften. Eine Abweichung an anderer Stelle muss eigens erklärt werden, auch wenn sie im selben Zeitfenster auftritt.

:::single-choice{#auditing-configuration-changes-approve-scope} Welche Änderung entspricht der beschriebenen Freigabe?

::option[Der Inhalt von site.conf hat sich auf web-01 geändert.]{#auditing-configuration-changes-approve-scope-b explanation="Diese Konfigurationsdatei fällt nicht unter die Freigabe."}
::option[Die Datei banner.txt ist auf einem anderen Host verschwunden.]{#auditing-configuration-changes-approve-scope-c explanation="Sowohl die beobachtete Aktion als auch der Host weichen ab."}
::option[Die Zugriffsrechte von banner.txt wurden auf web-01 auf 640 geändert.]{#auditing-configuration-changes-approve-scope-a .correct explanation="Datei, Eigenschaft, Host und Ergebnis stimmen mit dem genehmigten Eintrag überein."}
:::

## Beobachtungen vergleichen

Ein Vergleich zeigt, dass sich die Zugriffsrechte der Bannerdatei und der Inhalt von `site.conf` geändert haben. Ein separates Audit-Ereignis verzeichnet um 09:15 Uhr einen Schreibzugriff auf `site.conf` auf `web-01`. Damit hast du eine Uhrzeit für die weitere Untersuchung. Ob der Zugriff genehmigt war, geht daraus nicht hervor.

:::single-choice{#auditing-configuration-changes-source-comparison} Welcher Schluss ergibt sich aus den beiden Beobachtungen zu site.conf?

::option[Der Schreibzugriff war genehmigt, weil er in das Zeitfenster fällt.]{#auditing-configuration-changes-source-comparison-a explanation="Das Ticket nennt eine andere Aktion."}
::option[Der aufgezeichnete Schreibzugriff und der geänderte Inhalt geben Anlass, die Datei zu prüfen.]{#auditing-configuration-changes-source-comparison-b .correct explanation="Der Vergleich zeigt die Abweichung und das Audit-Ereignis grenzt den Zeitpunkt ein."}
::option[Die Änderung an der Bannerdatei hat den Schreibzugriff verursacht.]{#auditing-configuration-changes-source-comparison-c explanation="Die Beobachtungen belegen keinen ursächlichen Zusammenhang."}
:::

## Einen Prüfvermerk schreiben

Halte fest, welche Abweichung dem Plan entspricht und welche ungeklärt bleibt. Nenne Datei, Host, Uhrzeit und Quelle. Vergleiche als Nächstes die aktuelle Konfiguration mit der genehmigten Kopie und prüfe, ob die Änderung unter eine andere Freigabe fällt.

:::single-choice{#auditing-configuration-changes-useful-review} Was sollte bei der Übergabe zu site.conf stehen?

::option[Nenne die Abweichung, verweise auf den beobachteten Schreibzugriff und frage nach der zugehörigen Freigabe.]{#auditing-configuration-changes-useful-review-c .correct explanation="So bleiben die Belege und die noch offene Frage erhalten."}
::option[Markiere die Änderung als genehmigt und lass den Pfad weg.]{#auditing-configuration-changes-useful-review-a explanation="So geht das Ziel der Aktion verloren und du setzt eine Freigabe voraus, die aus den Aufzeichnungen nicht hervorgeht."}
::option[Schreibe sie der Person zu, die für die Banneränderung zuständig ist.]{#auditing-configuration-changes-useful-review-b explanation="Die Aufzeichnungen belegen diese Zuordnung nicht."}
:::

## Zwei Wartungseinträge vergleichen

Ein anderes Ticket genehmigt eine spätere Bearbeitung von site.conf. Vergleiche die beobachtete Uhrzeit, den Zielhost und die Datei mit dem Ticket, bevor du die Prüfung abschließt. Eine genehmigte Änderung an der richtigen Datei kann ein früheres Ereignis offenlassen.

:::single-choice{#auditing-configuration-changes-final-application} Das Ticket gilt für site.conf auf web-01 von 09:40 bis 10:00 Uhr. Welche Frage bleibt beim Schreibzugriff um 09:15 Uhr offen?

::option[Ob site.conf außerhalb des Ticketsystems existiert.]{#auditing-configuration-changes-final-application-b explanation="Die Konfigurationsdatei wurde bereits beim Dateivergleich erfasst."}
::option[Ob das spätere Ticket automatisch jeden früheren Schreibzugriff erklärt.]{#auditing-configuration-changes-final-application-c explanation="Die Freigabe gilt für die angegebene Aktion und Zeit."}
::option[Ob eine separate Freigabe den früheren Schreibzugriff abdeckt.]{#auditing-configuration-changes-final-application-a .correct explanation="Host und Pfad stimmen überein, aber die aufgezeichnete Uhrzeit liegt außerhalb des genehmigten Zeitfensters."}
:::

## Zusammenfassung

Du kannst jetzt nachvollziehen, was über eine Konfigurationsänderung bekannt ist.

1. Lies aus der Freigabe ab, welche Änderung vorgesehen war.
2. Beschreibe mithilfe von Vergleichen und Audit-Ereignissen, was beobachtet wurde.
3. Erkläre, welche Belege fehlen, und wähle die nächste Prüfung.
