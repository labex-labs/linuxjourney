---
lesson_id: "dev-directory"
course_id: "devices"
lang: "fr"
order_index: 1
title: "/dev directory"
description: "Découvrez comment Linux expose les interfaces de périphériques et les pseudo-périphériques par des nœuds sous `/dev`."
meta_title: "Répertoire /dev - Périphériques"
meta_description: "Découvrez la fonction du répertoire /dev sous Linux. Ce guide explique ce qu'est le dossier dev, comment l'explorer avec `ls /dev`, et le rôle des fichiers de périphériques pour le matériel système."
meta_keywords: "dev sous linux, répertoire /dev sous linux, dossier dev linux, ls /dev, commande dev linux, fichiers de périphériques, nœuds de périphériques, périphériques linux"
---

Linux expose de nombreuses interfaces de périphériques du noyau au moyen d'objets spéciaux du système de fichiers appelés nœuds de périphériques. Ils apparaissent normalement sous `/dev`, avec des liens symboliques utiles et des points de communication. Ouvrir un nœud connecte une application à un pilote du noyau plutôt qu'à des octets stockés dans un fichier ordinaire.

## Explorer `/dev`

Listez le répertoire sans déréférencer ni lire les périphériques :

```bash
$ ls -l /dev
```

Les entrées peuvent représenter du stockage physique, des terminaux, des interfaces d'entrée, des périphériques logiques ou des pseudo-périphériques fournis par le noyau. Chaque composant matériel n'a pas nécessairement son propre nœud visible, et un même périphérique peut apparaître par plusieurs liens ou interfaces.

Le premier caractère d'une liste longue indique le type d'objet. Les nœuds de périphériques caractère et bloc apparaissent comme `c` et `b` ; les leçons suivantes étudient ces types et leurs numéros majeur et mineur.

:::single-choice{#dev-directory-device-node-purpose} Que se passe-t-il lorsqu'un programme ouvre un nœud de périphérique sous `/dev` ?

::option[Il lit toujours un fichier ordinaire qui contient une copie du matériel.]{#dev-directory-ordinary-copy explanation="Un nœud est un objet spécial ; il ne stocke pas une copie des données du périphérique comme un fichier ordinaire."}
::option[Il accède à une interface mise en œuvre par un pilote du noyau.]{#dev-directory-kernel-interface .correct explanation="Les opérations sur le nœud sont acheminées vers le comportement d'un pilote du noyau selon l'identité du périphérique."}
::option[Il recompile le code source du pilote de ce périphérique.]{#dev-directory-recompile-driver explanation="L'ouverture d'une interface ne lance aucun compilateur et ne reconstruit pas les modules du noyau."}
:::

## Pseudo-périphériques

Certains nœuds fournissent des services du noyau sans correspondre à un matériel physique. `/dev/null` accepte et élimine les données écrites :

```bash
$ command > /dev/null
```

Parmi les autres exemples, `/dev/zero` produit des octets nuls et `/dev/urandom` fournit des octets aléatoires par le sous-système du noyau. Chacun possède une sémantique précise ; ne déduisez pas son comportement de son seul nom.

:::single-choice{#dev-directory-null-behavior} Que fait `/dev/null` des données qui y sont écrites ?

::option[Il les stocke jusqu'au prochain redémarrage.]{#dev-directory-null-temporary-storage explanation="Le périphérique null est un puits et ne constitue pas un stockage temporaire."}
::option[Il les envoie à tous les terminaux connectés.]{#dev-directory-null-broadcast explanation="La diffusion vers les terminaux n'a aucun rapport avec ce pseudo-périphérique."}
::option[Il les élimine.]{#dev-directory-null-discards .correct explanation="Le périphérique null accepte les écritures sans conserver leur contenu."}
:::

## Gestion dynamique des périphériques

Sur les systèmes Linux modernes, le `devtmpfs` soutenu par le noyau peut créer les nœuds élémentaires à mesure que les périphériques apparaissent. Un gestionnaire en espace utilisateur comme `udev` traite les événements, applique permissions et propriétaires et crée des liens symboliques utiles ou des noms pilotés par des règles. La répartition exacte des responsabilités dépend du système.

Des liens stables comme `/dev/disk/by-id/` ou `/dev/disk/by-uuid/` sont plus sûrs dans une configuration que des noms dépendant de l'ordre de détection comme `/dev/sda`, lequel peut changer avec la topologie ou l'ordre de découverte.

:::single-choice{#dev-directory-persistent-link} Pourquoi un administrateur peut-il préférer `/dev/disk/by-id/...` à `/dev/sda` dans une configuration ?

::option[Le lien fondé sur un identifiant dépend moins de l'ordre de découverte.]{#dev-directory-stable-identifier .correct explanation="Les liens persistants proviennent des propriétés du périphérique plutôt que d'une lettre attribuée selon l'ordre d'énumération."}
::option[Le lien sauvegarde automatiquement chaque bloc du périphérique.]{#dev-directory-link-backup explanation="Un lien symbolique désigne le même périphérique et ne crée aucune sauvegarde."}
::option[Le lien contourne toutes les permissions du périphérique cible.]{#dev-directory-link-permissions explanation="L'ouverture par un lien symbolique atteint toujours le périphérique cible et ses contrôles d'accès."}
:::

## Interagir sans risque

Les outils standard peuvent ouvrir les nœuds, mais les lectures et écritures arbitraires ne sont pas pour autant sûres. La lecture peut exposer des données sensibles ; l'écriture vers un disque, un terminal ou une interface de micrologiciel peut corrompre des données ou perturber des utilisateurs. Les permissions, groupes, ACL, capacités et services intermédiaires limitent donc l'accès.

Commencez par des outils de découverte en lecture seule, confirmez le nœud et l'identité exacte du périphérique, puis suivez sa documentation. N'envoyez jamais de données vers une entrée `/dev` inconnue sur un système important.

:::single-choice{#dev-directory-direct-write-risk} Pourquoi faut-il éviter d'écrire des données arbitraires dans un nœud inconnu ?

::option[Chaque nœud est nécessairement un fichier texte inoffensif.]{#dev-directory-harmless-text explanation="Les nœuds de périphériques ne sont précisément pas des fichiers texte ordinaires."}
::option[L'opération peut agir directement sur le matériel, le stockage ou une autre interface du noyau.]{#dev-directory-write-impact .correct explanation="Les écritures invoquent des opérations définies par le pilote et peuvent avoir des effets destructeurs ou perturbateurs."}
::option[Linux convertit chaque écriture vers un périphérique en liste en lecture seule.]{#dev-directory-write-listing explanation="Le pilote détermine la sémantique de l'écriture ; le noyau ne transforme pas toutes les écritures en listes."}
:::

Utilisez le laboratoire [Explorer les périphériques matériels sous Linux](https://labex.io/fr/labs/comptia-explore-hardware-devices-in-linux-590861) pour une inspection en lecture seule dans un environnement contrôlé.

## Résumé

Vous savez maintenant décrire `/dev` comme un ensemble d'interfaces actives vers le noyau.

1. Distinguer les nœuds de périphériques des fichiers ordinaires.
2. Reconnaître les pseudo-périphériques comme `/dev/null`.
3. Relier les nœuds dynamiques et les liens persistants à la gestion des périphériques.
4. Considérer l'accès direct comme propre à chaque interface et potentiellement destructeur.
