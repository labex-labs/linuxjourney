---
index: 4
lang: "de"
title: "NFS"
meta_title: "NFS - Netzwerkfreigabe"
meta_description: "Erfahren Sie mehr über die Einrichtung von NFS-Clients und das automatische Einhängen (Automounting) in Linux. Verstehen Sie, wie Sie sich mit Netzwerkdateifreigaben verbinden und Automount für nahtlosen Zugriff nutzen."
meta_keywords: "NFS-Client, Automount, Netzwerkdateisystem, Linux-Netzwerk, mount-Befehl, Linux-Tutorial, Anfänger"
---

## Lesson Content

Das gängigste Netzwerkdateisystem für Linux ist NFS (Network File System). NFS ermöglicht es einem Server, Verzeichnisse und Dateien mit einem oder mehreren Clients über das Netzwerk zu teilen.

Wir werden nicht auf die Details der Erstellung eines NFS-Servers eingehen, da dies komplex werden kann; wir werden jedoch die Einrichtung von NFS-Clients besprechen.

### NFS-Client einrichten

```bash
sudo service nfsclient start
sudo mount server:/directory /mount_directory
```

### Automatisches Einhängen (Automounting)

Angenommen, Sie verwenden den NFS-Server recht häufig und möchten ihn dauerhaft eingehängt lassen. Normalerweise würden Sie vielleicht daran denken, die Datei `/etc/fstab` zu bearbeiten, aber Sie erhalten möglicherweise nicht immer eine Verbindung zum Server, und das kann beim Booten zu Problemen führen. Stattdessen sollten Sie das automatische Einhängen (automounting) einrichten, damit Sie bei Bedarf eine Verbindung zum NFS-Server herstellen können. Dies geschieht mit dem Tool **automount** oder, in neueren Linux-Versionen, **amd**. Wenn auf eine Datei in einem bestimmten Verzeichnis zugegriffen wird, sucht automount den Remote-Server und hängt ihn automatisch ein.

## Exercise

Lesen Sie die Manpage für NFS, um mehr zu erfahren.

## Quiz Question

Welches Tool wird verwendet, um Mount-Punkte automatisch zu verwalten?

## Quiz Answer

automount
