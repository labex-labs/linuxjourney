---
index: 9
lang: "de"
title: "Prozesszustände"
meta_title: "Prozesszustände - Prozesse"
meta_description: "Lernen Sie Linux-Prozesszustände (R, S, D, Z, T) mit `ps aux`. Verstehen Sie gängige STAT-Codes und verwalten Sie Prozesse effektiv. Beginnen Sie Ihre Linux-Reise!"
meta_keywords: "Linux-Prozesszustände, ps aux, Prozessmanagement, Linux-Tutorial, Linux für Anfänger, STAT-Codes, Linux-Anleitung"
---

## Lesson Content

Schauen wir uns den Befehl `ps aux` noch einmal an:

```bash
ps aux
```

In der Spalte STAT sehen Sie viele Werte. Ein Linux-Prozess kann sich in verschiedenen Zuständen befinden. Die häufigsten Statuscodes, die Sie sehen werden, sind unten beschrieben:

- **R**: Running oder runnable; er wartet nur darauf, von der CPU verarbeitet zu werden.
- **S**: Interruptible sleep; wartet auf den Abschluss eines Ereignisses, wie z.B. eine Eingabe vom Terminal.
- **D**: Uninterruptible sleep; Prozesse, die nicht getötet oder durch ein Signal unterbrochen werden können. Normalerweise muss man neu starten oder das Problem beheben, um sie zu entfernen.
- **Z**: Zombie; wir haben in einer früheren Lektion besprochen, dass Zombies beendete Prozesse sind, die darauf warten, dass ihre Status gesammelt werden.
- **T**: Stopped; ein Prozess, der angehalten/gestoppt wurde.

## Exercise

Übung macht den Meister! Hier sind einige praktische Übungen, um Ihr Verständnis des Linux-Prozessmanagements und der Prozesszustände zu vertiefen:

1. **[Linux-Prozesse verwalten und überwachen](https://labex.io/de/labs/comptia-manage-and-monitor-linux-processes-590864)** – In diesem Lab lernen Sie wesentliche Fähigkeiten zur Verwaltung und Überwachung von Prozessen auf einem Linux-System. Sie erfahren, wie Sie mit Vordergrund- und Hintergrundprozessen interagieren, diese mit `ps inspizieren`, Ressourcen mit `top` überwachen, die Priorität mit `renice` anpassen und sie mit `kill` beenden.

Dieses Lab wird Ihnen helfen, die Konzepte der Prozesszustände in realen Szenarien anzuwenden und Vertrauen im Umgang mit dem Linux-Prozessmanagement aufzubauen.

## Quiz Question

Welcher STAT-Code wird verwendet, um einen ununterbrechbaren Schlaf darzustellen?

## Quiz Answer

D
