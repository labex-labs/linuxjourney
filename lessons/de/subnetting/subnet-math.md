---
lesson_id: "subnet-math"
course_id: "subnetting"
lang: "de"
order_index: 3
title: "Subnetzberechnung"
description: "Lerne, IPv4-Netzwerk, Broadcast, Bereich und Adressanzahl aus einem Präfix zu berechnen."
meta_title: "Subnetzberechnung – Subnetting"
meta_description: "Lerne die Grundlagen der Subnetzberechnung. Diese Anleitung erklärt, wie du mit Subnetzmasken die Anzahl verfügbarer Hosts berechnest und binäre IP-Adressierung verstehst."
meta_keywords: "Subnetzberechnung, Subnetzmaskenberechnung, IP-Adresse, Subnetzmaske, Netzwerkhosts, Binär, Linux-Vernetzung, Hostberechnung, Einsteiger-Tutorial"
---

Bei der Subnetzberechnung wird eine Präfixlänge auf die 32 Bit einer IPv4-Adresse angewandt. Binäres Denken verhindert Fehler an Präfixgrenzen, die nicht mit Dezimaloktetten übereinstimmen.

## Die Netzwerkadresse bestimmen

Verwende die Adresse `192.168.1.165/24`:

```text
address  11000000.10101000.00000001.10100101
mask     11111111.11111111.11111111.00000000
network  11000000.10101000.00000001.00000000
```

Ein bitweises UND bewahrt Adressbits dort, wo die Maske eins ist, und löscht Hostbits. Das Ergebnis lautet `192.168.1.0/24`.

:::single-choice{#subnet-math-network-operation} Welche Operation bestimmt eine IPv4-Netzwerkadresse aus Adresse und Maske?

::option[Aneinanderreihung dezimaler Zeichenfolgen.]{#subnet-math-concatenation explanation="Das Verbinden ausgegebener Oktette wendet keine Präfixbits an."}
::option[Subtraktion von Transportports.]{#subnet-math-port-subtraction explanation="Ports haben nichts mit dem Netzwerkpräfix zu tun."}
::option[Bitweises UND.]{#subnet-math-bitwise-and .correct explanation="Netzwerkbits bleiben bestehen, während durch Nullen maskierte Hostpositionen gelöscht werden."}
:::

## Adressen zählen

Für das Präfix `/p` enthält der Hostanteil `32 - p` Bits. Die Gesamtzahl der Adressen ist:

```text
2^(32 - p)
```

Ein `/24` enthält daher `2^8 = 256` Adressen. In einem herkömmlichen Broadcast-Subnetz ist der ausschließlich aus Nullen bestehende Hostwert die Netzwerkadresse und der ausschließlich aus Einsen bestehende Wert der gerichtete Broadcast. Damit bleiben 254 gewöhnliche Unicast-Hostadressen.

:::single-choice{#subnet-math-24-total} Wie viele Adressen enthält ein IPv4-`/24` insgesamt?

::option[24]{#subnet-math-total-24 explanation="Die Präfixlänge zählt Netzwerkbits und keine Adressen."}
::option[256]{#subnet-math-total-256 .correct explanation="Acht Hostbits erzeugen 2^8 unterschiedliche Adresswerte."}
::option[254]{#subnet-math-total-254 explanation="Dies ist nach Abzug zweier besonderer Adressen die herkömmliche Anzahl verwendbarer Hosts und nicht die Gesamtzahl."}
:::

## Eine Blockgrenze bestimmen

Für `/26` lautet die Maske `255.255.255.192`. Die Blockgröße des letzten Oktetts beträgt `256 - 192 = 64`, sodass die Subnetzgrenzen bei 0, 64, 128 und 192 liegen. Die Adresse `192.168.1.165/26` liegt in:

```text
network:   192.168.1.128
broadcast: 192.168.1.191
range:     192.168.1.129 through 192.168.1.190
```

:::single-choice{#subnet-math-165-network} Wie lautet die Netzwerkadresse für `192.168.1.165/26`?

::option[`192.168.1.0`]{#subnet-math-network-zero explanation="Dies ist der erste `/26`-Block, der 0 bis 63 umfasst."}
::option[`192.168.1.165`]{#subnet-math-network-self explanation="Die angegebene Adresse besitzt innerhalb des `/26` von null verschiedene Hostbits."}
::option[`192.168.1.128`]{#subnet-math-network-128 .correct explanation="Der Wert 165 liegt im Block von 128 bis 191."}
:::

## Präfixausnahmen berücksichtigen

Die Abkürzung `2^host_bits - 2` gilt nicht allgemein. IPv4-`/31`-Präfixe sind für Punkt-zu-Punkt-Verbindungen definiert, bei denen beide Adressen Endpunkte sein können und kein gerichteter Broadcast benötigt wird. Ein `/32` identifiziert eine einzelne Hostroute oder Schnittstellenadresse. Netzwerktechnik und Protokollverwendung bestimmen, welche Adressen zuweisbar sind.

:::single-choice{#subnet-math-31-exception} Warum solltest du nicht von jedem IPv4-Präfix zwei Adressen abziehen?

::option[IPv4-Adressen enthalten bei keinem Präfix Hostbits.]{#subnet-math-no-host-bits explanation="Die meisten Präfixe lassen mindestens ein Hostbit."}
::option[Punkt-zu-Punkt-Verbindungen mit `/31` können beide Adressen als Endpunkte verwenden.]{#subnet-math-31-both .correct explanation="Das Punkt-zu-Punkt-Modell benötigt keine herkömmliche Reservierung für Netzwerk und gerichteten Broadcast."}
::option[Alle IPv4-Netzwerke verwenden Multicast statt Unicast.]{#subnet-math-all-multicast explanation="Gewöhnliche Unicast-Adressierung bleibt grundlegend."}
:::

## Berechnungen überprüfen

Verwende ein unabhängiges Werkzeug oder eine Bibliothek, um die manuelle Arbeit zu prüfen, und vergleiche anschließend mit der tatsächlichen Schnittstellen- und Routenkonfiguration. Ein mathematisch gültiges Präfix kann dennoch mit einem anderen Subnetz überlappen oder einen Vergabeplan verletzen.

:::single-choice{#subnet-math-valid-not-safe} Was beweist eine korrekte Subnetzberechnung nicht?

::option[Dass der Adressplan keine Überlappung oder keinen Richtlinienkonflikt besitzt.]{#subnet-math-no-conflict .correct explanation="Betriebliche Vergabe- und Routingbelege sind weiterhin erforderlich."}
::option[Dass IPv4-Adressen 32 Bit enthalten.]{#subnet-math-proves-size explanation="Die Berechnung beruht auf dieser festen Größe."}
::option[Dass Zweierpotenzen Blockanzahlen bestimmen.]{#subnet-math-powers explanation="Binäre Adresskombinationen verwenden grundsätzlich Zweierpotenzen."}
:::

## Zusammenfassung

Du kannst IPv4-Subnetzgrenzen nun berechnen und häufige Ausnahmen erkennen.

1. Bestimme eine Netzwerkadresse mit bitweisem UND.
2. Zähle Gesamtadressen anhand der Anzahl der Hostbits.
3. Verwende Blockgrößen, um Netzwerk- und Broadcastgrenzen zu bestimmen.
4. Behandle `/31` und `/32` entsprechend ihrem beabsichtigten Einsatz.
5. Vergleiche mathematische Ergebnisse mit dem tatsächlichen Adressplan.
