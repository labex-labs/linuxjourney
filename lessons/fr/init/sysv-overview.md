---
index: 1
lang: "fr"
title: "Aperçu de System V"
meta_title: "Aperçu de System V - Init"
meta_description: "Explorez le système d'initialisation System V traditionnel, également connu sous le nom de SysV ou init v. Ce guide couvre la manière dont systemv gère les processus, son démarrage séquentiel et le rôle des niveaux d'exécution (runlevels) sous Linux. Apprenez les bases du processus classique initv."
meta_keywords: "System V, systemv, SysV init, systemv init, init v, initv, niveaux d'exécution Linux, système d'initialisation, gestion des processus, tutoriel Linux"
---

## Lesson Content

Le rôle principal d'un système d'initialisation (init) est de démarrer et d'arrêter les processus essentiels. Linux a connu trois implémentations majeures d'init : System V, Upstart et systemd. Cette leçon se concentre sur la version la plus traditionnelle, **System V init**, souvent appelée **SysV** ou simplement **systemv** (prononcé 'System Five').

Pour déterminer si votre système utilise l'implémentation **systemv**, vérifiez l'existence d'un fichier `/etc/inittab`. Si ce fichier est présent, vous utilisez très probablement une distribution basée sur SysV.

### Comment System V Gère les Processus

Le processus **systemv init** démarre et arrête les services séquentiellement. Par exemple, si un service nommé `foo-b` dépend de `foo-a`, `foo-b` ne peut pas démarrer tant que `foo-a` n'est pas entièrement opérationnel. Le système **initv** y parvient à l'aide de scripts shell. Ces scripts, situés dans des répertoires spécifiques, gèrent le démarrage et l'arrêt des services. Bien que vous puissiez écrire des scripts personnalisés, la plupart des systèmes s'appuient sur ceux pré-empaquetés qui gèrent les services essentiels du système d'exploitation.

### Avantages et Inconvénients

L'avantage principal de cette approche séquentielle est sa simplicité et sa prévisibilité. Le dépannage des dépendances est simple car vous savez que `foo-a` démarre toujours avant `foo-b`. Cependant, le principal inconvénient du modèle **init v** est la performance, car les services sont généralement démarrés un par un, ce qui entraîne des temps de démarrage plus lents par rapport aux systèmes parallèles modernes.

### Comprendre les Niveaux d'Exécution (Runlevels) dans System V

Dans un environnement **systemv**, l'état de la machine est défini par des **niveaux d'exécution** (runlevels), numérotés de 0 à 6. Ces modes peuvent varier légèrement entre les distributions Linux, mais ils suivent généralement cette convention standard :

- 0 : Arrêt (Shutdown)
- 1 : Mode Utilisateur Unique (Single User Mode)
- 2 : Mode multi-utilisateur sans mise en réseau
- 3 : Mode multi-utilisateur avec mise en réseau
- 4 : Inutilisé
- 5 : Mode multi-utilisateur avec mise en réseau et interface graphique (GUI)
- 6 : Redémarrage (Reboot)

### Scripts et Répertoires Init

Lorsque votre système démarre, il vérifie son niveau d'exécution configuré et exécute les scripts correspondants. Ces scripts se trouvent généralement dans des répertoires comme **/etc/rc.d/rc[runlevel].d/** ou dans un répertoire central **/etc/init.d**. Les scripts commençant par `S` (Start/Démarrer) sont exécutés au démarrage, tandis que ceux commençant par `K` (Kill/Tuer) sont exécutés lors de l'arrêt.

Les chiffres suivant `S` ou `K` dictent l'ordre d'exécution.

Par exemple :

```bash
pete@icebox:/etc/rc.d/rc0.d$ ls
K10updates  K80openvpn
```

Dans cet exemple, passer au niveau d'exécution 0 (arrêt) exécutera d'abord le script pour tuer le service de mises à jour, suivi du script pour OpenVPN. Vous pouvez trouver le niveau d'exécution par défaut de votre machine dans le fichier `/etc/inittab`, où vous pouvez également le modifier.

Il est important de noter que **System V** a été largement remplacé par `systemd` dans la plupart des distributions Linux modernes. Cependant, vous pourriez toujours rencontrer le concept de niveaux d'exécution dans les systèmes d'initialisation plus récents, car ils fournissent souvent une couche de compatibilité pour prendre en charge les services hérités qui dépendent des scripts **systemv init**.

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension de la gestion des processus Linux et de la configuration du système, qui sont fondamentaux pour le fonctionnement des systèmes d'initialisation :

1. **[Gérer et Surveiller les Processus Linux](https://labex.io/fr/labs/comptia-manage-and-monitor-linux-processes-590864)** - Entraînez-vous à interagir avec les processus au premier plan et à l'arrière-plan, à les inspecter avec `ps`, à surveiller les ressources avec `top` et à les terminer avec `kill`. Ceci est directement lié à l'aspect 'démarrer et arrêter les processus essentiels' de l'init.
2. **[Planifier des Tâches avec at et cron sous Linux](https://labex.io/fr/labs/comptia-schedule-tasks-with-at-and-cron-in-linux-590870)** - Apprenez à planifier des tâches uniques et récurrentes, ce qui s'appuie sur le concept d'exécution automatisée similaire à la manière dont les scripts init gèrent les services.
3. **[Gérer les Permissions des Fichiers et des Répertoires sous Linux](https://labex.io/fr/labs/comptia-manage-file-and-directory-permissions-in-linux-590844)** - Comprenez comment gérer les permissions des fichiers et des répertoires, une compétence essentielle pour travailler avec les fichiers de configuration système et les scripts comme ceux trouvés dans `/etc/init.d`.

Ces laboratoires vous aideront à appliquer les concepts dans des scénarios réels et à gagner en confiance avec les tâches fondamentales d'administration système Linux.

## Quiz Question

Quel niveau d'exécution est généralement utilisé pour l'arrêt (shutdown) ?

## Quiz Answer

0
