---
index: 8
lang: "de"
title: "Das Sticky Bit"
meta_title: "Das Sticky Bit - Berechtigungen"
meta_description: "Erkunden Sie den Zweck des Sticky Bits in Linux- und Unix-Dateiberechtigungen. Erfahren Sie, wie das Sticky Bit Dateien in gemeinsam genutzten Verzeichnissen wie /tmp schützt und wie man es mit chmod setzt."
meta_keywords: "sticky bit, sticky bit linux, unix dateiberechtigungen sticky bit, chmod +t, /tmp verzeichnis, dateiberechtigungen, linux sicherheit"
---

## Lesson Content

Jenseits der Standardberechtigungen Lesen, Schreiben und Ausführen bietet Linux spezielle Berechtigungen für eine erweiterte Zugriffskontrolle. Die letzte dieser speziellen Berechtigungen, die wir behandeln, ist das **Sticky Bit** (klebriges Bit).

### Was ist das Sticky Bit?

Das Sticky Bit ist eine Berechtigungseinstellung, die auf ein Verzeichnis angewendet werden kann. Wenn das Sticky Bit für ein Verzeichnis gesetzt ist, können Dateien in diesem Verzeichnis nur vom Besitzer der Datei, dem Besitzer des Verzeichnisses oder dem Root-Benutzer gelöscht oder umbenannt werden. Dies ist besonders nützlich für gemeinsam genutzte Verzeichnisse, in denen mehrere Benutzer ihre eigenen Dateien erstellen und verwalten müssen, ohne andere zu beeinträchtigen. Dieses Konzept ist ein Schlüsselbestandteil der Verwaltung von **Unix-Dateiberechtigungen mit Sticky Bit**.

### Ein praktisches Beispiel: Das /tmp-Verzeichnis

Ein häufiger Anwendungsfall für das **Sticky Bit unter Linux** ist das `/tmp`-Verzeichnis, ein für alle beschreibbarer Ort für temporäre Dateien. Untersuchen wir seine Berechtigungen:

```bash
$ ls -ld /tmp
drwxrwxrwt 17 root root 4096 Dez 15 11:45 /tmp
```

Beachten Sie das `t` am Ende der Berechtigungszeichenfolge (`rwxrwxrwt`). Dieses `t` zeigt an, dass das Sticky Bit gesetzt ist. Aus diesem Grund kann zwar jeder Benutzer Dateien in `/tmp` erstellen, aber er kann keine von anderen Benutzern erstellten Dateien löschen oder verschieben. Dies verhindert, dass ein Benutzer die Arbeit eines anderen in diesem gemeinsam genutzten Bereich stört.

### So setzen Sie das Sticky Bit

You können das Sticky Bit mit dem `chmod`-Befehl auf zwei Arten setzen: symbolischer Modus oder oktaler (numerischer) Modus.

Um das Sticky Bit im symbolischen Modus hinzuzufügen:

```bash
chmod +t mein_gemeinsames_verzeichnis
```

Um Berechtigungen im oktalen Modus festzulegen, stellen Sie der Standard-dreistelligen Berechtigungsziffer eine **1** voran. Die numerische Darstellung für das Sticky Bit ist **1**.

```bash
# Dies setzt die Berechtigungen auf rwxr-xr-x mit dem Sticky Bit
chmod 1755 mein_gemeinsames_verzeichnis
```

Das Verständnis des Sticky Bits ist entscheidend für die Verwaltung von Multi-User-Umgebungen und die effektive Sicherung gemeinsam genutzter Verzeichnisse.

## Exercise

Um Ihr Verständnis von Dateiberechtigungen, einschließlich spezieller Berechtigungen wie dem Sticky Bit, zu festigen, versuchen Sie diese praktischen Labs. Sie helfen Ihnen zu sehen, wie diese Konzepte in realen Szenarien angewendet werden.

1.  **[Linux-Benutzergruppe und Dateiberechtigungen](https://labex.io/de/labs/linux-linux-user-group-and-file-permissions-18002)** – Üben Sie das Erstellen von Benutzern und Gruppen sowie die Manipulation von Dateibesitz und Berechtigungen. Dieses Lab bietet eine Grundlage für das Verständnis der Funktionsweise spezieller Berechtigungen.
2.  **[Dateien löschen und verschieben](https://labex.io/de/labs/linux-delete-and-move-files-7777)** – Lernen Sie, wie man Dateien löscht und verschiebt, und sehen Sie, wie Berechtigungen, einschließlich des Sticky Bits auf einem Verzeichnis, diese Aktionen einschränken können.
3.  **[Eine Datei finden](https://labex.io/de/labs/linux-find-a-file-17993)** – Üben Sie das Auffinden von Dateien und das Festlegen von Zugriffskontrollen, um die Bedeutung von Dateiberechtigungen bei der Verwaltung des Dateizugriffs und der Änderung zu verstärken.

## Quiz Question

Welches einzelne Zeichen in der Berechtigungszeichenfolge stellt in einer langen Verzeichnisauflistung (ls -l) dar, dass das Sticky Bit gesetzt ist? Bitte antworten Sie mit einem einzelnen Kleinbuchstaben aus dem Englischen.

## Quiz Answer

t
