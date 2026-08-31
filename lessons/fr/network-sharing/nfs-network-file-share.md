---
lesson_id: "nfs-network-file-share"
course_id: "network-sharing"
lang: "fr"
order_index: 4
title: "NFS"
description: "Découvrez comment trouver, monter, valider et automatiser en toute sécurité le montage d’un partage NFS côté client."
meta_title: "NFS - Partage réseau"
meta_description: "Découvrez le système de fichiers réseau NFS sous Linux : préparation du client, commande mount, permissions et montage automatique des partages réseau."
meta_keywords: "NFS, client NFS, montage automatique, système de fichiers réseau, réseau Linux, commande mount, tutoriel Linux, débutant"
---

Le système de fichiers réseau NFS permet à un client d’accéder à une exportation de serveur dans l’espace de noms de son système de fichiers local. Le serveur contrôle les exportations et une grande partie de la politique d’accès ; le client contrôle où et quand une exportation autorisée est montée.

## Préparer le client

Installez les utilitaires clients NFS de la distribution, généralement fournis par `nfs-common` sur les systèmes de la famille Debian ou `nfs-utils` sur ceux de la famille Red Hat. Confirmez avec l’administrateur du serveur le fonctionnement du DNS ou l’accessibilité de l’adresse, les versions NFS autorisées, la politique du pare-feu et le chemin exact de l’exportation.

`showmount -e SERVEUR` peut répertorier les exportations fournies par l’ancien protocole de montage, mais ne fait pas autorité pour tous les serveurs utilisant uniquement NFSv4. L’échec de cette liste ne prouve pas qu’il n’existe aucune exportation NFSv4 autorisée.

