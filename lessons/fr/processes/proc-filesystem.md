---
title: "Système de fichiers /proc"
description: "Découvrez le système de fichiers /proc dans Linux, comment il stocke les informations de processus et sa structure. Explorez les détails des processus avec ce guide Linux essentiel."
keywords: "système de fichiers /proc, processus Linux, informations de processus, tutoriel Linux, Linux pour débutants, guide Linux"
---

## Lesson Content

Rappelez-vous, tout dans Linux est un fichier, même les processus. Les informations sur les processus sont stockées dans un système de fichiers spécial appelé le système de fichiers `/proc`.

```bash
ls /proc
```

Vous devriez voir plusieurs valeurs ici ; il y a des sous-répertoires pour chaque PID. Si vous avez regardé un PID dans la sortie `ps`, vous seriez capable de le trouver dans le répertoire `/proc`.

Allez-y et entrez dans l'un des processus et regardez ce fichier :

```bash
cat /proc/12345/status
```

Vous devriez voir des informations sur l'état du processus ainsi que des informations plus détaillées. Le répertoire `/proc` est la façon dont le noyau voit le système, il y a donc beaucoup plus d'informations ici que ce que vous verriez dans `ps`.

## Exercise

Pas d'exercices pour cette leçon.

## Quiz Question

Quel système de fichiers stocke les informations de processus ?

## Quiz Answer

/proc
