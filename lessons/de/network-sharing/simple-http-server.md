---
index: 3
lang: "de"
title: "Einfacher HTTP-Server"
meta_title: "Einfacher HTTP-Server - Netzwerkfreigabe"
meta_description: "Lernen Sie, einen einfachen HTTP-Server mit Pythons http.server-Modul zu erstellen. Teilen Sie schnell Dateien in Ihrem Netzwerk mit diesem anfängerfreundlichen Linux-Tutorial."
meta_keywords: "http.server, SimpleHTTPServer, Python Webserver, Dateifreigabe, Linux Tutorial, Anfängerleitfaden"
---

## Lesson Content

Python verfügt über ein äußerst nützliches Tool zum Bereitstellen von Dateien über HTTP. Dies ist großartig, wenn Sie schnell eine Netzwerkfreigabe erstellen möchten, auf die andere Maschinen in Ihrem Netzwerk zugreifen können. Gehen Sie dazu einfach in das Verzeichnis, das Sie freigeben möchten, und führen Sie Folgendes aus:

```bash
python -m http.server
```

Oder, wenn Sie noch Python 2 verwenden:

```bash
python -m SimpleHTTPServer
```

Dies richtet einen grundlegenden Webserver ein, auf den Sie über die Localhost-Adresse zugreifen können. Nehmen Sie also die IP-Adresse der Maschine, auf der Sie dies ausgeführt haben, und greifen Sie dann auf einer anderen Maschine im Browser darauf zu mit: `http://IP_ADDRESS:8000`. Auf Ihrer eigenen Maschine können Sie die verfügbaren Dateien anzeigen, indem Sie `http://localhost:8000` in Ihren Webbrowser eingeben.

## Exercise

Übung macht den Meister! Hier sind einige praktische Übungen, um Ihr Verständnis von Netzwerkkonnektivität und IP-Adressierung zu vertiefen, die für die Freigabe von Dateien über ein Netzwerk unerlässlich sind:

1. **[IP-Adresstypen und Erreichbarkeit in Linux erkunden](https://labex.io/de/labs/linux-explore-ip-address-types-and-reachability-in-linux-592780)** – Üben Sie das Identifizieren verschiedener IP-Adresstypen und das Testen der Netzwerkerreichbarkeit, entscheidend, um sicherzustellen, dass Ihr Python HTTP-Server zugänglich ist.
2. **[MAC- und IP-Adressen in Linux identifizieren](https://labex.io/de/labs/linux-identify-mac-and-ip-addresses-in-linux-592731)** – Lernen Sie, den Befehl `ip a` zu verwenden, um die IP-Adresse Ihrer Maschine zu finden, ein notwendiger Schritt, bevor Sie von einem anderen Gerät auf Ihre freigegebenen Dateien zugreifen.
3. **[Lokale Hostnamen-Auflösung in Linux verwalten](https://labex.io/de/labs/linux-manage-local-hostname-resolution-in-linux-592792)** – Lernen Sie, die lokale Hostnamen-Auflösung in Linux durch Bearbeiten der Datei /etc/hosts zu verwalten, eine Schlüsselkompetenz für die Webentwicklung und Netzwerktests.

Diese Labs helfen Ihnen, die Konzepte in realen Szenarien anzuwenden und Vertrauen in grundlegende Netzwerkoperationen in Linux aufzubauen.

## Quiz Question

Welches Tool können Sie verwenden, um einen einfachen HTTP-Server mit Python zu erstellen?

## Quiz Answer

http.server
