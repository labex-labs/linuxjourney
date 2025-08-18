---
lang: "fr"
title: "Noms des périphériques"
meta_title: "Noms des périphériques - Périphériques"
meta_description: "Apprenez les noms des périphériques Linux comme les périphériques SCSI (sd), pseudo et PATA (hd). Comprenez /dev/sda, /dev/null et plus encore dans ce guide convivial pour débutants."
meta_keywords: "noms de périphériques Linux, /dev, périphériques SCSI, pseudo-périphériques, périphériques PATA, tutoriel Linux, Linux pour débutants, fichiers de périphériques"
---

## Lesson Content

Voici les noms de périphériques les plus courants que vous rencontrerez :

### SCSI Devices

Si vous avez un quelconque stockage de masse sur votre machine, il y a de fortes chances qu'il utilise le protocole SCSI (prononcé "scuzzy"). SCSI signifie Small Computer System Interface ; c'est un protocole utilisé pour permettre la communication entre les disques, les imprimantes, les scanners et d'autres périphériques et votre système. Vous avez peut-être entendu parler des périphériques SCSI, qui ne sont plus réellement utilisés dans les systèmes modernes ; cependant, nos systèmes Linux associent les disques SCSI aux disques durs dans `/dev`. Ils sont représentés par un préfixe `sd` (SCSI disk) :

Fichiers de périphériques SCSI courants :

- `/dev/sda` - Premier disque dur
- `/dev/sdb` - Deuxième disque dur
- `/dev/sda3` - Troisième partition sur le premier disque dur

### Pseudo Devices

Comme nous l'avons vu précédemment, les pseudo-périphériques ne sont pas réellement connectés physiquement à votre système. La plupart des pseudo-périphériques courants sont des périphériques de caractères :

- `/dev/zero` - accepte et ignore toutes les entrées, produit un flux continu d'octets NULL (valeur zéro)
- `/dev/null` - accepte et ignore toutes les entrées, ne produit aucune sortie
- `/dev/random` - produit des nombres aléatoires

### PATA Devices

Parfois, dans les systèmes plus anciens, vous pouvez voir des disques durs désignés par un préfixe `hd` :

- `/dev/hda` - Premier disque dur
- `/dev/hdd2` - Deuxième partition sur le 4ème disque dur

## Exercise

Écrivez sur les pseudo-périphériques et voyez ce qui se passe. Faites attention à ne pas écrire vos disques sur ces périphériques !

## Quiz Question

Quel serait généralement le nom de périphérique pour la première partition sur le deuxième disque SCSI ?

## Quiz Answer

sdb1
