---
lesson_id: "setuid-set-user-id"
course_id: "permissions"
lang: "de"
order_index: 5
title: "Setuid"
description: "Erfahre, wie sich das Set-User-ID-Modusbit auf ausführbare Programme auswirkt und warum es eine sorgfältige Sicherheitsprüfung erfordert."
meta_title: "Setuid – Berechtigungen"
meta_description: "Lerne Linux-Setuid-Berechtigungen (SUID), ihre Funktionsweise und ihre Änderung kennen. Verstehe SUID für den sicheren Dateizugriff unter Linux."
meta_keywords: "Linux Setuid, SUID, Linux-Berechtigungen, chmod, passwd-Befehl, Linux-Sicherheit, Linux für Einsteiger, Linux-Tutorial"
---

Einige Programme benötigen eng begrenzten Zugriff, den ihre Aufrufer gewöhnlich nicht besitzen. Bei einer ausführbaren regulären Datei kann das Set-User-ID-Bit bewirken, dass ein neuer Prozess die Benutzer-ID des Dateieigentümers als effektive Benutzer-ID erhält. Das Programm kann dann Vorgänge ausführen, die für diese Identität autorisiert sind, und zugleich Informationen über den Aufrufer behalten.

Setuid ist keine allgemeine Anweisung, ein Programm „als root auszuführen“. Seine Wirkung hängt vom Eigentümer der ausführbaren Datei, vom Betriebssystem, vom Dateisystem und seinen Einhängeoptionen sowie davon ab, wie das Programm seine Zugangsdaten verwaltet.

## Setuid erkennen

Auf Systemen, die eine setuid-fähige ausführbare Datei `passwd` verwenden, kann eine ausführliche Auflistung so aussehen:

```bash
$ ls -l /usr/bin/passwd
-rwsr-xr-x 1 root root 68248 Jan 10 09:30 /usr/bin/passwd
```

Das kleingeschriebene `s` an der Ausführungsposition des Eigentümers bedeutet, dass sowohl setuid als auch die Ausführungsberechtigung des Eigentümers gesetzt sind. Wenn setuid vorhanden ist, aber die Ausführungsberechtigung des Eigentümers fehlt, zeigt `ls -l` an dieser Stelle ein großgeschriebenes `S` an.

Gehe nicht davon aus, dass jede Distribution denselben Modus oder denselben Authentifizierungsaufbau besitzt. Prüfe das tatsächliche System, statt dich auf das Beispiel zu verlassen.

