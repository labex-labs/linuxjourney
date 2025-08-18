---
lang: "de"
title: "Kernel-Protokollierung"
meta_description: "Erfahren Sie mehr über die Linux-Kernel-Protokollierung mit dmesg und kern.log. Verstehen Sie Boot-Meldungen und Hardware-Probleme. Erkunden Sie Kernel-Protokolle für Systemeinblicke."
meta_keywords: "dmesg, kern.log, Linux-Protokollierung, Kernel-Meldungen, Boot-Protokoll, Linux-Tutorial, Anfängerleitfaden"
---

## Lesson Content

### /var/log/dmesg

Beim Booten protokolliert Ihr System Informationen über den Kernel-Ringpuffer. Dies zeigt uns unter anderem Informationen über Hardware-Treiber, Kernel-Informationen und den Status während des Bootvorgangs. Diese Protokolldatei befindet sich unter `/var/log/dmesg` und wird bei jedem Bootvorgang zurückgesetzt. Sie sehen vielleicht jetzt keinen Nutzen darin, aber wenn Sie jemals Probleme mit etwas während des Bootvorgangs oder ein Hardwareproblem hätten, ist `dmesg` der beste Ort, um nachzusehen. Sie können dieses Protokoll auch mit dem Befehl `dmesg` anzeigen.

### /var/log/kern.log

Ein weiteres Protokoll, das Sie zur Anzeige von Kernel-Informationen verwenden können, ist die Datei `/var/log/kern.log`. Diese protokolliert Kernel-Informationen und -Ereignisse auf Ihrem System; sie protokolliert auch die `dmesg`-Ausgabe.

## Exercise

Look at your `dmesg` and `kern` logs. What differences do you notice?

## Quiz Question

Welcher Befehl kann verwendet werden, um Kernel-Bootmeldungen anzuzeigen?

## Quiz Answer

dmesg
