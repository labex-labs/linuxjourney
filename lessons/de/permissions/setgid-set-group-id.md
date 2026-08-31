---
lesson_id: "setgid-set-group-id"
course_id: "permissions"
lang: "de"
order_index: 6
title: "Setgid"
description: "Erfahre, wie Set-Group-ID ausführbare Zugangsdaten und die Gruppenvererbung in gemeinsam genutzten Verzeichnissen beeinflusst."
meta_title: "Setgid – Berechtigungen"
meta_description: "Lerne Linux-SGID-Berechtigungen (Set Group ID), ihre Funktionsweise und ihre Änderung kennen. Verstehe dieses entscheidende Linux-Sicherheitskonzept."
meta_keywords: "Linux SGID, Set Group ID, Linux-Berechtigungen, chmod g+s, Linux-Sicherheit, Linux für Einsteiger, Linux-Tutorial"
---

Das Set-Group-ID-Bit, meist setgid oder SGID genannt, hat zwei wichtige Einsatzgebiete. Bei einer ausführbaren regulären Datei kann es die effektive Gruppen-ID des neuen Prozesses ändern. Bei einem Verzeichnis sorgt es dafür, dass neu erstellte Einträge die Gruppe des Verzeichnisses erben, was besonders für gemeinsam bearbeitete Bäume nützlich ist.

## Setgid bei ausführbaren Dateien

Eine ausführliche Auflistung kann setgid an der Ausführungsposition der Gruppe anzeigen:

```bash
$ ls -l /path/to/program
-rwxr-sr-x 1 root operators 24576 Jan 10 09:30 /path/to/program
```

Ein kleingeschriebenes `s` bedeutet, dass sowohl setgid als auch die Gruppenausführungsberechtigung gesetzt sind. Ein großgeschriebenes `S` bedeutet, dass setgid gesetzt ist, die Gruppenausführungsberechtigung aber fehlt.

Wenn der Kernel dieses Bit bei der Ausführung berücksichtigt, erhält der Prozess eine effektive Gruppen-ID, die sich aus dem Gruppeneigentümer der ausführbaren Datei ableitet. Kontrollen wie das Einhängen mit `nosuid` können dieses Verhalten unterdrücken. Es darf nicht als allgemeine Garantie über sämtliche Dateitypen und Umgebungen hinweg betrachtet werden.

