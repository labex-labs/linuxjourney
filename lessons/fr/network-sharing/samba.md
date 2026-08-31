---
lesson_id: "samba"
course_id: "network-sharing"
lang: "fr"
order_index: 5
title: "Samba"
description: "Découvrez comment configurer, valider, utiliser et sécuriser un partage de fichiers Samba élémentaire."
meta_title: "Samba - Partage réseau"
meta_description: "Apprenez à créer un partage réseau Samba sous Linux : protocole SMB, installation, configuration, smb.conf et connexion depuis un client Linux."
meta_keywords: "Samba, SMB Linux, partage Samba, protocole SMB, partage de fichiers, smb.conf, cifs, smbclient, tutoriel Linux"
---

Samba met en œuvre le protocole Server Message Block sur les systèmes de type Unix, ce qui permet aux clients Linux, Windows, macOS et autres de partager des fichiers et des imprimantes. Les déploiements modernes emploient les versions actuelles de SMB ; l’ancien terme CIFS reste visible dans les outils clients Linux, mais ne justifie pas l’activation de l’obsolète SMB1.

## Planifier le partage

Avant d’installer ou de modifier Samba, définissez les clients autorisés, les identités, les besoins en lecture et en écriture, la zone réseau, le propriétaire des données, la politique de sauvegarde et la version SMB requise. Employez un répertoire dédié plutôt que d’exposer involontairement une arborescence personnelle ou système.

L’accès est contrôlé à la fois par la politique Samba et par les permissions du système de fichiers sous-jacent. Autoriser les écritures dans `smb.conf` ne peut pas accorder à un compte un accès qu’il ne possède pas dans le système de fichiers.

