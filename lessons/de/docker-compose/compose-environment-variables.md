---
lesson_id: "compose-environment-variables"
course_id: "docker-compose"
lang: "de"
order_index: 5
title: "Umgebungsvariablen"
description: "Lerne, wie du Werte, die Compose in eine Datei einsetzt, von Werten unterscheidest, die im Container ankommen."
meta_title: "Umgebungsvariablen - Docker Compose"
meta_description: "Lerne, wie du Werte, die Compose in eine Datei einsetzt, von Werten unterscheidest, die im Container ankommen."
meta_keywords: "Umgebungsvariablen, Interpolation, Docker Compose, DevOps, Linux Journey"
---

Eine Umgebungsvariable ist ein benannter Wert, den ein Programm lesen kann. Compose kann Variablen an zwei Stellen nutzen. Beim Einlesen der Datei kann es einen Wert in die Konfiguration einsetzen. Außerdem kann es Werte an ein Programm im Container übergeben.

## Einen Wert in die Datei einsetzen

Speichere dieses Beispiel als `compose.env.yaml` in deinem Übungsordner. Der Ausdruck `${PAGE_MODE:-demo}` verwendet den Wert von `PAGE_MODE`, wenn die Variable gesetzt und ihr Wert nicht leer ist. Andernfalls verwendet Compose `demo`.

```yaml
services:
  toolbox:
    image: busybox:1.36
    environment:
      PAGE_MODE: "${PAGE_MODE:-demo}"
```

Compose wertet den Ausdruck aus, bevor es den Container erstellt. Das nennt man **Interpolation**. Mit derselben Technik lässt sich etwa in einer anderen Datei ein Host-Port oder ein Image-Tag auswählen.

:::single-choice{#compose-environment-variables-interpolate-default} Welcher Wert steht in der ausgegebenen Konfiguration, wenn PAGE_MODE nicht gesetzt ist?

::option[Der unveränderte Ausdruck aus der Datei.]{#compose-environment-variables-interpolate-default-a explanation="Compose wertet den Ausdruck beim Einlesen der Datei aus."}
::option[Ein automatisch erzeugter Containername.]{#compose-environment-variables-interpolate-default-c explanation="Der Containername und der Umgebungswert werden unabhängig voneinander festgelegt."}
::option[Demo, der Wert nach dem Operator für den Standardwert.]{#compose-environment-variables-interpolate-default-b .correct explanation="Der Ausdruck legt demo als Ersatzwert fest."}
:::

## Den eingesetzten Wert anzeigen

Eine Variablenzuweisung vor einem Befehl setzt die Variable für genau diesen Aufruf. Damit kannst du ausprobieren, wie sich ein anderer Wert auswirkt. Der Befehl `config` gibt die aufgelösten Einstellungen aus, ohne einen Container zu erstellen.

```bash
$ PAGE_MODE=review docker compose -p journey-env -f compose.env.yaml config
```

Suche in den Umgebungseinstellungen des Dienstes nach `PAGE_MODE: review`. Der Wert `review` dient nur als Beispiel. Vertrauliche Werte gehören weder in Beispielkonfigurationen noch in deren Ausgabe.

:::single-choice{#compose-environment-variables-config-scope} Die ausgegebene Konfiguration zeigt review. Was ist bis hierhin passiert?

::option[Ein Dienst wurde bereits mit diesem Wert gestartet.]{#compose-environment-variables-config-scope-b explanation="Das Anzeigen der aufgelösten Konfiguration und das Starten eines Containers sind getrennte Vorgänge."}
::option[Compose hat den Wert beim Einlesen der Konfiguration eingesetzt.]{#compose-environment-variables-config-scope-a .correct explanation="Der Befehl config zeigt die aufgelösten Einstellungen an, bevor etwas gestartet wird."}
::option[Alle vorhandenen Container verwenden jetzt den Wert.]{#compose-environment-variables-config-scope-c explanation="Dieser Aufruf ändert keine laufenden Container."}
:::

## Einen Wert an den Container übergeben

Der Abschnitt `environment` übergibt den eingesetzten Wert an einen neuen Container. Mit `printenv` lässt du den Wert im eigens für den Aufruf gestarteten Container ausgeben.

```bash
$ PAGE_MODE=review docker compose -p journey-env -f compose.env.yaml run --rm toolbox printenv PAGE_MODE
```

Erwarte die Ausgabe `review`. Die Interpolation bestimmt den Wert, und der Umgebungseintrag übergibt ihn an den Container. Eine Variable, die nur den Host-Port festlegt, wird dadurch nicht automatisch Teil der Programmumgebung.

:::single-choice{#compose-environment-variables-actual-value} Wie prüfst du, welchen Wert das Programm im Werkzeugcontainer erhält?

::option[Gib PAGE_MODE im Container aus.]{#compose-environment-variables-actual-value-c .correct explanation="Die Umgebung des Programms zeigt, welcher Wert tatsächlich angekommen ist."}
::option[Lies nur den Standardwert in der ursprünglichen Datei.]{#compose-environment-variables-actual-value-a explanation="Ein anderer Wert kann den Standard aus der Datei ersetzen."}
::option[Ermittle die IP-Adresse des Werkzeugcontainers.]{#compose-environment-variables-actual-value-b explanation="Die Adresse gibt keinen Aufschluss über die Einstellungen des Programms."}
:::

## Zusammenfassung

Du kannst jetzt die beiden Verwendungen von Umgebungsvariablen unterscheiden.

1. Lies einen Ausdruck mit Standardwert in einer Compose-Datei.
2. Prüfe die aufgelöste Konfiguration vor dem Containerstart.
3. Prüfe den Wert in der Umgebung des gestarteten Programms.
