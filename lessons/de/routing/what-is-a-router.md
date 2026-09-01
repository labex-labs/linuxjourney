---
lesson_id: "what-is-a-router"
course_id: "routing"
lang: "de"
order_index: 1
title: "Was ist ein Router?"
description: "Lerne, wie Router nächste Hops auswählen und IP-Pakete zwischen Netzwerken weiterleiten."
meta_title: "Was ist ein Router? – Routing"
meta_description: "Eine Einführung in Router und Netzwerke. Lerne Routing, Paketvermittlung, Hops und die Verwendung von Routingtabellen zur Datenweiterleitung über Netzwerke kennen."
meta_keywords: "Router, Vernetzung, Routing, Hops, Paketvermittlung, Linux-Vernetzung, Einsteiger-Tutorial, Netzwerk-Anleitung"
---

Ein Router verbindet Domänen der Netzwerkschicht und leitet IP-Pakete zwischen ihnen weiter. Ein Linux-Host kann als Router arbeiten, wenn die Weiterleitung aktiviert ist und seine Schnittstellen, Routen, Nachbarerkennung sowie Filterrichtlinie angemessen konfiguriert sind.

## Routing und Weiterleitung

Routing erstellt oder wählt Informationen über erreichbare Präfixe aus. Die Weiterleitung wendet diese Informationen auf jedes Paket an: Ziel untersuchen, eine geeignete Route und den nächsten Hop auswählen, Hop-Limit verringern und über eine ausgehende Schnittstelle übertragen.

Dies sind getrennte Belange von Steuerungs- und Datenebene. Eine Route kann bestehen, während eine Firewallrichtlinie die Weiterleitung blockiert, oder eine Weiterleitungsschnittstelle kann aktiv sein, während keine gültige Route existiert.

:::single-choice{#router-forwarding-role} Was bewirkt die Paketweiterleitung?

::option[Sie wendet Routinginformationen an, um ein Paket zu seinem nächsten Hop zu senden.]{#router-apply-route .correct explanation="Weiterleitung ist die paketweise Aktion anhand der ausgewählten Route und Richtlinie."}
::option[Sie erstellt für jedes Ziel eine dauerhafte Anwendungsanmeldung.]{#router-create-login explanation="Routing verwaltet keine entfernten Anwendungskonten."}
::option[Sie kopiert jedes Paket auf alle Schnittstellen, wenn keine Route besteht.]{#router-flood-no-route explanation="Gewöhnliche IP-Weiterleitung verwirft ein nicht routbares Paket, statt ersatzweise Ethernet-artiges Fluten zu verwenden."}
:::

## Routingtabellen und Standardrouten

Eine Route verbindet ein Zielpräfix mit einer ausgehenden Schnittstelle, einem nächsten Hop, Messwert, einer Quellpräferenz oder weiteren Attributen. Die längste Präfixübereinstimmung bevorzugt eine spezifischere geeignete Route. Eine Standardroute, IPv4 `/0` oder IPv6 `::/0`, ist die unspezifischste Übereinstimmung und wird nur verwendet, wenn keine spezifischere Route gewinnt.

Wenn keine geeignete Route besteht, verwirft der Router das Paket und kann eine ICMP-Nichterreichbarkeitsmeldung erzeugen. Eine Standardroute ist optional und muss nicht unmittelbar in das öffentliche Internet zeigen.

:::single-choice{#router-default-route} Wann wird eine Standardroute ausgewählt?

::option[Bevor zielspezifische Präfixe geprüft werden.]{#router-default-first explanation="Spezifischere geeignete Präfixe haben Vorrang."}
::option[Nur, wenn das Paket ein Ethernet-Broadcast ist.]{#router-default-broadcast explanation="Die IP-Routenauswahl beruht auf Zielen der Netzwerkschicht."}
::option[Wenn keine spezifischere geeignete Route passt.]{#router-default-fallback .correct explanation="Das Präfix mit Länge null ist die unspezifischste Route."}
:::

## Lokaler und gerouteter Datenverkehr

Zwei Hosts im selben direkt erreichbaren Subnetz tauschen Frames gewöhnlich aus, ohne das IP-Paket durch einen Router zu senden. Ein Router wird beteiligt, wenn die Routenauswahl ihn als nächsten Hop bestimmt oder Topologie und Richtlinie die geroutete Durchquerung bewusst erzwingen.

Ein Heim-„Router“ verbindet gewöhnlich IP-Router, Ethernet-Switch, WLAN-Access-Point, DHCP-Dienst, NAT und Firewall. Jede Funktion sollte getrennt diagnostiziert werden.

:::single-choice{#router-same-subnet-path} Muss Datenverkehr zwischen zwei direkt erreichbaren Hosts ihren Standardrouter durchqueren?

::option[Ja, weil jedes Paket einen WAN-Port erreichen muss.]{#router-always-wan explanation="Lokale direkte Zustellung kann unmittelbar über die Verbindung erfolgen."}
::option[Ja, sofern nicht beide Hosts öffentliche Adressen besitzen.]{#router-public-required explanation="Öffentlicher oder privater Bereich bestimmt nicht die grundlegende direkte Weiterleitung."}
::option[Nein; der Sender kann das Ziel auf der lokalen Verbindung direkt adressieren.]{#router-direct-on-link .correct explanation="Die Routingtabelle kennzeichnet das verbundene Präfix als direkt erreichbar."}
:::

## Hops und Schleifenvermeidung

Ein gerouteter Hop ist ein Weiterleitungsschritt auf Netzwerkschicht. IPv4-TTL und IPv6-Hop-Limit werden an jedem Router verringert und begrenzen dadurch Schleifen. Die Hop-Anzahl ist kein vollständiger Entfernungs- oder Qualitätsmesswert: Verbindungen unterscheiden sich in Bandbreite, Latenz, Verlust, Richtlinie und Überlastung.

:::single-choice{#router-hop-count-limit} Was garantiert eine kleinere Hop-Anzahl nicht?

::option[Dass mindestens ein gerouteter Schritt besteht.]{#router-hop-exists explanation="Eine positive Hop-Anzahl zeigt unmittelbar geroutete Durchquerung an."}
::option[Einen schnelleren oder besseren Anwendungspfad.]{#router-hop-not-quality .correct explanation="Weniger Router können dennoch langsamere, überlastete oder durch Richtlinien eingeschränkte Verbindungen durchqueren."}
::option[Dass Hop-Limit-Felder endlich sind.]{#router-hop-limit-finite explanation="Diese Felder sind durch den Protokollentwurf endlich."}
:::

## Zusammenfassung

Du kannst die Routenauswahl eines Routers nun von seiner Weiterleitungsaktion trennen.

1. Definiere Router durch die Weiterleitung zwischen IP-Netzwerken.
2. Unterscheide Routing auf der Steuerungsebene von Weiterleitung auf der Datenebene.
3. Behandle die Standardroute als unspezifischste Ausweichroute.
4. Erkenne, dass die Hop-Anzahl allein keine Pfadqualität misst.
