---
lesson_id: "etc-fstab-file-system-table"
course_id: "filesystem"
lang: "fr"
order_index: 7
title: "/etc/fstab"
description: "Découvrez comment déclarer dans `/etc/fstab` les montages persistants de systèmes de fichiers et les espaces de swap, puis les valider sans risque."
meta_title: "/etc/fstab - Le système de fichiers"
meta_description: "Apprenez à utiliser /etc/fstab sous Linux pour monter automatiquement des systèmes de fichiers au démarrage et valider sa syntaxe."
meta_keywords: "fstab, fstab Linux, etc fstab, /etc/fstab, fichier fstab, monter systèmes de fichiers, démarrage Linux, tutoriel fstab"
---

`/etc/fstab`, la table des systèmes de fichiers, déclare les systèmes de fichiers, espaces de swap, montages bind, sources réseau et autres rattachements que les outils système peuvent monter ou activer. Les entrées peuvent participer au démarrage, mais des options comme `noauto`, l'intégration de l'automontage et les règles du gestionnaire de services influencent le moment où cela se produit, voire empêchent l'opération.

## Les six champs

Une entrée conventionnelle comporte six champs séparés par des espaces :

```text
UUID=130b882f-7d79-436d-a096-1e594c92bb76 /data ext4 defaults,nosuid,nodev 0 2
```

1. **Source** : un chemin de périphérique, `UUID=`, `LABEL=`, une source réseau ou une autre spécification prise en charge.
2. **Cible** : le point de montage, ou `none` pour des usages comme le swap lorsque cela convient.
3. **Type** : le type du système de fichiers, `swap`, `none` ou un type automatique accepté.
4. **Options** : une liste séparée par des virgules, interprétée par les assistants de montage et les couches d'intégration.
5. **Champ dump** : il contrôle historiquement l'utilitaire de sauvegarde `dump` ; `0` désactive généralement la participation.
6. **Champ pass** : il contrôle l'ordre de `fsck` au démarrage lorsqu'il s'applique ; `0` désactive la vérification automatique par ce mécanisme.

Un espace à l'intérieur d'un champ doit être échappé selon la syntaxe fstab, par exemple avec `\040`. Un `#` situé hors d'un champ commence un commentaire.

