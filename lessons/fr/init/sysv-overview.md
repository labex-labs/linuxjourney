---
index: 1
lang: "fr"
title: "Aperçu de System V"
meta_title: "Aperçu de System V - Init"
meta_description: "Apprenez sur l'init System V, ses niveaux d'exécution (runlevels) et comment il gère les processus sous Linux. Comprenez les bases de SysV pour les utilisateurs débutants et intermédiaires."
meta_keywords: "System V, SysV init, niveaux d'exécution Linux, système init, tutoriel Linux, guide du débutant, gestion des processus"
---

## Lesson Content

L'objectif principal d'init est de démarrer et d'arrêter les processus essentiels sur le système. Il existe trois implémentations majeures d'init sous Linux : System V, Upstart et systemd. Dans cette leçon, nous allons passer en revue la version la plus traditionnelle d'init, System V init ou Sys V (prononcé 'System Five').

Pour savoir si vous utilisez l'implémentation Sys V init, recherchez un fichier `/etc/inittab` ; s'il existe, vous exécutez très probablement Sys V.

Sys V démarre et arrête les processus séquentiellement. Par exemple, si vous vouliez démarrer un service nommé `foo-a`, `foo-b` ne pourrait pas fonctionner tant que `foo-a` n'est pas déjà en cours d'exécution. Sys V réalise cela avec des scripts. Ces scripts démarrent et arrêtent les services pour nous. Nous pouvons écrire nos propres scripts, ou la plupart du temps, utiliser ceux qui sont déjà intégrés au système d'exploitation et qui sont utilisés pour charger les services essentiels.

L'avantage d'utiliser cette implémentation d'init est qu'il est relativement facile de résoudre les dépendances, car vous savez que `foo-a` vient avant `foo-b`. Cependant, les performances ne sont pas excellentes car généralement une seule chose démarre ou s'arrête à la fois.

Lors de l'utilisation de Sys V, l'état de la machine est défini par des niveaux d'exécution (runlevels), qui sont définis de 0 à 6. Ces différents modes varieront en fonction de la distribution, mais ressembleront le plus souvent à ce qui suit :

- 0: Arrêt (Shutdown)
- 1: Mode Utilisateur Unique (Single User Mode)
- 2: Mode Multi-utilisateur sans mise en réseau (Multiuser mode without networking)
- 3: Mode Multi-utilisateur avec mise en réseau (Multiuser mode with networking)
- 4: Inutilisé (Unused)
- 5: Mode Multi-utilisateur avec mise en réseau et interface graphique (Multiuser mode with networking and GUI)
- 6: Redémarrage (Reboot)

Lorsque votre système démarre, il vérifie dans quel niveau d'exécution il se trouve et exécute les scripts situés dans la configuration de ce niveau d'exécution. Les scripts sont situés dans **/etc/rc.d/rc[runlevel number].d/** ou **/etc/init.d**. Les scripts commençant par S (start) ou K (kill) s'exécuteront respectivement au démarrage et à l'arrêt. Les nombres suivant ces caractères indiquent la séquence dans laquelle ils s'exécutent.

Par exemple :

```bash
pete@icebox:/etc/rc.d/rc0.d$ ls
K10updates  K80openvpn
```

Nous voyons que lorsque nous passons au niveau d'exécution 0 ou au mode d'arrêt, notre machine tentera d'exécuter un script pour arrêter les services de mise à jour, puis OpenVPN. Pour savoir dans quel niveau d'exécution votre machine démarre, vous pouvez consulter le niveau d'exécution par défaut dans le fichier `/etc/inittab`. Vous pouvez également modifier votre niveau d'exécution par défaut dans ce fichier.

Une chose à noter : System V a été largement remplacé par systemd dans la plupart des distributions Linux modernes. Cependant, vous pouvez voir des niveaux d'exécution apparaître dans d'autres implémentations d'init. Ceci est principalement destiné à prendre en charge les services qui ne sont démarrés ou arrêtés qu'à l'aide des scripts init System V.

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension de la gestion des processus Linux et de la configuration du système, qui sont fondamentales pour le fonctionnement des systèmes init :

1. **[Gérer et surveiller les processus Linux](https://labex.io/fr/labs/comptia-manage-and-monitor-linux-processes-590864)** - Entraînez-vous à interagir avec les processus au premier plan et à l'arrière-plan, à les inspecter avec `ps`, à surveiller les ressources avec `top` et à les terminer avec `kill`. Ceci est directement lié à l'aspect 'démarrer et arrêter les processus essentiels' de l'init.
2. **[Planifier des tâches avec at et cron sous Linux](https://labex.io/fr/labs/comptia-schedule-tasks-with-at-and-cron-in-linux-590870)** - Apprenez à planifier des tâches uniques et récurrentes, ce qui s'appuie sur le concept d'exécution automatisée similaire à la façon dont les scripts init gèrent les services.
3. **[Gérer les permissions de fichiers et de répertoires sous Linux](https://labex.io/fr/labs/comptia-manage-file-and-directory-permissions-in-linux-590844)** - Comprenez comment gérer les permissions de fichiers et de répertoires, une compétence essentielle pour travailler avec les fichiers de configuration système et les scripts tels que ceux trouvés dans `/etc/init.d`.

Ces laboratoires vous aideront à appliquer les concepts dans des scénarios réels et à renforcer votre confiance dans les tâches fondamentales d'administration système Linux.

## Quiz Question

Quel niveau d'exécution est généralement utilisé pour l'arrêt (shutdown) ?

## Quiz Answer

0
