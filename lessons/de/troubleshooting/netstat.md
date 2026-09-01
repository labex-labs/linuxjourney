---
lesson_id: "netstat"
course_id: "troubleshooting"
lang: "de"
order_index: 4
title: "netstat"
description: "Lerne, Linux-Sockets, Listener, Warteschlangen und TCP-Zustände mit ss zu untersuchen."
meta_title: "netstat – Fehlersuche"
meta_description: "Lerne, mit netstat und ss Netzwerkverbindungen, Ports und Sockets unter Linux zu analysieren. Diese Anleitung behandelt Zustände wie SYN-SENT und CLOSE-WAIT."
meta_keywords: "Linux netstat, netstat, netstat-Befehl, SYN-SENT netstat, netstat CLOSE-WAIT, Netzwerkverbindungen, Linux-Vernetzung, Netzwerkanalyse, Linux-Tutorial"
---

Das ältere Werkzeug `netstat` zeigt Sockets, Routen und Schnittstellenstatistiken an. Auf modernem Linux ist `ss` das bevorzugte Werkzeug zur Socketuntersuchung, weil es Kernel-Socketzustand effizient offenlegt und mit iproute2 gepflegt wird.

## Lauschende Sockets auflisten

Zeige lauschende TCP- und UDP-Sockets numerisch einschließlich ihrer Prozesse, sofern erlaubt:

```bash
$ sudo ss -lntup
```

`-l` wählt Listener aus, `-n` vermeidet Namensauflösung, `-t` und `-u` wählen TCP beziehungsweise UDP aus, und `-p` fordert Prozessdaten an. UDP ist verbindungslos; seine unverbundenen gebundenen Sockets besitzen daher keine TCP-artigen `LISTEN`-Handshakes.

