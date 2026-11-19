---
lesson_id: "web-https"
course_id: "web-security"
lang: "de"
order_index: 2
title: "HTTPS"
description: "Lerne zu erkennen, welchen Abschnitt einer Webanfrage HTTPS schützt."
meta_title: "HTTPS - Websicherheit"
meta_description: "Lerne zu erkennen, welchen Abschnitt einer Webanfrage HTTPS schützt."
meta_keywords: "HTTPS, TLS, Websicherheit, Cybersicherheit, Linux Journey"
---

HTTP legt fest, welche Nachrichten Browser und Server austauschen. HTTPS überträgt dieselben Nachrichten über **TLS**. Dieses Protokoll schützt die Verbindung und hilft dem Browser, den Server zu überprüfen.

## Die geschützte Verbindung erkennen

Stell dir vor, ein Browser verbindet sich mit `https://site.example`. Nach dem Aufbau der TLS-Verbindung können Browser und Server verschlüsselte HTTP-Nachrichten austauschen. Wer diesen Abschnitt des Netzes beobachtet, kann den HTTP-Inhalt nicht einfach mitlesen oder unbemerkt verändern.

```text
Browser  ===== HTTPS connection =====  Website server
```

Der Browser muss weiterhin die Identität überprüfen, die der Server vorlegt.

:::single-choice{#web-https-protected-hop} Was schützt HTTPS in diesem einfachen Aufbau?

::option[Die Seite, nachdem der Browser sie bereits angezeigt hat.]{#web-https-protected-hop-b explanation="Der Browser liest die Seite, nachdem er die Antwort entschlüsselt hat."}
::option[Alle Sicherungskopien der Website.]{#web-https-protected-hop-c explanation="Sicherungskopien brauchen einen eigenen Schutz."}
::option[Die HTTP-Nachrichten auf der geschützten Verbindung.]{#web-https-protected-hop-a .correct explanation="TLS schützt Nachrichten während der Übertragung zwischen seinen Endpunkten."}
:::

## Einen Weg mit mehreren Abschnitten lesen

Ein Proxy kann die Anfrage eines Browsers annehmen und an einen anderen Server weiterleiten. Endet TLS am Proxy, kann dieser die Anfrage vor dem Weiterleiten lesen. Die nächste Verbindung braucht einen eigenen Schutz. Prüfe deshalb jeden Abschnitt einzeln.

```text
Browser  === HTTPS ===  Proxy  --- HTTP ---  Internal server
```

In diesem Diagramm läuft die äußere Verbindung über TLS. Die innere Verbindung verwendet unverschlüsseltes HTTP.

:::single-choice{#web-https-inner-hop} Welcher Abschnitt braucht eine eigene Änderung, damit TLS ihn schützt?

::option[Vom Browser zum Proxy.]{#web-https-inner-hop-a explanation="Dieser Abschnitt verwendet bereits HTTPS."}
::option[Vom Proxy zum internen Server.]{#web-https-inner-hop-b .correct explanation="Dieser innere Abschnitt verwendet unverschlüsseltes HTTP."}
::option[Ein Browser-Tab, der die Website nie aufruft.]{#web-https-inner-hop-c explanation="Für diesen Tab zeigt das Diagramm keine Verbindung."}
:::

## Zugriffsentscheidungen gesondert prüfen

Eine gültige, sichere Verbindung hilft dir, die Identität des Servers zu überprüfen, und schützt die übertragenen Nachrichten. Die Anwendung entscheidet weiterhin, welches Konto eine Seite lesen oder eine Einstellung ändern darf. Eine private Seite kann gut durch TLS geschützt sein und braucht trotzdem Zugriffsregeln in der Anwendung.

:::single-choice{#web-https-access-vs-transport} Was sollte der Dienst vor der Ausgabe einer privaten Kontoseite prüfen?

::option[Ob das authentifizierte Konto die Seite lesen darf.]{#web-https-access-vs-transport-c .correct explanation="Die Autorisierung in der Anwendung legt fest, worauf das Konto zugreifen darf."}
::option[Nur ob die Verbindung TLS verwendet.]{#web-https-access-vs-transport-a explanation="HTTPS schützt die Übertragung. Der Dienst muss weiterhin über den Zugriff entscheiden."}
::option[Nur ob das Zertifikat für den angefragten Hostnamen gilt.]{#web-https-access-vs-transport-b explanation="Das Zertifikat hilft bei der Prüfung der Serveridentität. Die Anwendung regelt weiterhin den Zugriff auf private Seiten."}
:::

## Zusammenfassung

Du kannst jetzt beschreiben, was HTTPS auf dem Weg einer Webanfrage schützt.

1. Erkenne, wo TLS beginnt und endet.
2. Prüfe jeden Abschnitt, wenn ein Proxy die Anfrage weiterleitet.
3. Erkläre, warum die Anwendung weiterhin Zugriffskontrollen braucht.
