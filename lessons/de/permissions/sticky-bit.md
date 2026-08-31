---
lesson_id: "sticky-bit"
course_id: "permissions"
lang: "de"
order_index: 8
title: "Das Sticky-Bit"
description: "Erfahre, wie das Sticky-Bit Einträge in gemeinsam genutzten beschreibbaren Verzeichnissen wie `/tmp` schützt."
meta_title: "Das Sticky-Bit – Berechtigungen"
meta_description: "Erkunde den Zweck des Sticky-Bits in Linux- und Unix-Dateiberechtigungen. Erfahre, wie das Sticky-Bit Dateien in gemeinsam genutzten Verzeichnissen wie /tmp schützt und wie du es mit chmod setzt."
meta_keywords: "Sticky-Bit, Sticky-Bit Linux, Sticky-Bit Unix-Dateiberechtigungen, chmod +t, Verzeichnis /tmp, Dateiberechtigungen, Linux-Sicherheit"
---

Ein beschreibbares Verzeichnis erlaubt einem autorisierten Benutzer gewöhnlich, darin enthaltene Einträge zu entfernen oder umzubenennen, selbst wenn ihm die Dateien selbst nicht gehören. Das Sticky-Bit fügt eine Eigentumsbeschränkung hinzu, die gemeinsam genutzte beschreibbare Verzeichnisse sicherer macht.

## Wie das Sticky-Bit das Entfernen einschränkt

Wenn das Sticky-Bit auf einem Verzeichnis gesetzt ist, erlaubt Linux das Entfernen oder Umbenennen eines Eintrags im Allgemeinen nur einem entsprechend privilegierten Prozess, dem Verzeichniseigentümer oder dem Eigentümer des Eintrags. Die gewöhnlichen Schreib- und Suchberechtigungen des Verzeichnisses sind weiterhin erforderlich.

Die Einschränkung betrifft Verzeichniseinträge. Sie hindert einen Dateieigentümer nicht daran, den Dateiinhalt zu bearbeiten, wenn die Dateiberechtigungen diesen Vorgang anderweitig erlauben, und macht das Verzeichnis nicht privat.

