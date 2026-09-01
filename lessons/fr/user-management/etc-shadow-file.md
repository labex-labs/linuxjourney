---
lesson_id: "etc-shadow-file"
course_id: "user-management"
lang: "fr"
order_index: 4
title: "/etc/shadow"
description: "Découvrez comment les enregistrements shadow locaux représentent les hachages et le vieillissement sans exposer de données sensibles."
meta_title: "/etc/shadow - Gestion des utilisateurs"
meta_description: "Comprenez les neuf champs protégés de /etc/shadow, les hachages de mots de passe et les politiques d'expiration Linux."
meta_keywords: "/etc/shadow, Linux, hachage mot de passe, authentification, expiration compte"
---

`/etc/shadow` stocke les hachages protégés des mots de passe locaux et leurs champs de vieillissement. Les séparer de `/etc/passwd`, généralement lisible, réduit l'exposition aux attaques hors ligne.

## Protéger les données shadow

Les mots de passe ne sont pas chiffrés de façon réversible pour être réaffichés. Une entrée contient normalement un hachage à sens unique encodé avec algorithme, sel et paramètres. Un attaquant qui l'obtient peut tester des candidats hors ligne ; la base doit donc rester restreinte.

Propriétaire et permissions exacts varient, mais l'accès est souvent limité à root et à quelques composants autorisés. N'affichez, ne copiez, ne journalisez ni ne partagez le contenu pour simplement vérifier un état.

