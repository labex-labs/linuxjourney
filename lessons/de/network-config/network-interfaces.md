---
lesson_id: "network-interfaces"
course_id: "network-config"
lang: "de"
order_index: 1
title: "Netzwerkschnittstellen"
description: "Lerne, Zustand, Adressen, Statistiken und Eigentümer dauerhafter Konfiguration von Linux-Schnittstellen zu untersuchen."
meta_title: "Netzwerkschnittstellen – Netzwerkkonfiguration"
meta_description: "Eine umfassende Anleitung zu Linux-Netzwerkschnittstellen. Lerne ifconfig und den modernen Befehl ip kennen und verstehe Konfigurationsdateien wie /etc/network/interfaces."
meta_keywords: "Linux-Schnittstelle, Linux-Netzwerkschnittstelle, etc network interfaces, Debian-Netzwerkschnittstellen, ifconfig, ip-Befehl, Netzwerkkonfiguration, Linux-Vernetzung"
---

Eine Linux-Netzwerkschnittstelle verbindet einen Netzwerknamensraum mit einem physischen Gerät, Loopback-Pfad, einer Bridge, einem Tunnel, virtuellen Gerät oder einer anderen Verbindung. Schnittstellenzustand, Adressen, Routen, DNS und dauerhafte Konfiguration hängen zusammen, sind aber verschieden.

## Schnittstellen ermitteln

Verwende die modernen iproute2-Werkzeuge:

```bash
$ ip -brief link show
$ ip -brief address show
```

Schnittstellennamen können vorhersehbare, von Hardware abgeleitete Namen wie `enp1s0`, herkömmliche Namen wie `eth0` oder vom Administrator festgelegte Namen sein. Nimm niemals an, dass `eth0` existiert oder einen bestimmten Adapter bezeichnet.