:::single-choice{#sticky-bit-removal-rule}
Welcher gewöhnliche Benutzer kann in einem gemeinsam genutzten Verzeichnis mit Sticky-Bit einen bestimmten Eintrag normalerweise entfernen?

::option[Jeder Benutzer, der das Verzeichnis auflisten kann.]{#sticky-bit-any-reader explanation="Die Leseberechtigung eines Verzeichnisses kann Namen sichtbar machen, umgeht aber nicht die Eigentumsbeschränkung des Sticky-Bits."}
::option[Der Eigentümer des Eintrags, sofern der erforderliche Verzeichniszugriff besteht.]{#sticky-bit-entry-owner .correct explanation="Der Eigentümer des Eintrags gehört zu den Identitäten, denen die Regel eines Verzeichnisses mit Sticky-Bit das Entfernen gewöhnlich erlaubt."}
::option[Ausschließlich ein Mitglied der Gruppe des Eintrags.]{#sticky-bit-entry-group explanation="Eine Gruppenmitgliedschaft allein ist keine durch das Sticky-Bit festgelegte Eigentumsausnahme."}
:::

## Das Bit an `/tmp` erkennen

Das temporäre Systemverzeichnis ist ein verbreitetes Beispiel:

```bash
$ ls -ld /tmp
drwxrwxrwt 17 root root 4096 Dec 15 11:45 /tmp
```

Das abschließende kleingeschriebene `t` steht an der Ausführungsposition für andere. Es bedeutet, dass sowohl das Sticky-Bit als auch die Ausführungsberechtigung für andere vorhanden sind. Ein großgeschriebenes `T` bedeutet, dass das Sticky-Bit gesetzt ist, während die Ausführungsberechtigung für andere fehlt.

Da `/tmp` gewöhnlich für alle beschreibbar und durchsuchbar ist, können mehrere Benutzer dort Einträge erstellen. Das Sticky-Bit verhindert, dass ein gewöhnlicher Benutzer die Einträge eines anderen allein deshalb entfernen kann, weil das Verzeichnis für alle beschreibbar ist. Anwendungen müssen temporäre Objekte weiterhin sicher erstellen, da vorhersehbare Namen, unsichere Links und schwache Dateimodi getrennte Risiken darstellen.

:::single-choice{#sticky-bit-lowercase-t}
Was zeigt ein kleingeschriebenes `t` am Ende eines Verzeichnismodus an?

::option[Sticky-Bit und Ausführungsberechtigung für andere sind gesetzt.]{#sticky-bit-t-with-execute .correct explanation="Ein kleingeschriebenes `t` verbindet das besondere Sticky-Bit mit dem gewöhnlichen Ausführungsbit für andere."}
::option[Das Sticky-Bit ist gesetzt, aber die Ausführungsberechtigung für andere fehlt.]{#sticky-bit-t-without-execute explanation="Diese Kombination wird als großgeschriebenes `T` dargestellt."}
::option[Setgid und die Gruppenausführungsberechtigung sind gesetzt.]{#sticky-bit-setgid-position explanation="Setgid erscheint an der Gruppenausführungsposition und nicht an der abschließenden Position für andere."}
:::

## Das Sticky-Bit setzen und entfernen

Setze das Bit symbolisch:

```bash
$ chmod +t shared-directory
```

In einer führenden oktalen Ziffer für besondere Bits trägt Sticky den Wert `1` bei:

```bash
$ chmod 1777 shared-directory
```

Die führende `1` setzt Sticky, während `777` den gewöhnlichen Modus angibt. Dieser Modus ist nur dann angemessen, wenn das Verzeichnis bewusst von allen lokalen Benutzern gemeinsam verwendet wird. Für ein Teamverzeichnis können engere Gruppenberechtigungen besser geeignet sein. Entferne ausschließlich das Sticky-Bit mit `chmod -t shared-directory`.

:::single-choice{#sticky-bit-octal-value}
Welcher führende oktale Wert steht für das Sticky-Bit?

::option[`2`]{#sticky-bit-value-two explanation="Eine führende `2` steht für setgid."}
::option[`1`]{#sticky-bit-value-one .correct explanation="Das Sticky-Bit trägt `1` zur führenden Ziffer für besondere Bits bei."}
::option[`4`]{#sticky-bit-value-four explanation="Eine führende `4` steht für setuid."}
:::

## Die vollständige Verzeichnisrichtlinie überprüfen

Sticky gewährt weder Schreib- noch Suchzugriff; es schränkt nur das Entfernen und Umbenennen ein, nachdem die gewöhnlichen Berechtigungen eine Änderung des Verzeichnisses erlauben. Prüfe Eigentümer, Gruppe, gewöhnlichen Modus, ACLs und Einhängekontext des Verzeichnisses gemeinsam. Teste in einer isolierten Umgebung mit unprivilegierten Konten, statt `/tmp` auf einem laufenden System zu verändern.

:::single-choice{#sticky-bit-access-scope}
Macht das Hinzufügen des Sticky-Bits ein nicht beschreibbares Verzeichnis für andere Benutzer beschreibbar?

::option[Ja; Sticky fügt automatisch für jede Klasse die Schreibberechtigung hinzu.]{#sticky-bit-adds-write explanation="Das besondere Bit schreibt die Schreibbits für Eigentümer, Gruppe oder andere nicht um."}
::option[Ja; Sticky deaktiviert das Berechtigungstripel für andere.]{#sticky-bit-disables-other explanation="Das Tripel für andere ist weiterhin an gewöhnlichen Zugriffsprüfungen beteiligt."}
::option[Nein; gewöhnliche Schreib- und Suchberechtigungen steuern den Zugriff weiterhin.]{#sticky-bit-no-write-grant .correct explanation="Sticky schränkt bestimmte Entfernungs- und Umbenennungsvorgänge ein, fügt aber keine fehlenden gewöhnlichen Berechtigungen hinzu."}
:::

Erstelle zum Üben ein entbehrliches gemeinsam genutztes Verzeichnis, setze einen passenden gewöhnlichen Modus und das Sticky-Bit und teste anschließend das Entfernen von Einträgen als zwei unprivilegierte Benutzer. Das Lab [Dateien löschen und verschieben](https://labex.io/labs/linux-delete-and-move-files-7777) kann die zugrunde liegenden Umbenennungs- und Löschvorgänge festigen.

## Zusammenfassung

Du kannst nun das Sticky-Bit auf gemeinsam genutzten Verzeichnissen erklären und überprüfen.

1. Setze Sticky mit Eigentumsbeschränkungen beim Entfernen und Umbenennen in Beziehung.
2. Erkenne ein kleingeschriebenes `t` und ein großgeschriebenes `T` in einer ausführlichen Auflistung.
3. Setze das Bit symbolisch oder mit dem führenden oktalen Wert `1`.
4. Bewerte Sticky zusammen mit den gewöhnlichen Verzeichnisberechtigungen.
