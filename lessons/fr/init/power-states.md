---
index: 7
lang: "fr"
title: "États d'alimentation"
meta_title: "États d'alimentation - Init"
meta_description: "Apprenez à gérer les états d'alimentation du système Linux. Ce guide couvre les commandes essentielles d'arrêt (shutdown), de redémarrage (reboot) et de halt pour éteindre ou redémarrer votre système Linux en toute sécurité. Maîtrisez ces commandes Linux fondamentales pour l'administration système."
meta_keywords: "états alimentation linux, commande shutdown, commande reboot, commande halt, poweroff linux, redémarrer linux, administration système linux, linux débutants, commandes linux, systemd, init"
---

## Lesson Content

La gestion appropriée de l'état d'alimentation de votre système Linux est une compétence fondamentale. Bien que vous puissiez utiliser une interface graphique, la ligne de commande offre des options puissantes et flexibles pour éteindre ou redémarrer votre machine. Ces processus sont liés au système d'initialisation du système, tel que `init` ou `systemd`, qui gère différents états opérationnels, y compris le démarrage et l'arrêt.

### Arrêt du Système

La commande principale pour gérer les états d'alimentation est `shutdown`. Pour éteindre immédiatement votre système Linux, vous pouvez utiliser la commande `shutdown` avec l'indicateur `-h` (halt) et l'argument de temps `now` (maintenant). Des privilèges administratifs sont requis, vous devrez donc utiliser `sudo`.

```bash
sudo shutdown -h now
```

L'indicateur `-h` demande au système de s'arrêter (halt) après l'arrêt des services. Sur la plupart des matériels modernes, cela éteindra complètement la machine. Vous pouvez également planifier un arrêt pour une heure future. Pour éteindre le système dans un nombre spécifique de minutes, utilisez le format `+m`:

```bash
sudo shutdown -h +2
```

Cette commande arrêtera votre système dans deux minutes, ce qui est utile pour avertir les autres utilisateurs ou permettre aux processus d'arrière-plan de se terminer proprement.

### Redémarrage du Système

Pour redémarrer votre système Linux, vous pouvez utiliser la commande `shutdown` avec l'indicateur `-r` (reboot).

```bash
sudo shutdown -r now
```

Une alternative plus directe et couramment utilisée est la commande `reboot`, qui réalise le même objectif de redémarrer le système en toute sécurité.

```bash
sudo reboot
```

### Commandes d'Alimentation Alternatives

Pour un contrôle plus direct, vous pourriez également rencontrer les commandes `halt` et `poweroff`. Dans de nombreuses distributions Linux modernes, ce sont essentiellement des raccourcis qui appellent la commande `shutdown`. Par exemple, exécuter `poweroff` est souvent équivalent à exécuter `shutdown -h now`.

## Exercise

N'hésitez pas à pratiquer ces commandes dans une machine virtuelle. Pour des exercices plus guidés, explorez le [Parcours d'Apprentissage Linux](https://labex.io/fr/learn/linux) complet pour pratiquer un large éventail de compétences Linux.

## Quiz Question

What is the full command, including `sudo`, to schedule a system power off in 4 minutes? Please provide the complete command in English, paying attention to spacing and case.

## Quiz Answer

sudo shutdown -h +4
