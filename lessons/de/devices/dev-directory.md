---
index: 1
lang: "de"
title: "/dev-Verzeichnis"
meta_title: "/dev-Verzeichnis - Geräte"
meta_description: "Entdecken Sie den Zweck des /dev-Verzeichnisses unter Linux. Dieser Leitfaden erklärt, was der dev-Ordner ist, wie man ihn mit `ls /dev` erkundet und welche Rolle Geräte-Dateien für die Systemhardware spielen."
meta_keywords: "dev in linux, /dev verzeichnis linux, dev ordner linux, ls /dev, dev befehl linux, geräte dateien, geräte knoten, linux geräte"
---

## Lesson Content

In Linux wird jedes Gerät, das an Ihr System angeschlossen ist, von Festplatten bis hin zu Tastaturen, durch eine spezielle Datei dargestellt. Diese Dateien, bekannt als Gerätedateien oder Geräteknoten, bieten eine Möglichkeit für Software, mit den Hardwaretreibern zu interagieren. Der zentrale Ort für diese Dateien ist das Verzeichnis `/dev`.

### Was ist das /dev-Verzeichnis in Linux?

Das `/dev`-Verzeichnis ist ein grundlegender Bestandteil der Linux-Dateisystemhierarchie. Es enthält die speziellen Dateien, die Geräte repräsentieren. Da diese wie normale Dateien behandelt werden, können Sie Standard-Befehlszeilen-Dienstprogramme verwenden, um mit ihnen zu interagieren. Sie können beispielsweise den Befehl `ls /dev` verwenden, um eine Liste aller derzeit auf Ihrem System vorhandenen Gerätedateien anzuzeigen.

```bash
ls /dev
```

Die Ausführung von `ls /dev` zeigt eine große Anzahl von Einträgen an, die jeweils einem vom Kernel erkannten Hardwareteil oder einem virtuellen Gerät entsprechen.

### Interaktion mit Gerätedateien

Sie haben wahrscheinlich bereits mit einer Gerätedatei interagiert, auch wenn Sie es nicht bemerkt haben. Ein häufiges Beispiel für ein virtuelles Gerät ist `/dev/null`. Wenn Sie die Ausgabe eines Befehls nach `/dev/null` umleiten, senden Sie sie an ein spezielles Gerät, von dem der Kernel angewiesen ist, alle Eingaben einfach zu verwerfen.

Obwohl Sie Befehle verwenden, um mit dem Inhalt von `/dev` zu interagieren, ist es wichtig zu beachten, dass es keinen spezifischen `dev command in linux` gibt. Stattdessen verwenden Sie vorhandene Dienstprogramme wie `ls`, `cat` und andere, um aus diesen Gerätedateien zu lesen oder in sie zu schreiben, obwohl dies direkt mit Vorsicht erfolgen sollte.

### Die Entwicklung von /dev

In älteren Unix- und Linux-Systemen war das `/dev`-Verzeichnis statisch. Das bedeutete, dass Gerätedateien für alle möglichen Hardwaregeräte bei der Installation erstellt wurden. Dieser Ansatz führte zu einem überfüllten `dev folder linux`, das mit ungenutzten Gerätedateien für Hardware gefüllt war, die nicht einmal vorhanden war. Darüber hinaus konnten sich Gerätenamen zwischen Neustarts ändern, abhängig von der Reihenfolge, in der der Kernel sie erkannte, was zu Konfigurationsproblemen führte.

Glücklicherweise verwenden moderne Linux-Systeme einen dynamischen Ansatz. Ein System wie `udev` verwaltet nun die Umgebung `/dev in linux` und erstellt und entfernt dynamisch Gerätedateien, wenn Hardware angeschlossen und getrennt wird. Dies stellt sicher, dass `/dev` nur Dateien für Geräte enthält, die gerade verwendet werden, und bietet ein dauerhaftes Benennungsschema, was das System zuverlässiger und einfacher zu verwalten macht.

## Exercise

Übung macht den Meister! Hier sind einige praktische Übungen, um Ihr Verständnis von Hardwaregeräten und deren Interaktion mit dem Linux-System zu festigen:

1. **[Hardwaregeräte in Linux erkunden](https://labex.io/de/labs/comptia-explore-hardware-devices-in-linux-590861)** - In diesem Lab lernen Sie die wesentlichen Fähigkeiten kennen, um Hardwaregeräte in einer Linux-Umgebung zu erkunden, zu identifizieren und zu inspizieren. Sie erhalten praktische Erfahrung mit leistungsstarken Befehlszeilen-Dienstprogrammen, um zu verstehen, wie das Betriebssystem mit physischen Komponenten interagiert.

Dieses Lab hilft Ihnen, die Konzepte der Geräteinteraktion in realen Szenarien anzuwenden und Vertrauen in die Verwaltung von Hardware unter Linux aufzubauen.

## Quiz Question

Wo werden Gerätedateien auf dem System gespeichert? (Bitte geben Sie den absoluten Pfad an. Die Antwort ist groß-/kleinschreibungsempfindlich und sollte auf Englisch sein.)

## Quiz Answer

/dev
