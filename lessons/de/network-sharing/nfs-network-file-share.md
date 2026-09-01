---
lesson_id: "nfs-network-file-share"
course_id: "network-sharing"
lang: "de"
order_index: 4
title: "NFS"
description: "Lerne, eine NFS-Client-Einhängung zu ermitteln, einzuhängen, zu validieren und sicher zu automatisieren."
meta_title: "NFS – Netzwerkfreigaben"
meta_description: "Lerne das Network File System unter Linux kennen. Diese Lektion behandelt das Einrichten eines NFS-Clients, den Befehl mount und Automount für Netzwerkfreigaben."
meta_keywords: "NFS, NFS-Client, Automount, Network File System, Linux-Vernetzung, mount-Befehl, Linux-Tutorial, Einsteiger"
---

Das Network File System ermöglicht einem Client, über den lokalen Dateisystemnamensraum auf einen Serverexport zuzugreifen. Der Server steuert Exporte und einen großen Teil der Zugriffsrichtlinie; der Client bestimmt, wo und wann ein autorisierter Export eingehängt wird.

## Den Client vorbereiten

Installiere die NFS-Client-Werkzeuge der Distribution, die auf Systemen der Debian-Familie gewöhnlich als `nfs-common` und auf Systemen der Red-Hat-Familie als `nfs-utils` paketiert sind. Bestätige DNS- oder Adresserreichbarkeit, erlaubte NFS-Versionen, Firewallrichtlinie und den genauen Exportpfad mit dem Serveradministrator.

`showmount -e SERVER` kann Exporte auflisten, die über das ältere Mount-Protokoll bereitgestellt werden, ist jedoch nicht für jeden reinen NFSv4-Server maßgeblich. Eine fehlgeschlagene Auflistung beweist nicht, dass kein autorisierter NFSv4-Export existiert.

