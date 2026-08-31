---
lesson_id: "sticky-bit"
course_id: "permissions"
lang: "fr"
order_index: 8
title: "Le sticky bit"
description: "Découvrez comment le sticky bit protège les entrées des répertoires partagés accessibles en écriture tels que `/tmp`."
meta_title: "Le sticky bit - Permissions"
meta_description: "Explorez le rôle du sticky bit dans les permissions Linux et Unix, sa protection des fichiers dans /tmp et sa définition avec chmod."
meta_keywords: "sticky bit, sticky bit Linux, permissions fichiers Unix, chmod +t, répertoire /tmp, permissions fichiers, sécurité Linux"
---

Un répertoire accessible en écriture permet normalement à un utilisateur autorisé de supprimer ou de renommer ses entrées, même si cet utilisateur ne possède pas les fichiers eux-mêmes. Le sticky bit ajoute une restriction fondée sur la propriété qui rend les répertoires partagés accessibles en écriture plus sûrs.

## Comment le sticky bit limite la suppression

Lorsqu’un répertoire possède le sticky bit, Linux ne permet généralement de supprimer ou de renommer une entrée qu’à un processus suffisamment privilégié, au propriétaire du répertoire ou au propriétaire de l’entrée. Les permissions ordinaires d’écriture et de recherche du répertoire restent nécessaires.

Cette restriction concerne les entrées du répertoire. Elle n’empêche pas le propriétaire d’un fichier d’en modifier le contenu lorsque ses permissions l’autorisent, et ne rend pas le répertoire privé.

:::single-choice{#sticky-bit-removal-rule}
Dans un répertoire partagé doté du sticky bit, quel utilisateur ordinaire peut normalement supprimer une entrée particulière ?

::option[N’importe quel utilisateur capable de répertorier le répertoire.]{#sticky-bit-any-reader explanation="La permission de lecture du répertoire peut révéler les noms, mais ne contourne pas la restriction de propriété du sticky bit."}
::option[Le propriétaire de l’entrée, s’il possède l’accès requis au répertoire.]{#sticky-bit-entry-owner .correct explanation="Le propriétaire de l’entrée fait partie des identités normalement autorisées par la règle du répertoire doté du sticky bit."}
::option[Uniquement un membre du groupe de l’entrée.]{#sticky-bit-entry-group explanation="La seule appartenance au groupe ne constitue pas l’exception de propriété définie par le sticky bit."}
:::

## Reconnaître le bit sur `/tmp`

Le répertoire temporaire du système est un exemple courant :

```bash
$ ls -ld /tmp
drwxrwxrwt 17 root root 4096 Dec 15 11:45 /tmp
```

Le `t` minuscule final occupe la position d’exécution des autres. Il signifie que le sticky bit et la permission d’exécution des autres sont présents. Un `T` majuscule signifie que le sticky bit est défini tandis que l’exécution des autres est absente.

Comme `/tmp` est généralement accessible en écriture et en recherche à tous, plusieurs utilisateurs peuvent y créer des entrées. Le sticky bit empêche un utilisateur ordinaire de supprimer les entrées d’un autre utilisateur au seul motif que le répertoire est accessible en écriture à tous. Les applications doivent néanmoins créer les objets temporaires de manière sûre, car les noms prévisibles, les liens dangereux et les modes trop faibles constituent des risques distincts.

:::single-choice{#sticky-bit-lowercase-t}
Qu’indique un `t` minuscule à la fin du mode d’un répertoire ?

::option[Le sticky bit et l’exécution des autres sont définis.]{#sticky-bit-t-with-execute .correct explanation="Le `t` minuscule associe le bit spécial sticky au bit ordinaire d’exécution des autres."}
::option[Le sticky bit est défini, mais l’exécution des autres est absente.]{#sticky-bit-t-without-execute explanation="Cette combinaison est affichée sous la forme d’un `T` majuscule."}
::option[Setgid et l’exécution du groupe sont définis.]{#sticky-bit-setgid-position explanation="Setgid apparaît à la position d’exécution du groupe, et non à la position finale des autres."}
:::

## Définir et retirer le sticky bit

Définissez le bit symboliquement :

```bash
$ chmod +t shared-directory
```

Dans le premier chiffre octal des bits spéciaux, sticky contribue pour `1` :

```bash
$ chmod 1777 shared-directory
```

Le premier `1` définit sticky, tandis que `777` fournit le mode ordinaire. Ce mode ne convient que si le répertoire doit être partagé intentionnellement par tous les utilisateurs locaux. Des permissions de groupe plus étroites peuvent être préférables pour un répertoire d’équipe. Retirez uniquement le sticky bit avec `chmod -t shared-directory`.

:::single-choice{#sticky-bit-octal-value}
Quelle première valeur octale représente le sticky bit ?

::option[`2`]{#sticky-bit-value-two explanation="Un premier `2` représente setgid."}
::option[`1`]{#sticky-bit-value-one .correct explanation="Le sticky bit contribue pour `1` au premier chiffre des bits spéciaux."}
::option[`4`]{#sticky-bit-value-four explanation="Un premier `4` représente setuid."}
:::

## Vérifier la politique complète du répertoire

Sticky n’accorde ni l’écriture ni la recherche ; il ne fait que limiter la suppression et le changement de nom après que les permissions ordinaires ont autorisé la modification du répertoire. Vérifiez ensemble le propriétaire, le groupe, le mode ordinaire, les ACL et le contexte de montage du répertoire. Effectuez les tests avec des comptes sans privilèges dans un environnement isolé plutôt que de modifier `/tmp` sur un système en service.

:::single-choice{#sticky-bit-access-scope}
L’ajout du sticky bit rend-il un répertoire non accessible en écriture modifiable par les autres utilisateurs ?

::option[Oui ; sticky ajoute automatiquement l’écriture à chaque classe.]{#sticky-bit-adds-write explanation="Le bit spécial ne réécrit pas les bits d’écriture du propriétaire, du groupe ou des autres."}
::option[Oui ; sticky désactive le triplet de permissions des autres.]{#sticky-bit-disables-other explanation="Le triplet des autres continue de participer aux contrôles d’accès ordinaires."}
::option[Non ; les permissions ordinaires d’écriture et de recherche continuent de contrôler l’accès.]{#sticky-bit-no-write-grant .correct explanation="Sticky restreint certaines opérations de suppression et de changement de nom, mais n’ajoute pas de permissions ordinaires absentes."}
:::

Pour vous exercer, créez un répertoire partagé jetable, définissez un mode ordinaire approprié et le sticky bit, puis testez la suppression d’entrées avec deux utilisateurs sans privilèges. L’atelier [Supprimer et déplacer des fichiers](https://labex.io/fr/labs/linux-delete-and-move-files-7777) renforce les opérations sous-jacentes de changement de nom et de suppression.

## Résumé

Vous savez maintenant expliquer et vérifier le sticky bit sur les répertoires partagés.

1. Relier sticky aux restrictions de propriété lors de la suppression et du changement de nom.
2. Reconnaître le `t` minuscule et le `T` majuscule dans une liste détaillée.
3. Définir le bit symboliquement ou avec la première valeur octale `1`.
4. Évaluer sticky avec les permissions ordinaires du répertoire.
