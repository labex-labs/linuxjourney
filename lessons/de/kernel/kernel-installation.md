---
lang: "de"
title: "Kernel-Installation"
meta_description: "Erfahren Sie, wie Sie Linux-Kernel installieren und verwalten. Entdecken Sie Kernel-Versionen, verwenden Sie `uname -r` und apt-Befehle. Beginnen Sie Ihre Linux-Kernel-Reise!"
meta_keywords: "Linux-Kernel, Kernel installieren, uname -r, apt dist-upgrade, Kernel-Verwaltung, Linux-Tutorial, Linux für Anfänger, Linux-Anleitung"
---

## Lesson Content

Okay, nachdem wir all das langweilige Zeug hinter uns gebracht haben, sprechen wir jetzt über die eigentliche Installation und Modifikation von Kerneln. Sie können mehrere Kernel auf Ihrem System installieren; erinnern Sie sich an unsere Lektion über den Bootvorgang? In unserem GRUB-Menü können wir auswählen, welchen Kernel wir booten möchten.

Um zu sehen, welche Kernel-Version Sie auf Ihrem System haben, verwenden Sie den folgenden Befehl:

```bash
$ uname -r
3.19.0-43-generic
```

Der Befehl `uname` gibt Systeminformationen aus; die Option `-r` gibt die Kernel-Release-Version aus.

Sie können den Linux-Kernel auf verschiedene Arten installieren: Sie können das Quellpaket herunterladen und aus dem Quellcode kompilieren, oder Sie können es mit Paketverwaltungstools installieren.

```bash
sudo apt install linux-generic-lts-vivid
```

Und dann einfach in den installierten Kernel neu starten. Einfach, oder? Irgendwie schon. Sie müssen auch andere Linux-Pakete wie `linux-headers`, `linux-image-generic` usw. installieren. Sie können auch die Versionsnummer angeben, sodass der obige Befehl wie folgt aussehen kann: **`sudo apt install 3.19.0-43-generic`**

Alternativ, wenn Sie nur die aktualisierte Kernel-Version wünschen, verwenden Sie einfach `dist-upgrade`; es führt Upgrades für alle Pakete auf Ihrem System durch:

```bash
sudo apt dist-upgrade
```

Es gibt viele verschiedene Kernel-Versionen. Einige werden als LTS (Long Term Support) verwendet, einige sind die neuesten und besten. Die Kompatibilität kann zwischen Kernel-Versionen sehr unterschiedlich sein, daher möchten Sie vielleicht verschiedene Kernel ausprobieren.

## Exercise

1. Find out what kernel version you have.
2. Research the different versions of kernels available.

## Quiz Question

Wie sehen Sie die Kernel-Version Ihres Systems?

## Quiz Answer

uname -r
