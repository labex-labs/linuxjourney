---
index: 9
lang: "de"
title: "Festplattennutzung"
meta_title: "Festplattennutzung - Das Dateisystem"
meta_description: "Erfahren Sie, wie Sie die Festplattennutzung und den freien Speicherplatz unter Linux mit den Befehlen df und du überprüfen. Verstehen Sie ihre Unterschiede und wann Sie welchen verwenden sollten. Linux-Festplattenverwaltungs-Tutorial."
meta_keywords: "df Befehl, du Befehl, Linux Festplattennutzung, freien Speicherplatz prüfen, Linux Tutorial, Linux für Anfänger, Festplattenverwaltung, Linux Anleitung"
---

## Lesson Content

Es gibt einige Tools, mit denen Sie die Auslastung Ihrer Festplatten überprüfen können:

```bash
pete@icebox:~$ df -h
Filesystem     1K-blocks    Used Available Use% Mounted on
/dev/sda1       6.2G  2.3G  3.6G  40% /
```

Der Befehl `df` zeigt Ihnen die Auslastung Ihrer aktuell gemounteten Dateisysteme an. Das Flag `-h` liefert ein menschenlesbares Format. Sie können sehen, welches Gerät es ist und wie viel Kapazität belegt und verfügbar ist.

Angenommen, Ihre Festplatte wird voll und Sie möchten wissen, welche Dateien oder Verzeichnisse diesen Speicherplatz belegen; dafür können Sie den Befehl **du** verwenden.

```bash
du -h
```

Dies zeigt Ihnen die Festplattennutzung des aktuellen Verzeichnisses, in dem Sie sich befinden. Sie können mit `du -h /` einen Blick in das Stammverzeichnis werfen, aber das kann etwas unübersichtlich werden.

Beide Befehle sind sich in der Syntax so ähnlich, dass es schwierig sein kann, sich zu merken, welchen man verwenden soll. Um zu überprüfen, wie viel Speicherplatz auf Ihrer **Festplatte** **frei** ist, verwenden Sie `df`. Um die **Festplattennutzung** zu überprüfen, verwenden Sie `du`.

## Exercise

Übung macht den Meister! Hier sind einige praktische Labs, um Ihr Verständnis der Festplattenverwaltung und -nutzung unter Linux zu vertiefen:

1. **[Linux-Partitionen und Dateisysteme verwalten](https://labex.io/de/labs/comptia-manage-linux-partitions-and-filesystems-590845)** – Üben Sie das Erstellen, Formatieren und Mounten von Dateisystemen, die die zugrunde liegenden Strukturen sind, die von `df` und `du` gemeldet werden.
2. **[Eine Swap-Datei in Linux erstellen und aktivieren](https://labex.io/de/labs/comptia-create-and-activate-a-swap-file-in-linux-590858)** – Lernen Sie, den virtuellen Speicher auf der Festplatte zu verwalten, ein kritischer Aspekt der Systemressourcenverwaltung, der den Festplattenspeicher beeinflusst.

Diese Labs helfen Ihnen, die Konzepte in realen Szenarien anzuwenden und Vertrauen in die Verwaltung von Festplattenressourcen aufzubauen.

## Quiz Question

Welcher Befehl wird verwendet, um anzuzeigen, wie viel Speicherplatz auf Ihrer Festplatte frei ist?

## Quiz Answer

df
