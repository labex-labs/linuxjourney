---
lesson_id: "setuid-set-user-id"
course_id: "permissions"
lang: "fr"
order_index: 5
title: "Setuid"
description: "Découvrez comment le bit set-user-ID affecte les programmes exécutables et pourquoi il exige un examen de sécurité attentif."
meta_title: "Setuid - Permissions"
meta_description: "Découvrez les permissions Setuid ou SUID sous Linux, leur fonctionnement, leur modification et leurs implications pour la sécurité."
meta_keywords: "Setuid Linux, SUID, permissions Linux, chmod, commande passwd, sécurité Linux, Linux débutant, tutoriel Linux"
---

Certains programmes ont besoin d’un accès étroitement contrôlé que leurs appelants ne possèdent pas normalement. Sur un fichier ordinaire exécutable, le bit set-user-ID peut attribuer au nouveau processus l’identifiant utilisateur du propriétaire du fichier comme identifiant utilisateur effectif. Le programme peut alors effectuer des opérations autorisées pour cette identité tout en conservant des informations sur l’appelant.

Setuid n’est pas une instruction générale signifiant « exécuter en tant que root ». Son effet dépend du propriétaire de l’exécutable, du système d’exploitation, du système de fichiers et de ses options de montage, ainsi que de la manière dont le programme gère ses identifiants.

## Reconnaître setuid

Sur un système qui emploie un exécutable `passwd` setuid, une liste détaillée peut ressembler à ceci :

```bash
$ ls -l /usr/bin/passwd
-rwsr-xr-x 1 root root 68248 Jan 10 09:30 /usr/bin/passwd
```

Le `s` minuscule à la position d’exécution du propriétaire signifie que setuid et l’exécution du propriétaire sont tous deux définis. Si setuid est présent mais que l’exécution du propriétaire est absente, `ls -l` affiche un `S` majuscule à cette position.

Ne supposez pas que chaque distribution possède le même mode ou la même conception de l’authentification. Examinez le système réel au lieu de vous fier à l’exemple.

