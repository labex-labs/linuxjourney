---
lesson_id: "symlinks"
course_id: "filesystem"
lang: "de"
order_index: 12
title: "Symbolische Links"
description: "Lerne, wie sich symbolische und harte Links bei Pfadauflösung, Inode-Identität und Dateisystemumfang unterscheiden."
meta_title: "Symbolische Links – Das Dateisystem"
meta_description: "Lerne symbolische Links und Hardlinks unter Linux mit ln, ls und readlink kennen und verstehe Pfadauflösung, Inodes, Lebensdauer und Sicherheitsgrenzen."
meta_keywords: "Linux Symlinks, Hardlinks, ln Befehl, symbolische Links, ls Symlink, Linkanzahl Linux, readlink, Linux Dateisystem"
---

Ein Verzeichniseintrag gibt einem Inode einen Namen. Ein Hardlink erstellt einen weiteren Verzeichniseintrag für denselben Inode, während ein symbolischer Link einen anderen Inode erzeugt, dessen Inhalt ein aufzulösender Pfadname ist. Dieser Unterschied bestimmt Identität, Lebensdauer und Verhalten über Dateisystemgrenzen hinweg.

## Einen symbolischen Link erstellen und untersuchen

Erstelle einen Symlink mit `ln -s TARGET LINK_NAME`:

```bash
$ printf '%s\n' 'example' > myfile
$ ln -s -- myfile myfilelink
$ ls -li myfile myfilelink
151   -rw-r--r-- 1 user user 8 ... myfile
93403 lrwxrwxrwx 1 user user 6 ... myfilelink -> myfile
```

Der Symlink besitzt einen eigenen Inode und speichert den Text `myfile`. Wenn ein Programm `myfilelink` folgt, setzt sich die Pfadauflösung beim Ziel fort. Zeige den gespeicherten Text an, ohne ihm zu folgen:

```bash
$ readlink myfilelink
```

