---
lesson_id: "cron-jobs"
course_id: "process-utilization"
lang: "fr"
order_index: 8
title: "Tâches cron"
description: "Découvrez comment créer, examiner, tester et exploiter en toute sécurité des tâches récurrentes avec cron."
meta_title: "Tâches cron - Utilisation des processus"
meta_description: "Apprenez à planifier des tâches et automatiser des scripts sous Linux avec cron, la syntaxe de crontab et des commandes telles que crontab -e."
meta_keywords: "tâches cron, crontab, planifier tâches, automatisation Linux, commandes Linux, Linux débutant, tutoriel Linux, crontab -e, cron"
---

Cron exécute des commandes selon un calendrier récurrent sans shell interactif. L’automatisation répète aussi bien les comportements corrects que les erreurs ; testez donc la commande, employez des chemins explicites, limitez les privilèges et planifiez la journalisation et la notification des échecs avant de la programmer.

## Lire une entrée de crontab

Une entrée de crontab utilisateur contient cinq champs temporels suivis d’une commande :

```cron
30 8 * * * /home/pete/scripts/change_wallpaper
```

De gauche à droite, les champs sont la minute, l’heure, le jour du mois, le mois et le jour de la semaine. Cet exemple s’exécute à 08 h 30 selon le fuseau horaire applicable au démon cron. Un astérisque signifie chaque valeur permise dans ce champ.

Lorsque les champs du jour du mois et du jour de la semaine sont tous deux restreints, de nombreuses implémentations de cron exécutent la commande si l’un ou l’autre correspond. Confirmez la sémantique locale avant de bâtir un calendrier qui utilise les deux.

