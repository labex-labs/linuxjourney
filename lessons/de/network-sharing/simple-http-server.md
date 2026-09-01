---
lesson_id: "simple-http-server"
course_id: "network-sharing"
lang: "de"
order_index: 3
title: "Einfacher HTTP-Server"
description: "Lerne, mit Pythons HTTP-Server vorübergehend ein kontrolliertes Verzeichnis bereitzustellen."
meta_title: "Einfacher HTTP-Server – Netzwerkfreigaben"
meta_description: "Lerne, mit Pythons Modul http.server schnell einen einfachen HTTP-Server unter Linux einzurichten und Dateien im Netzwerk vorübergehend bereitzustellen."
meta_keywords: "einfacher HTTP-Server Linux, einfacher Linux-Webserver, Python http.server, Python SimpleHTTPServer, Dateifreigabe, Netzwerkserver"
---

Pythons Modul `http.server` kann statische Dateien für einen kurzlebigen Test oder eine vertrauenswürdige Übertragung bereitstellen. Es ist kein Produktionswebserver und bietet weder Authentifizierung, Autorisierung, TLS, Ratenbegrenzung noch gehärtete Verarbeitung feindlichen Datenverkehrs.

## Ein Freigabeverzeichnis vorbereiten

Erstelle ein eigenes Verzeichnis, das nur zur Freigabe bestimmte Dateien enthält. Prüfe vor dem Start versteckte Dateien, symbolische Links, Berechtigungen und vertrauliche Metadaten. Stelle weder ein Home-Verzeichnis noch ein Repository-Stammverzeichnis, Anmeldedatenverzeichnis oder einen Systempfad bereit.

Verwende `--directory`, damit der freigegebene Stamm eindeutig ist:

```bash
$ python3 -m http.server 8000 --directory /srv/temporary-share
```

Wenn keine Indexdatei vorhanden ist, erzeugt das Modul normalerweise eine Verzeichnisauflistung. Jeder, der den Listener erreichen kann, kann möglicherweise bereitgestellte Inhalte aufzählen und herunterladen.

:::single-choice{#http-server-directory-option} Warum solltest du `--directory /srv/temporary-share` verwenden?

::option[Die Option verschlüsselt jede HTTP-Antwort automatisch.]{#http-server-directory-tls explanation="Die Verzeichnisoption fügt kein TLS hinzu."}
::option[Sie erstellt für jeden Downloader ein Konto.]{#http-server-directory-accounts explanation="Das grundlegende Modul bietet keine Benutzerauthentifizierung."}
::option[Sie legt den beabsichtigten Dokumentstamm ausdrücklich fest.]{#http-server-explicit-root .correct explanation="Ein ausdrücklicher, geprüfter Stamm verringert die Gefahr, Dateien aus einem versehentlichen Arbeitsverzeichnis offenzulegen."}
:::

## Die lauschende Adresse steuern

Binde an Loopback, wenn nur derselbe Host eine Verbindung herstellen soll:

```bash
$ python3 -m http.server 8000 --bind 127.0.0.1 --directory /srv/temporary-share
```

Binde zur Freigabe in einem vertrauenswürdigen Netzwerk bewusst an eine geeignete Schnittstellenadresse und bestätige die Firewallrichtlinie. Ein Lauf ohne einschränkende Bindung lauscht gewöhnlich auf allen verfügbaren Schnittstellen und kann das Verzeichnis über das beabsichtigte Netzwerk hinaus offenlegen.

:::single-choice{#http-server-loopback-bind} Wer kann normalerweise einen an `127.0.0.1` gebundenen Server erreichen?

::option[Clients auf demselben Host.]{#http-server-local-clients .correct explanation="Die Loopback-Bindung eignet sich für lokale Tests oder den Einsatz hinter einem bewusst konfigurierten Tunnel."}
::option[Jeder Host im öffentlichen Internet.]{#http-server-public explanation="Loopback gilt lokal für denselben Netzwerknamensraum und ist keine öffentliche Schnittstelle."}
::option[Nur über Bluetooth verbundene Geräte.]{#http-server-bluetooth explanation="Die Adresse hat nichts mit Bluetooth-Transport zu tun."}
:::

## Zugriff testen

Fordere vom bereitstellenden Host eine bekannte Datei an und untersuche die Antwort:

```bash
$ curl -f http://127.0.0.1:8000/example.txt
```

Verwende für einen autorisierten entfernten Test statt Loopback die ausgewählte Schnittstellenadresse. Bestätige sowohl, dass die beabsichtigte Datei zugänglich ist, als auch, dass eine Datei außerhalb des Dokumentstamms nicht zugänglich ist. Ein erfolgreicher Browseraufruf allein belegt weder angemessene Offenlegung noch Vertraulichkeit.

:::single-choice{#http-server-default-port-command} Welcher Port wird in `python3 -m http.server 8000` ausdrücklich ausgewählt?

::option[22]{#http-server-port-22 explanation="Port 22 wird gewöhnlich SSH zugeordnet und hier nicht ausgewählt."}
::option[8000]{#http-server-port-8000 .correct explanation="Der positionelle Portoperand weist das Modul an, wo es lauschen soll."}
::option[443]{#http-server-port-443 explanation="Der Befehl konfiguriert kein HTTPS auf Port 443."}
:::

## Stoppen und aufräumen

Führe den temporären Dienst in einem überwachten Terminal aus und beende ihn nach der Übertragung mit `Ctrl-C`. Überprüfe, dass der Listener verschwunden ist:

```bash
$ ss -ltn 'sport = :8000'
```

Entferne temporäre Kopien gemäß der Richtlinie zum Umgang mit Daten und nimm jede vorübergehende Firewallregel zurück. Verwende für dauerhafte, authentifizierte oder öffentlich erreichbare Verteilung einen gepflegten Server mit Zugriffskontrolle und TLS.

:::single-choice{#http-server-completion-check} Was sollte nach Abschluss der vorübergehenden Übertragung geschehen?

::option[Den Server stoppen und überprüfen, dass der Port nicht mehr lauscht.]{#http-server-stop-verify .correct explanation="Die Überprüfung bestätigt, dass der temporäre Netzwerkdienst tatsächlich beendet wurde."}
::option[Den Listener weiterlaufen lassen, falls ihn später jemand benötigt.]{#http-server-leave-running explanation="Unnötige Offenlegung sollte entfernt werden, sobald der autorisierte Zweck endet."}
::option[Weitere private Dateien in den Dokumentstamm kopieren.]{#http-server-add-private explanation="In das bereitgestellte Verzeichnis gehören nur bewusst freigegebene Inhalte."}
:::

## Zusammenfassung

Du kannst nun einen temporären Python-HTTP-Server mit begrenzter Offenlegung ausführen.

1. Stelle nur ein eigenes, geprüftes Verzeichnis bereit.
2. Binde an die engstmögliche geeignete Adresse.
3. Teste beabsichtigten Zugriff und unbeabsichtigte Grenzen.
4. Stoppe den Listener und räume den temporären Zugang anschließend auf.
