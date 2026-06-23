---
index: 19
lang: "fr"
title: "exit"
meta_title: "exit - Ligne de commande"
meta_description: "Apprenez la commande Linux exit, comment fermer une session shell, la différence entre logout et exit, et le fonctionnement des codes de sortie."
meta_keywords: "commande exit, linux exit, commande logout, session shell, sortie terminal, code de sortie, bash exit"
---

## Lesson Content

Félicitations pour avoir terminé les leçons fondamentales de votre parcours Linux ! Vous avez couvert les bases essentielles de Linux, et il est maintenant temps d’apprendre comment terminer correctement votre session. Quitter le shell Linux est une étape simple mais importante.

### La commande Exit

La manière la plus courante de terminer une session shell est la commande `exit`. Lorsque vous tapez `exit` et appuyez sur Entrée, le processus shell actuel se termine. Cette commande fonctionne dans pratiquement tous les environnements shell.

```bash
$ exit
```

Si vous avez ouvert une fenêtre de terminal, `exit` ferme généralement le shell qui y est exécuté. Si vous êtes connecté via SSH, `exit` termine la session shell distante et vous ramène à votre invite locale.

### Codes de sortie

La commande `exit` peut aussi retourner un code de sortie. Un code `0` signifie généralement succès, et un code non nul indique une erreur ou une condition particulière.

```bash
$ exit 0
```

Vous verrez les codes de sortie plus souvent lors de l’écriture de scripts shell. Pour une utilisation interactive, taper simplement `exit` suffit.

### La commande Logout

Une autre commande que vous pouvez utiliser pour quitter un terminal est `logout`. Cette commande est spécialement conçue pour terminer un shell de connexion. Bien que sur de nombreux systèmes modernes elle se comporte de manière similaire à `exit`, il est bon de connaître les deux commandes.

```bash
$ logout
```

### Fermer la fenêtre du terminal

Si vous travaillez dans une interface graphique, vous avez aussi la possibilité de simplement fermer la fenêtre du terminal. Cette action envoie généralement un signal qui termine la session shell en cours.

### Moyens courants de quitter un shell

- Tapez `exit` pour terminer le shell actuel.
- Appuyez sur `Ctrl-D` sur une invite vide pour envoyer un signal de fin de fichier, ce qui quitte souvent le shell.
- Tapez `logout` lorsque vous êtes dans un shell de connexion.
- Fermez la fenêtre du terminal lorsque vous utilisez un terminal graphique.

### Questions fréquentes

**Est-ce que exit est la même chose que fermer la fenêtre du terminal ?** Souvent le résultat est similaire, mais `exit` indique proprement au shell de se terminer.

**Qu’est-ce que Ctrl-D ?** Il envoie un signal de fin de fichier au shell. Sur une invite vide, cela quitte généralement le shell.

**Que signifie exit 1 ?** Cela quitte avec le code de sortie `1`, souvent utilisé pour indiquer un échec dans les scripts.

Vous avez appris avec succès à naviguer, travailler avec les fichiers, obtenir de l’aide et quitter le shell.

## Exercise

Bien qu’il n’y ait pas de laboratoires spécifiques pour ce sujet, nous vous recommandons d’explorer le parcours complet [Linux Learning Path](https://labex.io/fr/learn/linux) pour pratiquer les compétences et concepts Linux associés.

## Quiz Question

Quelle est la commande la plus courante pour quitter le shell Linux ? Veuillez répondre en un seul mot en anglais, en minuscules.

## Quiz Answer

exit