:::single-choice{#setgid-executable-effect}
Welche Zugangsdaten stammen vom Gruppeneigentümer einer ausführbaren Datei, wenn setgid berücksichtigt wird?

::option[Die effektive Gruppen-ID des Prozesses.]{#setgid-effective-group .correct explanation="Die Set-Group-ID-Ausführung richtet die Gruppe des Eigentümers der ausführbaren Datei als effektive Gruppenidentität des Prozesses ein."}
::option[Die reale Benutzer-ID des Prozesses.]{#setgid-real-user explanation="Das Bit betrifft die Gruppenzugangsdaten und nicht die reale Benutzeridentität des Aufrufers."}
::option[Der Eigentümer jeder vom Prozess geöffneten Datei.]{#setgid-opened-owner explanation="Ausführungszugangsdaten schreiben keine Eigentumsmetadaten geöffneter Dateien um."}
:::

## Setgid bei Verzeichnissen

Setgid hat bei einem Verzeichnis einen anderen Zweck. Neue Dateien und Unterverzeichnisse erben gewöhnlich die Gruppe des Verzeichnisses statt der Standardgruppe des Erstellers. Unter Linux erben neue Unterverzeichnisse außerdem das setgid-Bit. Dadurch behält ein gemeinsam genutzter Projektbaum eine einheitliche Gruppe.

Setgid selbst gewährt keine Gruppenschreibberechtigung. Der Verzeichnismodus, die Prozess-umask, der angeforderte Erstellungsmodus, Standard-ACLs und andere Kontrollen bestimmen weiterhin den Zugriff.

```bash
$ sudo chgrp developers /srv/project
$ sudo chmod g+s /srv/project
$ ls -ld /srv/project
drwxr-sr-x 2 root developers 4096 Jan 10 09:30 /srv/project
```

:::single-choice{#setgid-directory-inheritance}
Was erbt eine neu erstellte Datei gewöhnlich durch setgid auf `/srv/project`?

::option[Den Benutzereigentümer des Verzeichnisses.]{#setgid-inherit-user explanation="Setgid auf einem Verzeichnis beeinflusst die Gruppenvererbung und nicht den Benutzereigentümer des neuen Eintrags."}
::option[Den vollständigen Berechtigungsmodus des Verzeichnisses.]{#setgid-inherit-mode explanation="Erstellungsberechtigungen werden weiterhin aus dem angeforderten Modus, der umask und möglichen ACLs berechnet."}
::option[Den Gruppeneigentümer des Verzeichnisses.]{#setgid-inherit-group .correct explanation="Ein neuer Eintrag erhält gewöhnlich die Gruppe des setgid-Verzeichnisses und unterstützt so einheitliches gemeinsames Eigentum."}
:::

## Setgid setzen und entfernen

Setze das Bit symbolisch mit:

```bash
$ sudo chmod g+s myfile
```

Setze es zusammen mit gewöhnlichen Modusbits durch eine führende oktale `2`:

```bash
$ sudo chmod 2755 myfile
```

Entferne ausschließlich das besondere Bit mit `chmod g-s myfile`.

:::single-choice{#setgid-octal-value}
Welchen Wert trägt setgid zur führenden oktalen Ziffer für besondere Bits bei?

::option[`4`]{#setgid-value-four explanation="Der Wert `4` steht in der Ziffer für besondere Bits für setuid."}
::option[`1`]{#setgid-value-one explanation="Der Wert `1` steht für das Sticky-Bit."}
::option[`2`]{#setgid-value-two .correct explanation="Setgid trägt `2` bei, wie im Modus `2755`."}
:::

## Gemeinsam genutzte Verzeichnisse sicher verwenden

Kombiniere für ein gemeinsam genutztes Verzeichnis den beabsichtigten Gruppeneigentümer, setgid und eng ausgewählte Zugriffsbits. Teste die Erstellung als repräsentative Benutzer und prüfe die Ergebnisse mit `ls -ld`. Mache einen Baum nicht für alle beschreibbar, nur um Probleme bei der gemeinsamen Gruppennutzung zu lösen. Eine eigene Gruppe, eine passende umask oder Standard-ACL und ein setgid-Verzeichnis bieten gewöhnlich eine klarere Kontrolle.

:::single-choice{#setgid-directory-write-access}
Erhalten Gruppenmitglieder allein durch das Setzen von setgid die Berechtigung, Dateien in einem Verzeichnis zu erstellen?

::option[Ja; setgid fügt immer Lesen, Schreiben und Ausführen für die Gruppe hinzu.]{#setgid-adds-rwx explanation="Das besondere Bit ändert die drei gewöhnlichen Gruppenberechtigungsbits nicht automatisch."}
::option[Ja; setgid deaktiviert alle Prüfungen für Gruppenmitglieder.]{#setgid-disables-checks explanation="Gewöhnliche frei bestimmbare und zusätzliche Sicherheitsprüfungen gelten weiterhin."}
::option[Nein; die zutreffenden Schreib- und Suchberechtigungen müssen die Erstellung ebenfalls erlauben.]{#setgid-no-automatic-write .correct explanation="Setgid steuert die Gruppenvererbung, während gewöhnliche Berechtigungen und andere Zugriffskontrollen das Schreiben in Verzeichnisse regeln."}
:::

## Zusammenfassung

Du kannst nun die Bedeutungen von setgid bei ausführbaren Dateien und Verzeichnissen unterscheiden.

1. Erkenne setgid an der Ausführungsposition der Gruppe.
2. Setze setgid bei ausführbaren Dateien mit der effektiven Gruppen-ID in Beziehung.
3. Verwende setgid bei Verzeichnissen, um das Gruppeneigentum in gemeinsam genutzten Bäumen zu bewahren.
4. Setze oder entferne das Bit, ohne es mit der gewöhnlichen Schreibberechtigung zu verwechseln.
