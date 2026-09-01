---
lesson_id: "network-file-sharing"
course_id: "network-sharing"
lang: "fr"
order_index: 1
title: "Présentation du partage de fichiers"
description: "Découvrez comment choisir et effectuer en toute sécurité un transfert de fichiers par SSH avec scp."
meta_title: "Présentation du partage de fichiers - Partage réseau"
meta_description: "Explorez le partage de fichiers sous Linux et apprenez à utiliser scp pour effectuer des transferts sécurisés de fichiers sur le réseau."
meta_keywords: "partage de fichiers Linux, commande scp, copie sécurisée, commandes Linux, cours Linux gratuit, transfert de fichiers réseau, ressources Linux"
---

Le déplacement de fichiers sur le réseau va de la copie ponctuelle aux partages montés en permanence et aux arborescences de répertoires synchronisées. Choisissez une méthode selon le sens du transfert, le volume des données, la fréquence des mises à jour, le modèle d’identité, la confiance accordée au réseau, les métadonnées requises et la nécessité d’un accès partagé en direct pour les clients.

## Choisir une méthode de transfert

- `scp` ou SFTP fournit une copie authentifiée par SSH ou un transfert interactif.
- `rsync` réconcilie efficacement des arborescences de répertoires localement ou par un transport tel que SSH.
- NFS présente les exportations d’un serveur comme des systèmes de fichiers montés, généralement entre des hôtes de type Unix.
- SMB, mis en œuvre par Samba sous Linux, permet un accès partagé depuis de nombreux systèmes d’exploitation.
- HTTP peut fournir de simples téléchargements, mais ne constitue pas un système de fichiers monté généraliste.

Une copie n’est pas automatiquement une sauvegarde. Une stratégie de sauvegarde doit également prévoir une conservation indépendante, des tests de restauration, des contrôles d’intégrité et une protection contre la même suppression ou compromission.

:::single-choice{#file-sharing-one-time-ssh-copy} Quel outil convient à une copie ponctuelle de fichiers par SSH ?

::option[`scp`]{#file-sharing-scp .correct explanation="SCP emploie l’authentification et le transport SSH pour copier des fichiers."}
::option[`uptime`]{#file-sharing-uptime explanation="Uptime indique la durée de fonctionnement et la charge de l’hôte au lieu de transférer des fichiers."}
::option[`logrotate`]{#file-sharing-logrotate explanation="Logrotate gère les générations de fichiers journaux sur un hôte."}
:::

## Comprendre les chemins de scp

La forme générale est `scp SOURCE DESTINATION`. Un opérande distant utilise couramment `utilisateur@hôte:chemin` :

```bash
$ scp -- report.txt alice@example.net:/srv/incoming/
$ scp -- alice@example.net:/srv/outgoing/result.txt ./result.txt
```

La première commande envoie un fichier local ; la seconde récupère un fichier distant. Les deux-points séparent l’hôte distant de son chemin. Placez entre guillemets les chemins qui contiennent des caractères interprétés par le shell et évitez les noms de fichiers non fiables ou ambigus.

:::single-choice{#file-sharing-scp-pull-source} Lors d’une récupération avec `scp`, où apparaît la spécification distante ?

::option[Comme source, avant la destination locale.]{#file-sharing-pull-source .correct explanation="Le sens de la copie suit l’ordre des opérandes source et destination."}
::option[Comme destination locale après chaque option.]{#file-sharing-pull-destination explanation="L’objet distant récupéré constitue l’opérande source."}
::option[Uniquement dans le fichier de configuration SSH de l’utilisateur.]{#file-sharing-pull-config explanation="La configuration SSH peut fournir des valeurs par défaut, mais le chemin distant copié reste un opérande."}
:::

## Copier un répertoire

Employez le mode récursif pour une arborescence de répertoires :

```bash
$ scp -r -- project/ alice@example.net:/srv/incoming/
```

Avant la copie, examinez la taille des données, les liens symboliques, les permissions, les exigences de propriété, l’espace libre et le nom de la destination. SCP ne définit pas de politique de synchronisation : des copies répétées de répertoires peuvent laisser à la destination des fichiers qui n’existent plus à la source.

:::single-choice{#file-sharing-scp-recursive} Que demande `scp -r` ?

::option[La suppression de la destination distante avant la copie.]{#file-sharing-scp-remove explanation="Le mode récursif parcourt les répertoires et ne définit aucune politique de nettoyage."}
::option[La copie récursive d’une arborescence de répertoires.]{#file-sharing-scp-tree .correct explanation="Cette option est nécessaire lorsque la source sélectionnée est un répertoire."}
::option[Un accès en lecture seule à la configuration SSH.]{#file-sharing-scp-readonly explanation="Cette option concerne le parcours des répertoires, et non l’accès à la configuration."}
:::

## Vérifier l’identité et les résultats

La vérification de la clé d’hôte SSH empêche de se connecter au mauvais serveur. Considérez une modification de la clé d’hôte comme un événement à vérifier par un canal de confiance plutôt que de contourner l’avertissement. Employez des comptes aux privilèges minimaux et une gestion des clés adaptée à l’environnement.

Après le transfert, vérifiez l’état de sortie, les fichiers attendus, leurs tailles, leurs métadonnées et, lorsque les exigences d’intégrité le demandent, les condensats calculés indépendamment aux deux extrémités. Confirmez que l’application de destination peut réellement lire les données.

:::single-choice{#file-sharing-host-key-change} Que faire lorsque SSH signale une modification inattendue de la clé d’hôte ?

::option[Désactiver la vérification des clés d’hôtes pour tous les transferts futurs.]{#file-sharing-disable-checking explanation="Cela supprime un contrôle important de l’identité du serveur."}
::option[Vérifier la nouvelle clé auprès d’une source de confiance avant de continuer.]{#file-sharing-verify-key .correct explanation="L’avertissement peut révéler un hôte reconstruit, une mauvaise destination ou une interception et doit être examiné."}
::option[Publier la clé privée d’authentification dans la sortie de la commande.]{#file-sharing-publish-key explanation="Les identifiants privés ne doivent pas être exposés."}
:::

## Résumé

Vous savez maintenant choisir et vérifier une copie ponctuelle et sécurisée de fichiers sur le réseau.

1. Adapter la méthode de partage aux besoins d’accès et de conservation.
2. Lire les opérandes locaux et distants de `scp` comme source et destination.
3. Employer délibérément le mode récursif pour les arborescences de répertoires.
4. Vérifier l’identité du serveur, le résultat du transfert et l’utilisabilité à la destination.
