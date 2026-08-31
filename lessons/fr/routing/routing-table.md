---
lesson_id: "routing-table"
course_id: "routing"
lang: "fr"
order_index: 2
title: "Table de routage"
description: "Découvrez comment lire les routes Linux et examiner celle qui est sélectionnée pour une destination."
meta_title: "Table de routage - Routage"
meta_description: "Guide de la table de routage Linux : interprétation de la destination, de la passerelle, du masque, de l’interface et de la commande ip route."
meta_keywords: "table routage Linux, genmask, eth0, commande route, routage réseau, routage IP, destination, passerelle, masque sous-réseau"
---

L’état de routage de Linux détermine le prochain saut, l’interface et la source admissibles pour une destination IP. L’ancienne vue `route -n` se rencontre encore, mais `ip route` expose plus directement les concepts modernes de routage du noyau.

## Lire les routes IPv4

Un exemple de sortie peut ressembler à ceci :

```text
$ ip -4 route show
default via 192.168.224.2 dev eth0 proto dhcp src 192.168.224.10 metric 100
192.168.224.0/24 dev eth0 proto kernel scope link src 192.168.224.10 metric 100
```

La route `/24` connectée envoie les destinations correspondantes directement par `eth0`. La route par défaut emploie la passerelle de prochain saut `192.168.224.2`. `proto` décrit comment la route a été installée, `src` indique une source privilégiée pour le trafic correspondant et une métrique aide à classer des routes par ailleurs comparables.

:::single-choice{#routing-table-via-meaning}
Qu’indique `via 192.168.224.2` ?

::option[La seule application autorisée à employer la route.]{#routing-table-application explanation="L’autorisation de l’application n’est pas encodée par le mot-clé `via`."}
::option[La passerelle de prochain saut de la route.]{#routing-table-next-hop .correct explanation="Le paquet est encapsulé dans une trame adressée à ce routeur local tout en conservant sa destination IP."}
::option[Le point de montage du système de fichiers de la route.]{#routing-table-mount explanation="Les entrées de routage concernent l’acheminement réseau, et non les systèmes de fichiers."}
:::

## Routes connectées et par défaut

Une route de `scope link` sans prochain saut `via` considère que le préfixe est directement accessible sur l’interface. Une route par défaut correspond à chaque adresse, mais perd face à toute route admissible plus spécifique.

:::single-choice{#routing-table-connected-route}
Comment une destination connectée de `scope link` est-elle normalement atteinte ?

::option[Par la passerelle par défaut même lorsqu’une route connectée correspond.]{#routing-table-connected-default explanation="Le préfixe connecté est plus spécifique et ne possède aucun opérande de passerelle."}
::option[En transformant la destination en serveur DNS.]{#routing-table-connected-dns explanation="Le service de noms n’intervient pas dans une route IP déjà sélectionnée."}
::option[Directement par l’interface nommée après la résolution du voisin.]{#routing-table-direct .correct explanation="L’hôte résout l’adresse de la destination sur la liaison et encapsule le trafic localement."}
:::

## Longueur du préfixe et métrique

La sélection des routes tient compte des règles de politique et choisit le préfixe admissible le plus long. Les métriques classent les routes au sein d’ensembles comparables appropriés ; une route par défaut à faible métrique ne l’emporte pas sur un `/24` correspondant simplement parce que son nombre est inférieur.

:::single-choice{#routing-table-prefix-before-default}
Quelle route correspond normalement le plus précisément à `192.168.224.50` ?

::option[`192.168.224.0/24 dev eth0`]{#routing-table-twenty-four .correct explanation="Le préfixe correspondant de 24 bits est le plus long parmi les routes présentées."}
::option[`default via 192.168.224.2`]{#routing-table-default-less-specific explanation="La route par défaut possède une longueur de préfixe nulle."}
::option[`192.168.0.0/16 via 192.168.224.3`]{#routing-table-sixteen explanation="Cette route couvre l’adresse, mais fixe moins de bits que `/24`."}
:::

## Règles de politique et tables multiples

Linux peut consulter plusieurs tables de routage selon les politiques d’`ip rule` fondées sur la source, une marque, l’interface ou d’autres sélecteurs. L’examen de la seule table principale peut donc manquer le chemin réel :

```bash
$ ip rule show
$ ip route show table all
```

Les espaces de noms réseau et les VRF peuvent également posséder un état distinct. Effectuez l’examen dans le même contexte que le processus concerné.

:::single-choice{#routing-table-policy-limit}
Pourquoi `ip route show` seul peut-il ne pas expliquer le chemin d’une application ?

::option[Des règles de politique ou un autre espace de noms réseau peuvent sélectionner un état de routage différent.]{#routing-table-policy-context .correct explanation="La recherche effective dépend des attributs du paquet et du contexte réseau du processus."}
::option[Les tables de routage Linux ne contiennent aucun préfixe de destination.]{#routing-table-no-prefixes explanation="Les préfixes de destination sont des clés fondamentales des routes."}
::option[Les applications n’envoient jamais de paquets IP.]{#routing-table-apps-never explanation="Le trafic des applications est transporté par les protocoles réseau et de transport."}
:::

## Interroger une route effective

Demandez au noyau d’évaluer une destination et une source facultative :

```bash
$ ip route get 203.0.113.10
$ ip route get 203.0.113.10 from 192.168.224.10
```

Le résultat prédit la recherche locale à cet instant. Il n’envoie aucune sonde et ne prouve pas l’accessibilité du voisin, des sauts en aval, du pare-feu ou de l’application.

:::single-choice{#routing-table-route-get-limit}
Que ne fait pas `ip route get` ?

::option[Afficher l’interface locale et le prochain saut choisis.]{#routing-table-get-does-interface explanation="Il s’agit de champs principaux du résultat de la recherche."}
::option[Évaluer la politique de routage locale actuelle pour une destination.]{#routing-table-get-does-policy explanation="La commande effectue une recherche de route dans le noyau."}
::option[Prouver la réussite de la livraison par chaque saut en aval.]{#routing-table-get-not-probe .correct explanation="Il s’agit d’une requête de décision locale, et non d’une sonde réseau de bout en bout."}
:::

## Résumé

Vous savez maintenant lire les entrées de routage Linux et interroger la décision locale effective.

1. Distinguer les routes connectées de celles qui passent par une passerelle.
2. Lire les champs de préfixe, interface, protocole, source et métrique.
3. Appliquer la correspondance au préfixe le plus long avant de comparer les métriques pertinentes.
4. Tenir compte des tables de politiques, des espaces de noms et des VRF.
5. Considérer `ip route get` comme une recherche, et non un test d’accessibilité.