:::single-choice{#nfs-showmount-limit} Warum kann `showmount -e` für einen NFSv4-Server unvollständig sein?

::option[Der Befehl fragt ein älteres Exportauflistungsprotokoll ab, das möglicherweise nicht bereitgestellt wird.]{#nfs-showmount-protocol .correct explanation="NFSv4 kann arbeiten, ohne diesen getrennten Auflistungsdienst verfügbar zu machen."}
::option[Er zeigt nur die lokale CPU-Temperatur an.]{#nfs-showmount-temperature explanation="Der Befehl betrifft Exportinformationen eines NFS-Servers."}
::option[Er deaktiviert jeden aufgelisteten Export dauerhaft.]{#nfs-showmount-disables explanation="Die Auflistung ist eine schreibgeschützte Ermittlungsanfrage."}
:::

## Einen Export einhängen

Erstelle einen leeren, eigenen Einhängepunkt und hänge den genehmigten Export ein:

```bash
$ sudo mkdir -p /mnt/team
$ sudo mount -t nfs server.example.net:/srv/team /mnt/team
```

Gib nur dann eine Version an, wenn Richtlinie oder Kompatibilität dies erfordern, beispielsweise `-o vers=4.2`. Errate keine Leistungs- oder Sicherheitsoptionen. Bestätige die resultierende Quelle, den Typ und die Optionen:

```bash
$ findmnt --target /mnt/team
```

:::single-choice{#nfs-mount-operands} Was ist im mount-Befehl `server.example.net:/srv/team`?

::option[Das lokale Verzeichnis, das den entfernten Export verdeckt.]{#nfs-local-mountpoint explanation="Der lokale Einhängepunkt im Beispiel ist `/mnt/team`."}
::option[Der Name des zu installierenden Clientpakets.]{#nfs-package-name explanation="Paketnamen sind distributionsspezifisch und keine Quelloperanden von mount."}
::option[Der Server und der exportierte entfernte Pfad.]{#nfs-remote-export .correct explanation="Host und der Pfad hinter dem Doppelpunkt identifizieren die NFS-Quelle."}
:::

## Identität und Berechtigungen verstehen

NFS-Zugriff verbindet Serverexportregeln, Protokollsicherheit, numerische Identitäten oder Verzeichnisdienste und Dateisystemberechtigungen. Übereinstimmende angezeigte Benutzernamen auf zwei Hosts garantieren keine übereinstimmenden numerischen IDs. Herkömmliches `AUTH_SYS` sendet vom Client bereitgestellte numerische Identitäten und hängt stark von vertrauenswürdigen Client- und Netzwerkkontrollen ab; stärker geschützte Umgebungen können bei durchgängiger Konfiguration Kerberos-Sicherheitsmodi verwenden.

Der Server ordnet entfernten root durch Root Squashing gewöhnlich eine unprivilegierte Identität zu. Deaktiviere diesen Schutz nicht nur zur Behebung eines Berechtigungsfehlers; untersuche IDs, Verzeichniseigentum, Exportrichtlinie und das beabsichtigte Sicherheitsmodell.

:::single-choice{#nfs-name-versus-id} Warum können zwei Benutzer mit demselben angezeigten Namen unterschiedliche NFS-Berechtigungen erhalten?

::option[NFS-Berechtigungen können von der Zuordnung numerischer Identitäten abhängen.]{#nfs-numeric-mapping .correct explanation="Übereinstimmende Namen allein belegen nicht, dass Client und Server dieselbe UID und dieselben Gruppen auflösen."}
::option[NFS ignoriert alle Dateisystemberechtigungen.]{#nfs-ignores-permissions explanation="Dateisystem- und Exportberechtigungen bleiben Teil der Autorisierung."}
::option[Jede Einhängung ändert automatisch die Kontendatenbank des Servers.]{#nfs-changes-accounts explanation="Eine Client-Einhängung schreibt Serveridentitäten nicht um."}
:::

## Netzwerkeinhängungen automatisieren

Eine einfache Boot-Einhängung über `/etc/fstab` kann den Start verzögern, wenn Netzwerk oder Server nicht verfügbar sind. Verwende je nach Host `autofs` für bedarfsgesteuerte Zuordnungen oder systemd-Mountoptionen wie `_netdev,nofail,x-systemd.automount`, nachdem du ihre genaue Semantik getestet hast:

```fstab
server.example.net:/srv/team /mnt/team nfs4 rw,_netdev,nofail,x-systemd.automount 0 0
```

Bewahre vor der Bearbeitung von fstab einen Wiederherstellungszugang und validiere mit einem nicht destruktiven Parser oder kontrollierten Mounttest. Automount verbessert das Verfügbarkeitsverhalten, behebt aber weder Autorisierungs- noch DNS- oder Serverausfälle.

:::single-choice{#nfs-automount-benefit} Was ist ein Hauptvorteil der bedarfsgesteuerten Einhängung einer NFS-Freigabe?

::option[Sie gewährt jedem Client root-Zugriff auf den Export.]{#nfs-automount-root explanation="Der Einhängezeitpunkt setzt die Serverautorisierung nicht außer Kraft."}
::option[Sie kann vermeiden, dass der Server beim anfänglichen Bootvorgang verfügbar sein muss.]{#nfs-automount-boot .correct explanation="Die Verbindung wird bei Zugriff ausgelöst, statt unbedingt den frühen Systemstart zu blockieren."}
::option[Sie kopiert das vollständige Serverdateisystem auf den lokalen Datenträger.]{#nfs-automount-copy explanation="Eine Einhängung stellt entfernten Zugriff bereit und ist keine vollständige lokale Kopie."}
:::

## Aushängen und überprüfen

Stoppe oder koordiniere vor dem Aushängen Prozesse, die die Freigabe verwenden, und schließe Anwendungsarbeit ab. Hänge anschließend den Einhängepunkt aus und überprüfe, dass er verschwunden ist:

```bash
$ sudo umount /mnt/team
$ findmnt --target /mnt/team
```

Erzwungenes oder verzögertes Aushängen kann aktive Referenzen verbergen und Anwendungsfehler verursachen. Verwende solche Optionen nur bei einem diagnostizierten Fehler und mit einem ausdrücklichen Wiederherstellungsplan.

:::single-choice{#nfs-safe-unmount} Was sollte einem normalen Aushängen von NFS vorausgehen?

::option[Prozesse koordinieren, die die Freigabe verwenden, und wichtige Schreibvorgänge abschließen.]{#nfs-coordinate-writers .correct explanation="Das Entfernen eines aktiven Dateisystems aus Anwendungen kann E/A unterbrechen oder Arbeit unvollständig lassen."}
::option[Das Exportverzeichnis auf dem Server löschen.]{#nfs-delete-export explanation="Das Aushängen auf dem Client erfordert nicht, Serverdaten zu zerstören."}
::option[Alle Netzwerkschnittstellen des Clients deaktivieren.]{#nfs-disable-network explanation="Dies kann den geordneten Abschluss erschweren und ist nicht die normale Reihenfolge."}
:::

## Zusammenfassung

Du kannst eine NFS-Client-Einhängung nun mit ausdrücklichen Annahmen zu Identität und Verfügbarkeit betreiben.

1. Bestätige Clientwerkzeuge, Exportpfad, Protokoll und Netzwerkrichtlinie.
2. Hänge an einem eigenen Pfad ein und überprüfe wirksame Quelle und Optionen.
3. Diagnostiziere Berechtigungen anhand von Identität und Exportrichtlinie.
4. Verwende getestete bedarfsgesteuerte Einhängung, wenn Bootverfügbarkeit wichtig ist.
5. Koordiniere Benutzer, hänge normal aus und überprüfe die Entfernung.
