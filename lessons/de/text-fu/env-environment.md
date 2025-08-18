---
lang: "de"
title: "env (Umgebung)"
meta_title: "env (Umgebung) - Text-Fu"
meta_description: "Erfahren Sie mehr über Linux-Umgebungsvariablen mit dem Befehl 'env'. Verstehen Sie die Variablen PATH, HOME und USER. Erhalten Sie eine Einführung in die Verwaltung Ihrer Linux-Umgebung."
meta_keywords: "env Befehl, Linux Umgebungsvariablen, PATH Variable, Linux Tutorial, Linux für Anfänger, Shell Variablen, Linux Anleitung"
---

## Lesson Content

Führen Sie den folgenden Befehl aus:

```bash
echo $HOME
```

Sie sollten den Pfad zu Ihrem Home-Verzeichnis sehen; bei mir sieht er so aus: /home/pete.

Was ist mit diesem Befehl?

```bash
echo $USER
```

Sie sollten Ihren Benutzernamen sehen!

Woher kommen diese Informationen? Sie stammen aus Ihren Umgebungsvariablen. Sie können diese anzeigen, indem Sie Folgendes eingeben:

```bash
env
```

Dies gibt eine ganze Menge Informationen über die Umgebungsvariablen aus, die Sie derzeit gesetzt haben. Diese Variablen enthalten nützliche Informationen, die die Shell und andere Prozesse verwenden können.

Hier ist ein kurzes Beispiel:

```plaintext
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/bin
PWD=/home/user
USER=pete
```

Eine besonders wichtige Variable ist die PATH variable. Sie können auf diese Variablen zugreifen, indem Sie ein `$` vor den Variablennamen setzen, wie folgt:

```bash
$ echo $PATH
/usr/local/sbin:/usr/local/bin:/usr/sbin:/bin
```

Dies gibt eine Liste von Pfaden zurück, die durch einen Doppelpunkt getrennt sind und die Ihr System durchsucht, wenn es einen Befehl ausführt. Nehmen wir an, Sie laden ein Paket manuell aus dem Internet herunter und installieren es in einem nicht standardmäßigen Verzeichnis, und Sie möchten diesen Befehl ausführen. Sie geben `$ coolcommand` ein, und die Eingabeaufforderung sagt "command not found". Nun, das ist albern; Sie sehen die Binärdatei in einem Ordner und wissen, dass sie existiert. Was passiert, ist, dass die `$PATH` Variable dieses Verzeichnis nicht nach dieser Binärdatei durchsucht, daher wird ein Fehler ausgegeben.

Nehmen wir an, Sie hätten Tonnen von Binärdateien, die Sie aus diesem Verzeichnis ausführen wollten; Sie können einfach die PATH variable ändern, um dieses Verzeichnis in Ihre PATH Umgebungsvariable aufzunehmen.

## Exercise

Was gibt Folgendes aus? Warum?

```bash
echo $HOME
```

## Quiz Question

Wie sehen Sie Ihre Umgebungsvariablen?

## Quiz Answer

env