:::single-choice{#samba-two-permission-layers}
Qu’est-ce qui doit autoriser un utilisateur à écrire dans un partage Samba ?

::option[Uniquement le commentaire affiché du partage.]{#samba-comment-permission explanation="Un commentaire est un texte descriptif qui n’accorde aucun accès."}
::option[À la fois les règles Samba et les permissions du système de fichiers.]{#samba-policy-and-filesystem .correct explanation="La requête doit satisfaire les règles du protocole et les autorisations du système de fichiers local."}
::option[Uniquement le réglage de l’arrière-plan du bureau du client.]{#samba-wallpaper explanation="L’apparence du client ne contrôle pas les fichiers du serveur."}
:::

## Définir un partage élémentaire

Le fichier de configuration principal est généralement `/etc/samba/smb.conf`. Voici un exemple restreint :

```ini
[team]
    path = /srv/samba/team
    browseable = yes
    read only = no
    valid users = @teamshare
```

Créez le répertoire et appliquez au groupe Unix une propriété et des permissions vérifiées :

```bash
$ sudo install -d -o root -g teamshare -m 2770 /srv/samba/team
```

Le bit set-group-ID aide les nouvelles entrées à hériter du groupe du répertoire, mais un accès collaboratif peut également nécessiter une ACL ou un masque de création soigneusement choisi. Testez les fichiers et les répertoires réellement obtenus au lieu de supposer que l’héritage suffit.

:::single-choice{#samba-valid-users}
Que signifie `valid users = @teamshare` ?

::option[Chaque utilisateur anonyme du réseau reçoit un accès en écriture.]{#samba-every-anonymous explanation="Cette règle restreint l’accès au lieu d’autoriser les écritures des invités."}
::option[Le serveur doit renommer le partage en `teamshare`.]{#samba-rename-share explanation="Le nom visible du partage reste celui de la section `[team]`."}
::option[Seuls les membres du groupe nommé sont autorisés par cette règle du partage.]{#samba-valid-group .correct explanation="Dans la syntaxe des listes d’utilisateurs de Samba, la forme avec `@` désigne un groupe."}
:::

## Configurer l’identité

Dans une configuration Samba autonome, un compte nécessite généralement une identité Unix correspondante et un identifiant Samba activé :

```bash
$ sudo smbpasswd -a alice
```

Les déploiements avec un domaine d’annuaire utilisent une conception différente des identités. Ne placez pas les mots de passe dans l’historique du shell ni dans une configuration lisible par des utilisateurs non concernés, et ne supposez pas qu’un mot de passe Samba soit automatiquement identique à celui du compte Unix.

:::single-choice{#samba-password-database}
Que fait généralement `smbpasswd -a alice` sur un serveur autonome ?

::option[La commande supprime le répertoire personnel de l’utilisateur Unix.]{#samba-delete-home explanation="Elle gère les identifiants Samba et ne supprime aucun répertoire personnel."}
::option[Elle ajoute ou initialise les identifiants Samba du compte.]{#samba-add-credential .correct explanation="La base d’authentification SMB est gérée séparément de la simple création d’un utilisateur Unix."}
::option[Elle monte tous les partages SMB visibles en tant qu’Alice.]{#samba-mount-all explanation="L’inscription d’un identifiant côté serveur est distincte du montage côté client."}
:::

## Valider et appliquer la configuration

Vérifiez la configuration analysée avant de recharger les services :

```bash
$ testparm -s
```

Examinez les valeurs par défaut inattendues et les erreurs, puis rechargez le service Samba de la distribution par son gestionnaire de services. Les noms varient et comprennent souvent `smbd.service` ou `smb.service`. Lorsqu’il est pris en charge, un rechargement perturbe moins qu’un redémarrage, mais vérifiez tout de même l’état, les sockets en écoute, la portée du pare-feu et les journaux.

Effectuez un test depuis un client en précisant l’utilisateur :

```bash
$ smbclient //server.example.net/team -U alice
```

:::single-choice{#samba-testparm-purpose}
Pourquoi exécuter `testparm -s` avant d’appliquer une modification de Samba ?

::option[La commande copie chaque fichier partagé vers un serveur de sauvegarde.]{#samba-testparm-backup explanation="Cet outil analyse et affiche la configuration au lieu de copier les données du partage."}
::option[Elle valide et affiche la configuration Samba effective.]{#samba-testparm-validate .correct explanation="La sortie de l’analyseur détecte les erreurs et révèle les paramètres interprétés avant d’affecter le service."}
::option[Elle accorde des privilèges d’administration à tous les clients.]{#samba-testparm-admin explanation="La validation ne modifie pas les autorisations des clients."}
:::

## Monter depuis Linux

Les clients Linux emploient généralement le pilote de système de fichiers `cifs` et ses utilitaires de montage. Évitez les mots de passe sur la ligne de commande, car les arguments peuvent apparaître dans l’historique ou lors de l’examen des processus. Employez un fichier d’identifiants lisible uniquement par root ou un mécanisme d’identification approuvé :

```bash
$ sudo mount -t cifs //server.example.net/team /mnt/team \
    -o credentials=/root/.smb-team,vers=3.1.1
```

Protégez le fichier d’identifiants, confirmez la version prise en charge aux deux extrémités et définissez délibérément les exigences d’UID, de GID, de permissions et de chiffrement. Après le montage, vérifiez avec `findmnt`, effectuez des tests de lecture et d’écriture autorisés, puis démontez après coordination avec les utilisateurs actifs.

:::single-choice{#samba-command-line-password}
Pourquoi éviter `password=...` directement dans une commande de montage ?

::option[Le secret peut être exposé dans l’historique ou les arguments des processus.]{#samba-password-exposure .correct explanation="Une source d’identifiants protégée réduit les divulgations accidentelles, mais exige toujours des permissions soigneuses."}
::option[SMB ne prend en charge aucune forme d’authentification par mot de passe.]{#samba-no-passwords explanation="L’authentification SMB par mot de passe est courante, même si d’autres systèmes d’identité existent également."}
::option[Cette option rend le partage définitivement accessible en lecture seule.]{#samba-password-readonly explanation="L’emplacement du secret ne détermine pas la politique d’écriture."}
:::

## Résumé

Vous savez maintenant configurer un partage Samba en tenant compte de la sécurité du protocole et de celle du système de fichiers.

1. Définir d’abord les clients, les identités, la portée réseau et la politique des données.
2. Restreindre le partage et aligner les permissions sous-jacentes.
3. Gérer les identifiants Samba avec le modèle d’identité approprié.
4. Valider avec `testparm` et effectuer un test client de bout en bout.
5. Protéger les identifiants du client et vérifier l’accès monté.
