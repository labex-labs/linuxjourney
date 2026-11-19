---
lesson_id: "host-file-integrity"
course_id: "system-auditing"
lang: "fr"
order_index: 3
title: "Intégrité des fichiers"
description: "Apprenez à comparer le contenu et les permissions d’un fichier à l’aide d’une empreinte et de métadonnées."
meta_title: "Intégrité des fichiers - Audit système"
meta_description: "Apprenez à comparer le contenu et les permissions d’un fichier à l’aide d’une empreinte et de métadonnées."
meta_keywords: "intégrité des fichiers, audit système, cybersécurité, Linux Journey"
---

Un contrôle d’intégrité vérifie si un fichier correspond toujours à une référence. Vérifiez séparément son contenu et ses métadonnées. Le contenu correspond aux octets du fichier. Les **métadonnées** comprennent des renseignements comme les droits d’accès.

## Noter une empreinte du contenu

Dans un dossier d’exercice vide, créez un petit fichier de configuration. La redirection remplace tout fichier existant du même nom. Utilisez donc un dossier neuf.

```bash
$ printf '%s\n' 'mode=preview' > site.conf
$ sha256sum site.conf
```

Le premier champ est l’**empreinte**, une valeur de longueur fixe calculée à partir des octets du fichier. Réutilisez la même méthode sur le même fichier plus tard. Une différence d’empreinte indique que les octets fournis au calcul ont changé.

:::single-choice{#host-file-integrity-changed-hash} La valeur SHA-256 change après une modification du fichier. Que montre la comparaison ?

::option[Le contenu diffère des octets mesurés auparavant.]{#host-file-integrity-changed-hash-a .correct explanation="L’empreinte varie selon le contenu fourni au calcul."}
::option[La modification était forcément non autorisée.]{#host-file-integrity-changed-hash-b explanation="L’autorisation reste à vérifier séparément."}
::option[Les droits d’un compte ont forcément changé.]{#host-file-integrity-changed-hash-c explanation="Une empreinte du contenu ne consigne pas les droits d’accès."}
:::

## Noter les permissions

Sous Linux, `stat -c` affiche les métadonnées demandées. Le champ `%a` affiche les permissions sous forme numérique et `%n` affiche le nom.

```bash
$ stat -c '%a %n' site.conf
```

Les permissions initiales exactes peuvent dépendre de la manière dont le fichier a été créé. Notez-les avec l’empreinte pour pouvoir comparer les deux propriétés plus tard.

:::single-choice{#host-file-integrity-mode-vs-content} L’empreinte correspond à la référence et stat indique un mode différent. Qu’est-ce qui a changé d’après ces contrôles ?

::option[Les octets du fichier ont changé et les permissions sont restées identiques.]{#host-file-integrity-mode-vs-content-a explanation="L’empreinte correspond à la référence et le mode diffère."}
::option[Le fichier a forcément été supprimé.]{#host-file-integrity-mode-vs-content-c explanation="Les deux contrôles ont fourni des informations sur le fichier."}
::option[Les permissions ont changé et l’empreinte du contenu observée est restée identique.]{#host-file-integrity-mode-vs-content-b .correct explanation="Ces deux outils mesurent des propriétés différentes."}
:::

## Tester un changement de permissions

La commande suivante applique le mode `640` à ce fichier d’exercice. Elle donne au propriétaire les droits de lecture et d’écriture et au groupe le droit de lecture. Exécutez de nouveau les deux contrôles et comparez les résultats.

```bash
$ chmod 640 site.conf
$ stat -c '%a %n' site.conf
$ sha256sum site.conf
```

Le mode affiché devrait être 640 et l’empreinte devrait correspondre à la première mesure.

:::single-choice{#host-file-integrity-repeat-check} Quel contrôle détecterait une modification ultérieure de mode=preview dans le fichier ?

::option[Le nom du fichier affiché par stat, à lui seul.]{#host-file-integrity-repeat-check-a explanation="Le nom peut rester identique après une modification."}
::option[Un nouveau calcul SHA-256 comparé au premier.]{#host-file-integrity-repeat-check-c .correct explanation="Une modification du contenu produirait une empreinte différente."}
::option[Le chiffre des permissions du propriétaire, à lui seul.]{#host-file-integrity-repeat-check-b explanation="Les permissions peuvent évoluer indépendamment de la plupart des modifications du contenu."}
:::

![Sortie enregistrée dans LabEx montrant des permissions passées à 640 et une empreinte du contenu identique](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/system-auditing/host-file-integrity/mode-vs-content.png)

## Résumé

Vous savez maintenant comparer indépendamment le contenu d’un fichier et ses droits d’accès.

1. Notez une empreinte SHA-256 du contenu.
2. Lisez les permissions avec stat.
3. Vérifiez l’effet d’un changement de permissions.