:::single-choice{#cron-daily-eight-thirty} Quand `30 8 * * * command` s’exécute-t-il ?

::option[Toutes les 30 minutes pendant huit heures.]{#cron-every-thirty explanation="Les champs occupent des positions dans un calendrier et n’expriment pas une durée."}
::option[Chaque jour à 08 h 30.]{#cron-eight-thirty .correct explanation="La minute 30 et l’heure 8 sont fixes, tandis que les trois champs de date autorisent toutes les valeurs."}
::option[À 30 h 08 le huitième jour de chaque mois.]{#cron-invalid-time explanation="Les heures vont de 0 à 23, et l’exemple ne limite pas le jour du mois."}
:::

## Gérer une crontab utilisateur

Modifiez la crontab de l’utilisateur actuel avec :

```bash
$ crontab -e
```

Répertoriez les entrées installées avant et après une modification :

```bash
$ crontab -l
```

`crontab -r` supprime toute la crontab de l’utilisateur et peut le faire sans ouvrir d’éditeur. Ne l’employez pas pour retirer une seule ligne ; modifiez la crontab et vérifiez les entrées restantes.

:::single-choice{#cron-list-current-user} Quelle commande répertorie les entrées cron installées de l’utilisateur actuel ?

::option[`crontab -l`]{#cron-list .correct explanation="L’option de liste affiche les entrées installées afin de les examiner."}
::option[`crontab -r`]{#cron-remove-all explanation="Cette option supprime la crontab au lieu de l’afficher."}
::option[`crontab -e`]{#cron-edit explanation="Cette option ouvre la crontab dans un éditeur plutôt que de simplement la répertorier."}
:::

## Tenir compte de l’environnement de cron

Cron fournit généralement un environnement limité et un shell non interactif. Employez des chemins absolus pour les commandes et les fichiers, définissez explicitement les variables requises et ne dépendez pas d’alias, du répertoire actuel d’un terminal ou des fichiers de démarrage du shell.

Redirigez la sortie standard et les erreurs vers un journal contrôlé ou employez un mécanisme de notification adapté au système. Protégez les identifiants secrets par des permissions restrictives et évitez de les intégrer directement dans une commande de crontab.

:::single-choice{#cron-absolute-paths} Pourquoi une commande cron doit-elle employer des chemins et des paramètres d’environnement explicites ?

::option[Cron s’exécute toujours dans le terminal actuel de l’utilisateur.]{#cron-current-terminal explanation="Les tâches planifiées s’exécutent indépendamment d’une session interactive."}
::option[Les chemins absolus font exécuter chaque commande en tant que root.]{#cron-path-root explanation="Les chemins sélectionnent des fichiers, mais n’accordent aucun privilège."}
::option[L’environnement de cron peut différer de celui du shell interactif.]{#cron-limited-environment .correct explanation="Des dépendances explicites évitent les échecs dus à des hypothèses sur PATH, le répertoire ou les fichiers de démarrage."}
:::

## Tester et empêcher les chevauchements

Exécutez le script manuellement en tant que même utilisateur avec un environnement tout aussi minimal. Faites-lui renvoyer des états de sortie utiles et écrire des résultats horodatés. Après l’installation, attendez un calendrier de test inoffensif ou une exécution contrôlée, puis vérifiez l’effet réel et les journaux.

Si une exécution peut durer plus longtemps que son intervalle, concevez-la pour la concurrence ou employez un mécanisme de verrouillage tel que `flock` lorsqu’il est disponible :

```cron
*/5 * * * * /usr/bin/flock -n /run/user/1000/report.lock /home/pete/bin/report
```

Choisissez un chemin de verrou que l’utilisateur de la tâche peut créer sans risque et déterminez si les exécutions ignorées sont acceptables. Cron ne garantit pas automatiquement l’exécution d’une seule instance.

:::single-choice{#cron-overlapping-runs} Quel risque existe lorsqu’une tâche dure plus longtemps que son intervalle de planification ?

::option[Plusieurs instances peuvent se chevaucher et se disputer les ressources.]{#cron-overlap .correct explanation="Cron peut lancer une nouvelle occurrence pendant que le processus précédent s’exécute encore."}
::option[Les cinq champs du calendrier acquièrent automatiquement un sixième champ de verrouillage.]{#cron-auto-lock explanation="La syntaxe de crontab n’ajoute pas d’exclusion mutuelle automatique."}
::option[Le script est définitivement converti en thread du noyau.]{#cron-kernel-thread explanation="La planification d’une commande ne modifie pas ainsi son modèle de processus."}
:::

## Choisir le bon planificateur

Cron convient aux commandes récurrentes simples. Sur les hôtes systemd, les minuteurs systemd peuvent fournir l’intégration des dépendances, le rattrapage persistant, un délai aléatoire et la journalisation. Les planificateurs d’application ou de grappe peuvent être plus sûrs lorsqu’une tâche ne doit s’exécuter qu’une seule fois sur plusieurs machines.

:::single-choice{#cron-cluster-exactly-once} Pourquoi cron ordinaire sur chaque hôte peut-il ne pas convenir à une tâche de grappe qui doit s’exécuter exactement une fois ?

::option[Chaque entrée cron est limitée à un caractère.]{#cron-one-character explanation="Les commandes d’une crontab peuvent contenir des lignes de commande ordinaires."}
::option[Chaque hôte peut lancer indépendamment sa propre copie.]{#cron-each-host .correct explanation="Un mécanisme de coordination distribué est nécessaire pour imposer une seule exécution sur tous les hôtes."}
::option[Cron ne peut pas exécuter de scripts enregistrés sur disque.]{#cron-no-scripts explanation="L’exécution de scripts est un usage courant de cron."}
:::

## Résumé

Vous savez maintenant exploiter une tâche cron récurrente avec des hypothèses explicites sur son calendrier et son exécution.

1. Lire les cinq champs temporels dans l’ordre défini.
2. Examiner et modifier les crontabs utilisateur sans supprimer les tâches sans rapport.
3. Définir les chemins, l’environnement, la journalisation et la gestion des identifiants secrets.
4. Tester en tant qu’utilisateur de la tâche et empêcher les chevauchements indésirables.
5. Choisir un planificateur adapté aux exigences de l’hôte et de coordination.
