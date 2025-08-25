---
index: 4
lang: "de"
title: "Kernel-Installation"
meta_title: "Kernel-Installation - Kernel"
meta_description: "Erfahren Sie, wie Sie Linux-Kernel installieren und verwalten. Entdecken Sie Kernel-Versionen, verwenden Sie `uname -r` und apt-Befehle. Beginnen Sie Ihre Linux-Kernel-Reise!"
meta_keywords: "Linux-Kernel, Kernel installieren, uname -r, apt dist-upgrade, Kernel-Verwaltung, Linux-Tutorial, Linux für Anfänger, Linux-Anleitung"
---

## Lesson Content

Okay, nachdem wir all das langweilige Zeug hinter uns gebracht haben, sprechen wir über die eigentliche Installation und Modifikation von Kerneln. Sie können mehrere Kernel auf Ihrem System installieren; erinnern Sie sich an unsere Lektion über den Bootvorgang? In unserem GRUB-Menü können wir auswählen, welchen Kernel wir booten möchten.

Um zu sehen, welche Kernel-Version Sie auf Ihrem System haben, verwenden Sie den folgenden Befehl:

```bash
$ uname -r
3.19.0-43-generic
```

Der Befehl `uname` gibt Systeminformationen aus; die Option `-r` gibt die Kernel-Release-Version aus.

Sie können den Linux-Kernel auf verschiedene Arten installieren: Sie können das Quellpaket herunterladen und aus dem Quellcode kompilieren, oder Sie können ihn mit Paketverwaltungstools installieren.

```bash
sudo apt install linux-generic-lts-vivid
```

Und dann starten Sie einfach in den installierten Kernel neu. Einfach, oder? Irgendwie schon. Sie müssen auch andere Linux-Pakete wie `linux-headers`, `linux-image-generic` usw. installieren. Sie können auch die Versionsnummer angeben, sodass der obige Befehl wie folgt aussehen kann: **`sudo apt install 3.19.0-43-generic`**

Alternativ, wenn Sie nur die aktualisierte Kernel-Version wünschen, verwenden Sie einfach `dist-upgrade`; es führt Upgrades für alle Pakete auf Ihrem System durch:

```bash
sudo apt dist-upgrade
```

Es gibt viele verschiedene Kernel-Versionen. Einige werden als LTS (Long Term Support) verwendet, andere sind die neuesten und besten. Die Kompatibilität kann zwischen Kernel-Versionen sehr unterschiedlich sein, daher möchten Sie vielleicht verschiedene Kernel ausprobieren.

## Exercise

Übung macht den Meister! Hier sind einige praktische Übungen, um Ihr Verständnis der Linux-Kernel-Verwaltung und verwandter Systemadministrationsaufgaben zu vertiefen:

1. **[Das GRUB2-Bootmenü in Linux anpassen](https://labex.io/de/labs/comptia-customize-the-grub2-boot-menu-in-linux-590859)** – Üben Sie das Ändern des GRUB2-Bootmenüs, was bei der Verwaltung mehrerer Kernel-Versionen und der Auswahl des zu startenden Kernels unerlässlich ist.
2. **[Kernel-Module in Linux verwalten](https://labex.io/de/labs/comptia-manage-kernel-modules-in-linux-590865)** – Lernen Sie, Kernel-Module aufzulisten, zu inspizieren, zu laden und zu entladen, ein grundlegender Aspekt der Kernel-Verwaltung und des Verständnisses, wie Hardware mit Ihrem System interagiert.
3. **[Software-Installation unter Linux](https://labex.io/de/labs/linux-software-installation-on-linux-18005)** – Sammeln Sie praktische Erfahrungen mit verschiedenen Methoden zur Installation und Verwaltung von Software, einschließlich der Verwendung von Paketmanagern, was eine gängige Methode zur Installation und Aktualisierung von Kerneln ist.

Diese Übungen helfen Ihnen, die Konzepte der Kernel-Verwaltung, der Boot-Prozesse und der Paketverwaltung in realen Szenarien anzuwenden und so Ihr Vertrauen in die Systemadministration zu stärken.

## Quiz Question

Wie sehen Sie die Kernel-Version Ihres Systems?

## Quiz Answer

uname -r
