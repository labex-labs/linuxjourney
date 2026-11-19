---
lesson_id: "host-file-integrity"
course_id: "system-auditing"
lang: "de"
order_index: 3
title: "Dateiintegrität"
description: "Lerne, Inhalt und Zugriffsrechte einer Datei anhand eines Hashwerts und ihrer Metadaten zu vergleichen."
meta_title: "Dateiintegrität - Systemaudit"
meta_description: "Lerne, Inhalt und Zugriffsrechte einer Datei anhand eines Hashwerts und ihrer Metadaten zu vergleichen."
meta_keywords: "Dateiintegrität, Hashwert, Systemaudit, Cybersicherheit, Linux Journey"
---

Bei einer Integritätsprüfung stellst du fest, ob eine Datei noch einer Referenz entspricht. Prüfe Inhalt und Metadaten einzeln. Der Inhalt besteht aus den Bytes in der Datei. Zu den **Metadaten** gehören Angaben wie die Zugriffsrechte.

## Einen Hashwert des Inhalts festhalten

Erstelle in einem leeren Übungsverzeichnis eine kleine Konfigurationsdatei. Die Umleitung überschreibt eine vorhandene Datei mit demselben Namen. Verwende daher ein neues Verzeichnis.

```bash
$ printf '%s\n' 'mode=preview' > site.conf
$ sha256sum site.conf
```

Das erste Feld enthält den **Hashwert**, einen Wert fester Länge, der aus den Bytes der Datei berechnet wird. Wende später dieselbe Methode auf dieselbe Datei an. Ein veränderter Hashwert weist auf andere Eingabedaten hin.

:::single-choice{#host-file-integrity-changed-hash} Der SHA-256-Wert ändert sich, nachdem die Datei bearbeitet wurde. Was zeigt der Vergleich?

::option[Der Inhalt weicht von den zuvor geprüften Bytes ab.]{#host-file-integrity-changed-hash-a .correct explanation="Der Hashwert ändert sich mit dem Inhalt, aus dem er berechnet wird."}
::option[Die Bearbeitung war zwangsläufig unbefugt.]{#host-file-integrity-changed-hash-b explanation="Ob es eine Freigabe gab, ist eine eigene Frage."}
::option[Die Rechte eines Kontos haben sich definitiv geändert.]{#host-file-integrity-changed-hash-c explanation="Ein Hashwert des Inhalts erfasst keine Zugriffsrechte."}
:::

## Die Zugriffsrechte festhalten

Unter Linux gibt `stat -c` ausgewählte Metadaten aus. Das Feld `%a` zeigt die Zugriffsrechte als Zahl und `%n` zeigt den Namen.

```bash
$ stat -c '%a %n' site.conf
```

Die anfänglichen Zugriffsrechte können davon abhängen, wie die Datei angelegt wurde. Halte sie zusammen mit dem Hashwert fest, damit du beide Eigenschaften später vergleichen kannst.

:::single-choice{#host-file-integrity-mode-vs-content} Der Hashwert stimmt mit der Referenz überein und stat meldet andere Zugriffsrechte. Was hat sich laut diesen Prüfungen geändert?

::option[Der Inhalt hat sich geändert und die Zugriffsrechte sind gleich geblieben.]{#host-file-integrity-mode-vs-content-a explanation="Der Hashwert stimmt überein und die Zugriffsrechte weichen ab."}
::option[Die Datei wurde zwangsläufig gelöscht.]{#host-file-integrity-mode-vs-content-c explanation="Beide Prüfungen haben Angaben zur Datei geliefert."}
::option[Die Zugriffsrechte haben sich geändert und der gemessene Hashwert des Inhalts ist gleich geblieben.]{#host-file-integrity-mode-vs-content-b .correct explanation="Die beiden Werkzeuge prüfen unterschiedliche Eigenschaften."}
:::

## Geänderte Zugriffsrechte testen

Der nächste Befehl setzt die Zugriffsrechte dieser Übungsdatei auf `640`. Der Eigentümer erhält Lese- und Schreibrechte und die Gruppe erhält Leserechte. Führe beide Prüfungen erneut aus und vergleiche die Ergebnisse.

```bash
$ chmod 640 site.conf
$ stat -c '%a %n' site.conf
$ sha256sum site.conf
```

Die Zugriffsrechte sollten als 640 angezeigt werden. Der Hashwert des Inhalts sollte mit der ersten Messung übereinstimmen.

:::single-choice{#host-file-integrity-repeat-check} Welche Prüfung würde eine spätere Änderung an mode=preview in der Datei erkennen?

::option[Nur der von stat angezeigte Dateiname.]{#host-file-integrity-repeat-check-a explanation="Der Name kann nach der Bearbeitung gleich bleiben."}
::option[Eine neue SHA-256-Prüfung im Vergleich zum ursprünglichen Wert.]{#host-file-integrity-repeat-check-c .correct explanation="Ein geänderter Inhalt würde einen anderen Hashwert ergeben."}
::option[Nur die Ziffer für die Rechte des Eigentümers.]{#host-file-integrity-repeat-check-b explanation="Die Zugriffsrechte bleiben bei den meisten Änderungen am Inhalt gleich."}
:::

![Aufgezeichnete LabEx-Ausgabe mit Zugriffsrechten, die auf 640 geändert wurden, und unverändertem Hashwert](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/system-auditing/host-file-integrity/mode-vs-content.png)

## Zusammenfassung

Du kannst jetzt Dateiinhalt und Zugriffsrechte unabhängig voneinander vergleichen.

1. Halte den SHA-256-Hashwert des Inhalts fest.
2. Lies die Zugriffsrechte mit stat aus.
3. Prüfe, wie sich eine Änderung der Zugriffsrechte auswirkt.
