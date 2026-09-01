---
lesson_id: "sysv-overview"
course_id: "init"
lang: "fr"
order_index: 1
title: "Présentation de System V"
description: "Découvrez comment le système d'initialisation traditionnel System V emploie des niveaux d'exécution et des liens ordonnés vers les scripts de services."
meta_title: "Présentation de System V - Init"
meta_description: "Explorez le système d'initialisation traditionnel System V, son démarrage, sa gestion des processus et les niveaux d'exécution Linux."
meta_keywords: "System V, systemv, SysV init, init v, niveaux exécution Linux, système initialisation, gestion processus"
---

Le système d'initialisation System V, généralement appelé SysV init ou sysvinit, est une conception traditionnelle de PID 1 et de démarrage des services. Il reste important sur les anciens systèmes et par l'intermédiaire de scripts de compatibilité, mais la présence de fichiers de style SysV ne prouve pas que sysvinit est le PID 1 en cours d'exécution.

## Identifier le système d'initialisation actif

Examinez le PID 1 réel :

```bash
$ ps -p 1 -o pid,comm,args=
$ readlink /proc/1/exe
```

Un fichier `/etc/inittab` ou un répertoire `/etc/init.d/` ne constitue qu'un indice secondaire. systemd et d'autres systèmes d'initialisation peuvent conserver ces fichiers pour la compatibilité, et les conteneurs peuvent présenter un espace de noms de PID différent de celui de l'hôte.

