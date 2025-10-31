---
index: 7
lang: "de"
title: "Border Gateway Protocol"
meta_title: "Border Gateway Protocol - Routing"
meta_description: "Erkunden Sie die Grundlagen des Border Gateway Protocol (BGP), des Kernprotokolls für das Internet-Routing. Erfahren Sie, wie BGP die Kommunikation zwischen autonomen Systemen ermöglicht und welche Prinzipien dem Border Gateway Protocol Routing zugrunde liegen."
meta_keywords: "BGP, Border Gateway Protocol, BGP-Routing, Internet-Routing, autonome Systeme, Linux-Netzwerke, BGP-Tutorial, Netzwerkprotokolle"
---

## Lesson Content

### Das Rückgrat des Internets

Das letzte wichtige Protokoll, das wir behandeln werden, ist das Border Gateway Protocol (BGP). BGP ist das grundlegende Protokoll, das es dem Internet ermöglicht, zu funktionieren, indem es verwaltet, wie Datenpakete über seine riesige Sammlung von Netzwerken weitergeleitet werden. Es wurde speziell entwickelt, um Routing- und Erreichbarkeitsinformationen zwischen verschiedenen Autonomen Systemen (AS) auszutauschen.

### Was ist ein Autonomes System?

Ein Autonomes System (AS) ist ein großes Netzwerk oder eine Gruppe von Netzwerken, die von einer einzigen administrativen Einheit verwaltet werden. Beispiele hierfür sind Internetdienstanbieter (ISPs), große Unternehmen, Universitäten und Regierungsbehörden. Ohne BGP wären diese Systeme isoliert und könnten nicht miteinander kommunizieren. Während andere Protokolle das Routing _innerhalb_ eines AS steuern, ist BGP für das Routing _zwischen_ ihnen verantwortlich.

### Der Prozess des Border Gateway Protocol Routings

Die Hauptfunktion von BGP ist das **Border Gateway Protocol Routing**. Betrachten wir ein Beispiel. Stellen Sie sich vor, Sie befinden sich in Ihrem Heimnetzwerk und ein Freund nutzt das WLAN in einem Café. Wenn Ihr Freund Ihnen eine Nachricht sendet, durchläuft das Datenpaket zunächst das lokale Netzwerk des Cafés. Es folgt internen Routing-Tabellen, bis es einen "Grenz"-Router am Rand dieses Netzwerks erreicht.

Dieser Grenz-Router verwendet BGP, um den besten Pfad zu bestimmen, den das Paket nehmen muss, um sein eigenes AS zu verlassen und über andere autonome Systeme zu reisen, um schließlich das AS Ihres Heimnetzwerks zu erreichen. BGP findet nicht nur einen Pfad; es trifft Richtlinienentscheidungen, um basierend auf den von Netzwerkadministratoren konfigurierten Regeln den _besten_ Pfad zu finden und so einen effizienten und zuverlässigen Datenaustausch über das globale Internet zu gewährleisten.

## Exercise

Obwohl es für dieses Thema keine spezifischen Labore gibt, empfehlen wir Ihnen, den umfassenden [Linux Lernpfad](https://labex.io/de/learn/linux) zu erkunden, um verwandte Linux-Fähigkeiten und -Konzepte zu üben.

## Quiz Question

Welches Protokoll lässt das Internet im Grunde funktionieren? Bitte antworten Sie mit dem englischen Akronym in Großbuchstaben.

## Quiz Answer

BGP
