---
index: 2
lang: "fr"
title: "Dépôts de Paquets"
meta_title: "Dépôts de Paquets - Paquets"
meta_description: "Explorez les dépôts de paquets Linux et leur rôle dans la gestion des paquets. Découvrez comment votre système utilise des sources comme le fichier /etc/apt/sources.list pour trouver et installer des paquets Linux."
meta_keywords: "dépôts paquets Linux, sources apt list, /etc/apt/sources.list, paquets Linux, Linux débutant, tutoriel Linux, gestion paquets"
---

## Lesson Content

Comment le grand nombre de paquets Linux disponibles en ligne parvient-il sur nos ordinateurs ? Bien que vous puissiez visiter la page de téléchargement de chaque logiciel, une solution beaucoup plus efficace existe : les dépôts de paquets (package repositories).

### Qu'est-ce qu'un dépôt de paquets

Un dépôt de paquets est un emplacement de stockage central pour les logiciels. Ces dépôts, hébergés sur des serveurs à travers Internet, contiennent des collections organisées de paquets Linux, éliminant le besoin de téléchargements et d'installations manuels. Ce système est une pierre angulaire de la gestion moderne des paquets Linux, offrant une manière rationalisée et sécurisée de gérer les logiciels.

### Comment fonctionnent les dépôts

Le gestionnaire de paquets de votre système doit savoir où trouver ces dépôts. Vous lui fournissez un lien source, et il s'occupe du reste.

Par exemple, pour installer Docker, vous ne le téléchargez pas directement depuis leur site web. Au lieu de cela, vous configurez votre gestionnaire de paquets pour utiliser le dépôt officiel de Docker, qui est hébergé à une URL telle que `https://download.docker.com/linux/ubuntu`. Une fois configuré, votre système peut accéder à tous les paquets de ce dépôt, tels que `docker-ce`, `docker-ce-cli` et `containerd.io`.

### Configuration des sources de dépôts

Votre distribution Linux est déjà livrée avec un ensemble de dépôts préconfigurés pour tous les paquets de base de votre système. Sur les systèmes basés sur Debian comme Ubuntu, la configuration principale de ces sources est gérée via la liste des sources `apt` (apt sources list).

Traditionnellement, cette liste est un fichier unique : `/etc/apt/sources.list`. Le gestionnaire de paquets de votre machine lit ce fichier pour savoir quels dépôts vérifier pour les logiciels et les mises à jour disponibles.

Il est également courant d'ajouter de nouvelles configurations de dépôts dans le répertoire `/etc/apt/sources.list.d/`. Les versions plus récentes d'Ubuntu (22.04+) utilisent même ce répertoire par défaut, organisant les sources dans des fichiers `.sources` structurés. Cette approche maintient les dépôts tiers séparés des sources par défaut du système, rendant la gestion des paquets plus propre et plus organisée. `/etc/apt/sources.list` et les fichiers dans `/etc/apt/sources.list.d/` sont tous deux utilisés par le gestionnaire de paquets `apt`.

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension de la gestion des paquets Linux et des dépôts :

1.  **[Installation de logiciels sur Linux](https://labex.io/fr/labs/linux-software-installation-on-linux-18005)** - Entraînez-vous à diverses méthodes pour installer et gérer des logiciels sur des systèmes Ubuntu, y compris l'utilisation d'apt et la gestion des fichiers .deb, ce qui est directement lié au concept de `sources.list`.
2.  **[Installation et suppression de paquets](https://labex.io/fr/labs/linux-installing-and-removing-packages-385380)** - Apprenez à mettre à jour le système, à installer et à supprimer des paquets sur un système basé sur Debian, consolidant ainsi votre compréhension de la manière dont les gestionnaires de paquets interagissent avec les dépôts.
3.  **[Interroger et mettre à jour les paquets avec YUM sous Linux](https://labex.io/fr/labs/rhel-query-and-update-packages-with-yum-in-linux-590869)** - Explorez comment gérer les paquets logiciels sur les systèmes Linux basés sur RHEL à l'aide de YUM, offrant une perspective plus large sur la gestion des paquets entre différentes distributions.

Ces laboratoires vous aideront à appliquer les concepts de dépôts de paquets et de gestion de logiciels dans des scénarios réels et à gagner en confiance dans les tâches d'administration système.

## Quiz Question

Sur un système Debian traditionnel, quel est le chemin complet vers le fichier principal qui liste les dépôts de paquets ? Veuillez répondre en utilisant le chemin de fichier complet.

## Quiz Answer

/etc/apt/sources.list