:::single-choice{#sysv-overview-detection} Quelle preuve démontre le mieux que sysvinit est actif ?

::option[L'exécutable du PID 1 réel est sysvinit ou son programme init.]{#sysv-overview-live-pid-one .correct explanation="L'examen du premier processus en cours d'exécution est plus direct qu'une déduction fondée sur les fichiers de compatibilité."}
::option[Un répertoire `/etc/init.d/` existe.]{#sysv-overview-init-d-only explanation="Les autres systèmes d'initialisation conservent souvent les scripts ou enveloppes SysV."}
::option[La description d'un paquet contient le mot service.]{#sysv-overview-package-word explanation="Le texte d'un paquet n'identifie pas le processus qui joue actuellement le rôle de PID 1."}
:::

## Niveaux d'exécution

Un niveau d'exécution est un mode de fonctionnement numérique nommé. Les configurations SysV emploient traditionnellement les niveaux `0` à `6` ainsi que des niveaux spéciaux, mais leur signification relève des règles de la distribution, pas d'une loi universelle. Parmi les conventions courantes :

- `0` : transition vers l'arrêt ou la mise hors tension ;
- `1` ou `S` : mode mono-utilisateur ou de secours ;
- `2` à `5` : modes multi-utilisateurs définis par la distribution ;
- `6` : transition vers le redémarrage.

Les systèmes de la famille Debian traitent historiquement les niveaux 2 à 5 de façon semblable, tandis que les conventions de la famille Red Hat distinguent les modes texte et graphique. Examinez `/etc/inittab`, la documentation d'init et les répertoires de niveaux sur la machine réelle.

:::single-choice{#sysv-overview-shutdown-runlevel} Quel niveau demande conventionnellement l'arrêt ou la mise hors tension sur de nombreux systèmes SysV ?

::option[`3`]{#sysv-overview-runlevel-three explanation="Il s'agit couramment d'un mode multi-utilisateur et non d'un arrêt."}
::option[`0`]{#sysv-overview-runlevel-zero .correct explanation="Le niveau zéro est conventionnellement la transition d'arrêt, même si les règles locales d'init font autorité."}
::option[`6`]{#sysv-overview-runlevel-six explanation="Le niveau six demande conventionnellement un redémarrage."}
:::

## Scripts init et liens des niveaux d'exécution

Les scripts de services se trouvent généralement sous `/etc/init.d/`. Des répertoires comme `/etc/rc2.d/` ou `/etc/rc.d/rc2.d/` contiennent des liens dont le nom encode l'action de transition et l'ordre :

- les liens `SNNnom` demandent une action de démarrage ;
- les liens `KNNnom` demandent une action d'arrêt ;
- `NN` détermine l'ordre lexical des liens pour cette transition.

L'algorithme et les répertoires exacts varient. Les dépendances peuvent aussi apparaître dans les en-têtes des scripts et être traitées par les outils de la distribution ; certaines implémentations parallélisent le travail. SysV ne garantit donc pas que chaque service démarre strictement l'un après l'autre.

:::single-choice{#sysv-overview-start-link} Que demande conventionnellement un lien `S20networking` lors de l'entrée dans un niveau d'exécution ?

::option[Envoyer directement le signal 20 à chaque processus réseau.]{#sysv-overview-signal-twenty explanation="Les chiffres constituent des métadonnées d'ordre, pas un numéro de signal."}
::option[Stocker vingt sauvegardes de la configuration réseau.]{#sysv-overview-twenty-backups explanation="Les liens de niveaux ne gèrent pas la conservation des sauvegardes."}
::option[Exécuter le script de service lié avec son action de démarrage dans l'ordre `S`.]{#sysv-overview-start-action .correct explanation="Le préfixe distingue les liens de démarrage, tandis que le nombre contribue à leur ordre."}
:::

## Passer d'un niveau d'exécution à un autre

Lorsqu'init change de niveau, le mécanisme rc de la distribution arrête les services devenus inutiles et lance ceux qu'exige le nouveau mode. Les scripts doivent être suffisamment idempotents pour accepter des opérations répétées d'état ou de transition et renvoyer des états significatifs.

Demander le niveau 0 ou 6 constitue une action destructrice de disponibilité à l'échelle du système. Employez l'interface d'arrêt du système, prévenez les utilisateurs, préservez le travail actif et vérifiez l'accès à une console distante au lieu de déclencher négligemment une transition init brute.

:::single-choice{#sysv-overview-runlevel-six-meaning} Que demande conventionnellement le niveau `6` ?

::option[La création de six comptes utilisateur supplémentaires.]{#sysv-overview-six-users explanation="Les niveaux d'exécution décrivent des modes de fonctionnement, pas un nombre de comptes."}
::option[Une transition de redémarrage du système.]{#sysv-overview-reboot .correct explanation="La politique SysV classique réserve le niveau six à l'arrêt des services et au redémarrage du système."}
::option[Le montage définitif en lecture seule de tous les systèmes de fichiers.]{#sysv-overview-six-readonly explanation="Ce n'est pas la fonction conventionnelle du niveau six."}
:::

## Limites de la compatibilité

Sur un hôte systemd, les scripts SysV peuvent être enveloppés dans des unités générées, mais les dépendances, délais, journaux et états de systemd continuent de s'appliquer. Exécuter directement un ancien script peut contourner le suivi du gestionnaire de services. Identifiez le gestionnaire actif et employez si possible son interface native.

:::single-choice{#sysv-overview-compatibility-script} Pourquoi faut-il normalement appeler un script de style SysV au moyen du gestionnaire de services sur un hôte systemd ?

::option[Son exécution directe peut contourner le suivi des dépendances et de l'état.]{#sysv-overview-manager-tracking .correct explanation="Le gestionnaire doit coordonner la propriété des processus, l'ordre, les délais et l'état."}
::option[Les scripts shell ne peuvent pas s'exécuter sur un système systemd.]{#sysv-overview-scripts-impossible explanation="Ils peuvent s'exécuter, mais contourner la supervision peut créer un état incohérent."}
::option[Systemd convertit chaque script de service en module du noyau.]{#sysv-overview-script-module explanation="Les unités de compatibilité restent un mécanisme de gestion des services dans l'espace utilisateur."}
:::

## Résumé

Vous savez maintenant interpréter une organisation SysV traditionnelle sans supposer qu'elle est active.

1. Identifier le PID 1 réel avant de choisir les commandes d'initialisation.
2. Considérer la signification des niveaux comme des conventions définies par la distribution.
3. Lire `S`, `K` et l'ordre numérique dans les liens de niveaux.
4. Employer des procédures contrôlées pour arrêter avec les niveaux 0 et 6.
5. Respecter le gestionnaire actif en présence de scripts de compatibilité.
