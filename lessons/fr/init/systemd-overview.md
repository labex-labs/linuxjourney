---
index: 5
lang: "fr"
title: "Aperçu de Systemd"
meta_title: "Aperçu de Systemd - Init"
meta_description: "Apprenez les bases de Systemd : comprenez les unités, les cibles et le processus de démarrage. Découvrez comment Systemd gère les services et les états du système sous Linux. Commencez votre parcours !"
meta_keywords: "Systemd, unités Systemd, cibles Systemd, processus de démarrage Linux, services Linux, débutant, tutoriel, guide"
---

## Lesson Content

Systemd est le système d'initialisation standard dans la plupart des distributions Linux modernes. Si vous possédez un répertoire `/usr/lib/systemd`, vous utilisez très probablement systemd.

Systemd utilise des objectifs (goals) pour que votre système démarre et fonctionne. Fondamentalement, vous avez une cible à atteindre, et cette cible a également des dépendances qui doivent être satisfaites. Systemd est extrêmement flexible et robuste ; il ne suit pas une séquence stricte pour démarrer les processus. Voici ce qui se passe lors d'un démarrage systemd typique :

1. D'abord, systemd charge ses fichiers de configuration, généralement situés dans `/etc/systemd/system` ou `/usr/lib/systemd/system`.
2. Ensuite, il détermine son objectif de démarrage, qui est généralement `default.target`.
3. Systemd détermine les dépendances de l'objectif de démarrage et les active.

Similaire aux niveaux d'exécution SysV, systemd démarre dans différentes cibles (targets) :

- `poweroff.target` - arrêt du système
- `rescue.target` - mode utilisateur unique
- `multi-user.target` - multi-utilisateur avec mise en réseau
- `graphical.target` - multi-utilisateur avec mise en réseau et interface graphique
- `reboot.target` - redémarrage

L'objectif de démarrage par défaut, `default.target`, pointe généralement vers `graphical.target`.

Les principaux objets avec lesquels systemd travaille sont connus sous le nom d'unités. Systemd ne fait pas que démarrer et arrêter des services ; il peut monter des systèmes de fichiers, surveiller vos sockets réseau, etc. En raison de cette robustesse, il dispose de différents types d'unités avec lesquelles il opère. Les unités les plus courantes sont :

- Unités de service (`Service units`) - ce sont les services que nous avons démarrés et arrêtés ; ces fichiers d'unité se terminent par `.service`.
- Unités de montage (`Mount units`) - Celles-ci montent des systèmes de fichiers ; ces fichiers d'unité se terminent par `.mount`.
- Unités de cible (`Target units`) - Celles-ci regroupent d'autres unités ; les fichiers se terminent par `.target`.

Par exemple, supposons que nous démarrions dans notre `default.target`. Cette cible regroupe l'unité `networking.service`, l'unité `crond.service`, etc., donc une fois que nous activons une seule unité, tout ce qui se trouve en dessous de cette unité est activé également.

## Exercise

Bien qu'il n'y ait pas de laboratoires spécifiques pour ce sujet, nous vous recommandons d'explorer le [Parcours d'apprentissage Linux complet](https://labex.io/fr/learn/linux) pour pratiquer les compétences et concepts Linux associés.

## Quiz Question

Quelle unité est utilisée pour regrouper d'autres unités ?

## Quiz Answer

target
