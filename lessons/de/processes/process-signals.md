---
index: 6
lang: "de"
title: "Signale"
meta_title: "Signale - Prozesse"
meta_description: "Erkunden Sie die Grundlagen von Linux-Signalen, einem Schlüsselmechanismus für die Prozessverwaltung. Erfahren Sie, wie Linux-Prozesssignale wie SIGTERM (Signal 15 Linux) und SIGKILL funktionieren, und verstehen Sie deren OS-Signalcodes."
meta_keywords: "linux signale, linux prozesssignale, signal 15 linux, os sig code, SIGKILL, SIGTERM, SIGINT, prozessverwaltung, linux tutorial"
---

## Lesson Content

Unter Linux ist ein Signal eine Softwareunterbrechung, die an einen Prozess gesendet wird, um ihn über ein wichtiges Ereignis zu informieren. Das Verständnis von **Linux-Signalen** ist grundlegend für die effektive Verwaltung von Prozessen und Systemverhalten.

### Der Zweck von Signalen

Signale dienen als primäre Methode der Interprozesskommunikation (IPC). Sie haben viele Verwendungszwecke:

- **Benutzerinteraktion**: Ein Benutzer kann spezielle Terminalzeichen wie `Strg-C` (SIGINT) oder `Strg-Z` (SIGTSTP) eingeben, um Vordergrundprozesse zu unterbrechen oder anzuhalten.
- **Kernel-Benachrichtigungen**: Der Kernel kann Signale an einen Prozess senden, um ihn über Hardware- oder Softwareprobleme zu informieren, wie z. B. einen ungültigen Speicherzugriff (SIGSEGV).
- **Prozessverwaltung**: Systemadministratoren und andere Prozesse verwenden Signale, um den Lebenszyklus anderer Prozesse zu verwalten, z. B. das Anfordern einer Beendigung oder einer Neuladung der Konfiguration.

### Der Signal-Lebenszyklus

Wenn ein Ereignis ein Signal erzeugt, wird es zunächst an einen Zielprozess übermittelt. Das Signal bleibt in einem „ausstehenden“ Zustand, bis der Kernel den Prozess ausführt. Wenn der Prozess eingeplant wird, wird das Signal zugestellt. Prozesse verfügen jedoch über Signalmasken, die so konfiguriert werden können, dass die Zustellung bestimmter Signale blockiert wird.

Wenn ein Signal zugestellt wird, kann der Prozess eine von mehreren Aktionen ausführen:

- **Das Signal ignorieren**: Der Prozess verwirft das Signal einfach und fährt mit der Ausführung fort.
- **Das Signal abfangen**: Der Prozess führt eine benutzerdefinierte Funktion aus, die als Signal-Handler bezeichnet wird, um auf das Ereignis zu reagieren.
- **Die Standardaktion ausführen**: Wenn das Signal nicht abgefangen oder ignoriert wird, wird die Standardaktion ausgeführt. Bei vielen Signalen bedeutet dies die Beendigung des Prozesses.
- **Das Signal blockieren**: Wenn sich das Signal in der Signalmaske des Prozesses befindet, bleibt es ausstehend, bis es entsperrt wird.

### Häufige Linux-Prozesssignale

Jedes Signal wird durch eine Ganzzahl definiert, aber sie werden fast immer anhand ihrer symbolischen Namen (dem **OS-Signalcode**) bezeichnet, die mit `SIG` beginnen. Obwohl die Zahlen zwischen den Architekturen leicht variieren können, sind die Namen konsistent. Hier sind einige der häufigsten **Linux-Prozesssignale**:

- **SIGHUP (1)**: Auflegen. Wird oft verwendet, um einem Daemon mitzuteilen, seine Konfiguration neu zu laden.
- **SIGINT (2)**: Unterbrechung. Gesendet durch `Strg-C`. Es ist eine Aufforderung zur Beendigung des Prozesses.
- **SIGKILL (9)**: Töten. Dies ist eine sofortige, erzwungene Beendigung. Der Prozess kann dieses Signal nicht abfangen, ignorieren oder blockieren.
- **SIGSEGV (11)**: Segmentierungsfehler. Zeigt an, dass der Prozess auf einen ungültigen Speicher zugegriffen hat.
- **SIGTERM (15)**: Beendigung. Dies ist die Standardmethode, um einen Prozess höflich zur Beendigung aufzufordern. Es ist das Standardsignal, das vom `kill`-Befehl gesendet wird. Ein Prozess kann dieses Signal abfangen, um vor dem Beenden Aufräumarbeiten durchzuführen. Dies wird oft als **Signal 15 Linux** bezeichnet.
- **SIGSTOP**: Anhalten. Pausiert den Prozess. Wie SIGKILL kann es nicht abgefangen oder ignoriert werden.

The key difference between `SIGTERM` (**linux signal 15**) and `SIGKILL` is that `SIGTERM` is a request that can be handled, while `SIGKILL` is a command that destroys the process immediately.

Der Hauptunterschied zwischen `SIGTERM` (**Linux-Signal 15**) und `SIGKILL` besteht darin, dass `SIGTERM` eine Anfrage ist, die behandelt werden kann, während `SIGKILL` ein Befehl ist, der den Prozess sofort zerstört.

## Exercise

Übung macht den Meister! Hier ist ein praktisches Labor, um Ihr Verständnis von Prozessen und der Verwendung von Signalen zu ihrer Interaktion zu festigen:

1. **[Linux-Prozesse verwalten und überwachen](https://labex.io/de/labs/comptia-manage-and-monitor-linux-processes-590864)** – In diesem Labor erlernen Sie wesentliche Fähigkeiten zur Verwaltung und Überwachung von Prozessen auf einem Linux-System. Sie werden untersuchen, wie man mit Vordergrund- und Hintergrundprozessen interagiert, sie mit `ps` inspiziert, Ressourcen mit `top` überwacht, die Priorität mit `renice` anpasst und sie mit `kill` beendet. Das Beenden von Prozessen mit `kill` ist eine direkte Anwendung des Sendens von Signalen.

Dieses Labor hilft Ihnen, die Konzepte der Prozessverwaltung und die zugrunde liegende Verwendung von Signalen in realen Szenarien anzuwenden und Vertrauen in die Linux-Systemadministration aufzubauen.

## Quiz Question

Welches Signal kann nicht blockiert werden? Bitte antworten Sie auf Englisch und verwenden Sie den genauen Signalnamen unter Beachtung der Groß- und Kleinschreibung.

## Quiz Answer

SIGKILL
