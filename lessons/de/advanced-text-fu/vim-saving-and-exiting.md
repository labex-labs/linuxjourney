---
lesson_id: "vim-saving-and-exiting"
course_id: "advanced-text-fu"
lang: "de"
order_index: 8
title: "In Vim speichern und Vim beenden"
description: "Lerne, wie du Änderungen in Vim schreibst, den Editor beendest, unter einem anderen Namen speicherst oder Änderungen bewusst verwirfst."
meta_title: "In Vim speichern und Vim beenden – Fortgeschrittenes Text-Fu"
meta_description: "Lerne, mit Befehlen wie :w in Vim zu speichern. Beherrsche das Speichern und Beenden mit :wq oder ZZ sowie das gezielte Verwerfen von Änderungen."
meta_keywords: "vim speichern, linux wq, vi schreiben und beenden, vim speichern und beenden, im vim editor speichern, datei in vim speichern, vim beenden, vim befehle"
---

Schreiben und Beenden sind in Vim getrennte Vorgänge. Bevor du einen Ex-Befehl eingibst, drückst du `Esc`, um in den Normalmodus zurückzukehren. Tippe dann `:`, gib den Befehl ein und drücke Enter. Lies Vims Status- oder Fehlermeldung, bevor du davon ausgehst, dass das Schreiben erfolgreich war.

## Den aktuellen Puffer schreiben

Mit `:w` schreibst du den aktuellen Puffer in die zugehörige Datei, ohne das Fenster zu schließen:

```vim
:w
```

Das Schreiben kann fehlschlagen, weil der Puffer keinen Dateinamen hat, das Verzeichnis nicht beschreibbar oder das Dateisystem voll ist oder eine andere Bedingung den Vorgang verhindert. Prüfe die von Vim ausgegebene Meldung.

Mit `:w copy.txt` schreibst du den aktuellen Puffer unter einen anderen Pfad, während der bisherige Name des aktuellen Puffers erhalten bleibt. Verwende `:saveas copy.txt`, wenn der Puffer den neuen Pfad übernehmen soll.

