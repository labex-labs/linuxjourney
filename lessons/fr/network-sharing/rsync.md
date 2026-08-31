---
lesson_id: "rsync"
course_id: "network-sharing"
lang: "fr"
order_index: 2
title: "rsync"
description: "Découvrez comment prévisualiser, exécuter et vérifier une synchronisation sûre de répertoires, localement ou par SSH, avec rsync."
meta_title: "rsync - Partage réseau"
meta_description: "Découvrez la commande rsync sous Linux pour synchroniser efficacement des fichiers, transférer des données à distance et contribuer à une stratégie de sauvegarde fiable."
meta_keywords: "rsync, rsync Linux, synchronisation de fichiers, sauvegarde de données, synchronisation distante, commande rsync, transfert de fichiers Linux, tutoriel rsync"
---

`rsync` réconcilie les fichiers et les arborescences de répertoires tout en évitant le transfert inutile de données inchangées. Son efficacité ne rend pas chaque appel sûr : la syntaxe de la source, les barres obliques finales, les métadonnées, les exclusions et la politique de suppression déterminent le résultat.

## Lire la source et la destination

Synchronisez localement le contenu de `source/` dans `destination/` :

```bash
$ rsync -a -- source/ destination/
```

La barre oblique finale de `source/` signifie « copier le contenu de ce répertoire ». Sans elle, `rsync -a source destination/` crée ou met à jour `destination/source`. Prévisualisez toujours les chemins produits lorsque vous modifiez la présence de cette barre.

:::single-choice{#rsync-source-trailing-slash}
Que signifie la barre oblique finale dans `rsync -a source/ destination/` ?

::option[Supprimer la source après un transfert réussi.]{#rsync-delete-source explanation="La suppression de la source exige une option et une politique explicites distinctes."}
::option[Copier le contenu de `source` dans la destination.]{#rsync-copy-contents .correct explanation="Le retrait de la barre après la source modifie l’organisation de premier niveau à la destination."}
::option[Interpréter la destination comme un partage Windows distant.]{#rsync-windows-share explanation="La barre contrôle le contenu du répertoire, et non le type de transport."}
:::

## Comprendre le mode archive

Le mode archive, `-a`, équivaut à un ensemble d’options récursives et de conservation des métadonnées souvent résumé par `-rlptgoD`. Il conserve les liens symboliques, les permissions, les dates de modification, les groupes, les propriétaires ainsi que les fichiers de périphérique ou spéciaux lorsque les permissions et la plateforme le permettent.

Le mode archive ne conserve pas les liens physiques, les ACL ni les attributs étendus ; ceux-ci nécessitent généralement `-H`, `-A` et `-X`. Il ne crée pas non plus de versions historiques à lui seul.

:::single-choice{#rsync-archive-limit}
Quelle métadonnée n’est pas incluse dans `-a` à elle seule ?

::option[Les relations entre liens physiques.]{#rsync-hard-links .correct explanation="La conservation des liens physiques nécessite l’option distincte `-H`."}
::option[Le parcours récursif des répertoires.]{#rsync-archive-recursion explanation="Le mode archive inclut le parcours récursif."}
::option[Les dates de modification.]{#rsync-archive-times explanation="Le mode archive inclut la conservation des dates."}
:::

## Prévisualiser un transfert

Effectuez une simulation avec le détail des modifications avant une synchronisation lourde de conséquences :

```bash
$ rsync -a --dry-run --itemize-changes -- source/ destination/
```

Une simulation prédit les actions à partir de l’analyse actuelle ; elle ne garantit pas que les fichiers resteront inchangés avant la vraie commande. Enregistrez et examinez la commande exacte, puis ne la relancez sans `--dry-run` qu’après avoir confirmé les deux extrémités.

:::single-choice{#rsync-dry-run-purpose}
Que fournit `--dry-run --itemize-changes` ?

::option[Un instantané permanent conservé sur un autre périphérique.]{#rsync-dry-backup explanation="Une simulation ne crée aucune copie des données ni conservation indépendante."}
::option[La garantie que les fichiers source ne pourront pas changer ensuite.]{#rsync-dry-lock explanation="La prévisualisation ne verrouille pas l’arborescence source."}
::option[Un aperçu des modifications actuellement prévues par rsync.]{#rsync-dry-preview .correct explanation="Le détail de la simulation révèle les décisions relatives aux chemins et aux métadonnées avant toute mutation."}
:::

## Synchroniser par SSH

Envoyez des données vers un hôte distant ou récupérez-les depuis celui-ci avec l’opérande distant habituel :

```bash
$ rsync -a -- source/ alice@example.net:/srv/data/
$ rsync -a -- alice@example.net:/srv/data/ destination/
```

Cette forme de rsync moderne emploie couramment SSH, mais vérifiez le shell distant configuré, la clé d’hôte, les privilèges du compte et la disponibilité de rsync sur l’hôte distant. La compression avec `-z` peut aider pour des données compressibles sur une liaison limitée, mais gaspiller du temps processeur pour des données déjà compressées.

:::single-choice{#rsync-pull-direction}
Quel ordre des opérandes récupère des données distantes dans un répertoire local ?

::option[`rsync -a local/ host:/data/`]{#rsync-local-first explanation="Cet ordre envoie le contenu local vers la destination distante."}
::option[`rsync --delete host local`]{#rsync-missing-path explanation="Cette commande n’exprime pas la syntaxe du chemin distant présentée et ajoute une option destructive sans rapport."}
::option[`rsync -a host:/data/ local/`]{#rsync-remote-first .correct explanation="L’arborescence distante est la source et l’arborescence locale la destination."}
:::

## Considérer la suppression comme destructive

`--delete` retire de la destination les entrées absentes de la source au sein du périmètre synchronisé. Une inversion des extrémités, une mauvaise barre oblique ou une exclusion erronée peut donc effacer des données valides. Prévisualisez l’opération sur une destination de test, assurez-vous de disposer de sauvegardes récupérables, vérifiez l’état des montages et envisagez une limite du nombre de suppressions avant de l’autoriser.

Après l’exécution réelle, examinez l’état de sortie et les journaux, comparez le nombre de fichiers et les métadonnées attendus, puis testez un contenu représentatif ou une restauration. La synchronisation rsync reproduit à elle seule les suppressions ou les altérations indésirables et ne constitue pas une stratégie de sauvegarde complète.

:::single-choice{#rsync-delete-effect}
Que peut faire `--delete` pendant la synchronisation ?

::option[Chiffrer chaque fichier transféré avec la clé d’hôte SSH.]{#rsync-delete-encrypt explanation="La politique de suppression est sans rapport avec le chiffrement des fichiers."}
::option[Empêcher toute modification du système de fichiers de destination.]{#rsync-delete-readonly explanation="Elle autorise explicitement des modifications supplémentaires à la destination."}
::option[Supprimer les entrées de destination absentes du périmètre source sélectionné.]{#rsync-delete-destination .correct explanation="Cette option aligne le contenu de la destination sur celui de la source et exige une prévisualisation vérifiée ainsi qu’un plan de récupération."}
:::

## Résumé

Vous savez maintenant prévisualiser et vérifier une opération `rsync` sans en masquer les cas limites destructifs.

1. Utiliser les barres obliques finales pour exprimer l’organisation voulue des répertoires.
2. Ajouter les options de métadonnées non couvertes par le mode archive si nécessaire.
3. Examiner le détail de la simulation avant la synchronisation réelle.
4. Vérifier l’identité SSH et le sens des extrémités.
5. Traiter la suppression et la conservation des sauvegardes comme des politiques explicites.
