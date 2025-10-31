---
index: 4
lang: "de"
title: "NFS"
meta_title: "NFS - Netzwerkfreigabe"
meta_description: "Erfahren Sie, wie Sie das Network File System (NFS) unter Linux verwenden. Diese Lektion behandelt die Einrichtung eines NFS-Clients, die Verwendung des mount-Befehls und die Konfiguration von automount für nahtlosen Zugriff auf Netzwerkfreigaben."
meta_keywords: "NFS, NFS-Client, automount, Network File System, Linux-Netzwerk, mount-Befehl, Linux-Tutorial, Anfänger"
---

## Lesson Content

Das gängigste Protokoll für die Netzwerkdateifreigabe in Linux ist NFS, was für **Network File System** steht. NFS ermöglicht es einem Server, seine Verzeichnisse und Dateien über ein Netzwerk mit einem oder mehreren Client-Rechnern zu teilen, sodass diese erscheinen, als wären sie lokale Ressourcen.

Diese Lektion konzentriert sich auf die Konfiguration eines **NFS-Clients**, da die Einrichtung eines NFS-Servers ein komplexerer Prozess sein kann.

### Einhängen einer NFS-Freigabe

Um sich mit einer NFS-Freigabe zu verbinden, müssen Sie zunächst sicherstellen, dass der NFS-Client-Dienst ausgeführt wird. Anschließend können Sie den `mount`-Befehl verwenden, um das Remote-Verzeichnis an einen lokalen Einhängepunkt auf Ihrem System anzuhängen.

```bash
sudo service nfsclient start
sudo mount server:/directory /mount_directory
```

In diesem Beispiel ist `server:/directory` die Remote-Freigabe, auf die Sie zugreifen möchten, und `/mount_directory` ist das lokale Verzeichnis, in dem die Freigabe eingehängt wird.

### Verwendung von Automount für NFS

Wenn Sie häufig auf eine NFS-Freigabe zugreifen, sollten Sie in Erwägung ziehen, das Einhängen dauerhaft zu machen. Obwohl das Hinzufügen eines Eintrags in die Datei `/etc/fstab` eine gängige Methode für lokale Laufwerke ist, kann dies zu erheblichen Startverzögerungen oder sogar Fehlern führen, wenn die Netzwerkverbindung oder der NFS-Server beim Systemstart nicht verfügbar ist.

Andererseits ist **automount** eine bessere Lösung für Netzwerkfreigaben. Dieser Dienst, der vom `automount`-Tool oder seiner modernen Implementierung `amd` verwaltet wird, hängt ein Dateisystem bei Bedarf dynamisch ein. Wenn auf eine Datei oder ein Verzeichnis innerhalb eines angegebenen Pfades zugegriffen wird, verbindet sich automount automatisch mit dem Remote-Server und hängt die Freigabe ein. Dies gewährleistet bei Bedarf einen nahtlosen Zugriff, ohne den Startvorgang des Systems zu beeinträchtigen.

## Exercise

Obwohl es für dieses Thema keine spezifischen Übungen gibt, empfehlen wir Ihnen, den umfassenden [Linux Lernpfad](https://labex.io/de/learn/linux) zu erkunden, um verwandte Linux-Fähigkeiten und Konzepte zu üben.

## Quiz Question

What tool is used to manage mount points automatically? Please answer in English, and note that the answer is case-sensitive.

## Quiz Answer

automount
