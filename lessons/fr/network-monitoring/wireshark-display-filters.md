---
lesson_id: "wireshark-display-filters"
course_id: "network-monitoring"
lang: "fr"
order_index: 4
title: "Filtres d’affichage Wireshark"
description: "Apprenez à limiter l’affichage d’une capture préparée à l’aide d’un filtre Wireshark."
meta_title: "Filtres d’affichage Wireshark - Supervision réseau"
meta_description: "Apprenez à limiter l’affichage d’une capture préparée à l’aide d’un filtre Wireshark."
meta_keywords: "filtres d’affichage Wireshark, supervision réseau, cybersécurité, Linux Journey"
---

Une capture de paquets peut contenir plusieurs protocoles. Un **filtre d’affichage** indique à Wireshark quels paquets enregistrés afficher. Il modifie la vue et laisse le fichier de capture intact.

## Sélectionner un protocole

Ouvrez la page de la [capture d’exemple](https://github.com/labex-labs/linuxjourney/blob/master/examples/network-monitoring/sample.pcap) sur GitHub et enregistrez le fichier sous le nom `sample.pcap`. Ouvrez-la dans Wireshark et saisissez `dns` dans le champ du filtre d’affichage. Dans un terminal Linux où TShark est installé, cette commande applique le même filtre au fichier enregistré. Le fichier contient une résolution sans danger et du trafic d’exercice distinct.

```bash
$ tshark -r sample.pcap -Y dns
```

L’option `-r` lit un fichier et `-Y` applique un filtre d’affichage. Cherchez une requête et sa réponse.

:::single-choice{#wireshark-display-filters-display-effect} La liste filtrée affiche deux lignes de moins que la vue initiale. Que sont devenus les autres paquets ?

::option[Ils ont été supprimés du fichier de capture.]{#wireshark-display-filters-display-effect-a explanation="Un filtre d’affichage modifie les résultats visibles."}
::option[Ils sont toujours enregistrés et ne correspondent pas à ce filtre.]{#wireshark-display-filters-display-effect-b .correct explanation="Effacez le filtre pour retrouver la vue complète."}
::option[Ils ont été renvoyés sur le réseau.]{#wireshark-display-filters-display-effect-c explanation="La lecture d’une capture enregistrée ne transmet pas ses paquets."}
:::

## Filtrer sur une adresse

Un filtre peut aussi cibler un champ du paquet. `ip.addr` correspond à une adresse IPv4 source ou de destination. Les deux signes égal comparent le champ à la valeur de l’exemple.

```bash
$ tshark -r sample.pcap -Y 'ip.addr == 192.0.2.10'
```

Les guillemets préservent l’expression sous forme d’un seul argument pour le shell. Vous pouvez repérer les deux extrémités dans les lignes affichées.

:::single-choice{#wireshark-display-filters-address-scope} Un paquet part d’une autre adresse et va vers 192.0.2.10. Correspond-il au filtre ?

::option[Oui, car une seule des deux extrémités doit correspondre.]{#wireshark-display-filters-address-scope-a .correct explanation="Le champ ip.addr peut correspondre à la source ou à la destination."}
::option[Non, car la condition vérifie uniquement la source.]{#wireshark-display-filters-address-scope-b explanation="Ce champ peut correspondre dans les deux sens."}
::option[Seulement si le paquet contient du DNS.]{#wireshark-display-filters-address-scope-c explanation="L’expression vérifie uniquement l’adresse IPv4."}
:::

![Sortie enregistrée de TShark comparant l’affichage limité au DNS à celui des deux protocoles de la capture d’exercice](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/network-monitoring/wireshark-display-filters/saved-dns-exchange.png)

## Interpréter une vue vide

Un résultat vide signifie que le filtre n’a trouvé aucun paquet correspondant dans le fichier examiné. Vérifiez l’expression, la période et le point de capture avant de faire un constat général. Commencez par effacer le filtre pour confirmer que la capture contient du trafic.

:::single-choice{#wireshark-display-filters-empty-capture-view} Vous appliquez dns à une capture enregistrée et aucune ligne ne s’affiche. Que pouvez-vous rapporter ?

::option[Personne n’a utilisé le DNS sur le réseau.]{#wireshark-display-filters-empty-capture-view-a explanation="Un fichier couvre un point de capture et une période limités."}
::option[Wireshark a effacé les traces DNS.]{#wireshark-display-filters-empty-capture-view-b explanation="Le filtre d’affichage ne supprime pas les paquets enregistrés."}
::option[Ce filtre n’a affiché aucun paquet DNS dans cette capture.]{#wireshark-display-filters-empty-capture-view-c .correct explanation="Le constat reste limité aux données examinées."}
:::

Pour examiner une autre capture dans un environnement accessible depuis le navigateur, essayez l’exercice sur les filtres d’affichage dans [Wireshark pour débutants](https://labex.io/courses/quick-start-with-wireshark).

## Résumé

Vous savez maintenant filtrer une capture de paquets enregistrée et expliquer la portée du résultat.

1. Sélectionnez un protocole à l’aide d’un filtre d’affichage.
2. Filtrez sur une adresse de paquet avec ip.addr.
3. Interprétez la vue filtrée en tenant compte des limites de visibilité de la capture.
