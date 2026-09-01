---
lesson_id: "packet-analysis"
course_id: "troubleshooting"
lang: "fr"
order_index: 5
title: "Analyse de paquets"
description: "Apprenez à capturer une trace de paquets bornée et filtrée, puis à l'analyser prudemment avec tcpdump."
meta_title: "Analyse de paquets - Dépannage"
meta_description: "Découvrez l'analyse de paquets réseau sous Linux et utilisez tcpdump pour capturer et interpréter le trafic."
meta_keywords: "tcpdump, analyse de paquets, capture réseau, Wireshark, trafic réseau Linux"
---

Une capture enregistre le trafic visible depuis un point d'observation. Elle révèle échanges et chronologie, mais peut aussi collecter identifiants, données personnelles et trafic d'autres utilisateurs. Obtenez l'autorisation, réduisez la portée, protégez les fichiers et respectez la conservation prévue.

## Choisir le point d'observation

Capturez sur l'interface et dans l'espace de noms où passe réellement le flux touché. Ponts, conteneurs, VPN, agrégats, VLAN et déchargement peuvent modifier ce qu'une interface montre. Utilisez `ip route get` et `ip link` pour repérer les candidates.

:::single-choice{#packet-analysis-interface-choice} Pourquoi le choix de l'interface de capture importe-t-il ?

::option[Chaque interface reflète automatiquement tout Internet.]{#packet-analysis-mirrors-internet explanation="Un hôte ne voit normalement que le trafic livré ou répliqué vers ses interfaces."}
::option[Seul le trafic visible à ce point d'observation peut être enregistré.]{#packet-analysis-visible-point .correct explanation="Espaces de noms, tunnels, ponts et routage peuvent placer le flux ailleurs."}
::option[Le nom de l'interface déchiffre les données TLS.]{#packet-analysis-name-decrypts explanation="Un nom ne fournit aucune capacité de déchiffrement."}
:::

## Capturer un flux borné

Capturez au plus 100 paquets sans résolution de noms, limités à un hôte et à un port TCP :

```bash
$ sudo tcpdump -i enp1s0 -n -c 100 -w incident.pcap \
    'host 192.0.2.25 and tcp port 443'
```

`-i` choisit l'interface, `-n` garde les valeurs numériques, `-c` borne le nombre, `-w` écrit le pcap, et l'expression finale filtre la capture. Ajoutez aussi une limite de temps externe lorsque le trafic peut être absent.

:::single-choice{#packet-analysis-count-bound} Que fait `-c 100` ?

::option[Il capture seulement le port TCP 100.]{#packet-analysis-port-hundred explanation="Le port se choisit dans l'expression de filtre."}
::option[Il compresse le fichier à 100 octets.]{#packet-analysis-compress-hundred explanation="Cette option compte les paquets, pas la taille du fichier."}
::option[Il s'arrête après 100 paquets capturés.]{#packet-analysis-hundred .correct explanation="Cette borne empêche une capture laissée seule de croître indéfiniment en nombre de paquets."}
:::

## Lire les paquets capturés

Analysez le fichier sans le modifier :

```bash
$ tcpdump -n -tttt -r incident.pcap
```

Lisez horodatage, protocole, source, destination, indicateurs, séquences, acquittements et longueur selon le protocole. L'horodatage marque l'observation sur cet hôte, pas forcément l'émission exacte ailleurs. La synchronisation des horloges compte pour corréler plusieurs systèmes.

:::single-choice{#packet-analysis-read-file} Quelle option lit les paquets d'un fichier pcap enregistré ?

::option[`-r`]{#packet-analysis-option-read .correct explanation="L'option read traite un fichier de capture existant."}
::option[`-i`]{#packet-analysis-option-interface explanation="Cette option choisit une interface de capture en direct."}
::option[`-w`]{#packet-analysis-option-write explanation="Cette option écrit les paquets bruts dans un fichier."}
:::

## Interpréter l'absence et le chiffrement

Une capture vide peut venir d'une mauvaise interface ou d'un mauvais espace de noms, de pertes de capture, d'un filtre trop étroit, du déchargement, d'un autre routage ou d'une absence de trafic. Vérifiez les compteurs reçus et perdus de tcpdump et reproduisez un événement connu.

TLS masque normalement les charges utiles mais laisse des métadonnées utiles : extrémités, temps, tailles, comportement TCP et parties des négociations. Ne tentez aucun déchiffrement non autorisé et ne collectez pas de clés privées sans précaution.

:::single-choice{#packet-analysis-no-packets} Que prouve une capture filtrée vide ?

::option[Que l'application distante a été définitivement supprimée.]{#packet-analysis-empty-deleted explanation="Une erreur de point d'observation ou de filtre produit le même résultat."}
::option[Que tout le réseau ne transporte aucun trafic.]{#packet-analysis-empty-network explanation="Un filtre étroit peut exclure tout le trafic sans rapport."}
::option[Seulement qu'aucun paquet correspondant n'a été enregistré à ce point.]{#packet-analysis-empty-limited .correct explanation="Validez interface, espace de noms, filtre, pertes de capture et génération du test."}
:::

## Protéger et partager les preuves

Stockez les pcaps avec des permissions restrictives. Notez commande, hôte, interface, fuseau horaire, filtre et fenêtre d'incident, et hachez les preuves si leur intégrité compte. Avant partage, réduisez ou assainissez les données tout en préservant les champs nécessaires ; charges utiles et métadonnées peuvent identifier utilisateurs et systèmes.

:::single-choice{#packet-analysis-pcap-safety} Comment faut-il traiter un pcap d'incident ?

::option[Comme une preuve sensible, avec accès restreint et provenance documentée.]{#packet-analysis-sensitive-evidence .correct explanation="Une capture peut contenir des informations confidentielles et exige intégrité comme confidentialité."}
::option[Comme un texte inoffensif publiable sans examen.]{#packet-analysis-public explanation="Les captures binaires peuvent révéler charges utiles, identités et infrastructure."}
::option[En modifiant ses octets sur place sans conserver l'original.]{#packet-analysis-edit-original explanation="Cela détruit la provenance et peut invalider l'analyse ultérieure."}
:::

## Résumé

Vous savez créer une capture utile sans la rendre inutilement large ou dangereuse.

1. Choisir l'interface et l'espace de noms corrects.
2. Borner par filtre, nombre de paquets et temps.
3. Enregistrer les paquets bruts et analyser le fichier en lecture seule.
4. Interpréter correctement absence et chiffrement.
5. Protéger confidentialité, intégrité et provenance.
