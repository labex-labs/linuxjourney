---
lang: "fr"
title: "États d'alimentation"
meta_title: "États d'alimentation - Init"
meta_description: "Apprenez les états d'alimentation du système Linux : commandes shutdown, reboot et halt. Comprenez comment éteindre ou redémarrer votre système Linux en toute sécurité. Démarrez avec les commandes essentielles !"
meta_keywords: "arrêt Linux, commande de redémarrage, système halt, éteindre Linux, commandes Linux, Linux débutant, tutoriel Linux, états du système"
---

## Lesson Content

Il est difficile de croire que nous n'avons pas encore abordé les moyens de contrôler l'état de votre système via la ligne de commande. Lorsque nous parlons d'`init`, nous discutons non seulement des modes qui démarrent notre système, mais aussi de ceux qui l'arrêtent.

Pour éteindre votre système :

```bash
sudo shutdown -h now
```

Cette commande arrêtera le système (l'éteindra). Vous devez également spécifier l'heure à laquelle vous souhaitez que cela se produise. Vous pouvez ajouter un temps en minutes qui éteindra le système dans ce laps de temps.

```bash
sudo shutdown -h +2
```

Cela éteindra votre système dans deux minutes. Vous pouvez également redémarrer avec la commande `shutdown` :

```bash
sudo shutdown -r now
```

Ou utilisez simplement la commande `reboot` :

```bash
sudo reboot
```

## Exercise

Que pensez-vous qu'il se passe avec `init` lorsque vous éteignez votre machine ?

## Quiz Question

Quelle est la commande pour éteindre votre système en 4 minutes ?

## Quiz Answer

sudo shutdown -h +4
