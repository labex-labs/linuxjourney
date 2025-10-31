---
index: 5
lang: "de"
title: "Anwendungsschicht"
meta_title: "Anwendungsschicht - Netzwerk Grundlagen"
meta_description: "Erkunden Sie die Anwendungsschicht, die oberste Schicht des TCP/IP-Modells. Erfahren Sie, was ein Anwendungsschichtprotokoll ist, sehen Sie ein Beispiel mit SMTP und verstehen Sie, wie der Anwendungsschicht-Header Daten für die Netzwerkkommunikation vorbereitet."
meta_keywords: "Anwendungsschicht, die Anwendungsschicht, Anwendungsschichtprotokoll, Beispiel für Anwendungsschichtprotokoll, Anwendungsschicht-Header, TCP/IP-Modell, SMTP, Netzwerkprotokolle"
---

## Lesson Content

Im TCP/IP-Modell ist die Netzwerkkommunikation in verschiedene Schichten unterteilt, und wir beginnen ganz oben mit der **Anwendungsschicht** (Application Layer). Dies ist die Schicht, mit der Sie am direktesten interagieren, da sie für die Bereitstellung von Netzwerkdiensten für Benutzeranwendungen wie Webbrowser und E-Mail-Clients verantwortlich ist.

### Die Rolle der Anwendungsschicht

**Die Anwendungsschicht** fungiert als Schnittstelle zwischen der Software auf einem Gerät und dem Netzwerk selbst. Wenn Sie eine E-Mail senden, eine Website durchsuchen oder eine Datei übertragen, ist es die Anwendungsschicht, die den Prozess initiiert. Ihre Hauptaufgabe besteht darin, Benutzerdaten vorzubereiten und eingehende Daten in einem benutzerfreundlichen Format darzustellen.

### Was ist ein Anwendungsschichtprotokoll

Zur Verwaltung der Kommunikation verwendet die Anwendungsschicht spezifische Protokolle. Was also **ist ein Anwendungsschichtprotokoll**? Es ist ein Satz von Regeln, der definiert, wie Anwendungen Daten über das Netzwerk austauschen. Verschiedene Aufgaben verwenden unterschiedliche Protokolle. Zum Beispiel verwendet das Surfen im Web HTTP oder HTTPS, Dateiübertragungen verwenden möglicherweise FTP, und das Senden von E-Mails verwendet typischerweise SMTP (Simple Mail Transfer Protocol). Jedes Protokoll stellt sicher, dass sowohl der Absender als auch der Empfänger das Format und die Bedeutung der Nachrichten verstehen.

### Ein Beispiel für ein Anwendungsschichtprotokoll

Nehmen wir eine E-Mail als **Beispiel für ein Anwendungsschichtprotokoll** in Aktion. Stellen Sie sich vor, Sie senden eine E-Mail an einen Freund.

1. Sie verfassen Ihre Nachricht in einem E-Mail-Client.
2. Wenn Sie auf „Senden“ klicken, übergibt der E-Mail-Client (die Anwendung) die Daten an die Anwendungsschicht.
3. Die Anwendungsschicht verwendet das SMTP-Protokoll, um die E-Mail korrekt zu formatieren.

### Datenkapselung und der Anwendungsschicht-Header

Bevor Daten an die nächste Schicht (die Transportschicht) gesendet werden, müssen sie vorbereitet werden. Dieser Prozess wird Kapselung genannt. Die Anwendungsschicht fügt den Rohdaten einen **Anwendungsschicht-Header** hinzu. Dieser Header enthält protokollspezifische Informationen, die die empfangende Anwendung benötigt, um die Daten zu verstehen.

Die Kombination aus Header und Ihren Daten wird zur Nutzlast für die nächste Schicht. Während Daten den Netzwerk-Stack durchlaufen, fügt jede Schicht ihren eigenen Header hinzu. Obwohl wir oft den allgemeinen Begriff „Paket“ verwenden, um Daten zu beschreiben, die über ein Netzwerk gesendet werden, haben verschiedene Schichten spezifische Namen für die Dateneinheit. Auf der Transportschicht ist es ein „Segment“ und auf der Linkschicht ein „Frame“.

In unserem E-Mail-Beispiel werden die SMTP-formatierten Daten über einen bestimmten Port (Port 25 für SMTP) an die Transportschicht übergeben, wo sie für ihre Reise durch das Netzwerk weiter gekapselt werden.

## Exercise

Übung macht den Meister! Hier ist ein praktisches Labor, um Ihr Verständnis von Netzwerkschichten und Ports zu festigen:

1. **[Netzwerkports und -sitzungen mit netstat unter Linux analysieren](https://labex.io/de/labs/comptia-analyze-network-ports-and-sessions-with-netstat-in-linux-592741)** – In diesem Labor lernen Sie, wie Sie den Befehl `netstat` verwenden, um die Netzwerkaktivität zu analysieren und grundlegende Konzepte wie Netzwerkports, Sockets und aktive Verbindungen zu untersuchen. Dies gibt Ihnen praktische Einblicke, wie Dienste über das Netzwerk kommunizieren, was direkt mit den diskutierten Konzepten der Transportschicht zusammenhängt.

Dieses Labor hilft Ihnen, die Konzepte der Netzwerkkommunikation und der Portnutzung in einer realen Linux-Umgebung anzuwenden und Ihr Vertrauen in das Verständnis der Interaktion von Anwendungen mit dem Netzwerk-Stack zu stärken.

## Quiz Question

What layer is used to present the packet data in a user-friendly format? (Please answer in English and pay attention to capitalization.)

## Quiz Answer

Application
