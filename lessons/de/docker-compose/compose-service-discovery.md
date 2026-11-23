---
lesson_id: "compose-service-discovery"
course_id: "docker-compose"
lang: "de"
order_index: 3
title: "Dienstsuche"
description: "Lerne, wie Compose-Dienste einander per Namen erreichen und wie der Host einen veröffentlichten Port nutzt."
meta_title: "Dienstsuche - Docker Compose"
meta_description: "Lerne, wie Compose-Dienste einander per Namen erreichen und wie der Host einen veröffentlichten Port nutzt."
meta_keywords: "Dienstsuche, Dienstnamen, Compose-Netzwerk, Docker Compose, DevOps, Linux Journey"
---

Ein Browser auf dem Docker-Host erreicht den Webdienst über seine veröffentlichte Adresse. Ein zweiter Container im Projekt nimmt einen anderen Weg. Compose verbindet die Dienste eines Projekts normalerweise über ein gemeinsames Netzwerk. Dort können sich die Dienste anhand ihrer Namen finden.

## Die Seite aus dem Werkzeugcontainer abrufen

Kehre in den Übungsordner mit `compose.yaml` zurück. Wenn sich der Werkzeugcontainer seit der vorigen Lektion beendet hat, starte ihn mit `docker compose start toolbox` erneut. Sobald beide Dienste laufen, kannst du mit `docker compose exec` einen Befehl im laufenden Werkzeugcontainer ausführen. Der BusyBox-Befehl `wget` ruft eine Seite ab. Die Option `-q` blendet Fortschrittsmeldungen aus, und `-O -` gibt die Seite im Terminal aus.

```bash
$ docker compose exec -T toolbox wget -q -O - http://web:80/
```

Die Option `-T` verhindert, dass Compose ein interaktives Terminal zuweist. Die URL enthält den Namen des Webdienstes und seinen Container-Port. Bei Erfolg erscheint der HTML-Inhalt der Nginx-Seite.

:::single-choice{#compose-service-discovery-sibling-url} Über welche Adresse sollte ein anderer Dienst im selben Compose-Netzwerk auf den Webcontainer zugreifen?

::option[`http://web:80/`]{#compose-service-discovery-sibling-url-c .correct explanation="Das gemeinsame Netzwerk löst web zum gewünschten Dienst auf. Port 80 führt zu dem Programm, das dort auf Anfragen wartet."}
::option[`http://127.0.0.1:8080/`]{#compose-service-discovery-sibling-url-a explanation="Die Loopback-Adresse in diesem anderen Dienst verweist auf seine eigene Netzwerkumgebung."}
::option[`http://web:8080/`]{#compose-service-discovery-sibling-url-b explanation="Innerhalb des Netzwerks lauscht der Webdienst in diesem Beispiel an Port 80."}
:::

![HTML-Ausgabe im Werkzeugcontainer nach einem Abruf des Webdienstes über seinen Namen](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/docker-compose/compose-service-discovery/internal-request.png)

## Die passende Adresse auf dem Host wählen

Öffne auf dem Docker-Host `http://127.0.0.1:8080/`, wenn du die ursprüngliche Zuordnung beibehalten hast. Wenn du in der vorigen Lektion den Host-Port geändert hast, verwende im Browser den neuen Port. Der Werkzeugcontainer nutzt weiterhin `http://web:80/`. Er verbindet sich im Compose-Netzwerk, in dem der Dienstname `web` verfügbar ist.

:::single-choice{#compose-service-discovery-host-url} Du änderst den Host-Port in der Zuordnung auf 8081. Welche Beispieladresse musst du ebenfalls ändern?

::option[Die URL des Werkzeugcontainers mit web an Port 80.]{#compose-service-discovery-host-url-b explanation="Diese Verbindung führt weiterhin direkt zum Port des Webcontainers."}
::option[Beide Beispieladressen.]{#compose-service-discovery-host-url-c explanation="Geändert wurde nur der Port auf der Host-Seite."}
::option[Die Adresse, die der Browser auf dem Host verwendet.]{#compose-service-discovery-host-url-a .correct explanation="Der Browser stellt die Verbindung über den neu veröffentlichten Host-Port her."}
:::

## Einen stabilen Dienstnamen verwenden

Beim Austausch eines Containers kann sich seine Netzwerkadresse ändern. Sein Compose-Dienstname bleibt gleich. Ein Client kann den Namen erneut auflösen und die Verbindung wiederherstellen. Eine offene Verbindung zum ersetzten Container kann dabei abbrechen.

:::single-choice{#compose-service-discovery-replacement} Der Webcontainer wurde neu erstellt und hat jetzt eine andere Adresse. Was kann der Werkzeugcontainer für seine nächste Anfrage verwenden?

::option[Die alte Adresse aus dem ursprünglichen Container.]{#compose-service-discovery-replacement-a explanation="Einem neuen Container kann eine andere Netzwerkadresse zugewiesen werden."}
::option[Denselben Webdienstnamen und Container-Port.]{#compose-service-discovery-replacement-b .correct explanation="Über den Namen findet der Werkzeugcontainer den aktuellen Webcontainer im Projektnetzwerk."}
::option[Den eigenen Namen des Werkzeugcontainers.]{#compose-service-discovery-replacement-c explanation="Dieser Dienstname bezeichnet den Container, der die Anfrage ausführt."}
:::

## Zusammenfassung

Du kannst jetzt anhand des Ausgangspunkts einer Anfrage die passende Dienstadresse wählen.

1. Verwende im Projektnetzwerk den Dienstnamen und den Container-Port.
2. Verwende für den Browser auf dem Host eine veröffentlichte Adresse.
3. Löse den Dienstnamen erneut auf, wenn ein Container ausgetauscht wurde.
