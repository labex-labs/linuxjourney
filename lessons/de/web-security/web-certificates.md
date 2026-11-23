---
lesson_id: "web-certificates"
course_id: "web-security"
lang: "de"
order_index: 3
title: "Zertifikate"
description: "Lerne, Name, Gültigkeitszeitraum und Aussteller eines TLS-Zertifikats zu prüfen."
meta_title: "Zertifikate - Websicherheit"
meta_description: "Lerne, Name, Gültigkeitszeitraum und Aussteller eines TLS-Zertifikats zu prüfen."
meta_keywords: "TLS-Zertifikate, Websicherheit, Cybersicherheit, Linux Journey"
---

Ein Browser braucht einen Nachweis, dass er die in der URL genannte Website erreicht hat. Ein TLS-**Zertifikat** enthält eine Identität und einen öffentlichen Schlüssel. Der Browser prüft mehrere Eigenschaften, bevor er der Identität vertraut.

## Die Namen ansehen

Öffne die GitHub-Dateiseite für das [öffentliche Übungszertifikat](https://github.com/labex-labs/linuxjourney/blob/master/examples/web-security/site-cert.pem) und speichere die Datei als `site-cert.pem`. Das Übungszertifikat ist selbstsigniert. Zeige mit OpenSSL den Aussteller, den Gültigkeitszeitraum und die alternativen Namen des Zertifikatsinhabers an. Die Option `-noout` unterdrückt die Ausgabe des kodierten Zertifikats.

```bash
$ openssl x509 -in site-cert.pem -noout -issuer -dates -ext subjectAltName
```

Im Abschnitt **Subject Alternative Name** stehen die DNS-Namen, für die das Beispielzertifikat gilt. Suche nach `DNS:site.example`. Der Browser gleicht den Namen aus der URL mit den Namen im Zertifikat ab.

:::single-choice{#web-certificates-wrong-name} Der einzige aufgeführte Name ist site.example. Welche URL passt zu diesem Namen?

::option[`https://site.example/`.]{#web-certificates-wrong-name-b .correct explanation="Der DNS-Name im Zertifikat stimmt mit dem Hostnamen in der URL überein."}
::option[`https://other.example/`.]{#web-certificates-wrong-name-a explanation="Das Beispielzertifikat führt einen anderen Namen auf."}
::option[`https://preview.site.example/`.]{#web-certificates-wrong-name-c explanation="Eine Subdomain gilt als eigener Name, falls das Zertifikat sie nicht abdeckt."}
:::

![Aufgezeichnete OpenSSL-Ausgabe mit dem Aussteller, dem Gültigkeitszeitraum und dem DNS-Namen site.example des Übungszertifikats](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/web-security/web-certificates/dns-name-and-validity.png)

## Den Gültigkeitszeitraum prüfen

`notBefore` und `notAfter` geben an, in welchem Zeitraum das Zertifikat verwendet werden kann. Vergleiche diese Angaben mit dem Zeitpunkt deiner Prüfung. Eine falsch eingestellte Uhr kann sich ebenfalls auf die Prüfung auswirken. Für eine vollständige Zertifikatsprüfung reichen die Datumsangaben allein nicht aus.

:::single-choice{#web-certificates-validity-period} Die aktuelle Uhrzeit liegt nach notAfter. Was solltest du untersuchen?

::option[Ob der richtige DNS-Name im Zertifikat steht.]{#web-certificates-validity-period-b explanation="Der Name ist für die Identitätsprüfung wichtig. Auch wenn er stimmt, liegt ein abgelaufenes Zertifikat außerhalb seines Gültigkeitszeitraums."}
::option[Ob sich das Passwort eines Nutzers geändert hat.]{#web-certificates-validity-period-c explanation="Die Anmeldung in der Anwendung ist von der Gültigkeit des Zertifikats unabhängig."}
::option[Ob das Zertifikat abgelaufen ist und erneuert werden muss.]{#web-certificates-validity-period-a .correct explanation="Der Endpunkt präsentiert ein Zertifikat außerhalb seines angegebenen Gültigkeitszeitraums."}
:::

## Die Vertrauenskette prüfen

Der **Aussteller** gibt an, wer das Zertifikat signiert hat. Browser prüfen normalerweise die Signaturen entlang einer Kette, die zu einer vertrauenswürdigen Zertifizierungsstelle führt. Der von OpenSSL angezeigte Aussteller ist ein Feld, das du lesen kannst. Die Prüfung der Kette ist ein eigener Schritt. Ein Übungszertifikat kann ausschließlich für eine Übungsumgebung gedacht sein.

:::single-choice{#web-certificates-trust-check} Der Name und der Gültigkeitszeitraum passen, aber der Browser vertraut dem Aussteller nicht. Was fehlt noch?

::option[Eine zweite Kopie der Datumsangabe aus dem Zertifikat.]{#web-certificates-trust-check-a explanation="Übereinstimmende Datumsangaben belegen nicht, wer für die Identität bürgt."}
::option[Eine gültige Zertifikatskette zu einer vertrauenswürdigen Stelle für diese Verbindung.]{#web-certificates-trust-check-c .correct explanation="Zusätzlich zu einem passenden Namen und gültigen Datumsangaben braucht der Browser eine vertrauenswürdige Kette."}
::option[Ein anderer Benutzername auf der Website.]{#web-certificates-trust-check-b explanation="Die Vertrauensprüfung findet vor der normalen Anmeldung in der Anwendung statt."}
:::

## Zusammenfassung

Du kannst jetzt drei wichtige Angaben für die Zertifikatsprüfung lesen.

1. Gleiche den Hostnamen aus der URL mit den Namen im Zertifikat ab.
2. Vergleiche die aktuelle Zeit mit dem Gültigkeitszeitraum des Zertifikats.
3. Prüfe die Vertrauenskette in einem eigenen Schritt.
