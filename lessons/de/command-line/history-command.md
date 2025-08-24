---
index: 9
lang: "de"
title: "history"
meta_title: "history - Befehlszeile"
meta_description: "Erfahren Sie, wie Sie den Linux-Befehl history, die Verknüpfung !! und Ctrl-R für den effizienten Befehlsabruf verwenden. Verbessern Sie Ihre Terminalproduktivität mit diesen wichtigen Tipps!"
meta_keywords: "Linux history, bash history, Ctrl-R, clear command, Linux tutorial, command line, beginner guide"
---

## Lesson Content

In Ihrer Shell gibt es eine Historie der zuvor eingegebenen Befehle. Sie können diese Befehle tatsächlich durchsuchen. Dies ist sehr nützlich, wenn Sie einen zuvor verwendeten Befehl finden und ausführen möchten, ohne ihn erneut eingeben zu müssen.

```bash
history
```

Möchten Sie denselben Befehl wie zuvor ausführen? Drücken Sie einfach die Pfeiltaste nach oben.

Möchten Sie den vorherigen Befehl ausführen, ohne ihn erneut einzugeben? Verwenden Sie `!!`. Wenn Sie `cat file1` eingegeben haben und es erneut ausführen möchten, können Sie einfach `!!` eingeben, und der zuletzt ausgeführte Befehl wird ausgeführt.

Eine weitere Verknüpfung für die Historie ist `Ctrl-R`. Dies ist der Befehl für die umgekehrte Suche. Wenn Sie `Ctrl-R` drücken und anfangen, Teile des gewünschten Befehls einzugeben, werden Ihnen Übereinstimmungen angezeigt. Sie können durch diese navigieren, indem Sie die Taste `Ctrl-R` erneut drücken. Sobald Sie den Befehl gefunden haben, den Sie erneut verwenden möchten, drücken Sie einfach die Eingabetaste.

Unser Terminal wird etwas unübersichtlich, nicht wahr? Lassen Sie uns ein wenig aufräumen. Verwenden Sie den Befehl `clear`, um Ihre Anzeige zu löschen.

```bash
clear
```

So, das sieht besser aus, oder?

Wo wir gerade von nützlichen Dingen sprechen: Eine der nützlichsten Funktionen in jeder Befehlszeilenumgebung ist die Tab-Vervollständigung. Wenn Sie den Anfang eines Befehls, einer Datei, eines Verzeichnisses usw. eingeben und die Tab-Taste drücken, wird die Eingabe automatisch vervollständigt, basierend auf dem, was im durchsuchten Verzeichnis gefunden wird, solange keine anderen Dateien mit diesen Buchstaben beginnen. Wenn Sie beispielsweise versuchen würden, den Befehl `chrome` auszuführen, können Sie `chr` eingeben und Tab drücken, und es wird zu `chrome` vervollständigt.

## Exercise

Navigieren Sie mit den Auf- und Ab-Tasten durch Ihre vorherige Befehlshistorie. Spielen Sie mit der `Ctrl-R` Rückwärtssuche herum.

Für zusätzliche praktische Übungen zur Navigation in der Linux-Befehlszeile erkunden Sie diese interaktiven Labs:

- [Linux Directory Navigation](https://labex.io/de/labs/linux-directory-navigation-387844)
- [Linux ls Command: Content Listing](https://labex.io/de/labs/linux-linux-ls-command-content-listing-219205)

## Quiz Question

Was ist der Befehl, um das Terminal zu leeren?

## Quiz Answer

clear
