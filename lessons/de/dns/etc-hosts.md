---
lesson_id: "etc-hosts"
course_id: "dns"
lang: "de"
order_index: 4
title: "/etc/hosts"
description: "Lerne, wie lokale Zuordnungen der Hosts-Datei an der Linux-Namensauflösung teilnehmen und wie du sie sicher testest."
meta_title: "/etc/hosts – DNS"
meta_description: "Erkunde /etc/hosts unter Linux. Lerne statische Hostnamen-Zuordnungen, die Reihenfolge des Name Service Switch sowie Tests mit getent und dig kennen."
meta_keywords: "/etc/hosts, Hosts Datei Linux, Linux Netzwerk, Hostname Zuordnung, DNS Auflösung, nsswitch, getent, resolv.conf"
---

`/etc/hosts` stellt dem lokalen Namensdienst des Systems statische Einträge aus Adressen und Namen bereit. Die Datei eignet sich für Loopback-Namen, Abhängigkeiten beim Systemstart und eng begrenzte Tests. Sie veröffentlicht jedoch keine Einträge für andere Hosts und aktualisiert DNS nicht.

## Die Datei lesen

Eine Zeile beginnt mit einer IPv4- oder IPv6-Adresse, gefolgt von einem oder mehreren Namen:

```text
127.0.0.1       localhost
192.0.2.25      app-test.example.net app-test
2001:db8::25    app-test-v6.example.net app-test-v6
```

Kommentare beginnen mit `#`. Manche Werkzeuge behandeln den ersten Namen üblicherweise als kanonisch und spätere Namen als Aliase. Das Verhalten von Anwendungen und Resolver-APIs kann jedoch abweichen. Vermeide doppelte oder widersprüchliche Einträge für denselben Namen.

