---
index: 1
lang: "fr"
title: "Présentation de System V"
meta_title: "Présentation de System V - Init"
meta_description: "Apprenez-en davantage sur System V init, ses niveaux d'exécution et la façon dont il gère les processus sous Linux. Comprenez les bases de SysV pour les utilisateurs débutants et intermédiaires."
meta_keywords: "System V, SysV init, niveaux d'exécution Linux, système init, tutoriel Linux, guide du débutant, gestion des processus"
---

## Lesson Content

Le but principal d'init est de démarrer et d'arrêter les processus essentiels sur le système. Il existe trois implémentations majeures d'init sous Linux : System V, Upstart et systemd. Dans cette leçon, nous allons examiner la version la plus traditionnelle d'init, System V init ou Sys V (prononcé « Système Cinq »).

Pour savoir si vous utilisez l'implémentation Sys V init, vérifiez la présence d'un fichier `/etc/inittab` ; s'il existe, vous utilisez très probablement Sys V.

Sys V démarre et arrête les processus séquentiellement. Par exemple, si vous vouliez démarrer un service nommé `foo-a`, `foo-b` ne peut pas fonctionner tant que `foo-a` n'est pas déjà en cours d'exécution. Sys V y parvient avec des scripts. Ces scripts démarrent et arrêtent les services pour nous. Nous pouvons écrire nos propres scripts, ou la plupart du temps, utiliser ceux qui sont déjà intégrés au système d'exploitation et qui sont utilisés pour charger les services essentiels.

Les avantages de l'utilisation de cette implémentation d'init sont qu'il est relativement facile de résoudre les dépendances, puisque vous savez que `foo-a` précède `foo-b`. Cependant, les performances ne sont pas excellentes car généralement une seule chose démarre ou s'arrête à la fois.

Lors de l'utilisation de Sys V, l'état de la machine est défini par des niveaux d'exécution (runlevels), qui sont définis de 0 à 6. Ces différents modes varient selon la distribution, mais la plupart du temps, ils ressembleront à ce qui suit :

- 0: Arrêt
- 1: Mode utilisateur unique
- 2: Mode multi-utilisateur sans réseau
- 3: Mode multi-utilisateur avec réseau
- 4: Inutilisé
- 5: Mode multi-utilisateur avec réseau et interface graphique
- 6: Redémarrage

Lorsque votre système démarre, il vérifie le niveau d'exécution dans lequel vous vous trouvez et exécute les scripts situés dans la configuration de ce niveau d'exécution. Les scripts sont situés dans **/etc/rc.d/rc[numéro de niveau d'exécution].d/** ou **/etc/init.d**. Les scripts qui commencent par S (start) ou K (kill) s'exécuteront respectivement au démarrage et à l'arrêt. Les nombres à côté de ces caractères indiquent la séquence dans laquelle ils s'exécutent.

Par exemple :

```bash
pete@icebox:/etc/rc.d/rc0.d$ ls
K10updates  K80openvpn
```

Nous voyons que lorsque nous passons au niveau d'exécution 0 ou au mode d'arrêt, notre machine essaiera d'exécuter un script pour arrêter les services de mise à jour, puis OpenVPN. Pour savoir à quel niveau d'exécution votre machine démarre, vous pouvez consulter le niveau d'exécution par défaut dans le fichier `/etc/inittab`. Vous pouvez également modifier votre niveau d'exécution par défaut dans ce fichier.

Une chose à noter : System V est lentement en train d'être remplacé, peut-être pas aujourd'hui, ni même dans des années. Cependant, vous pourriez voir des niveaux d'exécution apparaître dans d'autres implémentations d'init. Ceci est principalement destiné à prendre en charge les services qui ne sont démarrés ou arrêtés qu'à l'aide des scripts d'init de System V.

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension de la gestion des processus Linux et de la configuration du système, qui sont fondamentales pour le fonctionnement des systèmes init :

1. **[Gérer et surveiller les processus Linux](https://labex.io/fr/labs/comptia-manage-and-monitor-linux-processes-590864)** - Entraînez-vous à interagir avec les processus de premier plan et d'arrière-plan, à les inspecter avec `ps`, à surveiller les ressources avec `top` et à les terminer avec `kill`. Cela se rapporte directement à l'aspect « démarrer et arrêter les processus essentiels » d'init.
2. **[Planifier des tâches avec at et cron sous Linux](https://labex.io/fr/labs/comptia-schedule-tasks-with-at-and-cron-in-linux-590870)** - Apprenez à planifier des tâches uniques et récurrentes, ce qui s'appuie sur le concept d'exécution automatisée, similaire à la façon dont les scripts init gèrent les services.
3. **[Gérer les permissions de fichiers et de répertoires sous Linux](https://labex.io/fr/labs/comptia-manage-file-and-directory-permissions-in-linux-590844)** - Comprenez comment gérer les permissions de fichiers et de répertoires, une compétence essentielle pour travailler avec les fichiers de configuration système et les scripts comme ceux trouvés dans `/etc/init.d`.

Ces laboratoires vous aideront à appliquer les concepts dans des scénarios réels et à renforcer votre confiance dans les tâches fondamentales d'administration système Linux.

## Quiz Question

Quel niveau d'exécution est généralement utilisé pour l'arrêt ?

## Quiz Answer

0