:::single-choice{#setuid-lowercase-s} Was zeigt ein kleingeschriebenes `s` an der Ausführungsposition des Eigentümers an?

::option[Setuid ist gesetzt, aber die Ausführungsberechtigung des Eigentümers fehlt.]{#setuid-s-without-execute explanation="Diese Kombination wird als großgeschriebenes `S` und nicht als kleingeschriebenes `s` dargestellt."}
::option[Die Datei besitzt ein Sticky-Bit und die Gruppenausführungsberechtigung.]{#setuid-sticky-group explanation="Das Sticky-Bit erscheint an der Ausführungsposition für andere, während setuid an der Eigentümerposition steht."}
::option[Setuid und die Ausführungsberechtigung des Eigentümers sind gesetzt.]{#setuid-s-with-execute .correct explanation="Ein kleingeschriebenes `s` steht für das setuid-Bit zusammen mit dem gewöhnlichen Ausführungsbit des Eigentümers."}
:::

## Die Änderung der Zugangsdaten verstehen

Wenn der Kernel setuid bei der Ausführung berücksichtigt, erhält der neue Prozess gewöhnlich eine effektive Benutzer-ID, die sich aus dem Eigentümer der ausführbaren Datei ableitet. Bei einem root gehörenden Programm kann dies von root autorisierten Zugriff gewähren, allerdings nur während der Programmausführung und nur über die Vorgänge, die sein Code tatsächlich ausführt.

Dieser Mechanismus kann einem sorgfältig geschriebenen Programm ermöglichen, eine Anfrage zu validieren und eine begrenzte Änderung an geschützten Zuständen vorzunehmen. Ein lokales Werkzeug zur Passwortänderung kann beispielsweise kontrollierten Zugriff auf Authentifizierungsdaten benötigen, die gewöhnliche Benutzer nicht direkt bearbeiten dürfen. Moderne Implementierungen stützen sich außerdem auf PAM, Dateisperren, Richtlinien und weitere Schutzmaßnahmen; setuid allein erklärt nicht den gesamten Arbeitsablauf.

:::single-choice{#setuid-effective-identity} Welche Identität wird bei einer berücksichtigten setuid-Datei hauptsächlich vom Dateieigentümer übernommen?

::option[Der in `/etc/passwd` gespeicherte Anmeldename.]{#setuid-login-name explanation="Die Ausführung einer Datei schreibt weder den Kontoeintrag noch den Anmeldenamen des Aufrufers um."}
::option[Die effektive Benutzer-ID des Prozesses.]{#setuid-effective-user .correct explanation="Der Set-User-ID-Ausführungsmechanismus ändert die effektive Benutzeridentität, die für viele Autorisierungsprüfungen verwendet wird."}
::option[Der Gruppeneigentümer jeder geöffneten Datei.]{#setuid-opened-file-group explanation="Setuid beeinflusst Prozesszugangsdaten und nicht die Eigentumsmetadaten unabhängiger Dateien."}
:::

## Das Bit setzen und entfernen

Setze setuid symbolisch mit:

```bash
$ sudo chmod u+s myfile
```

In oktaler Schreibweise trägt setuid `4` zu einer führenden Ziffer für besondere Bits bei:

```bash
$ sudo chmod 4755 myfile
```

Hier setzt die führende `4` setuid, während `755` die gewöhnlichen Bits für Eigentümer, Gruppe und andere festlegt. Entferne setuid mit `chmod u-s myfile`, ohne den restlichen Modus zu ändern.

:::single-choice{#setuid-octal-value} Welcher führende oktale Wert steht für das besondere setuid-Bit?

::option[`4`]{#setuid-octal-four .correct explanation="Setuid trägt den Wert `4` zur führenden Ziffer für besondere Bits bei."}
::option[`1`]{#setuid-octal-one explanation="Eine führende `1` steht für das Sticky-Bit."}
::option[`2`]{#setuid-octal-two explanation="Eine führende `2` steht für das setgid-Bit."}
:::

## Setuid als sicherheitskritisch behandeln

Ein Fehler in einem privilegierten setuid-Programm kann zu einem Weg für Rechteausweitung werden. Solche Programme müssen Eingaben validieren, die als vertrauenswürdig behandelte Umgebung und Dateipfade kontrollieren, unsicheres Verhalten bei Unterprozessen vermeiden, privilegierten Code minimieren und erhöhte Zugangsdaten so früh wie möglich ablegen.

Linux berücksichtigt setuid bei interpretierten Skripten gewöhnlich nicht, weil eine sichere Umsetzung Probleme mit Race Conditions und Interpretern mit sich bringt. Mit `nosuid` eingehängte Dateisysteme unterdrücken außerdem die Wirkung von setuid und setgid. Bevorzuge engere Mechanismen wie durch Dienste vermittelte Vorgänge, sorgfältig begrenzte `sudo`-Richtlinien oder Capabilities, wenn sie zur Anforderung passen.

Füge niemals einer beliebigen Shell, einem Interpreter oder einem kopierten Programm experimentell setuid auf einem gemeinsam genutzten System hinzu. Prüfe bestehende setuid-Dateien und übe ausschließlich in einer isolierten, entbehrlichen Umgebung.

:::single-choice{#setuid-nosuid-mount} Welchen Zweck hat das Einhängen eines Dateisystems mit `nosuid`?

::option[Alle auf Dateien dieses Dateisystems gespeicherten Ausführungsbits zu entfernen.]{#setuid-nosuid-remove-execute explanation="Die Option schreibt gewöhnliche Ausführungsbits in Dateimetadaten nicht um."}
::option[Die Ausführungswirkung von setuid und setgid auf diesem Dateisystem zu unterdrücken.]{#setuid-nosuid-suppress .correct explanation="Die Einhängeoption `nosuid` verhindert, dass diese besonderen Modusbits ihr gewöhnliches Verhalten zur Änderung von Zugangsdaten bei der Ausführung entfalten."}
::option[Alle Dateien auf dem Dateisystem root zuzuweisen.]{#setuid-nosuid-root-owner explanation="Das Einhängen mit `nosuid` ändert keine Benutzer- oder Gruppeneigentumsfelder."}
:::

## Zusammenfassung

Du kannst nun setuid erkennen und seine Auswirkungen auf Zugangsdaten und Sicherheit erklären.

1. Finde `s` oder `S` an der Ausführungsposition des Eigentümers.
2. Setze die setuid-Ausführung mit der effektiven Benutzeridentität des Eigentümers der ausführbaren Datei in Beziehung.
3. Setze oder entferne das Bit mit symbolischen oder oktalen `chmod`-Modi.
4. Behandle jede privilegierte ausführbare Datei als sicherheitskritischen Code.
