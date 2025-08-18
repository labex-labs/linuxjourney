---
index: 5
lang: "es"
title: "CIDR"
meta_title: "CIDR - Subnetting"
meta_description: "Aprenda la notación CIDR para redes Linux. Comprenda las máscaras de subred, el direccionamiento IP y el cálculo de hosts con esta guía para principiantes. ¡Mejore sus habilidades de red!"
meta_keywords: "CIDR, subnet mask, IP addressing, network prefix, Linux networking, beginner, tutorial, guide"
---

## Lesson Content

CIDR (Classless Inter-Domain Routing) se utiliza para representar una máscara de subred de una manera más compacta. Es posible que vea subredes anotadas en notación CIDR, donde una subred como 10.42.3.0/255.255.255.0 se escribe como 10.42.3.0/24. Esta notación incluye tanto el prefijo de subred como la máscara de subred.

Recuerde, una dirección IP consta de 4 bytes o 32 bits. CIDR indica el número de bits utilizados como prefijo de red. Así, 123.12.24.0/23 significa que se utilizan los primeros 23 bits. ¿Qué significa eso? ¿Cuántos hosts son?

Un truco simple es restar la dirección CIDR (23) del número total de bits que puede tener una dirección IP (32). Esto deja 9 bits. Por lo tanto, 2^9 = 512. Sin embargo, debemos eliminar 2 direcciones (la dirección de subred y la dirección de broadcast), por lo que tenemos 510 hosts utilizables.

## Exercise

No exercises for this lesson.

## Quiz Question

No questions, move along!

## Quiz Answer
