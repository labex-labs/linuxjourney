---
index: 1
lang: "de"
title: "Benutzer und Gruppen"
meta_title: "Benutzer und Gruppen - Benutzerverwaltung"
meta_description: "Erfahren Sie mehr über Linux-Benutzer und -Gruppen, verstehen Sie UIDs, GIDs und den Root-Benutzer. Entdecken Sie, wie Sie den sudo-Befehl für erhöhte Berechtigungen verwenden. Beginnen Sie Ihre Linux-Reise!"
meta_keywords: "Linux-Benutzer, Linux-Gruppen, sudo-Befehl, Root-Benutzer, Linux-Berechtigungen, Linux-Tutorial, Linux für Anfänger, Linux-Anleitung"
---

## Lesson Content

In jedem traditionellen Betriebssystem gibt es Benutzer und Gruppen. Sie existieren ausschließlich für den Zugriff und Berechtigungen. Wenn ein Prozess ausgeführt wird, läuft er als der Eigentümer dieses Prozesses, sei es Jane oder Bob. Dateizugriff und -eigentum sind ebenfalls berechtigungsabhängig. Man möchte nicht, dass Jane Bobs Dokumente sieht und umgekehrt.

Jeder Benutzer hat sein eigenes Home-Verzeichnis, in dem seine benutzerspezifischen Dateien gespeichert sind. Dies befindet sich normalerweise unter `/home/username`, kann aber in verschiedenen Distributionen variieren.

Das System verwendet Benutzer-IDs (UID), um Benutzer zu verwalten. Benutzernamen sind die benutzerfreundliche Art, Benutzer mit einer Identifikation zu verknüpfen, aber das System identifiziert Benutzer anhand ihrer UID. Das System verwendet auch Gruppen, um Berechtigungen zu verwalten. Gruppen sind einfach Sätze von Benutzern mit Berechtigungen, die von dieser Gruppe festgelegt werden; sie werden vom System mit ihrer Gruppen-ID (GID) identifiziert.

Unter Linux haben Sie zusätzlich zu den normalen Menschen, die das System nutzen, auch Benutzer. Manchmal sind diese Benutzer System-Daemons, die kontinuierlich Prozesse ausführen, um das System funktionsfähig zu halten. Einer der wichtigsten Benutzer ist `root` oder `superuser`. `root` ist der mächtigste Benutzer auf dem System; `root` kann auf jede Datei zugreifen und jeden Prozess starten und beenden. Aus diesem Grund kann es gefährlich sein, ständig als `root` zu operieren; Sie könnten potenziell systemkritische Dateien entfernen. Glücklicherweise, wenn `root`-Zugriff benötigt wird und ein Benutzer `root`-Zugriff hat, kann er stattdessen einen Befehl als `root` mit dem `sudo`-Befehl ausführen. Der `sudo`-Befehl (superuser do) wird verwendet, um einen Befehl mit `root`-Zugriff auszuführen. Wir werden in einer späteren Lektion genauer darauf eingehen, wie ein Benutzer `root`-Zugriff erhält.

Versuchen Sie, eine geschützte Datei wie `/etc/shadow` anzuzeigen:

```bash
cat /etc/shadow
```

Beachten Sie, dass Sie eine Fehlermeldung "permission denied" erhalten. Sehen Sie sich die Berechtigungen an mit:

```bash
$ ls -la /etc/shadow

-rw-r----- 1 root shadow 1134 Dec 1 11:45 /etc/shadow
```

Wir haben die Berechtigungen noch nicht durchgenommen, aber was hier passiert, ist, dass `root` der Eigentümer der Datei ist, und Sie `root`-Zugriff benötigen oder Teil der `shadow`-Gruppe sein müssen, um den Inhalt zu lesen. Führen Sie den Befehl nun mit `sudo` aus:

```bash
sudo cat /etc/shadow
```

Jetzt können Sie den Inhalt der Datei sehen!

## Exercise

No exercises for this lesson.

## Quiz Question

Welchen Befehl verwenden Sie, um als `root` auszuführen?

## Quiz Answer

sudo