:::single-choice{#fstab-field-count} Combien de champs une entrée normale de `/etc/fstab` contient-elle ?

::option[Quatre.]{#fstab-four-fields explanation="La source, la cible, le type et les options sont suivis des champs dump et pass."}
::option[Huit.]{#fstab-eight-fields explanation="Huit n'est pas le nombre standard de champs d'un enregistrement fstab."}
::option[Six.]{#fstab-six-fields .correct explanation="Le format traditionnel contient les champs source, cible, type, options, dump et pass."}
:::

## Identifiants de sources stables

Pour les systèmes de fichiers locaux, un UUID de système de fichiers est souvent plus stable qu'un nom d'énumération `/dev/sdX` :

```bash
$ lsblk -f
$ sudo blkid
```

N'employez `UUID=...` qu'après avoir confirmé que l'identifiant appartient au système de fichiers prévu. Le reformatage crée un nouvel UUID et une copie au niveau des blocs peut en dupliquer un. `PARTUUID=` identifie plutôt une entrée de table de partitions et possède une sémantique différente.

:::single-choice{#fstab-uuid-source} Qu'identifie normalement `UUID=...` dans le champ source ?

::option[Le compte utilisateur propriétaire du point de montage.]{#fstab-user-uuid explanation="L'identité du compte n'est pas sélectionnée par la syntaxe d'UUID de système de fichiers de la source."}
::option[Les métadonnées du système de fichiers qui portent cet UUID.]{#fstab-filesystem-uuid .correct explanation="Mount résout l'identifiant du système de fichiers vers un périphérique bloc disponible au lieu de dépendre de son nom d'énumération."}
::option[Le processus qui a démonté le système de fichiers en dernier.]{#fstab-process-uuid explanation="L'historique des processus n'est pas encodé dans ce champ source."}
:::

## Options de montage et champs de vérification

`defaults` se développe en un ensemble conventionnel d'options défini par l'implémentation ; il ne s'agit pas nécessairement de la règle la plus sûre pour chaque montage. Ajoutez des options selon la confiance et la charge de travail, comme l'accès en lecture seule ou les restrictions sur les nœuds de périphériques et le comportement setuid. Les systèmes réseau ou amovibles peuvent exiger des règles de délai, dépendance ou tolérance aux pannes pour éviter de bloquer le démarrage de façon inattendue.

Pour les systèmes de fichiers pris en charge par `fsck`, le système racine utilise conventionnellement la valeur pass `1` et les autres systèmes locaux vérifiés la valeur `2`. Les pratiques propres aux formats peuvent différer : certains types n'emploient pas le fsck générique au démarrage. Suivez donc la documentation du système de fichiers installé et de la distribution au lieu d'attribuer mécaniquement `2`.

:::single-choice{#fstab-pass-zero} Que demande la valeur `0` dans le sixième champ ?

::option[Ignorer pour cette entrée l'ordonnancement automatique de fsck au moyen de fstab.]{#fstab-pass-zero-skip .correct explanation="La valeur pass zéro exclut l'entrée de la séquence de vérification au démarrage régie par ce champ."}
::option[Monter le système de fichiers en lecture seule dans toutes les situations.]{#fstab-pass-zero-readonly explanation="Le comportement en lecture seule se définit dans le champ des options de montage."}
::option[Effacer le système de fichiers avant chaque démarrage.]{#fstab-pass-zero-erase explanation="Le champ pass ne formate ni n'efface un système de fichiers."}
:::

## Modifier en prévoyant une méthode de récupération

Une entrée incorrecte pour la racine, le démarrage ou un réseau indispensable peut interrompre le lancement du système. Avant toute modification :

1. Confirmez la présence d'une sauvegarde récente et d'un accès à la console ou au mode de secours.
2. Copiez le fichier existant en préservant ses permissions.
3. Vérifiez l'identité de la source et créez le point de montage prévu.
4. Effectuez une seule modification ciblée.
5. Validez et testez avant de redémarrer.

Ne placez pas d'identifiants directement dans une entrée fstab lisible par tous. Employez le mécanisme protégé d'identifiants de l'assistant de montage concerné.

:::single-choice{#fstab-editing-recovery} Pourquoi faut-il confirmer l'accès au mode de secours avant de modifier une entrée fstab essentielle ?

::option[Les modifications de fstab effacent toujours immédiatement la table de partitions.]{#fstab-no-partition-erase explanation="La modification du texte ne réécrit pas les partitions, même si les montages ultérieurs peuvent avoir des effets."}
::option[Le fichier ne peut être modifié qu'à partir d'un autre système d'exploitation.]{#fstab-other-os-only explanation="Il peut être modifié sous Linux avec les privilèges et précautions appropriés."}
::option[Une mauvaise entrée peut empêcher le démarrage normal d'atteindre un système utilisable.]{#fstab-boot-failure .correct explanation="L'échec de montages essentiels peut ouvrir le mode d'urgence ou bloquer les services qui en dépendent."}
:::

## Valider sans supposer la réussite

Commencez par une vérification statique lorsqu'elle est prise en charge :

```bash
$ sudo findmnt --verify --verbose
```

Testez ensuite la nouvelle entrée précise dans des conditions contrôlées, confirmez-la avec `findmnt`, puis démontez-la si le test était temporaire. `mount -a` tente de monter de nombreuses entrées admissibles et peut contacter des réseaux ou attacher des sources non souhaitées ; il ignore aussi les entrées déjà montées et celles marquées `noauto`. Ce n'est donc ni un vérificateur de syntaxe inoffensif, ni une preuve complète.

Sur les systèmes fondés sur systemd, rechargez la configuration du gestionnaire après avoir modifié fstab afin d'actualiser les unités de montage générées, puis vérifiez les dépendances et le comportement au démarrage selon la documentation locale.

:::single-choice{#fstab-mount-a-limit} Pourquoi `mount -a` ne constitue-t-il pas à lui seul une validation complète de fstab ?

::option[Il reformate toujours chaque périphérique répertorié avant son montage.]{#fstab-mount-a-formats explanation="Mount ne crée normalement pas de systèmes de fichiers."}
::option[Il peut ignorer des entrées et exécute de vastes opérations de montage réelles plutôt qu'une simple analyse syntaxique.]{#fstab-mount-a-incomplete .correct explanation="Les entrées déjà montées ou `noauto` peuvent ne pas être testées, tandis que les sources admissibles peuvent subir des effets réels."}
::option[Il ne lit que l'historique du shell et ignore fstab.]{#fstab-mount-a-history explanation="La commande consulte bien fstab pour les entrées admissibles."}
:::

Exercez-vous avec [Gérer les partitions et systèmes de fichiers Linux](https://labex.io/fr/labs/comptia-manage-linux-partitions-and-filesystems-590845) sur le stockage secondaire du laboratoire prévu pour permettre la récupération.

## Résumé

Vous savez maintenant lire et valider une entrée persistante de la table des systèmes de fichiers.

1. Analyser les champs source, cible, type, options, dump et pass.
2. Choisir un identifiant vérifié possédant la sémantique d'identité voulue.
3. Définir les règles de montage et de vérification du système de fichiers réel.
4. Préserver l'accès au mode de secours et effectuer une seule modification ciblée.
5. Combiner validation statique, montage précis et vérification des règles de démarrage.
