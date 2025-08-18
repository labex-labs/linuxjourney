---
lang: "fr"
title: "Modification des permissions"
meta_title: "Modification des permissions - Permissions"
meta_description: "Apprenez à utiliser la commande chmod pour modifier les permissions de fichiers sous Linux. Comprenez les modes symboliques et numériques pour une gestion sécurisée des fichiers. Commencez à apprendre maintenant !"
meta_keywords: "commande chmod, permissions Linux, permissions de fichiers, tutoriel chmod, sécurité Linux, Linux pour débutants, guide Linux, chmod numérique"
---

## Lesson Content

Changer les permissions peut être facilement fait avec la commande `chmod`.

Tout d'abord, choisissez l'ensemble de permissions que vous souhaitez modifier : utilisateur, groupe ou autre. Vous pouvez ajouter ou supprimer des permissions avec un `+` ou un `-`. Examinons quelques exemples.

### Ajout d'un bit de permission sur un fichier

```bash
chmod u+x myfile
```

La commande ci-dessus se lit comme suit : changer la permission sur `myfile` en ajoutant le bit de permission exécutable à l'ensemble utilisateur. Ainsi, l'utilisateur a maintenant la permission d'exécution sur ce fichier !

### Suppression d'un bit de permission sur un fichier

```bash
chmod u-x myfile
```

### Ajout de plusieurs bits de permission sur un fichier

```bash
chmod ug+w
```

Il existe une autre façon de changer les permissions en utilisant le format numérique. Cette méthode vous permet de changer toutes les permissions en une seule fois. Au lieu d'utiliser r, w ou x pour représenter les permissions, vous utiliserez une représentation numérique pour un seul ensemble de permissions. Il n'est donc pas nécessaire de spécifier le groupe avec `g` ou l'utilisateur avec `u`.

Les représentations numériques sont les suivantes :

- 4: permission de lecture
- 2: permission d'écriture
- 1: permission d'exécution

Regardons un exemple :

```bash
chmod 755 myfile
```

Pouvez-vous deviner quelles permissions nous donnons à ce fichier ? Décomposons cela : `755` couvre les permissions pour tous les ensembles. Le premier chiffre (7) représente les permissions de l'utilisateur, le deuxième chiffre (5) représente les permissions du groupe, et le dernier 5 représente les autres permissions.

Attendez une minute, 7 et 5 n'étaient pas listés ci-dessus. D'où viennent ces chiffres ? N'oubliez pas que nous combinons maintenant toutes les permissions en un seul chiffre, vous devrez donc faire un peu de calcul.

7 = 4 + 2 + 1, donc 7 correspond aux permissions de l'utilisateur, et il a les permissions de lecture, d'écriture et d'exécution.

5 = 4 + 1, le groupe a les permissions de lecture et d'exécution.

5 = 4 + 1, et tous les autres utilisateurs ont les permissions de lecture et d'exécution.

Une chose à noter : ce n'est pas une bonne idée de changer les permissions à tort et à travers. Vous pourriez potentiellement exposer un fichier sensible à la modification par tout le monde. Cependant, de nombreuses fois, vous voulez légitimement changer les permissions ; prenez simplement des précautions lorsque vous utilisez la commande `chmod`.

## Exercise

Change some basic text file permissions and see the bits changing as you do an `ls -l`.

## Quiz Question

Quel chiffre représente la permission de lecture lors de l'utilisation du format numérique ?

## Quiz Answer

4
