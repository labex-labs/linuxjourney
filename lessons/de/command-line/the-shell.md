---
lang: "de"
title: "Die Shell"
meta_description: "Erfahren Sie mehr über die Linux-Shell, Bash und grundlegende Befehle wie 'echo'. Verstehen Sie Shell-Prompts und beginnen Sie Ihre Linux-Reise mit diesem anfängerfreundlichen Leitfaden."
meta_keywords: "Linux-Shell, Bash, echo-Befehl, Linux-Tutorial, Befehlszeile, Linux für Anfänger, Shell-Prompt, Linux-Leitfaden"
---

## Lesson Content

Die Welt steht Ihnen offen, oder besser gesagt, die Shell steht Ihnen offen. Was ist die Shell? Die Shell ist im Grunde ein Programm, das Ihre Befehle von der Tastatur entgegennimmt und an das Betriebssystem sendet, um sie auszuführen. Wenn Sie schon einmal eine GUI verwendet haben, haben Sie wahrscheinlich Programme wie "Terminal" oder "Konsole" gesehen; dies sind lediglich Programme, die eine Shell für Sie starten. Während dieses gesamten Kurses werden wir die Wunder der Shell kennenlernen.

In diesem Kurs werden wir das Shell-Programm Bash (Bourne Again Shell) verwenden. Fast alle Linux-Distributionen verwenden standardmäßig die Bash-Shell. Es gibt andere Shells, wie `ksh`, `zsh` und `tsch`, aber auf diese werden wir nicht eingehen.

Legen wir gleich los! Je nach Distribution kann sich Ihr Shell-Prompt ändern, aber größtenteils sollte er dem folgenden Format entsprechen:

```plaintext
username@hostname:current_directory
pete@icebox:/home/pete $
```

Beachten Sie das `$` am Ende des Prompts? Verschiedene Shells haben unterschiedliche Prompts. In unserem Fall steht das `$` für einen normalen Benutzer, der Bash, Bourne oder Korn Shell verwendet. Sie fügen das Prompt-Symbol nicht hinzu, wenn Sie den Befehl eingeben; wissen Sie einfach, dass es da ist.

Beginnen wir mit einem einfachen Befehl, `echo`. Der Befehl `echo` gibt einfach die Textargumente auf dem Bildschirm aus.

```bash
echo Hello World
```

## Exercise

Try some other Linux commands and see what they output:

1. `$ date`
2. `$ whoami`

## Quiz Question

Was sollte auf dem Bildschirm ausgegeben werden, wenn Sie `echo Hello World` eingeben?

## Quiz Answer

Hello World
