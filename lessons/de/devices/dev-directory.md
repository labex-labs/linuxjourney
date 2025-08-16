---
lang: "de"
title: "/dev-Verzeichnis"
description: "Erfahren Sie mehr über das /dev-Verzeichnis in Linux, wo Gerätedateien gespeichert werden. Verstehen Sie Geräteknoten und wie man mit ihnen interagiert. Erkunden Sie /dev mit ls. Linux-Anfängerhandbuch."
keywords: "/dev-Verzeichnis, Linux-Gerätedateien, Geräteknoten, Linux-Tutorial, ls /dev, Linux-Anfänger, Linux-Handbuch"
---

## Lesson Content

Wenn Sie ein Gerät an Ihren Computer anschließen, benötigt es im Allgemeinen einen Gerätetreiber, um ordnungsgemäß zu funktionieren. Sie können mit Gerätetreibern über Gerätedateien oder Geräteknoten interagieren; dies sind spezielle Dateien, die wie reguläre Dateien aussehen. Da diese Gerätedateien genau wie reguläre Dateien sind, können Sie Programme wie `ls`, `cat` usw. verwenden, um mit ihnen zu interagieren. Diese Gerätedateien werden im Allgemeinen im `/dev`-Verzeichnis gespeichert. Gehen Sie voran und führen Sie `ls` für das `/dev`-Verzeichnis auf Ihrem System aus; Sie werden eine große Anzahl von Gerätedateien sehen, die sich auf Ihrem System befinden.

```bash
ls /dev
```

Einige dieser Geräte haben Sie bereits verwendet und mit ihnen interagiert, wie z.B. `/dev/null`. Erinnern Sie sich, wenn wir die Ausgabe an `/dev/null` senden, weiß der Kernel, dass dieses Gerät alle unsere Eingaben aufnimmt und einfach verwirft, sodass nichts zurückgegeben wird.

Früher, wenn Sie ein Gerät zu Ihrem System hinzufügen wollten, haben Sie die Gerätedatei in `/dev` hinzugefügt und sie dann wahrscheinlich vergessen. Nun, wiederholen Sie das ein paar Mal, und Sie können sehen, wo es ein Problem gab. Das `/dev`-Verzeichnis würde mit statischen Gerätedateien von Geräten überladen werden, die Sie längst aktualisiert, nicht mehr verwendet usw. haben. Geräte werden auch Gerätedateien in der Reihenfolge zugewiesen, in der der Kernel sie findet. Wenn Sie also Ihr System jedes Mal neu starteten, könnten die Geräte je nach Zeitpunkt ihrer Erkennung unterschiedliche Gerätedateien haben.

Zum Glück verwenden wir diese Methode nicht mehr. Jetzt haben wir etwas, das wir verwenden, um Geräte, die derzeit auf dem System verwendet werden, dynamisch hinzuzufügen und zu entfernen, und wir werden dies in den kommenden Lektionen besprechen.

## Exercise

Schauen Sie sich den Inhalt des `/dev`-Verzeichnisses an. Erkennen Sie bekannte Geräte?

## Quiz Question

Wo werden Gerätedateien auf dem System gespeichert?

## Quiz Answer

/dev
