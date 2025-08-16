---
title: "Einfacher HTTP-Server"
description: "Lernen Sie, einen einfachen HTTP-Server mit Pythons http.server-Modul zu erstellen. Teilen Sie Dateien schnell in Ihrem Netzwerk mit diesem anfängerfreundlichen Linux-Tutorial."
keywords: "http.server, SimpleHTTPServer, Python Webserver, Dateifreigabe, Linux-Tutorial, Anfängerleitfaden"
---

## Lesson Content

Python verfügt über ein äußerst nützliches Tool zum Bereitstellen von Dateien über HTTP. Dies ist großartig, wenn Sie einfach eine schnelle Netzwerkfreigabe erstellen möchten, auf die andere Maschinen in Ihrem Netzwerk zugreifen können. Gehen Sie dazu einfach in das Verzeichnis, das Sie freigeben möchten, und führen Sie Folgendes aus:

```bash
python -m http.server
```

Oder, wenn Sie noch Python 2 verwenden:

```bash
python -m SimpleHTTPServer
```

Dies richtet einen grundlegenden Webserver ein, auf den Sie über die localhost-Adresse zugreifen können. Holen Sie sich also die IP-Adresse des Computers, auf dem Sie dies ausgeführt haben, und greifen Sie dann auf einem anderen Computer im Browser darauf zu mit: `http://IP_ADDRESS:8000`. Auf Ihrem eigenen Computer können Sie die verfügbaren Dateien anzeigen, indem Sie in Ihrem Webbrowser Folgendes eingeben: `http://localhost:8000`.

## Exercise

Versuchen Sie, einen `http.server` einzurichten!

## Quiz Question

Welches Tool können Sie verwenden, um einen einfachen HTTP-Server mit Python zu erstellen?

## Quiz Answer

http.server