:::single-choice{#shadow-restricted-reason} Pourquoi les données shadow sont-elles normalement protégées de la lecture générale ?

::option[Le fichier contient tous les mots de passe actuels en clair.]{#shadow-plaintext-passwords explanation="Les entrées correctes contiennent des hachages à sens unique ou des marqueurs, pas des mots de passe récupérables."}
::option[Des hachages divulgués peuvent subir des essais hors ligne.]{#shadow-offline-guessing .correct explanation="Un attaquant peut tester des mots de passe sans interagir avec le service de connexion."}
::option[Leur lecture change automatiquement toutes les dates d'expiration.]{#shadow-read-changes explanation="Lire ne met pas à jour les champs ; le danger est la divulgation."}
:::

## Lire le format à neuf champs

```text
alice:<password-field>:20000:0:90:7:14:20500:
```

Les champs sont :

1. **Nom de connexion**.
2. **Hachage ou marqueur spécial**.
3. **Dernier changement**, en jours depuis le 01-01-1970 ; `0` demande couramment un changement à la prochaine connexion par mot de passe.
4. **Âge minimal** du mot de passe.
5. **Âge maximal**.
6. **Période d'avertissement** avant expiration.
7. **Période d'inactivité** après expiration.
8. **Date d'expiration du compte**, en jours depuis le 01-01-1970.
9. **Champ réservé**.

Champs vides et valeurs spéciales ont des sens définis selon le champ et les outils. Utilisez les commandes de comptes plutôt qu'une édition visuelle.

:::single-choice{#shadow-account-expiration-field} Quel champ contient la date d'expiration du compte en jours depuis le 01-01-1970 ?

::option[Le champ 3]{#shadow-field-three explanation="Il indique la date du dernier changement de mot de passe."}
::option[Le champ 8]{#shadow-field-eight .correct explanation="Le huitième champ contient le nombre absolu de jours d'expiration du compte."}
::option[Le champ 5]{#shadow-field-five explanation="Il indique l'âge maximal du mot de passe."}
:::

## Interpréter prudemment le champ du mot de passe

Un hachage valide au champ 2 permet la vérification locale. Une valeur commençant par `!` verrouille couramment ce hachage ; `*` ou un autre marqueur invalide empêche sa vérification. Un champ vide est sensible et peut permettre une connexion sans mot de passe selon PAM.

Ces marqueurs ne décrivent que la voie du mot de passe local. Clés SSH, certificats, jetons ou identifiants applicatifs peuvent rester utilisables. L'expiration du compte au champ 8 est également distincte du verrouillage du mot de passe.

:::single-choice{#shadow-password-lock-scope} Que peut-on conclure sûrement d'un champ commençant par `!` ?

::option[Le hachage Unix stocké est rendu inutilisable pour la vérification normale du mot de passe.]{#shadow-password-locked .correct explanation="Le préfixe `!` empêche le hachage de correspondre à un mot de passe fourni par cette voie."}
::option[Toutes les méthodes de connexion sont désactivées.]{#shadow-all-login-disabled explanation="D'autres méthodes peuvent être indépendantes."}
::option[Le compte est supprimé de toutes les bases d'identités.]{#shadow-account-deleted explanation="L'enregistrement existe encore ; la suppression est une opération différente."}
:::

## Distinguer les dates du mot de passe et du compte

Les champs 3 à 7 concernent le vieillissement du mot de passe. Le champ 8 expire le compte à une date absolue, indépendamment de l'âge du mot de passe. Ainsi, un maximum de 90 jours évolue depuis le dernier changement, tandis qu'une expiration de compte reste fixe.

:::single-choice{#shadow-max-age-versus-expire} Quelle différence existe entre les champs 5 et 8 ?

::option[Le champ 5 contient le nom et le 8 le shell.]{#shadow-username-shell explanation="Le nom est au champ 1 et le shell figure dans `/etc/passwd`."}
::option[Le champ 5 contient le hachage et le 8 son sel.]{#shadow-hash-salt explanation="Le hachage encodé appartient au champ 2."}
::option[Le champ 5 est l'âge maximal du mot de passe ; le 8 une date absolue d'expiration du compte.]{#shadow-password-vs-account-expiry .correct explanation="L'âge est relatif au dernier changement, tandis que l'expiration est un nombre absolu de jours."}
:::

## Examiner et modifier la politique avec les outils

```bash
$ sudo passwd -S alice
$ sudo chage -l alice
```

`passwd -S` résume l'état local et `chage -l` présente le vieillissement lisiblement. Utilisez `passwd`, `chage`, `usermod` et outils associés pour les changements. Si une réparation manuelle est inévitable, `vipw -s` verrouille la base ; validez avec `pwck` et gardez une session de récupération.

:::single-choice{#shadow-list-aging-policy} Quelle commande liste lisiblement le vieillissement du mot de passe local d'`alice` ?

::option[`cat /etc/shadow`]{#shadow-cat-entire-file explanation="Cela expose toute la base et bien plus d'informations sensibles que nécessaire."}
::option[`passwd -d alice`]{#shadow-passwd-delete explanation="Cette opération supprime le hachage ; elle modifie un état sensible."}
::option[`chage -l alice`]{#shadow-chage-list .correct explanation="L'option `-l` demande à `chage` d'afficher les champs de vieillissement."}
:::

PAM et NSS peuvent intégrer des sources au-delà du fichier local. Un compte système peut donc ne pas avoir d'enregistrement shadow local ou utiliser d'autres services.

Pour vous exercer :

1. **[Gérer les comptes Linux avec useradd, usermod et userdel](https://labex.io/fr/labs/comptia-manage-linux-user-accounts-with-useradd-usermod-and-userdel-590837)** - Créez, sécurisez et supprimez des comptes.
2. **[Configurer les comptes et privilèges sudo](https://labex.io/fr/labs/comptia-configure-user-accounts-and-sudo-privileges-in-linux-590856)** - Appliquez les politiques de mots de passe et sécurisez les comptes.

## Résumé

Vous savez interpréter la politique shadow sans exposer toute la base.

1. Traiter les hachages comme du matériel d'authentification restreint.
2. Lire les neuf champs selon leur fonction.
3. Distinguer verrouillage du mot de passe et désactivation de toute connexion.
4. Séparer vieillissement du mot de passe et expiration du compte.
5. Examiner et modifier la politique avec des outils ciblés.
