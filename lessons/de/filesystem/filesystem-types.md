---
index: 2
lang: "de"
title: "Dateisystemtypen"
meta_title: "Dateisystemtypen - Das Dateisystem"
meta_description: "Erfahren Sie mehr über Linux-Dateisystemtypen wie ext4, Btrfs und XFS. Verstehen Sie Journaling und VFS für konsistente Daten. Entdecken Sie gängige Linux-Dateisysteme in diesem Leitfaden für Anfänger."
meta_keywords: "Linux-Dateisystemtypen, ext4, Btrfs, XFS, Journaling, VFS, Linux-Tutorial, Anfängerleitfaden"
---

## Lesson Content

Es gibt viele verschiedene Dateisystemimplementierungen. Einige sind schneller als andere, einige unterstützen größere Speicherkapazitäten, und andere funktionieren nur auf Speichern mit kleinerer Kapazität. Verschiedene Dateisysteme organisieren ihre Daten auf unterschiedliche Weise, und wir werden detailliert darauf eingehen, welche Arten von Dateisystemen es gibt. Da so viele verschiedene Implementierungen verfügbar sind, benötigen Anwendungen eine Möglichkeit, mit den verschiedenen Operationen umzugehen. Daher gibt es eine Abstraktionsschicht namens Virtual File System (VFS). Es ist eine Schicht zwischen Anwendungen und den verschiedenen Dateisystemtypen, sodass Ihre Anwendungen unabhängig vom Dateisystem damit arbeiten können.

Sie können viele Dateisysteme auf Ihren Festplatten haben, je nachdem, wie sie partitioniert sind, und wir werden dies in einer kommenden Lektion behandeln.

### Journaling

Journaling ist bei den meisten Dateisystemtypen standardmäßig aktiviert, aber falls nicht, sollten Sie wissen, was es bewirkt. Nehmen wir an, Sie kopieren eine große Datei und plötzlich fällt der Strom aus. Wenn Sie sich auf einem nicht-journaling-fähigen Dateisystem befinden, wäre die Datei beschädigt und Ihr Dateisystem inkonsistent. Wenn Sie dann neu starten, würde Ihr System eine Dateisystemprüfung durchführen, um sicherzustellen, dass alles in Ordnung ist. Die Reparaturen könnten jedoch eine Weile dauern, je nachdem, wie groß Ihr Dateisystem war.

Wenn Sie sich auf einem Journaling-System befinden, schreibt die Maschine, bevor sie überhaupt mit dem Kopieren der Datei beginnt, in eine Protokolldatei (Journal), was Sie tun werden. Wenn Sie die Datei tatsächlich kopieren und der Vorgang abgeschlossen ist, markiert das Journal diese Aufgabe als erledigt. Das Dateisystem ist dadurch immer in einem konsistenten Zustand, sodass es genau weiß, wo Sie aufgehört haben, wenn Ihre Maschine plötzlich heruntergefahren wurde. Dies verkürzt auch die Startzeit, da nicht das gesamte Dateisystem überprüft wird, sondern nur Ihr Journal.

### Gängige Desktop-Dateisystemtypen

- ext4 - Dies ist die aktuellste Version der nativen Linux-Dateisysteme. Es ist kompatibel mit den älteren Versionen ext2 und ext3. Es unterstützt Festplattenvolumen bis zu 1 Exabyte und Dateigrößen bis zu 16 Terabyte und vieles mehr. Es ist die Standardwahl für Linux-Dateisysteme.
- Btrfs - "Better or Butter FS" ist ein neues Dateisystem für Linux, das Snapshots, inkrementelle Backups, Leistungssteigerung und vieles mehr bietet. Es ist weit verbreitet, aber noch nicht ganz stabil und kompatibel.
- XFS - Hochleistungs-Journaling-Dateisystem, ideal für Systeme mit großen Dateien wie einem Medienserver.
- NTFS und FAT - Windows-Dateisysteme
- HFS+ - Macintosh-Dateisystem

Überprüfen Sie, welche Dateisysteme sich auf Ihrer Maschine befinden:

```plaintext
pete@icebox:~$ df -T
Filesystem     Type     1K-blocks    Used Available Use% Mounted on
/dev/sda1      ext4       6461592 2402708   3707604  40% /
udev           devtmpfs    501356       4    501352   1% /dev
tmpfs          tmpfs       102544    1068    101476   2% /run
/dev/sda6      xfs       13752320  460112  13292208   4% /home
```

Der Befehl **df** meldet die Festplattennutzung des Dateisystems und andere Details zu Ihrer Festplatte; wir werden später mehr über dieses Tool sprechen.

## Exercise

Übung macht den Meister! Hier ist ein praktisches Labor, um Ihr Verständnis von Linux-Dateisystemen und -Partitionen zu vertiefen:

1. **[Linux-Partitionen und Dateisysteme verwalten](https://labex.io/de/labs/comptia-manage-linux-partitions-and-filesystems-590845)** - Üben Sie das Erstellen einer neuen Partition, deren Formatierung, das Einhängen und die Konfiguration des persistenten Einhängens – alles grundlegende Fähigkeiten im Zusammenhang mit der Verwaltung verschiedener Dateisystemimplementierungen.

Dieses Labor wird Ihnen helfen, die Konzepte in realen Szenarien anzuwenden und Vertrauen im Umgang mit der Festplattenspeicherung unter Linux aufzubauen.

## Quiz Question

Was ist der gängige Linux-Dateisystemtyp?

## Quiz Answer

ext4
