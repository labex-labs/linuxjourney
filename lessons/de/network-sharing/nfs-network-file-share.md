---
index: 4
lang: "de"
title: "NFS"
meta_title: "NFS - Netzwerkfreigabe"
meta_description: "Erfahren Sie mehr über die Einrichtung von NFS-Clients und das automatische Einhängen in Linux. Verstehen Sie, wie Sie sich mit Netzwerk-Dateifreigaben verbinden und Automount für nahtlosen Zugriff verwenden."
meta_keywords: "NFS-Client, Automount, Network File System, Linux-Netzwerk, mount-Befehl, Linux-Tutorial, Anfänger"
---

## Lesson Content

Das gängigste Netzwerk-Dateisystem für Linux ist NFS (Network File System). NFS ermöglicht es einem Server, Verzeichnisse und Dateien mit einem oder mehreren Clients über das Netzwerk zu teilen.

Wir werden nicht auf die Details der Erstellung eines NFS-Servers eingehen, da dies komplex werden kann; wir werden jedoch die Einrichtung von NFS-Clients besprechen.

### NFS-Client einrichten

```bash
sudo service nfsclient start
sudo mount server:/directory /mount_directory
```

### Automatisches Einhängen (Automounting)

Nehmen wir an, Sie verwenden den NFS-Server sehr oft und möchten ihn dauerhaft eingehängt lassen. Normalerweise würden Sie vielleicht denken, dass Sie die Datei `/etc/fstab` bearbeiten würden, aber Sie erhalten möglicherweise nicht immer eine Verbindung zum Server, und das kann beim Booten zu Problemen führen. Stattdessen sollten Sie das automatische Einhängen (Automounting) einrichten, damit Sie bei Bedarf eine Verbindung zum NFS-Server herstellen können. Dies geschieht mit dem Tool **automount** oder, in neueren Linux-Versionen, **amd**. Wenn auf eine Datei in einem bestimmten Verzeichnis zugegriffen wird, sucht automount den Remote-Server und hängt ihn automatisch ein.

## Exercise

Obwohl es keine spezifischen Labs zu diesem Thema gibt, empfehlen wir Ihnen, den umfassenden [Linux-Lernpfad](https://labex.io/de/learn/linux) zu erkunden, um verwandte Linux-Fähigkeiten und -Konzepte zu üben.

## Quiz Question

Welches Tool wird verwendet, um Mount-Punkte automatisch zu verwalten?

## Quiz Answer

automount
