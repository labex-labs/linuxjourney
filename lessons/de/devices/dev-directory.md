---
index: 1
lang: "de"
title: "/dev-Verzeichnis"
meta_title: "/dev-Verzeichnis - Geräte"
meta_description: "Erfahren Sie mehr über das /dev-Verzeichnis in Linux, wo Gerätedateien gespeichert werden. Verstehen Sie Geräteknoten und wie Sie mit ihnen interagieren können. Erkunden Sie /dev mit ls. Linux-Anfängerhandbuch."
meta_keywords: "/dev-Verzeichnis, Linux-Gerätedateien, Geräteknoten, Linux-Tutorial, ls /dev, Linux-Anfänger, Linux-Handbuch"
---

## Lesson Content

Wenn Sie ein Gerät an Ihren Computer anschließen, benötigt es im Allgemeinen einen Gerätetreiber, um ordnungsgemäß zu funktionieren. Sie können mit Gerätetreibern über Gerätedateien oder Geräteknoten interagieren; dies sind spezielle Dateien, die wie reguläre Dateien aussehen. Da diese Gerätedateien genau wie reguläre Dateien sind, können Sie Programme wie `ls`, `cat` usw. verwenden, um mit ihnen zu interagieren. Diese Gerätedateien werden im Allgemeinen im Verzeichnis `/dev` gespeichert. Führen Sie ein `ls` des `/dev`-Verzeichnisses auf Ihrem System aus; Sie werden eine große Anzahl von Gerätedateien sehen, die sich auf Ihrem System befinden.

```bash
ls /dev
```

Einige dieser Geräte haben Sie bereits verwendet und mit ihnen interagiert, wie zum Beispiel `/dev/null`. Erinnern Sie sich, als wir die Ausgabe an `/dev/null` gesendet haben, wusste der Kernel, dass dieses Gerät all unsere Eingaben aufnimmt und einfach verwirft, sodass nichts zurückgegeben wird.

Früher, wenn Sie ein Gerät zu Ihrem System hinzufügen wollten, haben Sie die Gerätedatei in `/dev` hinzugefügt und sie dann wahrscheinlich vergessen. Nun, wiederholen Sie das ein paar Mal, und Sie können sehen, wo es ein Problem gab. Das `/dev`-Verzeichnis würde mit statischen Gerätedateien von Geräten überladen werden, die Sie längst aktualisiert, nicht mehr verwendet usw. haben. Geräte werden auch Gerätedateien in der Reihenfolge zugewiesen, in der der Kernel sie findet. Wenn Sie also jedes Mal, wenn Sie Ihr System neu starteten, die Geräte unterschiedliche Gerätedateien haben könnten, je nachdem, wann sie entdeckt wurden.

Glücklicherweise verwenden wir diese Methode nicht mehr. Jetzt haben wir etwas, das wir verwenden, um Geräte, die derzeit auf dem System verwendet werden, dynamisch hinzuzufügen und zu entfernen, und wir werden dies in den kommenden Lektionen besprechen.

## Exercise

Übung macht den Meister! Hier sind einige praktische Übungen, um Ihr Verständnis von Hardwaregeräten und deren Interaktion mit dem Linux-System zu vertiefen:

1. **[Hardwaregeräte in Linux erkunden](https://labex.io/de/labs/comptia-explore-hardware-devices-in-linux-590861)** – In diesem Lab lernen Sie die wesentlichen Fähigkeiten, um Hardwaregeräte in einer Linux-Umgebung zu erkunden, zu identifizieren und zu inspizieren. Sie sammeln praktische Erfahrungen mit leistungsstarken Befehlszeilenprogrammen, um zu verstehen, wie das Betriebssystem mit physischen Komponenten interagiert.

Dieses Lab hilft Ihnen, die Konzepte der Geräteinteraktion in realen Szenarien anzuwenden und Vertrauen im Umgang mit Hardware in Linux aufzubauen.

## Quiz Question

Wo werden Gerätedateien auf dem System gespeichert?

## Quiz Answer

/dev