:::single-choice{#vim-save-without-quit} Welcher Vim-Befehl schreibt den aktuellen Puffer in die zugehörige Datei, ohne Vim zu beenden?

::option[`:q`]{#vim-save-q explanation="`:q` fordert das Beenden an und schreibt einen geänderten Puffer nicht."}
::option[`:w`]{#vim-save-w .correct explanation="Der Befehl `:write` speichert den aktuellen Puffer und lässt das Bearbeitungsfenster geöffnet."}
::option[`:q!`]{#vim-save-q-force explanation="`:q!` verwirft nicht gespeicherte Änderungen und beendet Vim; der Befehl speichert sie nicht."}
:::

## Einen unveränderten Puffer beenden

Mit `:q` schließt du das aktuelle Fenster, wenn dabei keine ungespeicherten Änderungen eines Puffers verloren gehen:

```vim
:q
```

Ist der aktuelle Puffer geändert und würden seine Änderungen verloren gehen, verweigert Vim das Beenden normalerweise und zeigt eine Warnung an. Dieser Schutz gibt dir Gelegenheit, die Änderungen zu schreiben oder deine Entscheidung zu überdenken.

:::single-choice{#vim-quit-clean-buffer} Welcher Befehl schließt das aktuelle Vim-Fenster, wenn dabei keine ungespeicherten Änderungen verloren gehen?

::option[`:w`]{#vim-quit-w explanation="Dieser Befehl schreibt den Puffer, lässt das aktuelle Fenster aber geöffnet."}
::option[`:q`]{#vim-quit-q .correct explanation="Der gewöhnliche Beenden-Befehl schließt das Fenster, sofern Vims Schutz für geänderte Puffer dies zulässt."}
::option[`u`]{#vim-quit-u explanation="`u` macht im Normalmodus eine Änderung rückgängig und schließt das Editorfenster nicht."}
:::

## Ungespeicherte Änderungen verwerfen

Verwende `:q!` nur, wenn du das aktuelle Fenster bewusst schließen und Änderungen aufgeben möchtest, die das Beenden sonst verhindern würden:

```vim
:q!
```

Das Ausrufezeichen setzt die Warnung wegen ungespeicherter Änderungen außer Kraft. Diese Änderungen am Puffer werden nicht geschrieben. Vergewissere dich deshalb vor dem Drücken von Enter, dass du sie wirklich nicht mehr brauchst.

:::single-choice{#vim-quit-discard-changes} Der aktuelle Puffer enthält Änderungen, die du bewusst nicht speichern möchtest. Welcher Befehl schließt das aktuelle Fenster und verwirft sie?

::option[`:q`]{#vim-discard-plain-q explanation="Das einfache `:q` verweigert den Vorgang normalerweise, wenn beim Beenden Änderungen am Puffer verloren gingen."}
::option[`:wq`]{#vim-discard-wq explanation="`:wq` schreibt die Änderungen vor dem Beenden und bewirkt damit das Gegenteil des Verwerfens."}
::option[`:q!`]{#vim-discard-q-force .correct explanation="Das Ausrufezeichen übergeht die Änderungswarnung und schließt das Fenster, ohne die ungespeicherten Änderungen zu schreiben."}
:::

## Schreiben und Beenden verbinden

Verwende `:wq`, wenn der Puffer geschrieben und das aktuelle Fenster nach erfolgreichem Schreiben geschlossen werden soll:

```vim
:wq
```

Schlägt das Schreiben fehl, führt Vim das angeforderte Beenden nicht aus. Behebe den Fehler, statt anzunehmen, dass die Daten auf dem Datenträger angekommen sind.

:::single-choice{#vim-write-and-quit} Welcher Befehl schreibt den aktuellen Puffer und schließt anschließend das aktuelle Fenster, sofern das Schreiben erfolgreich ist?

::option[`:wq`]{#vim-save-wq .correct explanation="Dieser Befehl verbindet Schreiben und Beenden, wobei das Beenden vom erfolgreichen Schreiben abhängt."}
::option[`:q!`]{#vim-save-force-quit explanation="Dieser Befehl beendet Vim und verwirft Änderungen, statt sie zu schreiben."}
::option[`:w copy.txt`]{#vim-save-copy explanation="Dieser Befehl schreibt unter einen anderen Pfad, lässt das Bearbeitungsfenster aber geöffnet."}
:::

## :x und ZZ verwenden

`:x` schreibt den Puffer nur, wenn er geändert wurde, und beendet Vim anschließend. Im Normalmodus bewirkt das großgeschriebene `ZZ` dasselbe:

```vim
:x
```

```text
ZZ
```

Das unterscheidet sich geringfügig von `:wq`, das auch bei einem unveränderten Puffer einen Schreibvorgang anfordert. Das großgeschriebene `ZQ` ist im Normalmodus das Gegenstück für das Beenden ohne Schreiben, ähnlich wie `:q!`.

:::single-choice{#vim-write-if-modified-quit} Welcher Befehl des Normalmodus schreibt nur bei einem geänderten Puffer und beendet Vim anschließend?

::option[`ZZ`]{#vim-save-zz .correct explanation="Das großgeschriebene `ZZ` schreibt bei Bedarf und beendet Vim anschließend, genau wie `:x`."}
::option[`zz`]{#vim-center-screen explanation="Das kleingeschriebene `zz` zentriert die aktuelle Zeile im Fenster; es speichert und beendet nicht."}
::option[`ZQ`]{#vim-quit-zq explanation="Das großgeschriebene `ZQ` beendet Vim ohne zu schreiben und verwirft somit ungespeicherte Änderungen."}
:::

Sind mehrere Fenster oder Puffer beteiligt, schließt ein Befehl möglicherweise nur das aktuelle Fenster. Befehle wie `:qa`, `:wqa` und `:qa!` wirken über mehrere Fenster hinweg. Prüfe jedoch jeden geänderten Puffer, bevor du einen erzwungenen Befehl für alle Fenster verwendest.

Mit diesem praktischen Lab kannst du das Schreiben und Beenden an einer entbehrlichen Datei üben:

1. **[Textdateien unter Linux mit Vim und Nano bearbeiten](https://labex.io/labs/comptia-edit-text-files-in-linux-with-vim-and-nano-591076)** – Übe, Dateien anzulegen, Text zu bearbeiten und zu speichern sowie mit Vim und Nano zu navigieren. Das Lab festigt dein Verständnis grundlegender Vim-Abläufe einschließlich des Speicherns und Beendens.

## Zusammenfassung

Du kannst nun den Vim-Befehl zum Beenden passend zu deinen ungespeicherten Daten auswählen.

1. Schreibe mit `:w`, ohne Vim zu beenden.
2. Beende Vim sicher mit `:q`, wenn keine Änderungen verloren gehen.
3. Verwirf Änderungen bewusst mit `:q!`.
4. Schreibe und beende mit `:wq`.
5. Verwende `:x` oder `ZZ`, um nur bei Änderungen zu schreiben.
