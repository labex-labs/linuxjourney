---
lesson_id: "boot-process-bootloader"
course_id: "boot-system"
lang: "de"
order_index: 3
title: "Bootvorgang: Bootloader"
description: "Lerne, wie ein Bootloader Linux-Artefakte auswählt, die Kernel-Befehlszeile zusammenstellt und die Kontrolle übergibt."
meta_title: "Bootvorgang: Bootloader – Systemstart"
meta_description: "Lerne die Aufgaben eines Linux-Bootloaders kennen und erfahre, wie GRUB Kernel, initramfs und Parameter wie root= oder quiet für den Systemstart vorbereitet."
meta_keywords: "Linux Bootloader, Bootloader Linux, GRUB, Kernel Parameter, initramfs, initrd, Root Dateisystem, Linux Bootvorgang"
---

Ein Bootloader überbrückt die Ermittlung des Bootpfads durch die Firmware und die Ausführung des Kernels. GRUB ist auf Linux-PCs verbreitet, doch systemd-boot, U-Boot, das Laden eines EFI-Stub-Kernels durch die Firmware und andere Entwürfe übernehmen unterschiedliche Teile dieser Aufgabe.

## Bootartefakte auswählen

Ein Bootloader-Eintrag kann Folgendes angeben:

- ein Linux-Kernel-Abbild
- ein optionales initramfs- oder älteres initrd-Abbild
- eine Kernel-Befehlszeile
- plattformspezifische Metadaten oder den Bootloader eines anderen Betriebssystems

GRUB kann mehrere Kernel und Wiederherstellungseinträge anbieten. Ein Ersatzkernel ist nur dann nützlich, wenn seine passenden Module und seine initramfs weiterhin verfügbar und erprobt sind. Der Bootloader liest Dateien mithilfe seiner unterstützten Speicher- und Dateisystemmodule; er stützt sich nicht auf das noch nicht laufende Linux-VFS.

