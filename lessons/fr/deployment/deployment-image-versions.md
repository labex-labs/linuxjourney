---
lesson_id: "deployment-image-versions"
course_id: "deployment"
lang: "fr"
order_index: 2
title: "Versions d’image"
description: "Apprenez à distinguer une étiquette d’image d’une empreinte et à comparer les images exactes utilisées dans deux environnements."
meta_title: "Versions d’image - Déploiement"
meta_description: "Apprenez à distinguer une étiquette d’image d’une empreinte et à comparer les images exactes utilisées dans deux environnements."
meta_keywords: "versions d’image, étiquettes, empreintes, digest, déploiement, DevOps, Linux Journey"
---

Une étiquette comme `site:2` rend une référence d’image facile à lire. La personne qui publie une nouvelle image peut réattribuer cette étiquette. Pour identifier précisément le contenu d’une image, notez son **empreinte** (digest), calculée à partir du contenu référencé.

## Lire une étiquette

Supposons qu’un registre affiche les entrées suivantes à deux dates différentes. Les empreintes abrégées illustrent le principe. Il faut une empreinte complète pour récupérer une image.

```text
Monday    site:2    sha256:a1b2…
Tuesday   site:2    sha256:c3d4…
```

La même étiquette pointe désormais vers un autre contenu. Une machine qui a récupéré l’image lundi peut continuer à utiliser l’ancienne image.

:::single-choice{#deployment-image-versions-moving-tag} Les deux environnements indiquent l’étiquette site:2. Comment savoir quelle image chacun a réellement récupérée ?

::option[Avec leur seule étiquette commune.]{#deployment-image-versions-moving-tag-b explanation="Dans l’exemple, deux images différentes portent cette étiquette."}
::option[En comptant les conteneurs sur chaque machine.]{#deployment-image-versions-moving-tag-c explanation="Ce nombre ne permet pas d’identifier les images."}
::option[En consultant les empreintes enregistrées.]{#deployment-image-versions-moving-tag-a .correct explanation="L’étiquette peut changer de cible. L’empreinte identifie le contenu sélectionné lors de la récupération."}
:::

## Lire une référence avec empreinte

Une référence d’image peut contenir un `@` suivi de l’empreinte complète. La référence demande alors au registre cet objet précis. Utilisez l’empreinte complète issue du registre ou de la fiche de build. Les valeurs abrégées sont pratiques pour les exemples. Pour récupérer l’image, il faut la valeur complète.

:::single-choice{#deployment-image-versions-fixed-reference} Quelle référence sélectionne un objet précis du registre ?

::option[Le nom de l’image sans étiquette.]{#deployment-image-versions-fixed-reference-a explanation="Docker applique une étiquette par défaut, qui peut être réattribuée."}
::option[Le nom de l’image suivi de son empreinte complète.]{#deployment-image-versions-fixed-reference-c .correct explanation="L’empreinte désigne un contenu précis."}
::option[Un commentaire qui indique la date du build.]{#deployment-image-versions-fixed-reference-b explanation="Le registre ne peut pas récupérer d’objet à partir d’un commentaire."}
:::

## Comparer des images de la même plateforme

Un nom d’image peut désigner une liste de builds pour différents types de machine ou une image pour une plateforme précise. Pour comparer ce que deux hôtes exécutent réellement, notez leur plateforme et comparez les références des images qui y correspondent. Conservez la référence complète d’origine dans la fiche de release.

:::single-choice{#deployment-image-versions-compare-platform} Une release prévoit des images pour arm64 et amd64. Quelle comparaison est utile pour vérifier deux hôtes amd64 ?

::option[Comparer les références d’images amd64 sélectionnées par les hôtes.]{#deployment-image-versions-compare-platform-b .correct explanation="Vous comparez le contenu destiné à une même plateforme."}
::option[Comparer des images pour deux architectures différentes.]{#deployment-image-versions-compare-platform-a explanation="Ces objets correspondent à des plateformes différentes."}
::option[Comparer les noms d’hôte.]{#deployment-image-versions-compare-platform-c explanation="Ces noms identifient les machines sans préciser le contenu déployé."}
:::

## Résumé

Vous savez maintenant identifier l’image exacte utilisée derrière une étiquette lisible.

1. Expliquez pourquoi une même étiquette peut désigner différents contenus.
2. Reconnaissez une référence avec une empreinte complète.
3. Comparez les images correspondant à la plateforme concernée.