:::single-choice{#nfs-showmount-limit}
Pourquoi la sortie de `showmount -e` peut-elle être incomplète pour un serveur NFSv4 ?

::option[La commande interroge un ancien protocole de liste des exportations qui peut ne pas être exposé.]{#nfs-showmount-protocol .correct explanation="NFSv4 peut fonctionner sans rendre disponible ce service distinct de liste."}
::option[Elle affiche uniquement la température du processeur local.]{#nfs-showmount-temperature explanation="La commande concerne les informations d’exportation du serveur NFS."}
::option[Elle désactive définitivement chaque exportation affichée.]{#nfs-showmount-disables explanation="La liste est une demande de découverte en lecture seule."}
:::

## Monter une exportation

Créez un point de montage vide et dédié, puis montez l’exportation approuvée :

```bash
$ sudo mkdir -p /mnt/team
$ sudo mount -t nfs server.example.net:/srv/team /mnt/team
```

Ne précisez une version que si la politique ou la compatibilité l’exige, par exemple avec `-o vers=4.2`. Ne devinez pas les options de performances ou de sécurité. Confirmez la source, le type et les options obtenus :

```bash
$ findmnt --target /mnt/team
```

:::single-choice{#nfs-mount-operands}
Dans la commande de montage, que représente `server.example.net:/srv/team` ?

::option[Le répertoire local qui masque l’exportation distante.]{#nfs-local-mountpoint explanation="Dans l’exemple, le point de montage local est `/mnt/team`."}
::option[Le nom du paquet client à installer.]{#nfs-package-name explanation="Les noms des paquets varient selon les distributions et ne constituent pas des opérandes source du montage."}
::option[Le serveur et le chemin distant exporté.]{#nfs-remote-export .correct explanation="L’hôte et le chemin séparé par deux-points identifient la source NFS."}
:::

## Comprendre les identités et les permissions

L’accès NFS combine les règles d’exportation du serveur, la sécurité du protocole, les identités numériques ou les services d’annuaire et les permissions du système de fichiers. Des noms d’utilisateurs identiques affichés sur deux hôtes ne garantissent pas des identifiants numériques identiques. Le mécanisme traditionnel `AUTH_SYS` transmet les identités numériques fournies par le client et dépend fortement de la confiance accordée au client et des contrôles du réseau ; les environnements plus exigeants peuvent employer les modes de sécurité Kerberos lorsqu’ils sont configurés de bout en bout.

Le serveur associe généralement l’utilisateur root distant à une identité sans privilèges au moyen du mécanisme d’écrasement de root. Ne désactivez pas cette protection simplement pour résoudre une erreur de permission ; examinez les identifiants, la propriété du répertoire, la politique d’exportation et le modèle de sécurité voulu.

:::single-choice{#nfs-name-versus-id}
Pourquoi deux utilisateurs portant le même nom affiché peuvent-ils recevoir des permissions NFS différentes ?

::option[Les permissions NFS peuvent dépendre de l’association des identités numériques.]{#nfs-numeric-mapping .correct explanation="La concordance des noms ne prouve pas que le client et le serveur résolvent le même UID et les mêmes groupes."}
::option[NFS ignore toutes les permissions du système de fichiers.]{#nfs-ignores-permissions explanation="Les permissions du système de fichiers et des exportations participent toujours à l’autorisation."}
::option[Chaque montage modifie automatiquement la base des comptes du serveur.]{#nfs-changes-accounts explanation="Un montage client ne réécrit pas les identités du serveur."}
:::

## Automatiser les montages réseau

Un montage simple au démarrage dans `/etc/fstab` peut retarder le lancement du système lorsque le réseau ou le serveur est indisponible. Selon l’hôte, employez `autofs` pour des cartes de montage à la demande ou des options systemd telles que `_netdev,nofail,x-systemd.automount` après en avoir testé précisément le fonctionnement :

```fstab
server.example.net:/srv/team /mnt/team nfs4 rw,_netdev,nofail,x-systemd.automount 0 0
```

Avant de modifier fstab, préservez un accès de récupération et validez le fichier avec un analyseur non destructif ou un test de montage contrôlé. Un montage automatique améliore le comportement en cas d’indisponibilité, mais ne corrige ni les autorisations, ni le DNS, ni les pannes du serveur.

:::single-choice{#nfs-automount-benefit}
Quel est l’un des principaux avantages du montage à la demande d’un partage NFS ?

::option[Il accorde à chaque client un accès root à l’exportation.]{#nfs-automount-root explanation="Le moment du montage ne contourne pas les autorisations du serveur."}
::option[Il peut éviter d’exiger la disponibilité du serveur pendant le démarrage initial.]{#nfs-automount-boot .correct explanation="La connexion est déclenchée lors de l’accès au lieu de bloquer nécessairement les premières étapes du démarrage."}
::option[Il copie tout le système de fichiers du serveur sur le disque local.]{#nfs-automount-copy explanation="Un montage présente un accès distant et ne constitue pas une copie locale complète."}
:::

## Démonter et vérifier

Avant le démontage, arrêtez ou coordonnez les processus qui utilisent le partage et assurez-vous que les écritures importantes des applications sont terminées. Démontez ensuite le point de montage et vérifiez sa disparition :

```bash
$ sudo umount /mnt/team
$ findmnt --target /mnt/team
```

Un démontage forcé ou paresseux peut masquer des références actives et provoquer des erreurs applicatives ; réservez ces options à une panne diagnostiquée accompagnée d’un plan de récupération explicite.

:::single-choice{#nfs-safe-unmount}
Que faut-il faire avant un démontage NFS normal ?

::option[Coordonner les processus utilisant le partage et terminer les écritures importantes.]{#nfs-coordinate-writers .correct explanation="Retirer aux applications un système de fichiers actif peut interrompre les entrées-sorties ou laisser un travail inachevé."}
::option[Supprimer le répertoire exporté sur le serveur.]{#nfs-delete-export explanation="Le démontage côté client n’exige pas la destruction des données du serveur."}
::option[Désactiver toutes les interfaces réseau du client.]{#nfs-disable-network explanation="Cela peut compliquer l’achèvement ordonné et ne correspond pas à la procédure normale."}
:::

## Résumé

Vous savez maintenant exploiter un montage NFS côté client avec des hypothèses explicites sur l’identité et la disponibilité.

1. Confirmer les outils clients, le chemin exporté, le protocole et la politique réseau.
2. Monter sur un chemin dédié et vérifier la source et les options effectives.
3. Diagnostiquer les permissions au moyen des identités et de la politique d’exportation.
4. Employer un montage à la demande testé lorsque la disponibilité au démarrage est importante.
5. Coordonner les utilisateurs, démonter normalement et vérifier la disparition du montage.
