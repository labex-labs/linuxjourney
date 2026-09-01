---
lesson_id: "stdout-standard-out-redirect"
course_id: "text-fu"
lang: "fr"
order_index: 1
title: "stdout (sortie standard)"
description: "Découvrez comment la sortie standard arrive au terminal et comment Bash la redirige vers des fichiers."
meta_title: "stdout (sortie standard) - Text-Fu"
meta_description: "Maîtrisez stdout et la redirection d'E/S avec les opérateurs > et >> de Bash."
meta_keywords: "Linux, apprendre Linux, stdout, redirection E/S, sortie standard, Bash, shell"
---

Les programmes communiquent au moyen de flux d'entrée et de sortie. La sortie standard, abrégée **stdout**, est le flux normalement employé pour les résultats ordinaires. Dans un terminal, le shell le relie initialement à l'affichage.

## Écrire sur la sortie standard

La commande `echo` écrit ses arguments sur stdout :

```bash
$ echo Hello World
Hello World
```

Stdout correspond au descripteur de fichier `1`, utile lorsque plusieurs flux sont redirigés. Les programmes disposent aussi de stdin et stderr, étudiés dans les prochaines leçons.

:::single-choice{#stdout-default-destination} Sans redirection, où `echo Hello World` envoie-t-elle normalement sa sortie dans un terminal interactif ?

::option[Dans un fichier `stdout` du répertoire courant.]{#stdout-file explanation="La sortie standard est un flux, pas un fichier créé automatiquement."}
::option[Vers le terminal par la sortie standard.]{#stdout-terminal .correct explanation="Le shell relie normalement stdout au terminal, où `echo` s'affiche."}
::option[Vers l'entrée standard de la commande.]{#stdout-to-stdin explanation="Stdin transporte les données vers un programme ; `echo` émet son résultat par stdout."}
:::

## Remplacer un fichier avec >

Bash interprète `>` comme une redirection de sortie :

```bash
$ echo Hello World > peanuts.txt
```

Le texte ne s'affiche plus, car stdout va dans `peanuts.txt`. Le shell crée le fichier s'il manque et le tronque s'il existe, supprimant son ancien contenu.

```bash
$ cat peanuts.txt
Hello World
```

:::single-choice{#stdout-replace-file} `notes.txt` contient déjà du texte. Que fait `echo new > notes.txt` ?

::option[Elle remplace son contenu par `new`.]{#stdout-replace-existing .correct explanation="Avec `>`, le shell tronque la destination avant d'y diriger la sortie."}
::option[Elle ajoute `new` après le texte existant.]{#stdout-add-existing explanation="L'ajout exige `>>` ; `>` ne préserve pas l'ancien contenu."}
::option[Elle affiche `new` sans modifier le fichier.]{#stdout-display-only explanation="La redirection envoie stdout vers `notes.txt`."}
:::

Le shell ouvre la destination avant la commande. Vérifiez donc le chemin : une faute peut tronquer un fichier même si la commande échoue ensuite.

## Ajouter à un fichier avec >>

Utilisez `>>` pour ajouter la nouvelle sortie :

```bash
$ echo Another line >> peanuts.txt
$ cat peanuts.txt
Hello World
Another line
```

Comme `>`, `>>` crée une destination absente, mais ajoute au lieu de tronquer.

:::single-choice{#stdout-append-file} Quelle commande ajoute `Finished` à `status.log` sans effacer son contenu ?

::option[`echo Finished > status.log`]{#stdout-truncate-status explanation="`>` tronque la destination."}
::option[`echo Finished >> status.log`]{#stdout-append-status .correct explanation="`>>` ajoute la sortie de `echo` au fichier."}
::option[`cat Finished >> status.log`]{#stdout-cat-filename explanation="Cette commande demande à `cat` de lire un fichier nommé `Finished`."}
:::

## La redirection appartient au shell

Le shell retire `>` et `>>` des arguments transmis, ouvre le fichier et établit la connexion. La commande continue simplement d'écrire sur stdout.

```bash
$ pwd > current-directory.txt
$ ls -la >> directory-list.txt
```

:::single-choice{#stdout-shell-role} Qui interprète normalement `>` dans `pwd > current-directory.txt` ?

::option[La commande `pwd`, qui reçoit `>` comme argument.]{#stdout-pwd-redirection explanation="Le shell consomme cette syntaxe ; `pwd` ne la reçoit pas comme argument."}
::option[Le shell Bash avant de lancer `pwd`.]{#stdout-bash-redirection .correct explanation="Bash ouvre la destination et relie le descripteur 1 avant l'exécution."}
::option[Le terminal après l'affichage du chemin.]{#stdout-terminal-redirection explanation="Le flux est redirigé avant toute écriture."}
:::

Pour vous exercer :

1. **[Rediriger les entrées et sorties sous Linux](https://labex.io/fr/labs/comptia-redirecting-input-and-output-in-linux-590840)** - Manipulez stdout, stderr et stdin avec `>`, `>>`, `2>` et `tee`.

## Résumé

Vous savez maintenant rediriger stdout sans confondre remplacement et ajout.

1. Reconnaître stdout comme le flux des résultats ordinaires.
2. Remplacer un fichier avec `>`.
3. Ajouter avec `>>`.
4. Vérifier la destination avant son ouverture.
