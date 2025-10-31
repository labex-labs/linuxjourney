---
index: 5
lang: "fr"
title: "Aperçu de Systemd"
meta_title: "Aperçu de Systemd - Init"
meta_description: "Apprenez les fondamentaux du système d'initialisation systemd. Ce guide couvre comment systemd (ou system d) utilise les unités et les cibles pour gérer le processus de démarrage Linux et les services système. Comprenez les concepts clés de la norme moderne pour l'initialisation Linux."
meta_keywords: "systemd, system d, système d'init, unités systemd, cibles systemd, processus de démarrage linux, services linux, gestion système, débutant, tutoriel"
---

## Lesson Content

### Qu'est-ce que Systemd ?

Systemd est le système d'initialisation (init system) et le gestionnaire de services par défaut pour la plupart des distributions Linux modernes. Il est responsable de l'initialisation du système dans le bon ordre après le chargement du noyau. Une manière simple de vérifier si votre système l'utilise est de voir si le répertoire `/usr/lib/systemd` existe. Si c'est le cas, vous utilisez probablement un système géré par **systemd**.

### Le Processus de Démarrage de Systemd

Au lieu de scripts séquentiels rigides, **systemd** utilise le concept d'"objectifs" (goals) pour amener votre système à un état fonctionnel. Il identifie un objectif principal, ou `target` (cible), et travaille à satisfaire ses dépendances. Cette approche permet une plus grande flexibilité et parallélisation lors du démarrage. Un processus de démarrage typique géré par **systemd** suit ces étapes :

1. **systemd** charge d'abord ses fichiers de configuration à partir de répertoires comme `/etc/systemd/system` et `/usr/lib/systemd/system`.
2. Il identifie ensuite l'objectif de démarrage par défaut, qui est généralement un lien symbolique nommé `default.target`.
3. Enfin, **systemd** résout toutes les dépendances de cette cible et active les unités nécessaires pour atteindre l'état système souhaité.

### Comprendre les Cibles (Targets) de Systemd

Les cibles (Targets) dans **systemd** sont analogues aux niveaux d'exécution (runlevels) dans l'ancien système d'initialisation SysV. Elles représentent différents états dans lesquels le système peut se trouver. Les cibles courantes incluent :

- `poweroff.target` : Éteint le système.
- `rescue.target` : Démarre dans un shell mono-utilisateur pour la maintenance.
- `multi-user.target` : Un environnement multi-utilisateur standard avec mise en réseau mais sans interface graphique.
- `graphical.target` : Un environnement multi-utilisateur complet avec mise en réseau et une interface utilisateur graphique (IUG).
- `reboot.target` : Redémarre le système.

Le `default.target` est un lien symbolique qui pointe vers la cible dans laquelle le système démarrera par défaut, souvent `graphical.target` sur les systèmes de bureau.

### Concept Clé : Les Unités Systemd

Les objets fondamentaux que **systemd** gère sont appelés des "unités". Une unité est un fichier de configuration qui décrit une ressource ou un service. La puissance de l'architecture de **system d** réside dans sa capacité à gérer divers types de ressources, pas seulement des services. Chaque type d'unité est identifié par son extension de fichier. Les types les plus courants sont :

- **Unités de service (`.service`)** : Celles-ci gèrent les démons ou services système, comme un serveur web ou une base de données.
- **Unités de montage (`.mount`)** : Celles-ci contrôlent les points de montage du système de fichiers.
- **Unités de cible (`.target`)** : Celles-ci sont utilisées pour regrouper d'autres unités, créant des points de synchronisation lors du démarrage.

Par exemple, lorsque le système démarre dans `graphical.target`, cette unité cible s'assure que toutes ses dépendances, telles que `multi-user.target` et diverses unités de service comme `network.service`, sont démarrées en premier.

## Exercise

Bien qu'il n'y ait pas de laboratoires spécifiques pour ce sujet, nous vous recommandons d'explorer le [Parcours d'Apprentissage Linux](https://labex.io/fr/learn/linux) complet pour pratiquer les compétences et concepts Linux associés.

## Quiz Question

Quelle unité est utilisée pour regrouper d'autres unités ? Veuillez répondre par un seul mot anglais en minuscules.

## Quiz Answer

target
