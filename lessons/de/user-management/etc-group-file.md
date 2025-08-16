---
title: "/etc/group"
description: "Erfahren Sie mehr über die Datei /etc/group in Linux, verstehen Sie Gruppenverwaltung, GID und Benutzerberechtigungen. Ein grundlegendes Linux-Gruppendatei-Tutorial für Anfänger."
keywords: "/etc/group, Linux-Gruppen, Gruppenverwaltung, GID, Linux-Berechtigungen, Linux-Tutorial, Linux für Anfänger, Linux-Anleitung"
---

## Lesson Content

Eine weitere Datei, die in der Benutzerverwaltung verwendet wird, ist die Datei `/etc/group`. Diese Datei ermöglicht verschiedene Gruppen mit unterschiedlichen Berechtigungen.

```bash
$ cat /etc/group

root:*:0:pete
```

Sehr ähnlich der `/etc/passwd`-Datei sind die Felder der `/etc/group`-Datei wie folgt:

1. Gruppenname
2. Gruppenpasswort – es ist nicht notwendig, ein Gruppenpasswort festzulegen; die Verwendung eines erhöhten Privilegs wie `sudo` ist Standard. Ein Sternchen (`*`) wird als Standardwert eingesetzt.
3. Group ID (GID)
4. Liste der Benutzer – Sie können manuell Benutzer angeben, die Sie in einer bestimmten Gruppe haben möchten

## Exercise

Führen Sie den Befehl `groups` aus. Was sehen Sie?

## Quiz Question

Was ist die GID von root?

## Quiz Answer

0
