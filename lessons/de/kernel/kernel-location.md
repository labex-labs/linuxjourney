---
index: 5
lang: "de"
title: "Kernel-Speicherort"
meta_title: "Kernel-Speicherort - Kernel"
meta_description: "Erfahren Sie, wo der Kernel unter Linux gespeichert ist. Dieser Leitfaden erklärt den Speicherort des Linux-Kernels im /boot-Verzeichnis und beschreibt wichtige Dateien wie vmlinuz und initrd."
meta_keywords: "linux kernel speicherort, wo ist der kernel, kernel speicherort, wo befindet sich der kernel, wo ist der kernel unter linux gespeichert, vmlinuz, /boot verzeichnis"
---

## Lesson Content

Wenn Sie einen neuen Kernel installieren, fügt Ihr System mehrere wichtige Dateien in ein bestimmtes Verzeichnis ein. Wenn Sie sich jemals gefragt haben, **wo der Kernel unter Linux gespeichert ist**, lautet die Antwort typischerweise das Verzeichnis `/boot`. Dieses Verzeichnis ist der Standard-**Linux-Kernel-Speicherort** auf den meisten Systemen.

### Das /boot-Verzeichnis

Das Verzeichnis `/boot` enthält alle Dateien, die für den Start des Bootvorgangs benötigt werden. Wenn Sie hineinschauen, sehen Sie oft Dateien, die verschiedenen Kernel-Versionen entsprechen, sodass Sie in einen älteren Kernel booten können, falls ein neuer Probleme verursacht. Das Verständnis dieses **Kernel-Speicherorts** ist für die Systemwartung von entscheidender Bedeutung.

### Wichtige Kernel-Dateien

Wo genau **befindet sich der Kernel** in diesem Verzeichnis? Er wird von einigen anderen kritischen Dateien begleitet. Hier sind die wichtigsten, denen Sie begegnen werden:

- `vmlinuz`: Dies ist der komprimierte, ausführbare Linux-Kernel selbst. Das 'z' am Ende zeigt an, dass er komprimiert ist.
- `initrd`: Dies ist die initiale RAM-Disk. Wie bereits erwähnt, ist die `initrd` ein temporäres Root-Dateisystem, das beim Start in den Speicher geladen wird, um das echte Root-Dateisystem einzuhängen.
- `System.map`: Diese Datei enthält eine Symboltabelle, die Kernel-Funktionsnamen ihren Speicheradressen zuordnet. Sie wird hauptsächlich zur Diagnose von Kernel-Panics und Oopses verwendet.
- `config`: Diese Datei speichert die Konfigurationseinstellungen, die zum Kompilieren dieser spezifischen Kernel-Version verwendet wurden. Sie gibt detailliert an, welche Treiber und Funktionen enthalten waren.

### Verwaltung von Kernel-Dateien

Mit der Zeit kann Ihr `/boot`-Verzeichnis mit Dateien alter Kernel gefüllt werden. Wenn der Speicherplatz knapp wird, können Sie die Dateien älterer, nicht verwendeter Versionen entfernen. Der sicherste Weg dies zu tun, ist die Verwendung des Paketmanagers Ihrer Distribution (wie `apt` oder `dnf`). Das manuelle Löschen von Dateien kann riskant sein, seien Sie daher äußerst vorsichtig, wenn Sie nicht die Dateien des aktuell verwendeten Kernels entfernen.

## Exercise

Wenden Sie Ihr Wissen mit diesem praktischen Labor an, um Ihr Verständnis des Linux-Bootvorgangs und der Kernel-Verwaltung zu festigen:

1. **[Anpassen des GRUB2-Bootmenüs unter Linux](https://labex.io/de/labs/comptia-customize-the-grub2-boot-menu-in-linux-590859)** - Üben Sie die Änderung der GRUB2-Konfiguration, die direkt beeinflusst, wie Ihr Linux-System bootet und Kernel-Versionen auswählt. Dieses Labor hilft Ihnen, die praktischen Auswirkungen der im `/boot`-Verzeichnis besprochenen Dateien zu verstehen.

Dieses Labor hilft Ihnen, diese Konzepte in einem realen Szenario anzuwenden und Vertrauen in die Linux-Kernel- und Boot-Verwaltung aufzubauen.

## Quiz Question

Im Verzeichnis `/boot`, wie lautet der typische Name für die komprimierte Linux-Kernel-Image-Datei? Bitte antworten Sie auf Englisch und achten Sie auf die Groß-/Kleinschreibung.

## Quiz Answer

vmlinuz
