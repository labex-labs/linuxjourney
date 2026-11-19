---
lesson_id: "compose-files"
course_id: "docker-compose"
lang: "de"
order_index: 1
title: "Compose-Dateien"
description: "Lerne, wie du in einer Compose-Datei Dienste, Images, Befehle und Ports findest."
meta_title: "Compose-Dateien - Docker Compose"
meta_description: "Lerne, wie du in einer Compose-Datei Dienste, Images, Befehle und Ports findest."
meta_keywords: "Compose-Datei, Dienste, Docker Compose, DevOps, Linux Journey"
---

Einen Webserver und sein Hilfsprogramm kannst du einmalig mit getrennten Befehlen starten. Eine **Compose-Datei** fasst die Einstellungen zusammen, damit du dieselben Dienste später erneut starten kannst. Für diesen Kurs brauchst du Docker mit dem Compose-Plug-in, das den Befehl `docker compose` bereitstellt.

## Zwei Dienste definieren

Lege einen neuen Übungsordner namens `journey-compose` an und speichere das folgende Beispiel dort als `compose.yaml`. Ein **Dienst** beschreibt, wie Compose einen Container ausführen soll. Diese Datei definiert einen Webserver und einen kleinen Werkzeugcontainer, der für spätere Prüfungen weiterläuft.

```yaml
services:
  web:
    image: nginx:alpine
    ports:
      - "127.0.0.1:8080:80"
  toolbox:
    image: busybox:1.36
    command: ["sleep", "3600"]
```

Verwende Leerzeichen zur Einrückung. Die eingerückten Schlüssel unter `web` gehören zu diesem Dienst. Der Bindestrich unter `ports` leitet einen Listeneintrag ein. Die eckigen Klammern bei `command` bilden ebenfalls eine Liste. Sie enthält hier den Programmnamen und das zugehörige Argument.

:::single-choice{#compose-files-service-images} Welcher Dienst verwendet das BusyBox-Image?

::option[Der Dienst web.]{#compose-files-service-images-a explanation="In der Image-Zeile von web steht nginx."}
::option[Der Dienst toolbox.]{#compose-files-service-images-c .correct explanation="Im Feld image von toolbox steht busybox:1.36."}
::option[Beide Dienste.]{#compose-files-service-images-b explanation="Jeder Dienst hat eine eigene Image-Einstellung."}
:::

## Die Einstellungen des Webdienstes lesen

Der Webdienst veröffentlicht Port 80 des Containers an Port 8080 des Hosts. Sobald der Dienst läuft, kann eine Anfrage an `http://127.0.0.1:8080` auf demselben Rechner Nginx erreichen. Der Werkzeugcontainer veröffentlicht keinen Port. Sein Befehl `sleep` hält ihn für die Übung 3.600 Sekunden lang am Laufen.

:::single-choice{#compose-files-mapping-owner} Welche Einstellung legt fest, wie ein Browser auf dem Docker-Host Nginx erreicht?

::option[Die Einstellung ports unter web.]{#compose-files-mapping-owner-a .correct explanation="Der Eintrag ordnet Adresse und Port des Hosts dem Webcontainer zu."}
::option[Das Image-Tag unter toolbox.]{#compose-files-mapping-owner-b explanation="Damit wählst du das Image für den Werkzeugcontainer."}
::option[Das Argument von sleep unter toolbox.]{#compose-files-mapping-owner-c explanation="Das Argument bestimmt, wie lange dieses Programm läuft."}
:::

## Die eingelesene Konfiguration prüfen

Führe den folgenden Befehl im Ordner mit der Datei aus. Gib den Befehl nach dem Promptzeichen `$` ein. Compose liest `compose.yaml` und gibt die erkannte Konfiguration aus. Suche nach den Einträgen `web` und `toolbox`. Kurze Einstellungen können in der Ausgabe ausführlicher dargestellt sein.

```bash
$ docker compose config
```

:::single-choice{#compose-files-config-scope} Der Befehl gibt zwei Dienste aus. Was hast du damit überprüft?

::option[Beide Container sind gestartet.]{#compose-files-config-scope-a explanation="Der Befehl liest die Einstellungen ein und zeigt sie an."}
::option[Der Browser hat eine erfolgreiche Antwort erhalten.]{#compose-files-config-scope-c explanation="Eine Anfrage kannst du prüfen, sobald der Server läuft."}
::option[Compose kann beide Dienstdefinitionen lesen.]{#compose-files-config-scope-b .correct explanation="Die eingelesene Konfiguration lässt sich schon vor dem Start prüfen."}
:::

## Zusammenfassung

Du kannst jetzt die Bestandteile einer einfachen Compose-Datei erkennen.

1. Lies die Namen und Image-Angaben unter services.
2. Ordne die Einstellungen eines Dienstes dem zugehörigen Container zu.
3. Prüfe die eingelesene Datei mit docker compose config.