:::single-choice{#bootloader-primary-handoff}
An was übergibt ein Linux-Bootloader normalerweise die Kontrolle?

::option[An eine interaktive Benutzershell, in der bereits alle Dienste laufen.]{#bootloader-user-shell explanation="Userspace-Shells erscheinen erst, nachdem Kernel und Init-System gestartet sind."}
::option[An das ausgewählte Kernel-Abbild, nachdem die erforderlichen Bootartefakte geladen wurden.]{#bootloader-selected-kernel .correct explanation="Der Bootloader bereitet Kernel, Parameter und häufig eine initramfs vor, bevor er den Einstiegspunkt des Kernels ausführt."}
::option[An den Paketmanager des Dateisystems zur Auflösung von Abhängigkeiten.]{#bootloader-package-manager explanation="Die Paketverwaltung ist nicht die nächste Stufe, an die während des Bootens die Prozessorkontrolle übergeht."}
:::

## Parameter der Kernel-Befehlszeile

Der Bootloader übergibt eine Textbefehlszeile, die der Kernel und der frühe Userspace auswerten. Häufige Beispiele sind:

- `root=...`, um das vorgesehene Root-Dateisystem oder eine Quellspezifikation für den frühen Userspace anzugeben
- `ro` oder `rw`, um einen anfänglichen Einhängemodus für das Root-Dateisystem anzufordern
- `quiet`, um die Anzahl der Kernelmeldungen auf der Konsole zu verringern
- `init=...`, um für eine besondere Wiederherstellung ein anderes erstes Userspace-Programm anzufordern
- distributionsspezifische `rd.*`-Parameter, die von initramfs-Werkzeugen ausgewertet werden

`initrd` ist normalerweise eine Bootloader-Anweisung, die ein Abbild bezeichnet, und kein allgemeiner Kernel-Parameter. `BOOT_IMAGE=` kann in einer von manchen GRUB-Konfigurationen erzeugten Befehlszeile auftauchen, ist aber nicht der Mechanismus, der den Kernel lädt.

So siehst du die beim aktuellen Start verwendete Befehlszeile:

```bash
$ cat /proc/cmdline
```

:::single-choice{#bootloader-root-parameter}
Welchen Zweck hat der Kernel-Befehlszeilenparameter `root=`?

::option[Er bezeichnet das Root-Dateisystem, das beim Booten letztlich verwendet werden soll.]{#bootloader-root-filesystem .correct explanation="Der Kernel oder die initramfs wertet den Wert aus, um das eigentliche Root-Dateisystem zu finden und zusammenzusetzen."}
::option[Er legt das Anmeldepasswort des Root-Kontos fest.]{#bootloader-root-password explanation="Authentifizierungsgeheimnisse dürfen nicht als gewöhnlicher Text in der Kernel-Befehlszeile übergeben werden."}
::option[Er benennt PID 1 in das Wort `root` um.]{#bootloader-root-pid explanation="Die Benennung von Prozessen hat nichts mit diesem Speicherparameter zu tun."}
:::

:::single-choice{#bootloader-quiet-parameter}
Was fordert der Parameter `quiet` normalerweise an?

::option[Schreibgeschützten Zugriff auf jedes eingehängte Dateisystem.]{#bootloader-quiet-readonly explanation="Die anfängliche Schreibrichtlinie für das Root-Dateisystem verwendet Parameter wie `ro`, nicht `quiet`."}
::option[Weniger während des Bootens ausgegebene Kernelmeldungen.]{#bootloader-quiet-console .correct explanation="Der Parameter unterdrückt viele Informationsmeldungen, garantiert aber nicht, dass jede Bootkomponente still bleibt."}
::option[Das Abschalten sämtlicher Lüfter der Hardware.]{#bootloader-quiet-fans explanation="Der Parameter betrifft die Ausführlichkeit von Meldungen und nicht die Geräuschentwicklung der Hardware."}
:::

## Vorübergehende Bearbeitung und Wiederherstellung

GRUB erlaubt einem autorisierten Konsolenbenutzer häufig, einen Eintrag für einen einzigen Start zu bearbeiten, meist über eine im Menü angezeigte Bearbeitungstaste. Dies eignet sich, um `quiet` zu entfernen, Wiederherstellungsparameter auszuwählen oder eine falsche Root-Kennung zu korrigieren. Oberfläche und Autorisierung unterscheiden sich, besonders bei Secure Boot und passwortgeschützten GRUB-Konfigurationen.

Befehlszeilenparameter können vertraulichen Text über `/proc/cmdline`, Bootprotokolle und Absturzberichte offenlegen. Sie können außerdem die Sicherheit schwächen oder das System unbootbar machen. Hinterlege dort niemals Geheimnisse und bewahre einen bekanntermaßen funktionierenden Eintrag sowie einen Wiederherstellungsweg über die Konsole auf.

:::single-choice{#bootloader-temporary-edit}
Was ist eine typische Eigenschaft der interaktiven Bearbeitung eines GRUB-Menüeintrags für einen einzelnen Start?

::option[Sie schreibt automatisch jedes installierte Kernel-Abbild neu.]{#bootloader-rewrites-kernels explanation="Das Ändern des Befehlstexts verändert keine Kernel-Binärdateien."}
::option[Sie deaktiviert die Firmware-Prüfung dauerhaft auf allen Datenträgern.]{#bootloader-disables-firmware explanation="Die Firmware-Richtlinie ist eine getrennte Ebene und wird durch das Bearbeiten eines Eintrags nicht allgemein verändert."}
::option[Die Änderung gilt für diesen Start, sofern sie nicht gesondert in der Konfiguration gespeichert wird.]{#bootloader-one-boot-change .correct explanation="Die Bearbeitung im Menü verändert normalerweise den Eintrag im Arbeitsspeicher und nicht die dauerhafte Quellkonfiguration."}
:::

## Dauerhafte GRUB-Konfiguration

Distributionen erzeugen die endgültige GRUB-Konfiguration meist aus Vorlagen, Standardwerten, Skripten und gefundenen Kerneln. Bearbeite die erzeugte `grub.cfg` nicht direkt, sofern die Distribution diesen Ablauf nicht ausdrücklich dokumentiert; eine Neuerzeugung kann die Änderung überschreiben.

Nimm eine begrenzte Änderung an der Konfigurationsquelle vor, führe den von der Distribution dokumentierten Befehl zur Neuerzeugung aus, prüfe seine Ausgabe und teste mit einem weiterhin vorhandenen älteren, bekanntermaßen funktionierenden Eintrag sowie einem bootfähigen Wiederherstellungsmedium. Befehl und Ausgabepfad unterscheiden sich zwischen Debian, Fedora sowie UEFI- und BIOS-Installationen.

:::single-choice{#bootloader-generated-config}
Warum ist die direkte Bearbeitung einer erzeugten `grub.cfg` normalerweise unzuverlässig?

::option[Die Datei kann niemals lesbaren Text enthalten.]{#bootloader-config-binary explanation="Die GRUB-Konfiguration ist Text, doch entscheidend ist weiterhin, dass sie erzeugt und verwaltet wird."}
::option[GRUB liest ausschließlich Dateien in den Home-Verzeichnissen der Benutzer.]{#bootloader-grub-home explanation="Die Bootkonfiguration gilt systemweit und muss verfügbar sein, bevor Benutzersitzungen der Home-Verzeichnisse beginnen."}
::option[Eine spätere Neuerzeugung kann die manuelle Änderung überschreiben.]{#bootloader-regeneration-overwrites .correct explanation="Dauerhafte Einstellungen gehören im Allgemeinen in die Konfigurationsquellen und den Erzeugungsablauf der Distribution."}
:::

Verwende das Lab [GRUB2-Bootmenü anpassen](https://labex.io/labs/comptia-customize-the-grub2-boot-menu-in-linux-590859) nur in seiner wiederherstellbaren Lab-Umgebung.

## Zusammenfassung

Du kannst nun Bootloader-Anweisungen von Parametern der Kernel-Befehlszeile unterscheiden.

1. Erkenne Kernel, initramfs, Befehlszeile und alternative Einträge.
2. Verwende `root=`, `ro` und `quiet` entsprechend ihren tatsächlichen Aufgaben.
3. Prüfe die Parameter des laufenden Systems über `/proc/cmdline`.
4. Behandle interaktive Änderungen als vorübergehend und sicherheitsrelevant.
5. Ändere eine dauerhaft erzeugte Konfiguration über den Arbeitsablauf der Distribution.
