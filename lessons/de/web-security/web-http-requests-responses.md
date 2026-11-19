---
lesson_id: "web-http-requests-responses"
course_id: "web-security"
lang: "de"
order_index: 1
title: "HTTP-Anfragen und -Antworten"
description: "Lerne, Methode, Pfad, Status und Inhaltstyp in einem HTTP-Austausch zu lesen."
meta_title: "HTTP-Anfragen und -Antworten - Websicherheit"
meta_description: "Lerne, Methode, Pfad, Status und Inhaltstyp in einem HTTP-Austausch zu lesen."
meta_keywords: "HTTP-Anfragen, HTTP-Antworten, Websicherheit, Cybersicherheit, Linux Journey"
---

Ein Browser oder ein anderer Client fordert etwas von einem Webserver an, indem er eine **HTTP-Anfrage** sendet. Der Server gibt eine **HTTP-Antwort** zurück. In den beiden Nachrichten kannst du nachlesen, was der Client angefragt und was der Server zurückgegeben hat.

## Die Anfrage lesen

Hier siehst du eine kurze HTTP/1.1-Anfrage. `GET` ist die Methode. Sie beschreibt, welche Aktion der Client anfordert. `/health` ist der Pfad. Der Header `Host` nennt die Website, an die sich der Client wendet.

```http
GET /health HTTP/1.1
Host: site.example
```

Ein **Header** ist ein benanntes Feld mit Informationen über die Nachricht. Methode und Pfad stehen in der ersten Zeile der Anfrage.

:::single-choice{#web-http-requests-responses-request-path} Was soll der Server für den Client abrufen?

::option[Eine Datei mit dem Namen HTTP/1.1.]{#web-http-requests-responses-request-path-b explanation="Dieses Feld gibt die Protokollversion an."}
::option[Die Ressource unter /health.]{#web-http-requests-responses-request-path-a .correct explanation="Der Pfad steht in der ersten Zeile nach GET."}
::option[Eine Ressource unter /site.example.]{#web-http-requests-responses-request-path-c explanation="Der Header Host nennt die Website. Der Pfad steht in der ersten Zeile."}
:::

## Eine Antwort lesen

Erstelle in einem leeren Übungsverzeichnis eine Seite und starte einen Python-HTTP-Server auf der Loopback-Adresse. Die Umleitung schreibt die Seite in eine Datei. Lass den Server in diesem Terminal laufen, bis die Anfrage abgeschlossen ist, und beende ihn dann mit Strg+C.

```bash
$ mkdir web-demo
$ printf '%s\n' ready > web-demo/health.txt
$ python3 -m http.server 8094 --bind 127.0.0.1 --directory web-demo
```

Führe in einem zweiten Terminal auf demselben Rechner `curl -i` aus. Mit dieser Option erscheinen die Antwortheader vor dem Inhalt der Antwort.

```bash
$ curl -i http://127.0.0.1:8094/health.txt
```

In der ersten Zeile der Antwort steht ein **Statuscode**. `200` bedeutet, dass diese Anfrage erfolgreich war. Eine Leerzeile trennt die Header vom Antworttext. `Content-Type` gibt an, wie der Client den Inhalt interpretieren soll, zum Beispiel als Klartext.

:::single-choice{#web-http-requests-responses-response-parts} Welche Angabe hilft dem Client bei der Darstellung des Inhalts?

::option[Der Antwortheader Content-Type.]{#web-http-requests-responses-response-parts-b .correct explanation="Er beschreibt den Typ des Antwortinhalts."}
::option[Der Hostname in der ursprünglichen Anfrage.]{#web-http-requests-responses-response-parts-a explanation="Er bezeichnet die Website, an die sich der Client gewendet hat."}
::option[Allein der Pfad.]{#web-http-requests-responses-response-parts-c explanation="Der Pfad bezeichnet die Ressource und gibt kein Format für den zurückgegebenen Inhalt vor."}
:::

![Aufgezeichnete HTTP-Antwort aus LabEx mit Status 200, einem Text-Inhaltstyp und ready als Antwortinhalt](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/web-security/web-http-requests-responses/http-response.png)

## Zwei Ergebnisse vergleichen

Eine Antwort mit `404` meldet, dass der Server die angeforderte Ressource nicht gefunden hat oder sie nicht offenlegt. Eine Website kann für einen Pfad 200 und für einen anderen 404 zurückgeben. Achte beim Vergleich der Ergebnisse auf die genaue Methode und den genauen Pfad.

:::single-choice{#web-http-requests-responses-health-scope} Eine Anfrage an /health erhält 200. Was kannst du daraus über /welcome schließen?

::option[/welcome hat ebenfalls 200 zurückgegeben.]{#web-http-requests-responses-health-scope-a explanation="Im Beispiel wurde ein anderer Pfad geprüft."}
::option[Der Host war nicht erreichbar.]{#web-http-requests-responses-health-scope-b explanation="Für den Healthcheck kam eine Antwort zurück."}
::option[Du musst /welcome anfragen, um das Ergebnis zu erfahren.]{#web-http-requests-responses-health-scope-c .correct explanation="Die beiden Pfade können sich unterschiedlich verhalten."}
:::

Mit [Serververbindungen mit curl unter Linux testen](https://labex.io/tutorials/linux-how-to-test-server-connectivity-with-curl-in-linux-415082) kannst du üben, Antwortheader und Erreichbarkeit zu prüfen.

## Zusammenfassung

Du kannst jetzt die wichtigsten Teile eines einfachen HTTP-Austauschs lesen.

1. Finde Methode, Pfad und Host in einer Anfrage.
2. Lies Status und Inhaltstyp in einer Antwort.
3. Beschreibe das Ergebnis für genau die Anfrage, die gestellt wurde.