:::single-choice{#hosts-file-entry-order} Was steht auf einer normalen Zuordnungszeile in `/etc/hosts` an erster Stelle?

::option[Eine IP-Adresse.]{#hosts-file-address-first .correct explanation="Auf derselben Zeile folgen der Adresse ein oder mehrere Namen."}
::option[Die TTL eines DNS-Eintrags.]{#hosts-file-ttl-first explanation="Einträge der Hosts-Datei verwenden keine DNS-TTL-Felder."}
::option[Eine Transport-Portnummer.]{#hosts-file-port-first explanation="Die Datei ordnet Namen und Adressen, nicht Anwendungsports, einander zu."}
:::

## Resolver-Reihenfolge

Die Name-Service-Switch-Konfiguration, üblicherweise `/etc/nsswitch.conf`, bestimmt, wie Systemresolver-Funktionen `files`, DNS, Multicast-Systeme und andere Quellen kombinieren. Eine verbreitete Zeile lautet:

```text
hosts: files dns
```

Gehe nicht ohne Prüfung der Richtlinie davon aus, dass Dateien immer zuerst berücksichtigt werden. Anwendungen können außerdem eigene DNS-Bibliotheken, Caches, Proxys oder verschlüsselte Resolver verwenden und müssen dem Systempfad nicht folgen.

:::single-choice{#hosts-file-nss-order} Was bestimmt, ob der Systemresolver `/etc/hosts` vor DNS berücksichtigt?

::option[Die alphabetische Reihenfolge der Dateinamen unter `/etc`.]{#hosts-file-alphabetical explanation="Die Auflistungsreihenfolge des Dateisystems definiert keine Namensdienstrichtlinie."}
::option[Die Reihenfolge der Quellen in der Name-Service-Switch-Richtlinie.]{#hosts-file-nss-policy .correct explanation="Die Datenbankzeile `hosts:` steuert die normale Quellenreihenfolge des libc-Resolvers."}
::option[Die TCP-Fenstergröße des Ziels.]{#hosts-file-tcp-window explanation="Die Flusssteuerung des Transports steht in keinem Zusammenhang mit der lokalen Namenssuche."}
:::

## Über den Systemresolver testen

Verwende `getent`, um den konfigurierten Namensdienstpfad des Systems zu durchlaufen:

```bash
$ getent ahosts app-test.example.net
```

`dig` fragt DNS direkt ab und zeigt normalerweise keine Zuordnungen aus `/etc/hosts` an. Dieser Unterschied ist nützlich: Wenn `getent` erfolgreich ist, `dig` jedoch nicht, kann dies auf eine lokale Quelle oder eine abweichende Resolver-Richtlinie hinweisen.

:::single-choice{#hosts-file-getent-versus-dig} Welches Werkzeug eignet sich besser, um zu prüfen, ob die normale Systemauflösung einen Eintrag der Hosts-Datei erkennt?

::option[`dig`, weil es immer zuerst `/etc/hosts` liest.]{#hosts-file-dig-first explanation="Dig sendet DNS-Abfragen und umgeht den Suchpfad der Hosts-Datei."}
::option[`getent ahosts`, weil es die konfigurierten Namensdienstquellen verwendet.]{#hosts-file-getent .correct explanation="Es spiegelt den Resolver-Pfad wider, den viele native Anwendungen verwenden."}
::option[`ip route flush`, weil es alle Namen neu aufbaut.]{#hosts-file-flush-route explanation="Das Leeren von Routen ist zerstörerisch und steht in keinem Zusammenhang mit der Hosts-Datei."}
:::

## Sicher bearbeiten

Bewahre erforderliche Einträge für localhost und die Hostidentität, prüfe die beabsichtigte Adresse und nimm mit einem privilegierten Editorwerkzeug eine wiederherstellbare Änderung vor. Überschreibe nicht beiläufig eine echte öffentliche Domain für einen Test. Dadurch können Anmeldedaten oder Anwendungsverkehr unerwartet umgeleitet werden. Verwende einen eigenen Testnamen und entferne den Eintrag nach dem Experiment.

Teste nach der Bearbeitung die konkrete Anwendung, da sie einen Cache behalten oder einen anderen Resolver verwenden kann. Dokumentiere dauerhafte Überschreibungen, damit sie ihren Zweck nicht unbemerkt überdauern.

:::single-choice{#hosts-file-test-name} Warum solltest du einen eigenen Testnamen verwenden, statt den Namen eines öffentlichen Dienstes zu überschreiben?

::option[Öffentliche Namen dürfen keine Punkte enthalten.]{#hosts-file-public-no-dots explanation="Domainnamen bestehen häufig aus mehreren durch Punkte getrennten Bezeichnungen."}
::option[Eigene Namen erzeugen automatisch autoritative DNS-Zonen.]{#hosts-file-auto-zone explanation="Ein Eintrag der Hosts-Datei bleibt lokal und veröffentlicht keine Zone."}
::option[Das verringert das Risiko, echten Verkehr oder Anmeldedaten umzuleiten.]{#hosts-file-reduce-redirection .correct explanation="Eine lokale Überschreibung kann jeden Client des Systemresolvers betreffen, der den öffentlichen Namen verwendet."}
:::

## Resolver-Server konfigurieren

`/etc/resolv.conf` führt traditionell die Einstellungen des DNS-Resolvers auf, wird jedoch häufig von NetworkManager, systemd-resolved, DHCP oder einem anderen Manager erzeugt. Prüfe symbolische Links und Dateikommentare. Ändere anschließend die zuständige Konfigurationsquelle, statt eine erzeugte Ausgabe zu bearbeiten, die wieder überschrieben wird.

:::single-choice{#hosts-file-resolv-owner} Was solltest du vor der Bearbeitung von `/etc/resolv.conf` tun?

::option[`/etc/hosts` und alle Netzwerkrouten löschen.]{#hosts-file-delete-state explanation="Diese zerstörerischen Änderungen sind nicht relevant und können die Verbindung entfernen."}
::option[Annehmen, dass jede Distribution dauerhafte Einstellungen direkt dort speichert.]{#hosts-file-assume-direct explanation="Viele Systeme erzeugen die Datei dynamisch oder verlinken sie mit einem verwalteten Stub."}
::option[Ermitteln, ob ein anderer Dienst die Datei erzeugt und verwaltet.]{#hosts-file-identify-resolver-owner .correct explanation="Dauerhafte Änderungen an DNS-Servern gehören in die Konfiguration des aktiven Managers."}
:::

## Zusammenfassung

Du kannst `/etc/hosts` nun als kontrollierte lokale Eingabe des Resolvers verwenden.

1. Schreibe Zuordnungen mit der Adresse zuerst und bewusst gewählten Namen und Aliasen.
2. Prüfe die Name-Service-Switch-Reihenfolge, statt sie vorauszusetzen.
3. Teste die Systemauflösung mit `getent` und DNS getrennt mit `dig`.
4. Verwende eigene temporäre Namen und prüfe die tatsächliche Anwendung.
5. Ändere Resolver-Server über die zuständige Konfigurationsverwaltung.
