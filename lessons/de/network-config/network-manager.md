---
lesson_id: "network-manager"
course_id: "network-config"
lang: "de"
order_index: 4
title: "NetworkManager"
description: "Lerne, wie NetworkManager Geräte, dauerhafte Verbindungsprofile und aktiven Laufzeitzustand trennt."
meta_title: "NetworkManager – Netzwerkkonfiguration"
meta_description: "Entdecke die Rolle des NetworkManager-Daemons bei der modernen Linux-Netzwerkverwaltung. Lerne, wie er Netzwerkkonfiguration automatisiert und mit nmcli bedient wird."
meta_keywords: "NetworkManager, nm-tool, nmcli, Netzwerkmanager Linux, NetworkManager Linux, Linux-Netzwerkverwaltung, Netzwerkkonfiguration, Linux-Vernetzung"
---

NetworkManager verwaltet auf vielen Linux-Desktops und -Servern Netzwerkgeräte und aktiviert Verbindungsprofile. Er ist nicht allgemeingültig. Bestätige deshalb, dass er die Zielschnittstelle verwaltet, bevor du ihre Konfiguration mit `nmcli` änderst.

## Geräte und Verbindungen

Ein Gerät ist eine Kernelschnittstelle wie `enp1s0` oder `wlan0`. Eine Verbindung ist ein gespeichertes Profil mit IPv4-, IPv6-, DNS-, WLAN-, Routing- und weiteren Einstellungen. Ein Gerät kann mehrere Profile besitzen, doch normalerweise ist jeweils nur ein passendes Profil aktiv.

```bash
$ nmcli device status
$ nmcli connection show
$ nmcli connection show --active
```

:::single-choice{#networkmanager-device-profile} Was ist ein NetworkManager-Verbindungsprofil?

::option[Ein physischer Anschluss, der auf die Netzwerkkarte gelötet ist.]{#networkmanager-physical-connector explanation="Dies ist Hardware und kein NetworkManager-Profil."}
::option[Eine gespeicherte Einstellungsmenge, die auf einem Gerät aktiviert werden kann.]{#networkmanager-stored-settings .correct explanation="Profile speichern Konfiguration getrennt vom Kernelschnittstellenobjekt dauerhaft."}
::option[Ein von jedem aktiven Datenstrom aufgezeichnetes Paket.]{#networkmanager-packet-capture explanation="Profile beschreiben Konfiguration und enthalten nicht den gesamten Datenverkehr."}
:::

## Wirksamen Zustand untersuchen

Zeige das aktive Profil und Gerätedetails an:

```bash
$ nmcli -f GENERAL,IP4,IP6 device show enp1s0
$ nmcli connection show 'Wired connection 1'
```

Profileinstellungen, DHCP-Laufzeitergebnisse und Kernelzustand können sich unterscheiden. Vergleiche mit `ip address`, `ip route` und dem Resolver. Das veraltete `nm-tool` sollte keine Grundlage eines aktuellen Arbeitsablaufs sein.

:::single-choice{#networkmanager-active-command} Welcher Befehl listet aktive NetworkManager-Profile auf?

::option[`nmcli device delete --all`]{#networkmanager-delete-all explanation="Dies ist kein Untersuchungsbefehl und deutet auf eine destruktive Absicht hin."}
::option[`nmcli connection show --active`]{#networkmanager-show-active .correct explanation="Er filtert gespeicherte Verbindungen auf die aktuell aktivierten."}
::option[`ip route flush table all`]{#networkmanager-flush-routes explanation="Dies entfernt Routingzustand, statt Profile aufzulisten."}
:::

## Ein Profil ändern und aktivieren

Ändere ein benanntes Profil ausdrücklich und aktiviere es anschließend in einem Wartungsfenster:

```bash
$ sudo nmcli connection modify 'Wired connection 1' ipv4.method auto
$ sudo nmcli connection up 'Wired connection 1'
```

Die Änderung passt dauerhafte Profildaten an; die Aktivierung kann aktive Adressen, Routen und DNS ersetzen. Eine entfernte Änderung erfordert Konsolenzugang, gespeicherte ursprüngliche Einstellungen und eine unabhängige zeitgesteuerte Rücknahme. Verlasse dich nie darauf, dass die geänderte Verbindung ihren eigenen Wiederherstellungsbefehl transportiert.

:::single-choice{#networkmanager-modify-versus-up} Was ist der Unterschied zwischen `connection modify` und `connection up`?

::option[Modify startet den Host neu; up bearbeitet DNS-Quellcode.]{#networkmanager-reboot-source explanation="Keine der Beschreibungen entspricht den Befehlen."}
::option[Modify ändert Profileinstellungen; up aktiviert ein Profil.]{#networkmanager-change-activate .correct explanation="Dauerhaftigkeit und Laufzeitaktivierung hängen zusammen, sind aber getrennte Vorgänge."}
::option[Es sind schreibgeschützte Aliase, die Konnektivität niemals beeinflussen können.]{#networkmanager-readonly explanation="Beide können in diesem Arbeitsablauf den Zustand verändern."}
:::

## Überprüfen und Geheimnisse schützen

Überprüfe nach der Aktivierung Profilzustand, Kerneladressen und -routen, DNS, beide Adressfamilien und die beabsichtigte Anwendung. WLAN-, VPN-, 802.1X- und Mobilfunkprofile können Geheimnisse enthalten. Beschränke Profilberechtigungen und gib geheime Felder nicht in gemeinsamen Protokollen oder Shelltranskripten aus.

:::single-choice{#networkmanager-verification} Was beweist mehr als die NetworkManager-Meldung „connected“?

::option[Der Profilname enthält das Wort Wired.]{#networkmanager-name-proof explanation="Eine Bezeichnung belegt weder Pfad- noch Dienstzustand."}
::option[Das Terminalfenster bleibt geöffnet.]{#networkmanager-terminal-open explanation="Ein Terminal kann manche teilweisen Netzwerkfehler überstehen."}
::option[Die beabsichtigten DNS- und Anwendungstests sind erfolgreich.]{#networkmanager-end-to-end .correct explanation="Der Managerzustand muss mit Kernel- und Dienstverhalten verknüpft werden."}
:::

## Zusammenfassung

Du kannst NetworkManager-Profile nun verwalten, ohne sie mit Schnittstellenobjekten zu verwechseln.

1. Bestätige, dass NetworkManager das Zielgerät verwaltet.
2. Unterscheide gespeicherte Profile vom aktiven Laufzeitzustand.
3. Untersuche Geräte, alle Profile und aktive Profile getrennt.
4. Behandle Ändern, Aktivieren, Wiederherstellen und Überprüfen als getrennte Schritte.
