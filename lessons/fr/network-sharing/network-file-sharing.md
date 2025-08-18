---
lang: "fr"
title: "Aperçu du partage de fichiers"
meta_title: "Aperçu du partage de fichiers - Partage Réseau"
meta_description: "Apprenez le partage de fichiers Linux et la commande de copie sécurisée (scp). Transférez des fichiers entre des hôtes sur votre réseau. Démarrez avec ce guide convivial pour débutants !"
meta_keywords: "Partage de fichiers Linux, commande scp, copie sécurisée, transfert de fichiers réseau, tutoriel Linux, Linux pour débutants, guide Linux"
---

## Lesson Content

Vous n'êtes généralement pas le seul ordinateur sur votre réseau, surtout si vous travaillez dans un environnement commercial. Lorsque nous voulons transférer des données d'une machine à l'autre, il est parfois plus facile de connecter une clé USB et de les copier manuellement. Mais pour la plupart, si vous travaillez avec des machines sur le même réseau, la méthode de transfert de données est le partage de fichiers réseau.

Dans ce cours, nous allons passer en revue quelques méthodes différentes pour copier des données vers et depuis différentes machines de votre réseau. Nous discuterons de quelques copies de fichiers simples, puis nous parlerons du montage de répertoires entiers sur votre machine qui agissent comme un lecteur séparé.

Un outil simple de partage de fichiers est la commande **scp**. La commande scp signifie secure copy (copie sécurisée) ; elle fonctionne exactement comme la commande cp, mais vous permet de copier d'un hôte à un autre hôte sur le même réseau. Elle fonctionne via ssh, de sorte que toutes vos actions utilisent la même authentification et la même sécurité que ssh.

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

Essayez de copier un fichier avec scp d'une machine à l'autre.

## Quiz Question

Quelle commande pouvez-vous utiliser pour copier des fichiers de manière sécurisée d'un hôte à un autre ?

## Quiz Answer

scp
