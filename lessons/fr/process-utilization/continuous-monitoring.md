---
lesson_id: "continuous-monitoring"
course_id: "process-utilization"
lang: "fr"
order_index: 7
title: "Surveillance continue"
description: "Découvrez comment la collecte de sysstat et les rapports de sar permettent l’analyse historique des performances Linux."
meta_title: "Surveillance continue - Utilisation des processus"
meta_description: "Découvrez la surveillance continue d’un système Linux avec sar : installation, collecte des données et analyse historique de l’utilisation des ressources."
meta_keywords: "sar, sysstat, surveillance Linux, performances système, surveillance continue, débutant, tutoriel, guide"
---

Les outils interactifs montrent ce qui se passe pendant que vous les observez. Une surveillance historique est nécessaire lorsqu’un ralentissement est déjà terminé. La suite `sysstat` recueille périodiquement les compteurs du système, et `sar` lit soit les compteurs actuels, soit des fichiers d’activité enregistrés.

## Activer la collecte des données

Installez le paquet `sysstat` de la distribution, puis confirmez que son collecteur et son mécanisme de conservation sont activés. Les services, minuteurs et chemins de configuration exacts varient selon la distribution ; l’installation du paquet ne garantit pas le démarrage de la collecte.

Sur un hôte systemd, examinez les unités fournies par le paquet au lieu d’en deviner le nom :

```bash
$ systemctl list-unit-files | grep sysstat
$ systemctl list-timers --all | grep sysstat
```

Vérifiez que de nouveaux fichiers d’activité sont créés dans le répertoire de données sysstat de la distribution et examinez leurs permissions et leur politique de conservation.

:::single-choice{#sar-installation-verification}
Que faut-il vérifier après l’installation de `sysstat` ?

::option[Que la collecte est activée et que les fichiers d’activité sont actualisés.]{#sar-collector-updating .correct explanation="L’installation du paquet et la collecte périodique active sont deux conditions distinctes."}
::option[Que chaque processus a été redémarré manuellement.]{#sar-restart-processes explanation="L’installation d’un collecteur de surveillance n’exige pas le redémarrage de chaque charge."}
::option[Que tous les fichiers historiques sont accessibles en écriture à tous.]{#sar-world-writable explanation="Les données de surveillance doivent conserver des contrôles d’accès appropriés."}
:::

## Lire les échantillons actuels

Demandez à `sar` de recueillir trois rapports du processeur à une seconde d’intervalle :

```bash
$ sar -u 1 3
```

Parmi les autres rapports courants figurent la file d’exécution et la charge (`-q`), la mémoire (`-r`), la pagination (`-B`), les périphériques bloc (`-d`) et l’activité par processeur (`-P ALL`). Les options et les champs varient avec la version de sysstat ; consultez `sar --help` ou le manuel local.

:::single-choice{#sar-one-second-count}
Que demande `sar -u 1 3` ?

::option[Trois rapports du processeur à une seconde d’intervalle.]{#sar-three-cpu-samples .correct explanation="Le premier nombre représente l’intervalle en secondes et le second le nombre de rapports."}
::option[Un rapport couvrant exactement trois jours.]{#sar-three-days explanation="Les opérandes indiquent l’intervalle et le nombre d’échantillons, et non une plage de dates."}
::option[La suppression de trois fichiers du processeur enregistrés.]{#sar-delete-files explanation="La commande lit les compteurs et ne demande aucune suppression."}
:::

## Lire les fichiers historiques

Les emplacements et les noms des fichiers enregistrés varient, souvent sous `/var/log/sysstat` ou `/var/log/sa`. Transmettez un fichier d’activité choisi avec `-f` :

```bash
$ sar -q -f /var/log/sysstat/sa02
```

Confirmez la date complète du fichier dans les en-têtes du rapport ; un suffixe à deux chiffres désigne généralement un jour du mois et peut être ambigu entre plusieurs périodes de conservation. Les formats binaires enregistrés peuvent également nécessiter une version compatible de sysstat.

:::single-choice{#sar-historical-file-option}
Quelle option demande à `sar` de lire un fichier d’activité précis ?

::option[`-P`]{#sar-option-p explanation="Cette option sélectionne le rapport par processeur plutôt qu’un fichier d’entrée."}
::option[`-q`]{#sar-option-q explanation="Cette option sélectionne le rapport de file et de charge."}
::option[`-f`]{#sar-option-f .correct explanation="L’option de fichier sélectionne les données d’activité enregistrées à lire."}
:::

## Mettre les indices d’un incident en relation

Établissez l’heure et le fuseau horaire de l’incident, puis comparez plusieurs signaux sur le même intervalle. Recherchez les changements de charge, de processeur, de file d’exécution, de pagination, d’activité des périphériques, de trafic réseau et de latence applicative. Les variations des compteurs montrent une corrélation, pas nécessairement une causalité ; les enregistrements de déploiements et les journaux des applications peuvent expliquer le déclencheur.

Les lacunes peuvent signifier que l’hôte était arrêté, que le collecteur a échoué ou que la politique de conservation a supprimé les données. Surveillez la chaîne de surveillance elle-même afin que les indices manquants soient visibles avant un incident.

:::single-choice{#sar-incident-method}
Comment employer les données historiques de `sar` pendant l’examen d’un incident ?

::option[Considérer le compteur isolé le plus élevé comme la cause profonde prouvée.]{#sar-single-root explanation="Une corrélation unique n’établit pas une causalité."}
::option[Comparer plusieurs mesures sur la même fenêtre temporelle vérifiée.]{#sar-correlate-window .correct explanation="Des signaux alignés aident à distinguer les hypothèses et à relier le comportement du système à l’incident."}
::option[Ignorer les lacunes, car la collecte est garantie après l’installation.]{#sar-ignore-gaps explanation="La collecte peut échouer ou être désactivée ; les lacunes doivent donc être expliquées."}
:::

## Résumé

Vous savez maintenant employer `sar` pour analyser les performances en dehors d’une session interactive.

1. Vérifier que la collecte et la conservation sont réellement actives.
2. Demander des échantillons actuels bornés par un intervalle et un nombre.
3. Sélectionner explicitement les fichiers d’activité historiques.
4. Aligner plusieurs mesures avec l’heure de l’incident et les indices de la charge.
