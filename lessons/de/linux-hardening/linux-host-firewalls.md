---
lesson_id: "linux-host-firewalls"
course_id: "linux-hardening"
lang: "de"
order_index: 5
title: "Host-Firewalls"
description: "Lerne, einfache Regeln einer Host-Firewall zu lesen und Prüfungen von den relevanten Standorten zu planen."
meta_title: "Host-Firewalls - Linux-Härtung"
meta_description: "Lerne, einfache Regeln einer Host-Firewall zu lesen und Prüfungen von den relevanten Standorten zu planen."
meta_keywords: "Host-Firewall, Linux-Härtung, Cybersicherheit, Linux Journey"
---

Eine **Host-Firewall** kann eingehenden Netzwerkverkehr anhand von Quelladresse, Protokoll und Zielport zulassen oder blockieren. Kläre zuerst, welchen Verkehr der Dienst benötigt.

## Eine Beispielrichtlinie lesen

Die folgende vereinfachte Richtlinie gilt für einen einzelnen Host. Die Schreibweise mit Schrägstrich in `192.0.2.0/24` bezeichnet einen Bereich von IPv4-Adressen. In diesem Beispiel liegt `192.0.2.44` innerhalb des Bereichs und `198.51.100.8` außerhalb.

```text
Allow TCP port 443 from any source.
Allow TCP port 22 from 192.0.2.0/24.
Deny other new inbound connections.
```

Über Port 443 ist die öffentliche Website erreichbar. Port 22 ist dem Wartungsnetz vorbehalten. Die Standardregel gilt für Verbindungen, die unter keine der beiden Freigaben fallen.

:::single-choice{#linux-host-firewalls-match-trusted-network} Welche neue Verbindung entspricht der Wartungsregel?

::option[TCP-Port 22 von 198.51.100.8 aus.]{#linux-host-firewalls-match-trusted-network-b explanation="Der Port passt, aber diese Quelle liegt außerhalb des Wartungsnetzes."}
::option[TCP-Port 443 von 192.0.2.44 aus.]{#linux-host-firewalls-match-trusted-network-c explanation="Diese Verbindung fällt unter die Regel für die öffentliche Website."}
::option[TCP-Port 22 von 192.0.2.44 aus.]{#linux-host-firewalls-match-trusted-network-a .correct explanation="Zielport und Quelladressbereich stimmen überein."}
:::

![Simulierte Host-Firewall-Regeln mit öffentlichem HTTPS und eingeschränktem Wartungszugang](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/linux-hardening/linux-host-firewalls/sample-policy.png)

## Firewall-Regeln und Dienst prüfen

Auch eine zugelassene Verbindung kann scheitern, wenn kein Programm auf dem Port lauscht. Umgekehrt kann ein funktionierender Dienst auf einem Zugriffsweg unerreichbar sein, den die Firewall sperrt. Lies die Richtlinie und prüfe gesondert, ob der Dienst auf dem Port lauscht.

:::single-choice{#linux-host-firewalls-allowed-but-failed} Die Regel erlaubt Port 443, aber auf dem Host lauscht dort kein Programm. Was solltest du prüfen?

::option[Ob der Client den SSH-Zugang für die Wartung verwenden soll.]{#linux-host-firewalls-allowed-but-failed-a explanation="Das ist ein anderer Dienst."}
::option[Ob der öffentliche Webdienst auf dem erwarteten Port lauscht.]{#linux-host-firewalls-allowed-but-failed-b .correct explanation="Eine Firewall-Freigabe startet keinen Dienst auf dem Port."}
::option[Ob die Anfrage aus dem Wartungsnetz kam.]{#linux-host-firewalls-allowed-but-failed-c explanation="Die öffentliche Regel erlaubt in diesem Beispiel jede Quelle."}
:::

## Eine sichere Prüfung planen

Halte bei der Überprüfung einer kontrollierten Änderung einen berechtigten Wartungszugang offen. Teste den erlaubten Zugriffsweg aus dem Wartungsnetz. Prüfe von einem freigegebenen Standort außerhalb des Netzes, dass die Verbindung dort blockiert wird. Notiere für jeden Test Quelle, Ziel und erwartetes Ergebnis.

:::single-choice{#linux-host-firewalls-verification-pair} Welche Kombination prüft die vorgesehene SSH-Beschränkung?

::option[Je eine genehmigte Prüfung von Port 22 innerhalb und außerhalb des Wartungsnetzes.]{#linux-host-firewalls-verification-pair-c .correct explanation="Damit testest du sowohl den erlaubten als auch den gesperrten Zugriff."}
::option[Zwei SSH-Anfragen von demselben zugelassenen Rechner.]{#linux-host-firewalls-verification-pair-a explanation="So würdest du den erlaubten Zugriff zweimal prüfen."}
::option[Zwei Browseranfragen an die öffentliche Startseite.]{#linux-host-firewalls-verification-pair-b explanation="Damit prüfst du den öffentlichen Port. Der Wartungszugang bleibt ungeprüft."}
:::

## Zusammenfassung

Du kannst jetzt die Regeln einer Host-Firewall zusammen mit dem Zustand eines Dienstes beurteilen.

1. Gleiche Protokoll, Ziel und Quelle mit der Regel ab.
2. Prüfe, ob der zugelassene Dienst auf dem Port lauscht.
3. Überprüfe sowohl die vorgesehenen Zugänge als auch die vorgesehenen Sperren.
