---
lang: "fr"
title: "Présentation de Systemd"
meta_title: "Présentation de Systemd - Init"
meta_description: "Apprenez les bases de Systemd : comprenez les unités, les cibles et le processus de démarrage. Découvrez comment Systemd gère les services et les états du système sous Linux. Commencez votre parcours !"
meta_keywords: "Systemd, unités Systemd, cibles Systemd, processus de démarrage Linux, services Linux, débutant, tutoriel, guide"
---

## Lesson Content

Systemd est lentement en train de devenir le standard émergent pour init. Si vous avez un répertoire `/usr/lib/systemd`, vous utilisez très probablement systemd.

Systemd utilise des objectifs pour démarrer votre système. En gros, vous avez une cible que vous voulez atteindre, et cette cible a également des dépendances qui doivent être satisfaites. Systemd est extrêmement flexible et robuste ; il ne suit pas une séquence stricte pour démarrer les processus. Voici ce qui se passe lors d'un démarrage systemd typique :

1. Tout d'abord, systemd charge ses fichiers de configuration, généralement situés dans `/etc/systemd/system` ou `/usr/lib/systemd/system`.
2. Ensuite, il détermine son objectif de démarrage, qui est généralement `default.target`.
3. Systemd détermine les dépendances de la cible de démarrage et les active.

Similaire aux niveaux d'exécution SysV, systemd démarre dans différentes cibles :

- `poweroff.target` - éteindre le système
- `rescue.target` - mode utilisateur unique
- `multi-user.target` - multi-utilisateur avec réseau
- `graphical.target` - multi-utilisateur avec réseau et GUI
- `reboot.target` - redémarrer

L'objectif de démarrage par défaut de `default.target` pointe généralement vers le `graphical.target`.

Les principaux objets avec lesquels systemd travaille sont appelés unités. Systemd ne se contente pas d'arrêter et de démarrer des services ; il peut monter des systèmes de fichiers, surveiller vos sockets réseau, etc. En raison de cette robustesse, il dispose de différents types d'unités avec lesquelles il opère. Les unités les plus courantes sont :

- Unités de service - ce sont les services que nous avons démarrés et arrêtés ; ces fichiers d'unité se terminent par `.service`.
- Unités de montage - Celles-ci montent des systèmes de fichiers ; ces fichiers d'unité se terminent par `.mount`.
- Unités cibles - Celles-ci regroupent d'autres unités ; les fichiers se terminent par `.target`.

Par exemple, supposons que nous démarrions dans notre `default.target`. Cette cible regroupe l'unité `networking.service`, l'unité `crond.service`, etc., donc une fois que nous activons une seule unité, tout ce qui se trouve en dessous de cette unité est également activé.

## Exercise

No exercises for this lesson.

## Quiz Question

Quelle unité est utilisée pour regrouper d'autres unités ?

## Quiz Answer

target
