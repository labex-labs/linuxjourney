---
index: 1
lang: "fr"
title: "Aperçu du partage de fichiers"
meta_title: "Aperçu du partage de fichiers - Partage réseau"
meta_description: "Découvrez le partage de fichiers Linux et la commande de copie sécurisée (scp). Transférez des fichiers entre les hôtes de votre réseau. Démarrez avec ce guide convivial pour débutants !"
meta_keywords: "partage de fichiers Linux, commande scp, copie sécurisée, transfert de fichiers réseau, tutoriel Linux, Linux pour débutants, guide Linux"
---

## Lesson Content

Vous n'êtes généralement pas le seul ordinateur sur votre réseau, surtout si vous travaillez dans un environnement commercial. Lorsque nous voulons transférer des données d'une machine à une autre, il est parfois plus facile de connecter une clé USB et de les copier manuellement. Mais la plupart du temps, si vous travaillez avec des machines sur le même réseau, la façon de transférer des données est le partage de fichiers réseau.

Dans ce cours, nous allons passer en revue quelques méthodes différentes pour copier des données vers et depuis différentes machines de votre réseau. Nous discuterons de copies de fichiers simples, puis nous parlerons du montage de répertoires entiers sur votre machine qui agissent comme un lecteur séparé.

Un outil de partage de fichiers simple est la commande **scp**. La commande scp signifie copie sécurisée (secure copy) ; elle fonctionne exactement comme la commande cp, mais vous permet de copier d'un hôte vers un autre hôte sur le même réseau. Elle fonctionne via ssh, de sorte que toutes vos actions utilisent la même authentification et la même sécurité que ssh.

### Pour copier un fichier d'un hôte local vers un hôte distant

```bash
scp myfile.txt username@remotehost.com:/remote/directory
```

### Pour copier un fichier d'un hôte distant vers votre hôte local

```bash
scp username@remotehost.com:/remote/directory/myfile.txt /local/directory
```

### Pour copier un répertoire de votre hôte local vers un hôte distant

```bash
scp -r mydir username@remotehost.com:/remote/directory
```

## Exercise

La pratique rend parfait ! Voici un laboratoire pratique pour renforcer votre compréhension du transfert de fichiers réseau sécurisé :

1. **[Accès à distance sécurisé sous Linux avec SSH](https://labex.io/fr/labs/linux-secure-remote-access-in-linux-with-ssh-592816)** - Pratiquez l'authentification par clé, le transfert sécurisé de fichiers avec `scp` et la création de tunnels SSH pour le transfert de port.

Ce laboratoire vous aidera à appliquer les concepts d'accès à distance sécurisé et de transfert de fichiers dans un scénario réel et à renforcer votre confiance avec `scp`.

## Quiz Question

Quelle commande pouvez-vous utiliser pour copier des fichiers en toute sécurité d'un hôte à un autre ?

## Quiz Answer

scp
