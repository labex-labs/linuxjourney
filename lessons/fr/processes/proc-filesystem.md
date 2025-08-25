---
index: 10
lang: "fr"
title: "/proc filesystem"
meta_title: "/proc filesystem - Processus"
meta_description: "Découvrez le système de fichiers /proc dans Linux, comment il stocke les informations sur les processus et sa structure. Explorez les détails des processus avec ce guide Linux essentiel."
meta_keywords: "/proc filesystem, processus Linux, informations sur les processus, tutoriel Linux, Linux pour débutants, guide Linux"
---

## Lesson Content

Rappelez-vous, tout dans Linux est un fichier, même les processus. Les informations sur les processus sont stockées dans un système de fichiers spécial appelé système de fichiers `/proc`.

```bash
ls /proc
```

Vous devriez voir plusieurs valeurs ici ; il y a des sous-répertoires pour chaque PID. Si vous avez regardé un PID dans la sortie de `ps`, vous seriez en mesure de le trouver dans le répertoire `/proc`.

Allez-y et entrez dans l'un des processus et regardez ce fichier :

```bash
cat /proc/12345/status
```

Vous devriez voir les informations sur l'état du processus ainsi que des informations plus détaillées. Le répertoire `/proc` est la façon dont le noyau voit le système, il y a donc beaucoup plus d'informations ici que ce que vous verriez dans `ps`.

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension des processus Linux et de la surveillance du système :

1. **[Gérer et surveiller les processus Linux](https://labex.io/fr/labs/comptia-manage-and-monitor-linux-processes-590864)** - Dans ce laboratoire, vous apprendrez les compétences essentielles pour gérer et surveiller les processus sur un système Linux. Vous explorerez comment interagir avec les processus de premier plan et d'arrière-plan, les inspecter avec `ps`, surveiller les ressources avec `top`, ajuster la priorité avec `renice` et les terminer avec `kill`.

Ces laboratoires vous aideront à appliquer les concepts dans des scénarios réels et à renforcer votre confiance dans la gestion des processus et l'observation du système.

## Quiz Question

Quel système de fichiers stocke les informations sur les processus ?

## Quiz Answer

/proc
