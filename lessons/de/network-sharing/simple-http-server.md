---
index: 3
lang: "de"
title: "Einfacher HTTP-Server"
meta_title: "Einfacher HTTP-Server - Netzwerkfreigabe"
meta_description: "Erfahren Sie, wie Sie mit dem Modul http.server von Python schnell einen einfachen HTTP-Server unter Linux einrichten. Diese Anleitung erklärt, wie Sie einen einfachen Linux-Webserver für die einfache Dateiübertragung in Ihrem Netzwerk erstellen."
meta_keywords: "linux einfacher http server, einfacher http server linux, einfacher linux webserver, python http.server, was ist python simplehttpserver, dateifreigabe, netzwerkserver"
---

## Lesson Content

Python verfügt über ein integriertes Modul, mit dem Sie sofort einen Webserver erstellen können, was für die gemeinsame Nutzung von Dateien über ein Netzwerk unglaublich nützlich ist. Die Einrichtung eines **linux simple http server** ist ein unkomplizierter Prozess, der nur einen einzigen Befehl erfordert.

### Starten eines einfachen HTTP-Servers unter Linux

Um zu beginnen, navigieren Sie im Terminal zu dem Verzeichnis, das Sie freigeben möchten. Sobald Sie sich im gewünschten Verzeichnis befinden, können Sie mit dem folgenden Befehl eine **simple http server linux**-Umgebung starten, wenn Sie Python 3 verwenden:

```bash
python -m http.server
```

Dieser Befehl startet einen grundlegenden Webserver und macht den Inhalt Ihres aktuellen Verzeichnisses über HTTP zugänglich.

### Veraltete Methode für Python 2

Für ältere Systeme, die noch Python 2 verwenden, ist der Befehl leicht unterschiedlich. Das Modul hieß früher `SimpleHTTPServer`. Wenn Sie sich jemals gefragt haben, **what is python simplehttpserver**, handelt es sich dabei einfach um das Äquivalent des `http.server`-Moduls in Python 2. Sie können es ausführen mit:

```bash
python -m SimpleHTTPServer
```

### Zugriff auf Ihren einfachen Linux-Webserver

Nachdem Sie den Befehl ausgeführt haben, ist Ihr **simple linux web server** aktiv. Sie können von einem anderen Rechner im selben Netzwerk auf die freigegebenen Dateien zugreifen, indem Sie einen Webbrowser öffnen und zu `http://IP_ADDRESS:8000` navigieren. Ersetzen Sie dabei `IP_ADDRESS` durch die lokale IP-Adresse des Rechners, auf dem der Server läuft.

Um die Dateien auf demselben Rechner anzuzeigen, können Sie die Localhost-Adresse verwenden: `http://localhost:8000`.

## Exercise

Übung macht den Meister! Hier sind einige praktische Labs, um Ihr Verständnis von Netzwerkverbindungen und IP-Adressierung zu festigen, die für die gemeinsame Nutzung von Dateien über ein Netzwerk unerlässlich sind:

1. **[Explore IP Address Types and Reachability in Linux](https://labex.io/de/labs/comptia-explore-ip-address-types-and-reachability-in-linux-592780)** - Üben Sie die Identifizierung verschiedener IP-Adress-Typen und das Testen der Netzwerkerreichbarkeit, was entscheidend ist, um sicherzustellen, dass Ihr Python HTTP-Server zugänglich ist.
2. **[Identify MAC and IP Addresses in Linux](https://labex.io/de/labs/comptia-identify-mac-and-ip-addresses-in-linux-592731)** - Lernen Sie, den Befehl `ip a` zu verwenden, um die IP-Adresse Ihres Geräts zu finden, ein notwendiger Schritt, bevor Sie von einem anderen Gerät auf Ihre freigegebenen Dateien zugreifen.
3. **[Manage Local Hostname Resolution in Linux](https://labex.io/de/labs/comptia-manage-local-hostname-resolution-in-linux-592792)** - Lernen Sie, die lokale Hostnamensauflösung unter Linux zu verwalten, indem Sie die Datei /etc/hosts bearbeiten, eine Schlüsselkompetenz für die Webentwicklung und das Netzwerk-Testing.

Diese Labs helfen Ihnen, die Konzepte in realen Szenarien anzuwenden und Vertrauen in grundlegende Netzwerkoperationen unter Linux aufzubauen.

## Quiz Question

Für Python 3, wie lautet der Name des Moduls, das zur Erstellung eines einfachen HTTP-Servers verwendet wird? (Bitte antworten Sie auf Englisch und achten Sie auf die Groß-/Kleinschreibung).

## Quiz Answer

http.server