:::single-choice{#symlinks-create-symbolic} Welcher Befehl erstellt den symbolischen Link `myfilelink` mit dem Zieltext `myfile`?

::option[`ln -s -- myfile myfilelink`]{#symlinks-ln-s .correct explanation="Die Option `-s` fordert einen symbolischen Link an, gefolgt von Ziel und neuem Linknamen."}
::option[`ln -- myfile myfilelink`]{#symlinks-ln-hard explanation="Ohne `-s` fordert `ln` einen Hardlink auf den vorhandenen Inode an."}
::option[`readlink myfile myfilelink`]{#symlinks-readlink-create explanation="Readlink untersucht einen Symlink und erstellt keinen."}
:::

## Relative und absolute Symlink-Ziele

Ein absolutes Ziel beginnt bei `/`. Ein relatives Ziel wird relativ zum Verzeichnis aufgelöst, das den Symlink enthält – nicht relativ zum aktuellen Verzeichnis der Shell, wenn jemand ihn später öffnet.

```bash
$ mkdir -p tree/data tree/current
$ printf '%s\n' 'value' > tree/data/item
$ ln -s ../data/item tree/current/item
```

Das Verschieben der gesamten `tree`-Hierarchie erhält diese relative Beziehung. Wird nur der Link oder das Ziel verschoben, kann sie brechen. Ein Symlink darf ein nicht vorhandenes Ziel enthalten und heißt dann verwaist oder defekt.

:::single-choice{#symlinks-relative-resolution} Von welchem Ort aus wird ein relatives Symlink-Ziel aufgelöst?

::option[Vom Home-Verzeichnis des Benutzers, der es erstellt hat.]{#symlinks-creator-home explanation="Die Identität des Erstellers wird nicht zur dauerhaften Auflösungsbasis."}
::option[Vom aktuellen Verzeichnis der Shell, die es zuerst auflistet.]{#symlinks-listing-shell explanation="Der Kontext der Auflistung schreibt die gespeicherte Zielbeziehung nicht um."}
::option[Vom Verzeichnis, das den Symlink enthält.]{#symlinks-containing-directory .correct explanation="Die Pfadverfolgung setzt den gespeicherten relativen Text am Ort des Symlinks ein."}
:::

## Einen Hardlink erstellen

Erstelle ohne `-s` einen weiteren Namen für eine vorhandene gewöhnliche Datei:

```bash
$ ln -- myfile myhardlink
$ ls -li myfile myhardlink
151 -rw-r--r-- 2 user user 8 ... myfile
151 -rw-r--r-- 2 user user 8 ... myhardlink
```

Beide Namen gehören zum selben Dateisystem und verweisen auf dieselbe Inode-Nummer. Die Linkanzahl beträgt nun 2. Keiner der Namen ist von Natur aus das „Original“; Änderungen des Inhalts über einen Namen verändern das gemeinsame Objekt, und das Entfernen eines Namens lässt den anderen bestehen.

Hardlinks können Dateisystemgrenzen nicht überschreiten, weil eine Inode-Nummer nur innerhalb ihres Dateisystems Bedeutung besitzt. Linux hindert gewöhnliche Benutzer außerdem daran, Hardlinks auf Verzeichnisse anzulegen, und kann Links auf Dateien einschränken, die ihnen nicht gehören. Dadurch werden Zyklen und Sicherheitsprobleme vermieden.

:::single-choice{#symlinks-hard-link-inode} Was teilen zwei Hardlinks auf dieselbe gewöhnliche Datei?

::option[Nur ähnliche Dateinamen bei getrennten Dateidaten.]{#symlinks-separate-data explanation="Das würde unabhängige Kopien und keine Hardlinks beschreiben."}
::option[Einen Pfadnamen, der in einem getrennten Symlink-Inode gespeichert ist.]{#symlinks-stored-path explanation="Gespeicherter Pfadtext ist der kennzeichnende Mechanismus eines symbolischen Links."}
::option[Denselben Inode und Dateiinhalt.]{#symlinks-same-inode .correct explanation="Jeder Verzeichniseintrag benennt dasselbe Dateisystemobjekt."}
:::

## Lebensdauer und Löschen

Das Entfernen eines Symlinks entfernt das Linkobjekt und nicht sein Ziel:

```bash
$ rm -- myfilelink
```

Das Entfernen eines Hardlink-Namens verringert die Linkanzahl des gemeinsamen Inodes. Das Dateisystem kann das Objekt erst zurückgewinnen, wenn die Anzahl null ist und keine offenen Dateibeschreibungen oder anderen Dateisystemreferenzen es am Leben halten.

Vermeide beim Entfernen eines Symlinks auf ein Verzeichnis einen abschließenden Schrägstrich, weil die Pfadauflösung dadurch abhängig vom Befehl der Verzeichnissemantik folgen kann. Untersuche ihn mit `ls -ld -- LINK` und entferne bewusst den Linknamen.

:::single-choice{#symlinks-remove-symbolic} Was geschieht normalerweise, wenn du den Symlink selbst entfernst?

::option[Inode und Name des Symlinks werden entfernt, das Ziel bleibt erhalten.]{#symlinks-remove-link-only .correct explanation="Das Entfernen des symbolischen Links wirkt nicht auf das Objekt, das durch seinen gespeicherten Zieltext benannt wird."}
::option[Das Ziel und jeder Hardlink darauf werden automatisch gelöscht.]{#symlinks-remove-target explanation="Der Symlink ist ein getrenntes Dateisystemobjekt und besitzt sein Ziel nicht."}
::option[Das Ziel wird vor dem Entfernen in den Symlink kopiert.]{#symlinks-copy-target explanation="Beim Entfernen wird der Zielinhalt nicht im Link bewahrt."}
:::

## Links sicher folgen

Symlinks können ein privilegiertes Programm aus einem erwarteten Verzeichnis heraus umleiten oder sich zwischen Validierung und Nutzung ändern. Sichere Programme sollten Check-then-open-Rennen bei Pfadnamen vermeiden und für Sprache und Betriebssystem geeignete verzeichnisrelative, No-Follow- oder eingeschränkt auflösende Schnittstellen verwenden.

Für gewöhnliche Untersuchungen:

- `ls -ld LINK` zeigt den Link selbst.
- `readlink LINK` gibt seinen gespeicherten Zieltext aus.
- `stat LINK` meldet üblicherweise Linkmetadaten, während `stat -L LINK` bei GNU coreutils dem Link folgt.
- `find -L` folgt Links und kann auf Zyklen treffen; verwende es nur bewusst.

Als `lrwxrwxrwx` angezeigte Berechtigungen sind keine allgemeine Zugriffsgewährung. Der Zugriff wird durch Verzeichnisverfolgung, Richtlinie zum Folgen von Links und Zielberechtigungen entschieden; bei manchen Regeln für geschützte Verzeichnisse ist außerdem die Symlink-Eigentümerschaft relevant.

:::single-choice{#symlinks-readlink-output} Was gibt `readlink LINK` standardmäßig aus?

::option[Den im symbolischen Link gespeicherten Pfadtext.]{#symlinks-readlink-target-text .correct explanation="Der Befehl untersucht das Linkobjekt, ohne den Inhalt der Zieldatei zu lesen."}
::option[Den vollständigen Byteinhalt der gewöhnlichen Zieldatei.]{#symlinks-readlink-file-content explanation="Verwende nach bewusster Auflösung einen Dateilesebefehl für den Zielinhalt."}
::option[Jeden Hardlink im gesamten Dateisystem.]{#symlinks-readlink-all-hard explanation="Die Suche nach Hardlinks erfordert Inode-bewusste Dateisystemsuchen und steht nicht mit dem Zieltext eines Symlinks in Zusammenhang."}
:::

Nutze das Lab [Dateien und Verzeichnisse unter Linux verwalten](https://labex.io/labs/comptia-manage-files-and-directories-in-linux-590835), um Links an entbehrlichen Dateien zu üben und Inode-Nummern zu vergleichen.

## Zusammenfassung

Du kannst nun die richtige Art von Dateisystemlink auswählen und untersuchen.

1. Verwende `ln -s TARGET LINK` für einen pfadbasierten symbolischen Link.
2. Löse relative Ziele vom enthaltenden Verzeichnis des Links aus auf.
3. Verwende `ln EXISTING LINK` für einen weiteren Inode-Namen im selben Dateisystem.
4. Unterscheide das Entfernen eines Symlinks vom Entfernen eines Hardlinks.
5. Vermeide unsicheres Folgen von Links bei privilegierten oder rekursiven Operationen.
