---
lang: "fr"
title: "Présentation de System V"
description: "Découvrez System V init, ses niveaux d'exécution et comment il gère les processus sous Linux. Comprenez les bases de SysV pour les débutants et les utilisateurs intermédiaires."
keywords: "System V, SysV init, niveaux d'exécution Linux, système init, tutoriel Linux, guide du débutant, gestion des processus"
---

## Lesson Content

Le but principal d'init est de démarrer et d'arrêter les processus essentiels sur le système. Il existe trois implémentations majeures d'init sous Linux : System V, Upstart et systemd. Dans cette leçon, nous allons examiner la version la plus traditionnelle d'init, System V init ou Sys V (prononcé « Système Cinq »).

Pour savoir si vous utilisez l'implémentation Sys V init, vérifiez la présence d'un fichier `/etc/inittab` ; s'il existe, vous exécutez très probablement Sys V.

Sys V démarre et arrête les processus séquentiellement. Par exemple, si vous vouliez démarrer un service nommé `foo-a`, `foo-b` ne peut pas fonctionner tant que `foo-a` n'est pas déjà en cours d'exécution. Sys V y parvient avec des scripts. Ces scripts démarrent et arrêtent les services pour nous. Nous pouvons écrire nos propres scripts, ou la plupart du temps, utiliser ceux qui sont déjà intégrés au système d'exploitation et sont utilisés pour charger les services essentiels.

Les avantages de l'utilisation de cette implémentation d'init sont qu'il est relativement facile de résoudre les dépendances, puisque vous savez que `foo-a` précède `foo-b`. Cependant, les performances ne sont pas excellentes car généralement une seule chose démarre ou s'arrête à la fois.

Lorsque vous utilisez Sys V, l'état de la machine est défini par des niveaux d'exécution (runlevels), qui sont définis de 0 à 6. Ces différents modes varieront en fonction de la distribution, mais la plupart du temps, ils ressembleront à ce qui suit :

- 0: Arrêt
- 1: Mode utilisateur unique
- 2: Mode multi-utilisateur sans réseau
- 3: Mode multi-utilisateur avec réseau
- 4: Inutilisé
- 5: Mode multi-utilisateur avec réseau et interface graphique
- 6: Redémarrage

Lorsque votre système démarre, il vérifie le niveau d'exécution dans lequel vous vous trouvez et exécute les scripts situés dans la configuration de ce niveau d'exécution. Les scripts sont situés dans **/etc/rc.d/rc[numéro_de_niveau_d'exécution].d/** ou **/etc/init.d**. Les scripts qui commencent par S (start) ou K (kill) s'exécuteront respectivement au démarrage et à l'arrêt. Les nombres à côté de ces caractères indiquent la séquence dans laquelle ils s'exécutent.

Par exemple :

```bash
pete@icebox:/etc/rc.d/rc0.d$ ls
K10updates  K80openvpn
```

Nous voyons que lorsque nous passons au niveau d'exécution 0 ou au mode d'arrêt, notre machine essaiera d'exécuter un script pour arrêter les services de mise à jour, puis OpenVPN. Pour savoir à quel niveau d'exécution votre machine démarre, vous pouvez consulter le niveau d'exécution par défaut dans le fichier `/etc/inittab`. Vous pouvez également modifier votre niveau d'exécution par défaut dans ce fichier.

Une chose à noter : System V est lentement en train d'être remplacé, peut-être pas aujourd'hui, ni même dans des années. Cependant, vous pourriez voir des niveaux d'exécution apparaître dans d'autres implémentations d'init. C'est principalement pour prendre en charge les services qui ne sont démarrés ou arrêtés qu'à l'aide des scripts d'init de System V.

## Exercise

Si vous utilisez System V, changez le niveau d'exécution par défaut de votre machine pour autre chose et voyez ce qui se passe.

## Quiz Question

Quel niveau d'exécution est généralement utilisé pour l'arrêt ?

## Quiz Answer

0