:::single-choice{#netstat-ss-numeric} Warum solltest du bei der Socketfehlersuche `-n` verwenden?

::option[Die Option erstellt einen neuen Netzwerknamensraum.]{#netstat-new-namespace explanation="Die Option steuert die Namensauflösung in der Ausgabe."}
::option[Sie verhindert die Auflösung von Adress- und Portnamen.]{#netstat-numeric-output .correct explanation="Numerische Ausgabe verhindert, dass eine Dienstnamenzuordnung mit der beobachteten Protokollidentität verwechselt wird."}
::option[Sie schließt jeden nicht lauschenden Socket.]{#netstat-close-sockets explanation="Die Untersuchung beendet keine Sockets."}
:::

## Ports, Endpunkte und Dienste

Ein lokaler Socketendpunkt verbindet eine Adresse, ein Transportprotokoll und einen Port. Eine TCP-Verbindung wird durch Protokoll sowie Quell- und Zieladressen und -ports unterschieden. `/etc/services` ordnet herkömmliche Namen Zahlen zu, beweist aber weder, welcher Prozess aktuell einen Port besitzt, noch welches Anwendungsprotokoll er spricht.

:::single-choice{#netstat-services-file-limit} Was belegt ein `/etc/services`-Eintrag wie `https 443/tcp`?

::option[Dass aktuell ein fehlerfreier HTTPS-Server lauscht.]{#netstat-healthy-listener explanation="Eine statische Namensdatenbank beweist keinen Laufzeitzustand."}
::option[Die herkömmliche Dienstnamenzuordnung für diesen Port.]{#netstat-conventional-name .correct explanation="Socketeigentum und tatsächliches Protokollverhalten erfordern Laufzeituntersuchung und Tests."}
::option[Dass sämtlicher Datenverkehr auf Port 443 korrekt verschlüsselt ist.]{#netstat-all-encrypted explanation="Eine Portnummer kann TLS-Verhalten nicht validieren."}
:::

## TCP-Zustände lesen

Häufige Zustände sind:

- `SYN-SENT`: Der lokale Endpunkt hat eine Verbindungsanfrage gesendet und wartet auf Fortschritt.
- `ESTAB`: Die TCP-Verbindung ist hergestellt.
- `CLOSE-WAIT`: Der Peer hat seine Senderichtung geschlossen, doch die lokale Anwendung hat ihren Socket noch nicht geschlossen.
- `TIME-WAIT`: Der aktiv schließende Endpunkt wartet, damit verzögerte Segmente ablaufen und der letzte Austausch sicher verarbeitet werden kann.

Große oder wachsende `CLOSE-WAIT`-Mengen weisen häufig auf das Aufräumverhalten der lokalen Anwendung hin. `TIME-WAIT` ist ein normaler Protokollzustand; Anzahl und Ressourcenauswirkungen bestimmen, ob er betrieblich problematisch ist.

:::single-choice{#netstat-close-wait-owner} Welche Seite muss einen Socket in `CLOSE-WAIT` noch schließen?

::option[Jeder Router im Internet.]{#netstat-all-routers-close explanation="Router besitzen den Endpunktsocket nicht."}
::option[Der autoritative DNS-Server.]{#netstat-dns-close explanation="Der Namensdienst hat nichts mit der lokalen TCP-Schließverarbeitung zu tun."}
::option[Die lokale Anwendung.]{#netstat-local-close .correct explanation="TCP hat das FIN des Peers empfangen und wartet, bis der lokale Prozess seine Seite schließt."}
:::

## Warteschlangen interpretieren

Die Bedeutung von `Recv-Q` und `Send-Q` hängt von Zustand und Protokoll ab. Bei hergestellten TCP-Sockets können sie Daten anzeigen, die auf den Empfang durch die Anwendung oder die Bestätigung der Übertragung warten. Bei lauschenden Sockets beschreiben Warteschlangenfelder den Verbindungsrückstau und nicht auf dieselbe Weise Byte der Anwendungsnutzlast.

Eine Momentaufnahme allein belegt weder Leak noch Engpass. Erfasse Stichproben über die Zeit und verknüpfe sie mit Prozessverhalten, Anwendungslatenz, erneuten Übertragungen und Ressourcengrenzen.

:::single-choice{#netstat-queue-snapshot} Warum reicht eine einzelne Momentaufnahme einer großen Socketwarteschlange nicht zur Diagnose?

::option[Linux speichert niemals Daten in Socketwarteschlangen.]{#netstat-no-queues explanation="Das Kernelnetzwerk ist auf Sende- und Empfangswarteschlangen angewiesen."}
::option[Jeder Warteschlangenwert ist eine Dateisystemberechtigung.]{#netstat-queue-permission explanation="Die Felder beschreiben Netzwerkzustand."}
::option[Die Auswirkungen einer Warteschlange benötigen Zustand, Verlauf und Arbeitslastkontext.]{#netstat-queue-context .correct explanation="Eine vorübergehende Spitze unterscheidet sich von einem anhaltenden Anwendungs- oder Netzwerkengpass."}
:::

## Eine Untersuchung filtern

Beschränke die Ausgabe auf das betreffende Protokoll, den Zustand, Endpunkt oder Prozess:

```bash
$ ss -tn state established
$ ss -ltn 'sport = :443'
```

Ein Listener beweist lokale Transportbereitschaft und keine entfernte Erreichbarkeit oder einen fehlerfreien Anwendungszustand. Führe anschließend zum Symptom passende Routen-, Firewall-, Paket-, TLS- und Anwendungstests durch.

:::single-choice{#netstat-listener-limit} Was beweist ein TCP-Listener auf Port 443 nicht?

::option[Dass ein lokaler Socket eine Bind- und Listenoperation angenommen hat.]{#netstat-listen-local explanation="Dies ist genau der angezeigte lokale Zustand."}
::option[Dass entfernte Clients eine gültige HTTPS-Anfrage abschließen können.]{#netstat-not-remote-proof .correct explanation="Pfadrichtlinie, TLS und Anwendungsverhalten bleiben ungetestet."}
::option[Dass TCP ein numerisches Portfeld besitzt.]{#netstat-port-field explanation="Die Listenerausgabe enthält eines unmittelbar."}
:::

## Zusammenfassung

Du kannst `ss` nun zur Untersuchung des Socketzustands verwenden, ohne Ports mit Anwendungen zu verwechseln.

1. Liste Listener numerisch mit Prozesskontext auf.
2. Unterscheide herkömmliche Dienstnamen von Laufzeiteigentum.
3. Interpretiere TCP-Schließzustände aus Sicht des lokalen Endpunkts.
4. Erfasse Warteschlangen im Zeitverlauf mit Arbeitslastkontext.
5. Überprüfe entferntes Anwendungsverhalten über einen lokalen Listener hinaus.
