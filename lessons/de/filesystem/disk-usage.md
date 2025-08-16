---
lang: "de"
title: "Festplattennutzung"
description: "Erfahren Sie, wie Sie die Festplattennutzung und den freien Speicherplatz in Linux mit den Befehlen df und du überprüfen. Verstehen Sie deren Unterschiede und wann Sie welchen verwenden sollten. Linux-Festplattenverwaltungstutorial."
keywords: "df command, du command, Linux Festplattennutzung, freien Speicherplatz überprüfen, Linux Tutorial, Linux für Anfänger, Festplattenverwaltung, Linux Anleitung"
---

## Lesson Content

Es gibt einige Tools, mit denen Sie die Auslastung Ihrer Festplatten überprüfen können:

```bash
pete@icebox:~$ df -h
Filesystem     1K-blocks    Used Available Use% Mounted on
/dev/sda1       6.2G  2.3G  3.6G  40% /
```

Der Befehl `df` zeigt Ihnen die Auslastung Ihrer aktuell gemounteten Dateisysteme. Das Flag `-h` liefert ein menschenlesbares Format. Sie können sehen, welches Gerät es ist und wie viel Kapazität belegt und verfügbar ist.

Nehmen wir an, Ihre Festplatte wird voll und Sie möchten wissen, welche Dateien oder Verzeichnisse diesen Speicherplatz belegen; dafür können Sie den Befehl **du** verwenden.

```bash
du -h
```

Dies zeigt Ihnen die Speicherbelegung des aktuellen Verzeichnisses, in dem Sie sich befinden. Sie können mit `du -h /` einen Blick auf das Root-Verzeichnis werfen, aber das kann etwas unübersichtlich werden.

Beide Befehle sind sich in der Syntax so ähnlich, dass es schwierig sein kann, sich zu merken, welchen man verwenden soll. Um zu überprüfen, wie viel Speicherplatz auf Ihrer **Festplatte** **frei** ist, verwenden Sie `df`. Um die **Speicherbelegung** zu überprüfen, verwenden Sie `du`.

## Exercise

Überprüfen Sie Ihre Speicherbelegung und den freien Speicherplatz sowohl mit `du` als auch mit `df`.

## Quiz Question

Welcher Befehl wird verwendet, um anzuzeigen, wie viel Speicherplatz auf Ihrer Festplatte frei ist?

## Quiz Answer

df
