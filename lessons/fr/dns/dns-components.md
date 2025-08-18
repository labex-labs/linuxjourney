---
lang: "fr"
title: "Composants DNS"
meta_title: "Composants DNS - DNS"
meta_description: "Découvrez les composants DNS : serveurs de noms, fichiers de zone et enregistrements de ressources. Comprenez comment fonctionne le DNS pour les débutants. Commencez votre parcours de mise en réseau Linux !"
meta_keywords: "composants DNS, serveur de noms, fichier de zone, enregistrements de ressources, tutoriel DNS, mise en réseau Linux, guide du débutant"
---

## Lesson Content

La base de données DNS d'Internet repose sur des sites et des organisations qui fournissent une partie de cette base de données. Pour ce faire, ils ont besoin de :

### Name Server

Nous configurons le DNS via des "serveurs de noms". Les serveurs de noms chargent nos paramètres et configurations DNS et répondent à toutes les questions des clients ou d'autres serveurs qui veulent savoir des choses comme "Qui est google.com ?". Si le serveur de noms ne connaît pas la réponse à cette requête, il redirigera la demande vers d'autres serveurs de noms. Les serveurs de noms peuvent être "autoritaires", ce qui signifie qu'ils détiennent les enregistrements DNS réels que vous recherchez, ou "récursifs", ce qui signifie qu'ils demanderaient à d'autres serveurs, et ces serveurs demanderaient à d'autres serveurs jusqu'à ce qu'ils trouvent un serveur autoritaire qui contient les enregistrements DNS. Les serveurs récursifs peuvent également avoir les informations que nous voulons en cache au lieu d'atteindre un serveur autoritaire.

### Zone File

À l'intérieur d'un serveur de noms se trouvent des fichiers appelés fichiers de zone. Les fichiers de zone sont la façon dont le serveur de noms stocke les informations sur le domaine ou comment accéder au domaine s'il ne le connaît pas.

### Resource Records

Un fichier de zone est composé d'entrées d'enregistrements de ressources. Chaque ligne est un enregistrement et contient des informations sur les hôtes, les serveurs de noms, d'autres ressources, etc. Les champs se composent des éléments suivants :

- Record name
- TTL - Le temps après lequel nous rejetons l'enregistrement et en obtenons un nouveau. En DNS, le TTL est indiqué par le temps, de sorte que les enregistrements peuvent avoir un TTL d'une heure. La raison pour laquelle nous faisons cela est que l'Internet est en constante évolution ; une minute un hôte peut être mappé à l'adresse IP X, puis la suivante il peut être à l'adresse IP Y.
- Class - Espace de noms des informations d'enregistrement. Le plus souvent, IN est utilisé pour Internet.
- Type - Type d'informations stockées dans les données de l'enregistrement. Nous n'entrerons pas dans les types d'enregistrements, mais vous avez probablement vu des types courants comme A pour l'adresse, MX pour l'échangeur de courrier, etc.
- Data - Ce champ peut contenir une adresse IP s'il s'agit d'un enregistrement A ou autre chose selon le type d'enregistrement.

```plaintext
patty    IN  A      192.168.0.4
```

## Exercise

Pas d'exercices pour cette leçon.

## Quiz Question

Quel type d'enregistrement de ressource est utilisé pour les échangeurs de courrier ?

## Quiz Answer

MX
