---
lang: "de"
title: "System V Dienst"
meta_description: "Lernen Sie, System V-Dienste mit Befehlszeilentools zu verwalten. Entdecken Sie, wie Sie Dienste auflisten, starten, stoppen und neu starten können, mit diesem anfängerfreundlichen Linux-Tutorial."
meta_keywords: "System V-Dienste, Linux-Dienste, service-Befehl, SysV init, Linux-Tutorial, Linux für Anfänger, Dienstverwaltung, Linux-Anleitung"
---

## Lesson Content

Es gibt viele Befehlszeilentools, die Sie zur Verwaltung von Sys V-Diensten verwenden können.

### Dienste auflisten

```bash
service --status-all
```

### Einen Dienst starten

```bash
sudo service networking start
```

### Einen Dienst stoppen

```bash
sudo service networking stop
```

### Einen Dienst neu starten

```bash
sudo service networking restart
```

Diese Befehle sind nicht spezifisch für Sys V-Init-Systeme; Sie können sie auch zur Verwaltung von Upstart-Diensten verwenden. Da Linux versucht, sich von den traditionelleren Sys V-Init-Skripten zu lösen, gibt es immer noch Mechanismen, die diesen Übergang unterstützen.

## Exercise

Verwalten Sie ein paar Dienste und ändern Sie deren Zustände. Was beobachten Sie?

## Quiz Question

Was ist der Befehl, um einen Dienst namens `peanut` mit Sys V zu stoppen?

## Quiz Answer

sudo service peanut stop
