---
lesson_id: "tracking-processes-lsof-fuser"
course_id: "process-utilization"
lang: "fr"
order_index: 2
title: "lsof et fuser"
description: "Découvrez comment identifier les processus qui utilisent des fichiers, des répertoires, des points de montage et des sockets réseau."
meta_title: "lsof et fuser - Utilisation des processus"
meta_description: "Explorez les commandes lsof et fuser sous Linux pour identifier les processus qui utilisent des fichiers et résoudre les erreurs de ressource occupée."
meta_keywords: "lsof, fuser, commande fuser, fuser Linux, fuser ou lsof, fuser -k Linux, fichiers ouverts, gestion processus, périphérique occupé"
---

Un système de fichiers peut rester occupé parce qu’un processus possède un fichier ouvert, mappe un fichier en mémoire ou emploie un répertoire comme répertoire de travail actuel. `lsof` et `fuser` aident à identifier ces relations. Commencez par examiner la situation ; l’arrêt des processus constitue une décision distincte aux conséquences opérationnelles.

## Répertorier les fichiers ouverts avec lsof

`lsof` signifie « list open files ». Interrogez un chemin pour afficher les enregistrements de fichiers ouverts correspondants :

```bash
$ sudo lsof -- /mnt/usb
```

Pour toute une arborescence du même système de fichiers, les implémentations prennent couramment en charge `+D`, mais les analyses récursives peuvent être coûteuses :

```bash
$ sudo lsof +D /mnt/usb
```

Les colonnes utiles comprennent `COMMAND`, `PID`, `USER`, le descripteur de fichier (`FD`), le type, le périphérique et `NAME`. Un enregistrement dont le champ `FD` vaut `cwd` indique que le processus emploie ce répertoire comme répertoire de travail actuel. La sortie sans privilèges peut être incomplète pour les processus appartenant à d’autres utilisateurs.

:::single-choice{#lsof-cwd-record} Qu’indique `cwd` dans la colonne `FD` ?

::option[Le processus emploie ce répertoire comme répertoire de travail actuel.]{#lsof-current-directory .correct explanation="Le répertoire actuel d’un processus peut maintenir un système de fichiers monté occupé."}
::option[Le fichier a été fermé pendant son écriture.]{#lsof-closed-write explanation="Ce marqueur décrit une relation avec un répertoire, et non un événement de fermeture."}
::option[Le processus possède le périphérique du système de fichiers.]{#lsof-device-owner explanation="La propriété du système de fichiers n’est pas représentée par l’étiquette de descripteur `cwd`."}
:::

## Identifier les utilisateurs avec fuser

`fuser` indique les identifiants des processus qui utilisent un fichier ou un système de fichiers donné. La sortie détaillée ajoute les utilisateurs, les types d’accès et les noms des commandes :

```bash
$ sudo fuser -v /mnt/usb
```

Pour traiter l’argument comme un système de fichiers monté et trouver les processus qui accèdent aux fichiers qu’il contient, employez l’option de montage prise en charge par `fuser` de procps :

```bash
$ sudo fuser -vm /mnt/usb
```

Vérifiez que le chemin est bien le point de montage voulu avec un outil tel que `findmnt --target /mnt/usb`. Les montages liés, les espaces de noms, les permissions et les conditions de concurrence peuvent influencer ce qu’une requête unique révèle.

:::single-choice{#fuser-verbose-purpose} Pourquoi employer `fuser -v` plutôt que `fuser` seul pendant une investigation ?

::option[La commande démonte automatiquement le système de fichiers sélectionné.]{#fuser-verbose-unmount explanation="Le mode détaillé affiche des informations et ne demande aucun démontage."}
::option[Elle ajoute des informations telles que l’utilisateur, le type d’accès et la commande.]{#fuser-verbose-details .correct explanation="Ces colonnes supplémentaires aident à évaluer les processus qui peuvent être coordonnés ou arrêtés sans risque."}
::option[Elle empêche définitivement les processus de rouvrir des fichiers.]{#fuser-verbose-prevent explanation="La production d’un rapport ne crée aucune règle de contrôle d’accès."}
:::

## Traiter un système de fichiers occupé

Suivez une séquence délibérée au lieu de tuer immédiatement chaque PID correspondant :

1. Confirmez l’hôte, le chemin, la source du montage et la maintenance prévue.
2. Identifiez les processus avec les deux outils lorsque c’est possible.
3. Déterminez si chaque processus peut être arrêté, quitter le répertoire ou terminer son travail.
4. Arrêtez-le par son gestionnaire de services ou l’interface de l’application lorsqu’ils existent.
5. Interrogez de nouveau, puis démontez et vérifiez le résultat.

`fuser -k` envoie un signal aux processus correspondants. Sur les implémentations procps courantes, le signal par défaut est `SIGKILL` et ne permet donc pas un arrêt ordonné. Si une terminaison explicitement approuvée est nécessaire, choisissez un signal adapté, vérifiez le PID et son propriétaire, et gardez à l’esprit que l’ensemble des processus peut changer entre l’examen et l’action.

:::single-choice{#fuser-k-risk} Pourquoi `fuser -k /mnt/usb` constitue-t-il une mauvaise première étape de dépannage ?

::option[La commande affiche uniquement l’espace libre du système de fichiers.]{#fuser-k-space explanation="Cette option cible des processus au lieu d’indiquer la capacité."}
::option[Elle peut tuer plusieurs processus correspondants sans nettoyage ordonné.]{#fuser-k-kills .correct explanation="Cette action large peut interrompre des écritures ou des services ; l’investigation et la coordination doivent donc la précéder."}
::option[Elle modifie le répertoire de travail de chaque processus correspondant.]{#fuser-k-chdir explanation="Elle envoie un signal et ne déplace pas les répertoires des processus."}
:::

## Choisir l’outil

Employez `lsof` lorsque vous avez besoin d’enregistrements détaillés sur les fichiers ouverts, les descripteurs ou les sockets. Employez `fuser` pour une vue centrée sur un chemin des PID et des types d’accès correspondants. Aucun résultat ne vous indique à lui seul si l’arrêt d’un processus est sûr.

Pour les sockets réseau, utilisez un espace de noms de protocole explicite avec `fuser` ou un outil centré sur les sockets tel que `ss` :

```bash
$ sudo fuser -v 22/tcp
$ sudo ss -lntp
```

:::single-choice{#lsof-fuser-tool-choice} Quel outil convient à une liste détaillée des descripteurs de fichiers ouverts et de leurs processus propriétaires ?

::option[`lsof`]{#lsof-detailed-records .correct explanation="Sa sortie s’organise autour des enregistrements de fichiers ouverts et des métadonnées de leurs processus."}
::option[`uptime`]{#lsof-uptime explanation="Uptime indique la durée de fonctionnement et les charges moyennes, et non les descripteurs ouverts."}
::option[`free`]{#lsof-free explanation="Free résume la mémoire plutôt que l’utilisation des fichiers."}
:::

## Résumé

Vous savez maintenant analyser l’utilisation des fichiers et des systèmes de fichiers sans considérer la terminaison comme la réponse par défaut.

1. Employer `lsof` pour les enregistrements détaillés des fichiers ouverts.
2. Employer `fuser` pour les PID et les types d’accès centrés sur un chemin.
3. Confirmer le montage et tenir compte des permissions et des conditions de concurrence.
4. Coordonner un arrêt ordonné avant d’envisager un signal.
5. Interroger de nouveau et vérifier le démontage ou le résultat sur le service.
