---
lesson_id: "boot-process-bootloader"
course_id: "boot-system"
lang: "fr"
order_index: 3
title: "Processus de Démarrage : Chargeur d'Amorçage"
description: "Découvrez comment un chargeur sélectionne les artefacts Linux, construit la ligne de commande du noyau et lui transfère le contrôle."
meta_title: "Processus de Démarrage : Chargeur d'Amorçage - Démarrer le Système"
meta_description: "Guide sur le chargeur d'amorçage (bootloader) sous Linux. Découvrez ce qu'est un chargeur d'amorçage Linux, ses fonctions principales et comment GRUB utilise des paramètres noyau comme initrd et root pour démarrer le système."
meta_keywords: "chargeur d'amorçage linux, bootloader linux, chargeur d'amorçage linux, grub, qu'est-ce qu'un bootloader linux, paramètres noyau, initrd, système de fichiers root, processus de démarrage linux"
---

Un chargeur de démarrage fait le lien entre la découverte par le micrologiciel et l'exécution du noyau. GRUB est courant sur les PC Linux, mais systemd-boot, U-Boot, le chargement par le micrologiciel d'un noyau doté d'un stub EFI et d'autres conceptions remplissent différentes parties de ce rôle.

## Sélectionner les artefacts de démarrage

Une entrée du chargeur peut désigner :

- une image de noyau Linux ;
- une image initramfs facultative ou l'ancien initrd ;
- une ligne de commande du noyau ;
- des métadonnées propres à la plateforme ou le chargeur d'un autre système d'exploitation.

GRUB peut présenter plusieurs noyaux et entrées de récupération. Un noyau de repli n'est utile que si les modules et l'initramfs correspondants restent disponibles et testés. Le chargeur lit les fichiers grâce aux modules de stockage et de système de fichiers qu'il prend en charge ; il ne dépend pas du VFS Linux, qui ne fonctionne pas encore.

