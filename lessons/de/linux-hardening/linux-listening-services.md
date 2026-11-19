---
lesson_id: "linux-listening-services"
course_id: "linux-hardening"
lang: "de"
order_index: 4
title: "Lauschende Dienste"
description: "Lerne, die Adresse eines lauschenden Linux-Dienstes zu lesen und seine Erreichbarkeit vom passenden Standort zu prüfen."
meta_title: "Lauschende Dienste - Linux-Härtung"
meta_description: "Lerne, die Adresse eines lauschenden Linux-Dienstes zu lesen und seine Erreichbarkeit vom passenden Standort zu prüfen."
meta_keywords: "Lauschende Dienste, Linux-Härtung, Cybersicherheit, Linux Journey"
---

Ein Dienst kann auf einer bestimmten Adresse und einem Port auf Verbindungen warten. Ein **lauschender Socket** ist bereit, eingehende Verbindungen anzunehmen. Seine Adresse gibt dir einen Hinweis darauf, wer ihn erreichen kann.

## Lauschende TCP-Sockets auflisten

Führe diesen Befehl auf einem Linux-Übungshost aus. Er ändert nichts am System. Mit den Optionen zeigt `ss` lauschende TCP-Sockets mit numerischen Adressen und Ports an.

```bash
$ ss -lnt
```

Sieh dir die Spalte mit der lokalen Adresse an. Im Beispiel verwendet eine Webvorschau `127.0.0.1:8091`. Der Port ist 8091. Die **Loopback-Adresse** verweist auf den Host selbst.

:::single-choice{#linux-listening-services-local-listener} Ein Browser auf demselben Host benötigt die Vorschau aus dem Beispiel. Welche Adresse sollte er verwenden?

::option[0.0.0.0:8091.]{#linux-listening-services-local-listener-a explanation="Diese Schreibweise gibt an, auf welchen Adressen ein Dienst lauscht. Hier ist eine konkrete Zieladresse angegeben."}
::option[127.0.0.1:8091.]{#linux-listening-services-local-listener-b .correct explanation="Der Dienst lauscht auf dieser Loopback-Adresse und auf diesem Port."}
::option[Port 80 auf einem anderen Server.]{#linux-listening-services-local-listener-c explanation="Der Dienst im Beispiel verwendet Port 8091 auf seinem eigenen Host."}
:::

![Aufgezeichnete ss-Ausgabe von LabEx für den Übungsdienst auf dem Loopback-Port 8091](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/linux-hardening/linux-listening-services/loopback-listener.png)

## Alle Schnittstellen einordnen

Die lokale IPv4-Adresse `0.0.0.0:8091` bedeutet, dass der Dienst auf allen IPv4-Schnittstellen des Hosts lauscht. Dazu können Schnittstellen gehören, die von anderen Rechnern aus erreichbar sind. Die Liste zeigt, auf welchen lokalen Adressen der Prozess Verbindungen annimmt. Firewall-Regeln und Routen können begrenzen, welche davon ein anderer Rechner erreicht.

:::single-choice{#linux-listening-services-all-interfaces} Ein Dienst wechselt auf demselben Port von 127.0.0.1 zu 0.0.0.0. Was ändert sich?

::option[Er kann auf mehr IPv4-Schnittstellen lauschen.]{#linux-listening-services-all-interfaces-a .correct explanation="Mit dieser Einstellung kann der Dienst Verbindungen auf mehr lokalen Adressen annehmen."}
::option[Er lauscht jetzt auf einem anderen Port.]{#linux-listening-services-all-interfaces-b explanation="Die Portnummer ist gleich geblieben."}
::option[Er ist garantiert sofort aus jedem Netz erreichbar.]{#linux-listening-services-all-interfaces-c explanation="Netzwerkregeln und Routen bestimmen weiterhin, über welche Wege er erreichbar ist."}
:::

## Den vorgesehenen Zugriffsweg prüfen

Ein interner Dienst für Mitarbeitende kann für ein einzelnes Netz vorgesehen sein. Prüfe ihn aus diesem Netz. Prüfe bei Bedarf auch von einem freigegebenen Teststandort außerhalb, ob die Beschränkung greift. Kontrolliere sowohl den lauschenden Dienst als auch den Zugriffsweg. Die lokale Liste allein zeigt nicht, was ein entfernter Client erlebt.

:::single-choice{#linux-listening-services-verify-from-client} Du siehst einen Dienst, der auf allen lokalen Schnittstellen lauscht. Wie prüfst du, ob eine Arbeitsstation der Mitarbeitenden ihn erreichen kann?

::option[Lies den Hostnamen noch einmal.]{#linux-listening-services-verify-from-client-a explanation="Der Hostname prüft den Zugriffsweg nicht."}
::option[Zähle die lauschenden Sockets.]{#linux-listening-services-verify-from-client-b explanation="Die Anzahl zeigt nicht, ob der Zugriff von der Arbeitsstation funktioniert."}
::option[Sende eine genehmigte Anfrage aus dem Netz der Mitarbeitenden.]{#linux-listening-services-verify-from-client-c .correct explanation="Damit prüfst du den vorgesehenen Zugriffsweg."}
:::

Um lauschende Dienste auf einem Linux-Host zu prüfen, beginne mit der Übung Audit Listening Services im Kurs [Linux-Sicherheit für DevSecOps](https://labex.io/courses/linux-security-for-devsecops).

## Zusammenfassung

Du kannst jetzt die Adresse eines lauschenden Dienstes lesen und entscheiden, von wo aus du den Zugriff prüfst.

1. Liste die lokalen lauschenden TCP-Sockets auf, ohne das System zu verändern.
2. Unterscheide die Loopback-Adresse von einer Bindung an alle IPv4-Schnittstellen.
3. Prüfe die Verbindung vom relevanten Client-Standort aus.
