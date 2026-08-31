---
lesson_id: "route"
course_id: "network-config"
lang: "fr"
order_index: 2
title: "route"
description: "Découvrez comment examiner, ajouter, remplacer, supprimer et vérifier en toute sécurité les routes Linux avec ip."
meta_title: "route - Configuration réseau"
meta_description: "Apprenez à gérer la table de routage Linux : ajout, remplacement et suppression de routes avec la commande moderne ip route et l’ancienne commande route."
meta_keywords: "commande ip route Linux, route Linux, ajouter une route, supprimer une route, table de routage, routage réseau, réseau Linux, ip route"
---

Les routes manuelles modifient la manière dont le noyau choisit une interface de sortie et un prochain saut. Une erreur peut déconnecter l’hôte ou rediriger du trafic sensible ; examinez donc la route effective, le gestionnaire de configuration et la voie de récupération avant de modifier l’état.

## Examiner la décision actuelle

Relevez les routes pertinentes et demandez au noyau comment il atteint actuellement la destination :

```bash
$ ip -4 route show
$ ip route get 192.168.2.25
```

Examinez également les règles de routage par politiques et les tables secondaires lorsqu’elles existent. La recherche de route constitue une preuve locale ; elle n’envoie aucun trafic.

:::single-choice{#route-get-before-change}
Pourquoi exécuter `ip route get DESTINATION` avant de modifier une route ?

::option[Cette commande relève la décision locale actuelle afin de permettre une comparaison et un retour en arrière.]{#route-get-baseline .correct explanation="L’interface, le prochain saut et la source sélectionnés contribuent à définir la modification voulue."}
::option[Elle réserve définitivement la destination sur chaque routeur.]{#route-get-reserves explanation="La commande effectue une recherche locale et ne modifie aucun état distant."}
::option[Elle désactive toutes les règles de routage par politiques.]{#route-get-disables-policy explanation="La recherche évalue les politiques au lieu de les supprimer."}
:::

## Ajouter ou remplacer une route

Ajoutez une route vers le préfixe canonique en passant par un prochain saut accessible :

```bash
$ sudo ip route add 192.168.2.0/23 via 10.11.12.3 dev enp1s0
```

La passerelle doit être accessible par la liaison concernée ou conformément à une conception explicite et valide qui la considère comme directement connectée. `add` échoue lorsqu’une route équivalente existe déjà. `replace` crée ou modifie une route, ce qui convient aux configurations idempotentes, mais peut écraser un état fonctionnel ; examinez d’abord précisément la cible.

:::single-choice{#route-add-existing}
Que se passe-t-il généralement si `ip route add` vise une route qui existe déjà ?

::option[La commande supprime silencieusement l’ancien préfixe de destination.]{#route-add-deletes explanation="Add signale normalement que l’objet existe au lieu de le remplacer."}
::option[Elle échoue au lieu de remplacer la route existante.]{#route-add-fails .correct explanation="N’utilisez délibérément `replace` qu’après avoir examiné l’entrée qui sera modifiée."}
::option[Elle redémarre la passerelle sélectionnée.]{#route-add-reboots explanation="Une configuration de route locale ne peut pas demander ainsi le redémarrage d’un système distant."}
:::

## Supprimer avec précision

Précisez tous les attributs de la route à supprimer lorsque plusieurs routes candidates ou tables peuvent exister :

```bash
$ sudo ip route del 192.168.2.0/23 via 10.11.12.3 dev enp1s0
```

Une suppression indiquant uniquement la destination peut avoir une portée plus large que prévu ou être ambiguë. Avant de retirer la route, relevez la commande d’origine qui permettra de la restaurer.

:::single-choice{#route-delete-precision}
Pourquoi inclure le prochain saut et le périphérique lors de la suppression d’une route ?

::option[Pour identifier plus précisément l’entrée visée.]{#route-delete-exact .correct explanation="Des attributs explicites réduisent le risque de supprimer une autre route possédant le même préfixe."}
::option[Pour supprimer également l’adaptateur réseau physique.]{#route-delete-adapter explanation="La suppression d’une route ne retire pas l’objet de liaison du noyau."}
::option[Pour effacer la zone DNS de la destination.]{#route-delete-dns explanation="Le routage et les données DNS faisant autorité sont des systèmes distincts."}
:::

## Persistance et sécurité à distance

Une commande `ip route` ne modifie que l’état actuel du noyau. NetworkManager, systemd-networkd, netplan, ifupdown, DHCP, les démons de routage ou un système d’orchestration peuvent ensuite la remplacer. N’enregistrez la route auprès du gestionnaire actif qu’après avoir testé son comportement à l’exécution.

Sur un hôte distant, conservez une console indépendante et utilisez un mécanisme de retour en arrière qui ne dépend pas de la route modifiée. Vérifiez ensuite la recherche de route, l’état des voisins, le trafic dans les deux sens et le service réel.

:::single-choice{#route-runtime-persistence}
Que peut-il arriver à une route ajoutée manuellement après le rechargement du gestionnaire de réseau ?

::option[Elle devient pour toujours une fonction immuable du noyau.]{#route-manual-immutable explanation="Les routes d’exécution peuvent être supprimées ou remplacées."}
::option[Elle apparaît automatiquement sur chaque hôte du sous-réseau.]{#route-manual-all-hosts explanation="La commande ne modifie que l’espace de noms réseau actuel."}
::option[Elle peut disparaître si elle ne figure pas dans la politique persistante.]{#route-manual-disappears .correct explanation="Le gestionnaire réconcilie l’état du noyau avec ses profils configurés."}
:::

## Résumé

Vous savez maintenant modifier une route Linux de manière ciblée et récupérable.

1. Relever les routes, les règles et la recherche effective actuelles.
2. Utiliser un préfixe canonique et un prochain saut accessible.
3. Distinguer l’ajout du remplacement délibéré.
4. Supprimer la route exacte et conserver une commande de restauration.
5. Assurer la persistance par le gestionnaire actif et vérifier les deux sens du trafic.
