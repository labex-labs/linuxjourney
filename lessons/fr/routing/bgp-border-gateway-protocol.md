---
lesson_id: "bgp-border-gateway-protocol"
course_id: "routing"
lang: "fr"
order_index: 7
title: "Border Gateway Protocol"
description: "Découvrez comment BGP échange l’accessibilité IP contrôlée par des politiques entre les systèmes autonomes et en leur sein."
meta_title: "Border Gateway Protocol - Routage"
meta_description: "Explorez BGP, le protocole central du routage Internet, les systèmes autonomes, les vecteurs de chemins et la sélection par politiques."
meta_keywords: "BGP, Border Gateway Protocol, routage BGP, routage Internet, systèmes autonomes, réseau Linux, tutoriel BGP"
---

Border Gateway Protocol est le protocole de routage à vecteur de chemins d’Internet. Il échange l’accessibilité des préfixes IP et les attributs de chemins afin que les réseaux puissent appliquer une politique administrative plutôt que de choisir les routes uniquement selon leur distance physique.

## Systèmes autonomes et sessions

Un système autonome est un ensemble de réseaux placés sous une administration de routage commune, identifié pour BGP par un numéro de système autonome. BGP externe échange les routes entre systèmes autonomes ; BGP interne distribue l’accessibilité BGP au sein d’un même AS.

Les pairs BGP établissent une session sur le port TCP 179. Une session TCP fonctionnelle ne constitue que la base du transport ; les capacités de BGP, les politiques et l’échange de routes doivent également réussir.

:::single-choice{#bgp-external-session}
Qu’échange BGP externe ?

::option[Les sommes de contrôle des trames Ethernet au sein d’un commutateur.]{#bgp-ethernet-fcs explanation="BGP fonctionne au-dessus de TCP et échange l’accessibilité de la couche réseau."}
::option[Les mots de passe des utilisateurs entre les navigateurs web.]{#bgp-browser-passwords explanation="Les identifiants applicatifs ne sont pas des attributs de routage."}
::option[Les informations d’accessibilité et de chemins entre systèmes autonomes.]{#bgp-between-as .correct explanation="eBGP relie des administrations de routage distinctes et applique la politique interdomaine."}
:::

## Informations du vecteur de chemins

Une annonce contient un préfixe et des attributs. `AS_PATH` répertorie les systèmes autonomes traversés et aide à détecter les boucles. Parmi les autres attributs courants figurent `LOCAL_PREF`, `MED`, l’origine, le prochain saut et les communautés. Leur effet dépend du sens, de l’implémentation et de la politique.

:::single-choice{#bgp-as-path-loop}
Comment `AS_PATH` aide-t-il à prévenir les boucles entre AS ?

::option[Un AS peut rejeter un chemin qui contient déjà son propre numéro.]{#bgp-own-as-reject .correct explanation="Le vecteur de chemins expose la suite des AS employés pour atteindre le préfixe annoncé."}
::option[Il chiffre chaque paquet qui traverse ces systèmes.]{#bgp-aspath-encryption explanation="Cet attribut décrit le chemin de routage et ne chiffre pas la charge utile."}
::option[Il attribue une adresse MAC à chaque AS.]{#bgp-aspath-mac explanation="Les numéros de systèmes autonomes et les adresses de liaison appartiennent à des espaces de noms distincts."}
:::

## Sélection fondée sur les politiques

Le « meilleur » chemin BGP est celui qui l’emporte dans un processus de décision configuré. Les opérateurs peuvent privilégier les routes de clients, modifier la préférence locale, filtrer les préfixes, employer des communautés et appliquer des politiques d’ingénierie du trafic. Un `AS_PATH` plus court peut compter à une étape, mais ne l’emporte pas universellement sur les attributs plus prioritaires.

Après la sélection des candidats par BGP, l’acheminement IP ordinaire applique encore la correspondance au préfixe le plus long. Un `/24` sélectionné est employé pour ses destinations plutôt qu’un `/16` sélectionné qui le couvre.

:::single-choice{#bgp-best-path-meaning}
Que représente un meilleur chemin BGP ?

::option[La route qui l’emporte dans le processus local de décision des attributs et des politiques.]{#bgp-policy-winner .correct explanation="L’intention administrative est centrale dans la sélection des chemins interdomaine."}
::option[La route physiquement la plus courte dans tous les cas.]{#bgp-shortest-cable explanation="BGP ne possède aucune carte complète des distances physiques."}
::option[La garantie de la plus faible latence applicative actuelle.]{#bgp-lowest-latency explanation="Par défaut, la sélection BGP n’optimise pas continuellement la latence des utilisateurs finaux."}
:::

## Annonce et accessibilité

L’annonce d’un préfixe affirme son accessibilité conformément à la politique ; elle ne crée pas la route sous-jacente et ne garantit pas le chemin du retour. Avant d’annoncer un préfixe, assurez-vous de la validité de l’acheminement, du comportement de l’agrégation, des filtres, du basculement et de l’autorisation de propriété.

:::single-choice{#bgp-advertisement-limit}
Qu’est-ce que l’annonce d’un préfixe ne garantit pas ?

::option[Que les pairs peuvent recevoir une route du plan de contrôle.]{#bgp-peers-control explanation="L’annonce et l’acceptation réussies peuvent établir ce fait limité du plan de contrôle."}
::option[Que le préfixe contient des bits d’adresse.]{#bgp-prefix-bits explanation="Un préfixe IP se définit par des bits d’adresse et une longueur."}
::option[Qu’il peut livrer des paquets pour tout le préfixe.]{#bgp-data-plane-not-guaranteed .correct explanation="Les routes sous-jacentes, les prochains sauts, le filtrage et la santé des services doivent encore être vérifiés."}
:::

## Sécurité du routage et contrôle des changements

Les fuites et les détournements de routes peuvent affecter le trafic bien au-delà d’un routeur. Les opérateurs emploient des filtres stricts à l’importation et à l’exportation, des limites du nombre maximal de préfixes, des politiques de pairs, la surveillance et, lorsque cela convient, la validation d’origine de la Resource Public Key Infrastructure. La validation d’origine RPKI vérifie si un AS est autorisé à annoncer un préfixe ; elle ne valide pas tout le chemin d’AS.

Les changements BGP nécessitent un déploiement progressif, l’examen des différences de routes, un accès hors bande, un retour en arrière et une vérification des plans de contrôle et de données.

:::single-choice{#bgp-rpki-limit}
Que contrôle la validation d’origine RPKI ?

::option[Si la charge utile de chaque paquet est exempte de logiciel malveillant.]{#bgp-payload-malware explanation="RPKI n’examine pas le contenu applicatif."}
::option[Si tout le chemin d’AS possède la plus faible latence.]{#bgp-path-latency explanation="La validation d’origine n’est ni une sélection de performances ni une validation complète du chemin."}
::option[Si l’AS d’origine est autorisé.]{#bgp-origin-authorized .correct explanation="Elle valide l’autorisation de l’origine, et non chaque relation de transit du chemin d’AS."}
:::

## Résumé

Vous savez maintenant décrire BGP comme un routage à vecteur de chemins contrôlé par des politiques.

1. Distinguer les sessions BGP externes et internes.
2. Employer `AS_PATH` comme information de chemin et de boucle.
3. Interpréter le meilleur chemin au moyen des attributs et de la politique locaux.
4. Vérifier l’acheminement sous-jacent à chaque préfixe annoncé.
5. Appliquer le filtrage, la validation d’origine, la surveillance et le retour en arrière.
