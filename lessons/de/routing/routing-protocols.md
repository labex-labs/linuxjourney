---
title: "Routing-Protokolle"
description: "Erfahren Sie mehr über Routing-Protokolle wie Distanzvektor und Link-State. Verstehen Sie Netzwerkkonvergenz und wie Router sich an Änderungen anpassen. Beginnen Sie Ihre Linux-Netzwerkreise!"
keywords: "Routing-Protokolle, Netzwerkkonvergenz, Distanzvektor, Link-State, Linux-Netzwerk, Anfängerleitfaden, Netzwerk-Tutorial"
---

## Lesson Content

Es wäre mühsam, Routen auf einer Routing-Tabelle für jedes Gerät in Ihrem Netzwerk manuell konfigurieren zu müssen. Stattdessen verwenden wir sogenannte Routing-Protokolle. Routing-Protokolle helfen unserem System, sich an Netzwerkänderungen anzupassen; sie lernen verschiedene Routen, bauen sie in die Routing-Tabelle ein und leiten unsere Pakete dann auf diese Weise weiter. Es gibt zwei primäre Routing-Protokolltypen: Distanzvektor-Protokolle und Link-State-Protokolle.

### Konvergenz

Bevor wir über die Protokolle sprechen, sollten wir einen im Routing verwendeten Begriff behandeln, der als Konvergenz bekannt ist. Bei der Verwendung von Routing-Protokollen kommunizieren Router mit anderen Routern, um Informationen über das Netzwerk zu sammeln und auszutauschen. Wenn sie sich darüber einig sind, wie ein Netzwerk aussehen sollte, bildet jede Routing-Tabelle die vollständige Topologie des Netzwerks ab und "konvergiert" somit. Wenn etwas in der Netzwerktopologie auftritt, wird die Konvergenz vorübergehend unterbrochen, bis alle Router über diese Änderung informiert sind.

## Exercise

No exercises for this lesson.

## Quiz Question

Wie nennt man den Zustand, wenn alle Routing-Tabellen die Netzwerktopologie kennen?

## Quiz Answer

Convergence