:::single-choice{#interfaces-name-assumption} Warum sollte ein Skript `eth0` ermitteln, statt es vorauszusetzen?

::option[Jede Schnittstelle muss `lo` heißen.]{#interfaces-all-loopback explanation="Loopback ist eine besondere Schnittstelle und nicht der Name jeder Verbindung."}
::option[Linux-Systeme können mehrere Benennungsschemata für Schnittstellen verwenden.]{#interfaces-naming-varies .correct explanation="Von Hardware abgeleitete, virtuelle und benutzerdefinierte Namen machen eine feste Annahme zu `eth0` unzuverlässig."}
::option[Schnittstellennamen sind immer entfernte Passwörter.]{#interfaces-name-password explanation="Namen identifizieren Kernelgeräte und sind keine Anmeldedaten."}
:::

## Administrativer und betrieblicher Zustand

`UP` bedeutet, dass die Schnittstelle administrativ aktiviert ist. `LOWER_UP` zeigt gewöhnlich an, dass die untere Schicht Betriebsbereitschaft meldet, etwa einen Ethernet-Träger. Keines der Kennzeichen beweist für sich allein, dass IP-Adresse, Route, DNS, Firewall oder Anwendungspfad funktionieren.

```bash
$ ip -details link show dev enp1s0
$ ip -s link show dev enp1s0
```

Die Statistikansicht kann Fehler, verworfene Pakete und Zähler sichtbar machen, doch Zähler werden erst zusammen mit einem Zeitintervall und einer Grundlinie aussagekräftig.

:::single-choice{#interfaces-up-limit} Was beweist der administrative Zustand `UP` nicht?

::option[Dass die Ende-zu-Ende-Verbindung funktioniert.]{#interfaces-up-not-connectivity .correct explanation="Fehler bei unterer Schicht, Adressierung, Routing, Filterung, Benennung und Dienst können weiterhin bestehen."}
::option[Dass der Administrator die Schnittstelle aktiviert hat.]{#interfaces-up-does-prove explanation="Dies ist die unmittelbare Bedeutung des Zustands."}
::option[Dass die Schnittstelle ein Kernelobjekt besitzt.]{#interfaces-up-kernel-object explanation="Der angezeigte Zustand gehört zu einer vorhandenen Kernelschnittstelle."}
:::

## Laufzeitzustand ändern

Zu den Laufzeitbefehlen gehören:

```bash
$ sudo ip link set dev enp1s0 up
$ sudo ip address add 192.0.2.10/24 dev enp1s0
```

Diese Änderungen beeinflussen den aktuellen Kernelzustand und können mit einem Netzwerkmanager in Konflikt geraten, der später sein Profil erneut anwendet. Das Deaktivieren einer Schnittstelle zur Fernverwaltung kann den Zugriff sofort beenden. Überprüfe vorher das genaue Gerät, bewahre Konsolenzugang, erfasse den aktuellen Zustand und bereite eine zeitgesteuerte oder getestete Rücknahme vor.

:::single-choice{#interfaces-ip-address-add-persistence} Garantiert `ip address add` für sich allein Dauerhaftigkeit nach einem Neustart?

::option[Nein; das aktive Konfigurationssystem muss die Einstellung ebenfalls speichern.]{#interfaces-manager-persistence .correct explanation="NetworkManager, systemd-networkd, ifupdown oder ein anderer Eigentümer wendet dauerhafte Richtlinien an."}
::option[Ja, weil jede Kerneländerung alle Managerprofile bearbeitet.]{#interfaces-runtime-always-persistent explanation="Kernel-Laufzeitänderungen aktualisieren nicht allgemein die dauerhafte Konfiguration."}
::option[Nur, wenn die Adresse eine private IPv4-Adresse ist.]{#interfaces-private-persistent explanation="Der Adressbereich macht einen Laufzeitbefehl nicht dauerhaft."}
:::

## Eigentümer der Konfiguration ermitteln

Dauerhafte Pfade unterscheiden sich zwischen Distributionen und Installationen. Möglichkeiten sind NetworkManager-Profile, systemd-networkd-Units, Netplan-Eingaben, `/etc/network/interfaces`, cloud-init oder Orchestrierung. Ermittle vor der Bearbeitung von Dateien, welcher Dienst das Gerät verwaltet:

```bash
$ systemctl --type=service --state=running | grep -E 'NetworkManager|networkd|networking'
$ networkctl status
$ nmcli device status
```

Verwende nur Befehle, die für den ermittelten Manager vorhanden sind. Zwei Manager, die dieselbe Verbindung steuern, können miteinander konkurrieren und gegenseitig ihren Zustand überschreiben.

:::single-choice{#interfaces-config-owner} Was sollte einer dauerhaften Schnittstellenänderung vorausgehen?

::option[Jede mögliche Netzwerkkonfigurationsdatei bearbeiten.]{#interfaces-edit-all explanation="Konkurrierende Definitionen erzeugen Konflikte und unvorhersehbare erneute Anwendung."}
::option[Ermitteln, welcher Netzwerkmanager die Schnittstelle verwaltet.]{#interfaces-identify-owner .correct explanation="Die richtige Konfigurationsquelle und Anwendungsmethode hängen von dieser Zuständigkeit ab."}
::option[Vor der Untersuchung alle aktuellen Routen löschen.]{#interfaces-delete-routes explanation="Dies ist destruktiv und kann den Wiederherstellungszugang entfernen."}
:::

## Eine Änderung überprüfen

Überprüfe Verbindungszustand, zugewiesene Adressen und Laufzeiten, ausgewählte Routen, Resolverzustand, Nachbarerreichbarkeit und die tatsächliche Anwendung. Teste bei einer dauerhaften Änderung einen kontrollierten Dienstneustart oder Systemneustart nur, wenn ein Wiederherstellungszugang besteht.

:::single-choice{#interfaces-change-verification} Was liefert bessere Belege, als nur die neue Adresse in `ip address` zu sehen?

::option[Der Schnittstellenname enthält eine Ziffer.]{#interfaces-digit explanation="Die Benennung bietet keine Ende-zu-Ende-Validierung."}
::option[Die Shell-Eingabeaufforderung hat noch dieselbe Farbe.]{#interfaces-prompt-color explanation="Das Erscheinungsbild des Terminals hat nichts mit dem Netzwerkbetrieb zu tun."}
::option[Routen, Resolverzustand und die beabsichtigte Anwendung funktionieren ebenfalls.]{#interfaces-end-to-end .correct explanation="Eine verwendbare Konfiguration hängt vom vollständigen Pfad und Dienstverhalten ab."}
:::

## Zusammenfassung

Du kannst eine Schnittstelle nun untersuchen und ändern, ohne Laufzeitzustand mit dauerhafter Richtlinie zu verwechseln.

1. Ermittle tatsächliche Schnittstellennamen und Adressen.
2. Trenne administrativen Zustand von betrieblicher Konnektivität.
3. Behandle direkte `ip`-Änderungen als aktuellen Kernelzustand.
4. Ermittle vor dauerhaften Änderungen den aktiven Konfigurationseigentümer.
5. Überprüfe anschließend Routing, Auflösung und Anwendungsverhalten.