:::single-choice{#setuid-lowercase-s}
Qu’indique un `s` minuscule à la position d’exécution du propriétaire ?

::option[Setuid est défini, mais l’exécution du propriétaire est absente.]{#setuid-s-without-execute explanation="Cette combinaison s’affiche sous la forme d’un `S` majuscule, et non d’un `s` minuscule."}
::option[Le fichier possède un sticky bit et l’exécution du groupe.]{#setuid-sticky-group explanation="Le sticky bit apparaît à la position d’exécution des autres, tandis que setuid apparaît à celle du propriétaire."}
::option[Setuid et l’exécution du propriétaire sont tous deux définis.]{#setuid-s-with-execute .correct explanation="Le `s` minuscule représente le bit setuid accompagné du bit ordinaire d’exécution du propriétaire."}
:::

## Comprendre le changement d’identifiant

Lorsque le noyau honore setuid pendant l’exécution, le nouveau processus reçoit normalement un identifiant utilisateur effectif dérivé du propriétaire de l’exécutable. Pour un programme appartenant à root, cela peut fournir un accès autorisé pour root, mais uniquement pendant l’exécution du programme et à travers les opérations réalisées par son code.

Ce mécanisme peut permettre à un programme soigneusement écrit de valider une demande et d’apporter une modification limitée à un état protégé. Par exemple, un utilitaire local de changement de mot de passe peut nécessiter un accès contrôlé à des données d’authentification que les utilisateurs ordinaires ne peuvent pas modifier directement. Les implémentations modernes reposent aussi sur PAM, le verrouillage des fichiers, des politiques et d’autres protections ; setuid seul n’explique pas toute la procédure.

:::single-choice{#setuid-effective-identity}
Lorsqu’un exécutable setuid est honoré, quelle identité provient principalement du propriétaire du fichier ?

::option[Le nom de connexion enregistré dans `/etc/passwd`.]{#setuid-login-name explanation="L’exécution d’un fichier ne réécrit ni l’enregistrement du compte ni le nom de connexion de l’appelant."}
::option[L’identifiant utilisateur effectif du processus.]{#setuid-effective-user .correct explanation="Le mécanisme d’exécution set-user-ID modifie l’identité utilisateur effective employée pour de nombreux contrôles d’autorisation."}
::option[Le groupe propriétaire de chaque fichier ouvert.]{#setuid-opened-file-group explanation="Setuid affecte les identifiants du processus, pas les métadonnées de propriété de fichiers sans rapport."}
:::

## Définir et retirer le bit

Définissez setuid symboliquement avec :

```bash
$ sudo chmod u+s myfile
```

En notation octale, setuid contribue pour `4` au premier chiffre des bits spéciaux :

```bash
$ sudo chmod 4755 myfile
```

Ici, le premier `4` définit setuid et `755` les bits ordinaires du propriétaire, du groupe et des autres. Retirez setuid sans modifier le reste du mode avec `chmod u-s myfile`.

:::single-choice{#setuid-octal-value}
Quelle première valeur octale représente le bit spécial setuid ?

::option[`4`]{#setuid-octal-four .correct explanation="Setuid contribue pour `4` au premier chiffre des bits spéciaux."}
::option[`1`]{#setuid-octal-one explanation="Un premier `1` représente le sticky bit."}
::option[`2`]{#setuid-octal-two explanation="Un premier `2` représente le bit setgid."}
:::

## Considérer setuid comme sensible pour la sécurité

Une faille dans un programme setuid privilégié peut devenir une voie d’élévation des privilèges. Ces programmes doivent valider leurs entrées, contrôler l’environnement et les chemins auxquels ils font confiance, éviter les comportements dangereux des sous-processus, réduire le code privilégié au minimum et abandonner les identifiants élevés dès que possible.

Linux n’honore normalement pas setuid sur les scripts interprétés, car une mise en œuvre sûre pose des problèmes de concurrence et d’interpréteur. Les systèmes de fichiers montés avec `nosuid` suppriment également les effets de setuid et setgid. Préférez des mécanismes plus étroits, tels que les opérations médiées par un service, une politique `sudo` soigneusement limitée ou les capacités lorsqu’ils répondent au besoin.

N’ajoutez jamais setuid à un shell, un interpréteur ou un programme copié arbitrairement pour faire une expérience sur un système partagé. Auditez les fichiers setuid existants et entraînez-vous uniquement dans un environnement isolé et jetable.

:::single-choice{#setuid-nosuid-mount}
Quel est le but du montage d’un système de fichiers avec `nosuid` ?

::option[Retirer chaque bit d’exécution enregistré sur ses fichiers.]{#setuid-nosuid-remove-execute explanation="Cette option ne réécrit pas les bits ordinaires d’exécution dans les métadonnées des fichiers."}
::option[Supprimer les effets de setuid et setgid lors de l’exécution sur ce système de fichiers.]{#setuid-nosuid-suppress .correct explanation="L’option de montage `nosuid` empêche ces bits spéciaux d’accorder leur comportement habituel de changement d’identifiants à l’exécution."}
::option[Attribuer tous les fichiers du système de fichiers à root.]{#setuid-nosuid-root-owner explanation="Le montage avec `nosuid` ne modifie pas les champs d’utilisateur ou de groupe propriétaires."}
:::

## Résumé

Vous savez maintenant reconnaître setuid et expliquer ses conséquences sur les identifiants et la sécurité.

1. Repérer `s` ou `S` à la position d’exécution du propriétaire.
2. Relier l’exécution setuid à l’identité utilisateur effective du propriétaire de l’exécutable.
3. Définir ou retirer le bit avec les modes symboliques ou octaux de `chmod`.
4. Considérer chaque exécutable privilégié comme du code sensible pour la sécurité.
