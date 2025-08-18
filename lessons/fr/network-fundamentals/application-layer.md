---
lang: "fr"
title: "Couche application"
meta_title: "Couche application - Bases du Réseau"
meta_description: "Découvrez la couche application dans le modèle TCP/IP, comment elle gère les données pour le courrier électronique (SMTP) et son rôle dans la communication réseau. Comprenez les couches réseau."
meta_keywords: "Couche application, modèle TCP/IP, SMTP, couches réseau, réseau Linux, tutoriel débutant, communication réseau"
---

## Lesson Content

Disons que je voulais envoyer un e-mail à Patty. Nous allons passer en revue chacune des couches TCP/IP pour voir cela en action.

Rappelez-vous que les paquets sont utilisés pour transmettre des données à travers les réseaux. Un paquet se compose d'un en-tête et d'une charge utile. L'en-tête contient des informations sur la destination et l'origine du paquet. La charge utile est la donnée réelle qui est transférée. Au fur et à mesure que notre paquet traverse le réseau, chaque couche ajoute un peu d'informations à l'en-tête du paquet. Gardez également à l'esprit que différentes couches utilisent un terme différent pour notre « paquet ». Dans la couche transport, nous encapsulons essentiellement nos données dans un segment, et dans la couche liaison, nous appelons cela une trame, mais sachez simplement que « paquet » peut être utilisé pour désigner la même chose.

Tout d'abord, nous commençons par la couche application. Lorsque nous envoyons notre e-mail via notre client de messagerie, la couche application encapsulera ces données. La couche application communique avec la couche transport via un port spécifié, et via ce port, elle envoie ses données. Nous voulons envoyer un e-mail via le protocole de la couche application SMTP (Simple Mail Transfer Protocol). Les données sont envoyées via notre protocole de transport, qui ouvre une connexion à ce port (le port 25 est utilisé pour SMTP). Ainsi, ces données sont envoyées via ce port, et ces données sont envoyées à la couche Transport pour être encapsulées en segments.

## Exercise

Pas d'exercices pour cette leçon.

## Quiz Question

Quelle couche est utilisée pour présenter les données du paquet dans un format convivial pour l'utilisateur ?

## Quiz Answer

Application