:::single-choice{#bootloader-primary-handoff}
À quoi un chargeur de démarrage Linux transfère-t-il normalement le contrôle ?

::option[À un shell utilisateur interactif où tous les services fonctionnent déjà.]{#bootloader-user-shell explanation="Les shells de l'espace utilisateur n'apparaissent qu'après le démarrage du noyau et du système init."}
::option[À l'image de noyau choisie après avoir chargé les artefacts nécessaires.]{#bootloader-selected-kernel .correct explanation="Le chargeur prépare le noyau, ses paramètres et souvent un initramfs avant d'exécuter le point d'entrée du noyau."}
::option[Au gestionnaire de paquets chargé de résoudre les dépendances.]{#bootloader-package-manager explanation="La gestion des paquets n'est pas la prochaine étape du transfert de contrôle du processeur pendant le démarrage."}
:::

## Paramètres de la ligne de commande du noyau

Le chargeur transmet une ligne de commande textuelle que le noyau et l'espace utilisateur précoce analysent. Parmi les exemples courants :

- `root=...` pour identifier le système de fichiers racine voulu ou sa spécification dans l'espace utilisateur précoce ;
- `ro` ou `rw` pour demander un mode initial de montage de la racine ;
- `quiet` pour réduire les messages du noyau sur la console ;
- `init=...` pour demander un autre premier programme de l'espace utilisateur lors d'une récupération spécialisée ;
- les paramètres `rd.*` propres aux distributions et interprétés par les outils de l'initramfs.

`initrd` est normalement une directive du chargeur qui désigne une image, pas un paramètre générique du noyau. `BOOT_IMAGE=` peut apparaître dans une ligne de commande produite par certaines configurations GRUB, mais ce n'est pas le mécanisme qui charge le noyau.

Inspectez la ligne de commande utilisée pour le démarrage actuel avec :

```bash
$ cat /proc/cmdline
```

:::single-choice{#bootloader-root-parameter}
Quel est le rôle du paramètre `root=` de la ligne de commande du noyau ?

::option[Identifier le système de fichiers racine que le démarrage devra finalement utiliser.]{#bootloader-root-filesystem .correct explanation="Le noyau ou l'initramfs interprète cette valeur pour localiser et assembler la véritable racine."}
::option[Définir le mot de passe de connexion du compte root.]{#bootloader-root-password explanation="Les secrets d'authentification ne doivent pas être transmis en clair dans la ligne de commande du noyau."}
::option[Renommer le PID 1 en `root`.]{#bootloader-root-pid explanation="Le nommage des processus n'a aucun rapport avec ce paramètre de stockage."}
:::

:::single-choice{#bootloader-quiet-parameter}
Que demande normalement le paramètre `quiet` ?

::option[Un accès en lecture seule à tous les systèmes de fichiers montés.]{#bootloader-quiet-readonly explanation="La politique initiale d'écriture de la racine utilise des paramètres comme `ro`, pas `quiet`."}
::option[La réduction des messages du noyau affichés pendant le démarrage.]{#bootloader-quiet-console .correct explanation="Ce paramètre masque de nombreux messages d'information, sans garantir le silence de tous les composants du démarrage."}
::option[La désactivation de tous les ventilateurs de refroidissement.]{#bootloader-quiet-fans explanation="Ce paramètre concerne la quantité de messages, pas le bruit du matériel."}
:::

## Modification temporaire et récupération

GRUB permet généralement à un utilisateur autorisé de la console de modifier une entrée pour un seul démarrage, souvent avec une touche d'édition indiquée dans le menu. Cette fonction permet de retirer `quiet`, choisir des paramètres de récupération ou corriger un mauvais identifiant de racine. L'interface et les autorisations varient, notamment avec Secure Boot et les configurations GRUB protégées par mot de passe.

La ligne de commande peut exposer du texte sensible dans `/proc/cmdline`, les journaux de démarrage et les rapports de plantage. Ses paramètres peuvent aussi affaiblir la sécurité ou empêcher le démarrage. N'y placez jamais de secret et conservez une entrée fonctionnelle ainsi qu'une procédure de récupération par la console.

:::single-choice{#bootloader-temporary-edit}
Quelle propriété caractérise généralement la modification interactive d'une entrée GRUB pour un démarrage ?

::option[Elle réécrit automatiquement toutes les images de noyau installées.]{#bootloader-rewrites-kernels explanation="La modification du texte de commande ne change pas les binaires du noyau."}
::option[Elle désactive définitivement la vérification du micrologiciel sur tous les disques.]{#bootloader-disables-firmware explanation="La politique du micrologiciel est distincte et n'est pas universellement modifiée par l'édition d'une entrée."}
::option[Le changement ne s'applique qu'à ce démarrage, sauf enregistrement séparé dans la configuration.]{#bootloader-one-boot-change .correct explanation="L'édition du menu modifie normalement l'entrée en mémoire, pas les sources persistantes de la configuration."}
:::

## Configuration GRUB persistante

Les distributions génèrent généralement la configuration GRUB finale à partir de modèles, de valeurs par défaut, de scripts et des noyaux détectés. Ne modifiez pas directement le fichier `grub.cfg` généré, sauf si la distribution documente explicitement cette méthode ; une régénération peut écraser vos changements.

Apportez une modification ciblée à la source, exécutez la commande de régénération documentée par la distribution, inspectez son résultat et testez en conservant une ancienne entrée fonctionnelle ainsi qu'un support de récupération amorçable. La commande et le chemin de sortie diffèrent entre Debian, Fedora et les installations UEFI ou BIOS.

:::single-choice{#bootloader-generated-config}
Pourquoi la modification directe d'un fichier `grub.cfg` généré est-elle généralement peu fiable ?

::option[Le fichier ne peut jamais contenir de texte lisible.]{#bootloader-config-binary explanation="La configuration GRUB est du texte, mais son caractère généré reste déterminant."}
::option[GRUB ne lit que les fichiers des répertoires personnels.]{#bootloader-grub-home explanation="La configuration de démarrage se situe au niveau du système et doit être disponible avant les sessions utilisateur."}
::option[Une régénération ultérieure peut écraser la modification manuelle.]{#bootloader-regeneration-overwrites .correct explanation="Les réglages persistants appartiennent généralement aux sources de configuration et au flux de génération de la distribution."}
:::

N'utilisez le laboratoire [Personnaliser le menu de démarrage GRUB2](https://labex.io/fr/labs/comptia-customize-the-grub2-boot-menu-in-linux-590859) que dans son environnement permettant la récupération.

## Résumé

Vous savez maintenant distinguer les directives du chargeur des paramètres de la ligne de commande du noyau.

1. Identifier le noyau, l'initramfs, la ligne de commande et les entrées alternatives.
2. Utiliser `root=`, `ro` et `quiet` selon leur rôle réel.
3. Inspecter les paramètres du démarrage actuel dans `/proc/cmdline`.
4. Considérer les modifications interactives comme temporaires et sensibles pour la sécurité.
5. Modifier une configuration générée persistante par le flux de travail de la distribution.
