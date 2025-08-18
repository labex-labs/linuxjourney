---
index: 8
lang: "de"
title: "Das Sticky Bit"
meta_title: "Das Sticky Bit - Berechtigungen"
meta_description: "Erfahren Sie mehr über das Linux Sticky Bit, seinen Zweck in freigegebenen Verzeichnissen wie /tmp und wie Sie es mit chmod setzen. Verstehen Sie diese wichtige Dateiberechtigung!"
meta_keywords: "Linux Sticky Bit, chmod +t, /tmp Verzeichnis, Linux Berechtigungen, Dateisicherheit, Linux Tutorial, Linux für Anfänger"
---

## Lesson Content

Ein letztes spezielles Berechtigungsbit, über das ich sprechen möchte, ist das Sticky Bit.

Dieses Berechtigungsbit „klebt eine Datei/ein Verzeichnis“, was bedeutet, dass nur der Eigentümer oder der Root-Benutzer die Datei löschen oder ändern kann. Dies ist sehr nützlich für freigegebene Verzeichnisse. Sehen Sie sich das folgende Beispiel an:

```bash
$ ls -ld /tmp
drwxrwxrwx+t 6 root root 4096 Dec 15 11:45 /tmp
```

Sie werden hier am Ende ein spezielles Berechtigungsbit **t** sehen. Das bedeutet, dass jeder Dateien im Verzeichnis `/tmp` hinzufügen, schreiben und ändern kann, aber nur root das Verzeichnis `/tmp` löschen kann.

### Modify sticky bit

```bash
sudo chmod +t mydir

sudo chmod 1755 mydir
```

Die numerische Darstellung für das Sticky Bit ist **1**.

## Exercise

Welche anderen Dateien und Verzeichnisse haben Ihrer Meinung nach ein Sticky Bit aktiviert?

## Quiz Question

Welches Symbol repräsentiert das Sticky Bit?

## Quiz Answer

t
