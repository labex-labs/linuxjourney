---
lang: "de"
title: "Dateisysteme erstellen"
meta_description: "Erfahren Sie, wie Sie Dateisysteme unter Linux mit mkfs erstellen. Dieser anfängerfreundliche Leitfaden behandelt ext4 und die Festplattenpartitionierung. Beginnen Sie Ihre Linux-Reise!"
meta_keywords: "mkfs, Dateisystem erstellen, ext4, Linux-Partitionierung, Linux-Tutorial, Linux für Anfänger, Festplattenverwaltung, Linux-Leitfaden"
---

## Lesson Content

Nachdem Sie nun tatsächlich eine Festplatte partitioniert haben, lassen Sie uns ein Dateisystem erstellen!

```bash
sudo mkfs -t ext4 /dev/sdb2
```

So einfach ist das! Das Werkzeug **mkfs** (make filesystem) ermöglicht es uns, den gewünschten Dateisystemtyp und den Speicherort anzugeben. Sie sollten ein Dateisystem nur auf einer neu partitionierten Festplatte oder beim Neupartitionieren einer alten erstellen. Wenn Sie versuchen, ein Dateisystem über ein bestehendes zu erstellen, werden Sie Ihr Dateisystem höchstwahrscheinlich in einem beschädigten Zustand hinterlassen.

## Exercise

Erstellen Sie ein ext4-Dateisystem auf dem USB-Laufwerk.

## Quiz Question

Welcher Befehl wird verwendet, um ein Dateisystem zu erstellen?

## Quiz Answer

mkfs
